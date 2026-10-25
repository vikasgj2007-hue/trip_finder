import json
import os

india_bookings = [
    {
        "id": "IN-849201",
        "placeId": "jaipur-rajasthan",
        "placeName": "Jaipur (The Pink City)",
        "placeLocation": "Rajasthan, India",
        "placeImage": "https://images.unsplash.com/photo-1603262110263-fb010d6b63d4?auto=format&fit=crop&w=800&q=80",
        "tierId": "jp-std",
        "tierName": "Composite Monument Pass",
        "unitPrice": 300,
        "quantity": 2,
        "subtotal": 600,
        "serviceFee": 40,
        "discount": 50,
        "totalAmount": 590,
        "currency": "INR",
        "travelDate": "2026-11-15",
        "timeSlot": "09:30 AM - Morning Heritage Slot",
        "customerName": "Aarav Sharma",
        "customerEmail": "aarav.sharma@gmail.com",
        "customerPhone": "+91 98765 43210",
        "specialRequests": "Audio guide in Hindi and English",
        "status": "Confirmed",
        "bookedAt": "2026-10-24T12:30:00Z",
        "qrCodeData": "WP-BHARAT:IN-849201:JAIPUR:2026-11-15:VERIFIED"
    },
    {
        "id": "IN-632194",
        "placeId": "kerala-munnar-backwaters",
        "placeName": "Munnar & Alleppey Backwaters",
        "placeLocation": "Kerala, India",
        "placeImage": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80",
        "tierId": "kl-houseboat",
        "tierName": "Alleppey Day Houseboat Cruise",
        "unitPrice": 6500,
        "quantity": 1,
        "subtotal": 6500,
        "serviceFee": 150,
        "discount": 500,
        "totalAmount": 6150,
        "currency": "INR",
        "travelDate": "2026-12-05",
        "timeSlot": "12:00 PM - Afternoon Houseboat Departure",
        "customerName": "Pooja Nair",
        "customerEmail": "pooja.nair@yahoo.com",
        "customerPhone": "+91 94471 23456",
        "specialRequests": "Traditional Kerala vegetarian sadhya meals requested",
        "status": "Confirmed",
        "bookedAt": "2026-10-23T09:15:00Z",
        "qrCodeData": "WP-BHARAT:IN-632194:KERALA:2026-12-05:VERIFIED"
    }
]

with open(os.path.join("data", "bookings.json"), "w", encoding="utf-8") as f:
    json.dump(india_bookings, f, indent=2, ensure_ascii=False)

print("Updated data/bookings.json with Indian reservations.")
