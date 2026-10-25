import json
import os
from datetime import datetime

sample_bookings = [
    {
        "id": "TK-849201",
        "placeId": "santorini-caldera",
        "placeName": "Santorini Caldera & Oia Village",
        "placeLocation": "Santorini, Greece",
        "placeImage": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=800&q=80",
        "tierId": "st-sunset",
        "tierName": "VIP Sunset Cliffside Terrace Access",
        "unitPrice": 55,
        "quantity": 2,
        "subtotal": 110,
        "serviceFee": 6.5,
        "discount": 10,
        "totalAmount": 106.5,
        "currency": "USD",
        "travelDate": "2026-11-15",
        "timeSlot": "17:30 - Sunset Session",
        "customerName": "Elena Vance",
        "customerEmail": "elena.vance@wanderpulse.travel",
        "customerPhone": "+1 (555) 382-9012",
        "specialRequests": "Cliffside terrace table if possible",
        "status": "Confirmed",
        "bookedAt": "2026-10-22T14:30:00Z",
        "qrCodeData": "WP-TICKET:TK-849201:SAN-CALDERA:2026-11-15:CONFIRMED"
    },
    {
        "id": "TK-632194",
        "placeId": "kyoto-arashiyama",
        "placeName": "Arashiyama Bamboo Forest & Tenryu-ji",
        "placeLocation": "Kyoto, Japan",
        "placeImage": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=800&q=80",
        "tierId": "kyo-vip",
        "tierName": "Early Bird Sunrise Rickshaw & Tea Experience",
        "unitPrice": 85,
        "quantity": 1,
        "subtotal": 85,
        "serviceFee": 5.0,
        "discount": 0,
        "totalAmount": 90.0,
        "currency": "USD",
        "travelDate": "2026-12-05",
        "timeSlot": "06:30 - Early Morning Tour",
        "customerName": "Marcus Sterling",
        "customerEmail": "marcus.sterling@gmail.com",
        "customerPhone": "+44 7911 123456",
        "specialRequests": "Vegetarian matcha sweets preferred",
        "status": "Confirmed",
        "bookedAt": "2026-10-23T09:15:00Z",
        "qrCodeData": "WP-TICKET:TK-632194:KYO-ARASHI:2026-12-05:CONFIRMED"
    }
]

with open(os.path.join("data", "bookings.json"), "w", encoding="utf-8") as f:
    json.dump(sample_bookings, f, indent=2, ensure_ascii=False)

print("Created data/bookings.json successfully")
