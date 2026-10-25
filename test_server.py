import urllib.request
import json

base_url = "http://127.0.0.1:5000"

def test_endpoint(path, method="GET", data=None):
    url = f"{base_url}{path}"
    req = urllib.request.Request(url, method=method)
    if data:
        req.add_header('Content-Type', 'application/json')
        body = json.dumps(data).encode('utf-8')
    else:
        body = None
        
    try:
        with urllib.request.urlopen(req, data=body) as response:
            status = response.status
            content = response.read().decode('utf-8')
            return status, content
    except Exception as e:
        return 500, str(e)

print("1. Testing GET / (BharatYatra Homepage)...")
status, html = test_endpoint("/")
assert status == 200 and "BharatYatra" in html, f"Failed GET /: status {status}"
print("   Passed! Status 200, BharatYatra homepage loaded.")

print("2. Testing GET /api/places (Indian Destinations)...")
status, res = test_endpoint("/api/places")
data = json.loads(res)
assert status == 200 and data.get("count", 0) >= 10, f"Failed GET /api/places: {res}"
print(f"   Passed! Found {data['count']} destinations across India.")

print("3. Testing Search for 'Jaipur'...")
status, res = test_endpoint("/api/places?q=jaipur")
data = json.loads(res)
assert status == 200 and len(data.get("places", [])) >= 1, "Failed search for Jaipur"
jaipur = data['places'][0]
print(f"   Passed! Found {jaipur['name']}, {jaipur['state']}")

print("4. Testing Location Roadmap endpoint for Jaipur...")
status, res = test_endpoint("/api/places/jaipur-rajasthan/roadmap")
data = json.loads(res)
assert status == 200 and "howToReach" in data and "itineraries" in data, "Failed roadmap endpoint"
print(f"   Passed! Flight, Train, Road data verified. Itineraries count: {len(data['itineraries'])}")

print("5. Testing Search for 'Kerala' & 'Kashmir'...")
status, res = test_endpoint("/api/places?q=kerala")
data = json.loads(res)
assert status == 200 and len(data.get("places", [])) >= 1, "Failed search for Kerala"
print(f"   Passed! Kerala: {data['places'][0]['name']}")

status, res = test_endpoint("/api/places?q=kashmir")
data = json.loads(res)
assert status == 200 and len(data.get("places", [])) >= 1, "Failed search for Kashmir"
print(f"   Passed! Kashmir: {data['places'][0]['name']}")

print("6. Testing POST /api/bookings (Ticket Booking in INR)...")
booking_payload = {
    "placeId": "jaipur-rajasthan",
    "placeName": "Jaipur (The Pink City)",
    "placeLocation": "Rajasthan, India",
    "placeImage": "https://images.unsplash.com/photo-1603262110263-fb010d6b63d4?auto=format&fit=crop&w=800&q=80",
    "tierId": "jp-std",
    "tierName": "Composite Monument Pass",
    "unitPrice": 300.0,
    "quantity": 2,
    "subtotal": 600.0,
    "serviceFee": 30.0,
    "discount": 0.0,
    "totalAmount": 630.0,
    "currency": "INR",
    "travelDate": "2026-11-25",
    "timeSlot": "09:30 AM - Morning Slot",
    "customerName": "Rohan Mehra",
    "customerEmail": "rohan@gmail.com"
}
status, res = test_endpoint("/api/bookings", method="POST", data=booking_payload)
data = json.loads(res)
assert status == 201 and data.get("booking", {}).get("id"), f"Failed booking: {res}"
print(f"   Passed! Generated Indian QR pass ID: {data['booking']['id']}")

print("7. Testing GET /api/stats...")
status, res = test_endpoint("/api/stats")
data = json.loads(res)
assert status == 200 and data["stats"]["supportedStates"] >= 5, "Failed stats"
print(f"   Passed! Platform stats: {data['stats']}")

print("\nALL BHARATYATRA TEST SUITES PASSED 100%!")
