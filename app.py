import os
import json
import uuid
from datetime import datetime, timezone
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DESTINATIONS_FILE = os.path.join(DATA_DIR, 'destinations.json')
BOOKINGS_FILE = os.path.join(DATA_DIR, 'bookings.json')

def load_destinations():
    if not os.path.exists(DESTINATIONS_FILE):
        return []
    with open(DESTINATIONS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_destinations(data):
    with open(DESTINATIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_bookings():
    if not os.path.exists(BOOKINGS_FILE):
        return []
    with open(BOOKINGS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_bookings(data):
    with open(BOOKINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/places', methods=['GET'])
def get_places():
    places = load_destinations()
    
    # Text query search (matches location name, state, city, category, highlights, things to do)
    query = request.args.get('q', '').strip().lower()
    if query:
        places = [
            p for p in places
            if query in p.get('name', '').lower()
            or query in p.get('state', '').lower()
            or query in p.get('region', '').lower()
            or query in p.get('tagline', '').lower()
            or query in p.get('category', '').lower()
            or query in p.get('description', '').lower()
            or any(query in t.lower() for t in p.get('thingsToDo', []))
        ]
        
    # Category filter
    category = request.args.get('category', '').strip()
    if category and category.lower() != 'all':
        places = [p for p in places if p.get('category', '').lower() == category.lower()]
        
    # Region filter
    region = request.args.get('region', '').strip()
    if region and region.lower() != 'all':
        places = [p for p in places if p.get('region', '').lower() == region.lower()]

    # Sort
    sort_by = request.args.get('sort', 'rating')
    if sort_by == 'price_low':
        places.sort(key=lambda x: x.get('entryFee', 0))
    elif sort_by == 'price_high':
        places.sort(key=lambda x: x.get('entryFee', 0), reverse=True)
    elif sort_by == 'reviews':
        places.sort(key=lambda x: x.get('reviewsCount', 0), reverse=True)
    else:  # default rating
        places.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
    return jsonify({
        "success": True,
        "count": len(places),
        "places": places
    })

@app.route('/api/places/<place_id>', methods=['GET'])
def get_place(place_id):
    places = load_destinations()
    place = next((p for p in places if p.get('id') == place_id), None)
    if not place:
        return jsonify({"success": False, "error": "Destination not found"}), 404
    return jsonify({"success": True, "place": place})

@app.route('/api/places/<place_id>/roadmap', methods=['GET'])
def get_place_roadmap(place_id):
    places = load_destinations()
    place = next((p for p in places if p.get('id') == place_id), None)
    if not place:
        return jsonify({"success": False, "error": "Destination not found"}), 404
    return jsonify({
        "success": True,
        "placeId": place_id,
        "placeName": place.get('name'),
        "howToReach": place.get('howToReach', {}),
        "itineraries": place.get('itineraries', []),
        "thingsToDo": place.get('thingsToDo', []),
        "nearbyHotels": place.get('nearbyHotels', []),
        "nearbyPlaces": place.get('nearbyPlaces', [])
    })

@app.route('/api/bookings', methods=['GET', 'POST'])
def handle_bookings():
    bookings = load_bookings()
    
    if request.method == 'GET':
        bookings.sort(key=lambda x: x.get('bookedAt', ''), reverse=True)
        return jsonify({"success": True, "count": len(bookings), "bookings": bookings})
        
    if request.method == 'POST':
        data = request.get_json() or {}
        
        required_fields = ['placeId', 'placeName', 'tierName', 'totalAmount', 'travelDate', 'customerName', 'customerEmail']
        for field in required_fields:
            if not data.get(field):
                return jsonify({"success": False, "error": f"Missing required field: {field}"}), 400
                
        booking_code = f"IN-{str(uuid.uuid4().hex[:6]).upper()}"
        
        new_booking = {
            "id": booking_code,
            "placeId": data.get('placeId'),
            "placeName": data.get('placeName'),
            "placeLocation": data.get('placeLocation', ''),
            "placeImage": data.get('placeImage', ''),
            "tierId": data.get('tierId', 'std'),
            "tierName": data.get('tierName'),
            "unitPrice": float(data.get('unitPrice', 0)),
            "quantity": int(data.get('quantity', 1)),
            "subtotal": float(data.get('subtotal', 0)),
            "serviceFee": float(data.get('serviceFee', 30.0)),
            "discount": float(data.get('discount', 0)),
            "totalAmount": float(data.get('totalAmount', 0)),
            "currency": data.get('currency', 'INR'),
            "travelDate": data.get('travelDate'),
            "timeSlot": data.get('timeSlot', '09:00 AM - Morning Slot'),
            "customerName": data.get('customerName'),
            "customerEmail": data.get('customerEmail'),
            "customerPhone": data.get('customerPhone', ''),
            "specialRequests": data.get('specialRequests', ''),
            "status": "Confirmed",
            "bookedAt": datetime.now(timezone.utc).isoformat(),
            "qrCodeData": f"WP-BHARAT:{booking_code}:{data.get('placeId')}:{data.get('travelDate')}:CONFIRMED"
        }
        
        bookings.insert(0, new_booking)
        save_bookings(bookings)
        
        return jsonify({
            "success": True,
            "message": "Ticket successfully confirmed!",
            "booking": new_booking
        }), 201

@app.route('/api/bookings/<booking_id>', methods=['DELETE', 'PATCH'])
def manage_single_booking(booking_id):
    bookings = load_bookings()
    booking_idx = next((i for i, b in enumerate(bookings) if b.get('id') == booking_id), None)
    
    if booking_idx is None:
        return jsonify({"success": False, "error": "Booking not found"}), 404
        
    if request.method == 'DELETE':
        permanent = request.args.get('purge', 'false').lower() == 'true'
        if permanent:
            removed = bookings.pop(booking_idx)
            save_bookings(bookings)
            return jsonify({"success": True, "message": "Booking deleted", "booking": removed})
        else:
            bookings[booking_idx]['status'] = 'Cancelled'
            save_bookings(bookings)
            return jsonify({"success": True, "message": "Booking cancelled", "booking": bookings[booking_idx]})
            
    if request.method == 'PATCH':
        updates = request.get_json() or {}
        booking = bookings[booking_idx]
        
        if 'travelDate' in updates:
            booking['travelDate'] = updates['travelDate']
        if 'timeSlot' in updates:
            booking['timeSlot'] = updates['timeSlot']
            
        booking['qrCodeData'] = f"WP-BHARAT:{booking['id']}:{booking.get('placeId')}:{booking.get('travelDate')}:RESCHEDULED"
        save_bookings(bookings)
        return jsonify({"success": True, "message": "Booking rescheduled successfully", "booking": booking})

@app.route('/api/places', methods=['POST'])
def add_new_place():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    state = data.get('state', '').strip()
    
    if not name or not state:
        return jsonify({"success": False, "error": "Name and state are required"}), 400
        
    places = load_destinations()
    slug = f"{name.lower().replace(' ', '-')[:25]}-{uuid.uuid4().hex[:4]}"
    hero_image = data.get('heroImage') or "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=1200&q=80"
    
    new_place = {
        "id": slug,
        "name": name,
        "state": state,
        "region": data.get('region', 'North India'),
        "category": data.get('category', 'Heritage & Forts'),
        "tagline": data.get('tagline', f"Explore the majestic beauty of {name}, {state}"),
        "rating": float(data.get('rating', 4.9)),
        "reviewsCount": int(data.get('reviewsCount', 100)),
        "priceLevel": data.get('priceLevel', '₹₹'),
        "entryFee": float(data.get('entryFee', 100)),
        "currency": "INR",
        "bestTimeToVisit": data.get('bestTimeToVisit', 'October to March'),
        "weather": {"temp": "22°C", "condition": "Pleasant & Clear", "icon": "sun"},
        "coordinates": {
            "lat": float(data.get('lat', 26.9124)),
            "lng": float(data.get('lng', 75.7873))
        },
        "heroImage": hero_image,
        "gallery": [hero_image, "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1000&q=80"],
        "description": data.get('description', f"A wonderful tourist destination in {state}, India offering magnificent sights and culture."),
        "howToReach": {
            "flight": f"Nearest airport connecting {name} with domestic flights from major Indian hubs.",
            "train": f"Major railway station serving {name} with express trains.",
            "road": f"Well-connected via National Highways and state buses."
        },
        "itineraries": [
            {
                "duration": "1-2 Days (Highlights)",
                "plan": [
                    {"day": "Day 1", "title": "Iconic Sights & Sunset", "activities": f"Visit the primary landmark of {name} and enjoy the sunset viewpoint."},
                    {"day": "Day 2", "title": "Local Culture & Cuisine", "activities": f"Experience local street food, cultural markets, and historic temples."}
                ]
            }
        ],
        "thingsToDo": [f"Explore the historical monuments of {name}", f"Sample famous local delicacies of {state}", "Visit scenic photo viewpoints"],
        "ticketTiers": [
            {"id": f"{slug}-std", "name": "General Monument Entry Pass", "price": float(data.get('entryFee', 100)), "desc": "Standard admission ticket"}
        ],
        "nearbyHotels": [
            {
                "id": f"h-{slug}-1",
                "name": f"Grand {name} Heritage Palace",
                "stars": 4,
                "rating": 4.8,
                "distance": "1 km from center",
                "pricePerNight": 4500,
                "currency": "INR",
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Traditional Architecture", "Complimentary Breakfast", "Free Wi-Fi", "Parking"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": f"p-{slug}-1",
                "name": f"{name} Heritage Bazaar",
                "category": "Historic Market & Local Handicrafts",
                "distance": "500 m walk",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=800&q=80",
                "description": f"Vibrant bustling marketplace of {name} filled with local spices and crafts."
            }
        ]
    }
    
    places.insert(0, new_place)
    save_destinations(places)
    
    return jsonify({
        "success": True,
        "message": f"'{name}' added successfully!",
        "place": new_place
    }), 201

@app.route('/api/stats', methods=['GET'])
def get_stats():
    places = load_destinations()
    bookings = load_bookings()
    active_bookings = [b for b in bookings if b.get('status') == 'Confirmed']
    total_revenue = sum(float(b.get('totalAmount', 0)) for b in active_bookings)
    
    total_reviews = sum(p.get('reviewsCount', 0) for p in places)
    avg_rating = round(sum(p.get('rating', 0) for p in places) / max(len(places), 1), 2)
    states = len(set(p.get('state', '') for p in places))
    
    return jsonify({
        "success": True,
        "stats": {
            "totalDestinations": len(places),
            "totalBookings": len(bookings),
            "confirmedBookings": len(active_bookings),
            "totalRevenue": round(total_revenue, 2),
            "totalReviews": total_reviews,
            "averageRating": avg_rating,
            "supportedStates": states
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting BharatYatra India Tourist Place Finder on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
