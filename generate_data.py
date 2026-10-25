import json
import os

destinations = [
    {
        "id": "santorini-caldera",
        "name": "Santorini Caldera & Oia Village",
        "city": "Santorini",
        "country": "Greece",
        "region": "Europe",
        "category": "Islands & Coast",
        "rating": 4.95,
        "reviewsCount": 2420,
        "priceLevel": "$$$",
        "tagline": "Cobalt blue domes, whitewashed cliffs, and world-famous Aegean sunsets",
        "description": "Perched on volcanic cliffs soaring 300 meters above the azure Aegean Sea, Santorini is the jewel of the Cyclades. Oia is renowned for its labyrinthine marble alleys, cliffside cave houses, blue-domed churches, and panoramic views of sunsets over the sunken volcanic caldera.",
        "bestTimeToVisit": "Late April to early November",
        "weather": {"temp": "24°C", "condition": "Sunny & Breezy", "icon": "sun"},
        "coordinates": {"lat": 36.4618, "lng": 25.3753},
        "entryFee": 25,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Sunset Point at Oia Castle", "Amoudi Bay Seafood Docks", "Caldera Catamaran Cruise", "Akrotiri Archaeological Ruins"],
        "ticketTiers": [
            {"id": "st-std", "name": "Caldera Historic Trail & Audio Tour", "price": 25, "desc": "Self-guided access to historic footpath with multi-language GPS audio guide"},
            {"id": "st-sunset", "name": "VIP Sunset Cliffside Terrace Access", "price": 55, "desc": "Reserved sunset viewing lounge seat with local Assyrtiko wine tasting"},
            {"id": "st-cruise", "name": "Luxury Catamaran & Volcanic Springs Pass", "price": 120, "desc": "Full 5-hour sailing tour with Greek BBQ lunch and snorkeling gear"}
        ],
        "nearbyHotels": [
            {
                "id": "h-san-1",
                "name": "Canaves Oia Suites & Spa",
                "stars": 5,
                "rating": 4.9,
                "distance": "0.2 km from village center",
                "pricePerNight": 580,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Infinity Caldera Pool", "Private Cave Jacuzzis", "Complimentary Gourmet Breakfast", "Free Valet & WiFi"]
            },
            {
                "id": "h-san-2",
                "name": "Charisma Suites Oia",
                "stars": 5,
                "rating": 4.8,
                "distance": "0.4 km from sunset point",
                "pricePerNight": 490,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Windmill Views", "Sunset Cocktail Bar", "Spa Treatments", "Airport Shuttles"]
            },
            {
                "id": "h-san-3",
                "name": "Aisling Micro Hotel Oia",
                "stars": 4,
                "rating": 4.7,
                "distance": "0.6 km from pedestrian strip",
                "pricePerNight": 260,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Rooftop Sunbed Terrace", "Breakfast In Bed", "Express Concierge", "Free Wi-Fi"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-san-1",
                "name": "Amoudi Bay Harbor",
                "category": "Scenic Fishing Harbor & Taverns",
                "distance": "300 steps below Oia (800 m)",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=800&q=80",
                "description": "Picturesque cove beneath red volcanic rocks lined with authentic fresh octopus taverns."
            },
            {
                "id": "p-san-2",
                "name": "Fira to Oia Caldera Hiking Path",
                "category": "Scenic Trekking Trail",
                "distance": "Starts right in Oia (10.5 km trail)",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
                "description": "One of the world's most spectacular coastal cliff hikes tracing the volcanic rim."
            },
            {
                "id": "p-san-3",
                "name": "Red Beach (Akrotiri)",
                "category": "Natural Phenomenon Beach",
                "distance": "16 km (25 min drive)",
                "rating": 4.6,
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
                "description": "Dramatic crimson pulverized lava cliffs meeting deep turquoise waters."
            }
        ]
    },
    {
        "id": "kyoto-arashiyama",
        "name": "Arashiyama Bamboo Forest & Tenryu-ji",
        "city": "Kyoto",
        "country": "Japan",
        "region": "Asia",
        "category": "Culture & Nature",
        "rating": 4.92,
        "reviewsCount": 3150,
        "priceLevel": "$$",
        "tagline": "Whispering emerald bamboo canopies and thousand-year Zen sanctuaries",
        "description": "Located in western Kyoto, the Arashiyama Bamboo Grove is recognized by Japan's Ministry of the Environment as one of the '100 Soundscapes of Japan'. Walking beneath the towering bamboo stalks reaching high into the sky while gentle winds rustle creates an ethereal, meditative atmosphere.",
        "bestTimeToVisit": "March - May (Cherry Blossoms) & Oct - Nov (Autumn Foliage)",
        "weather": {"temp": "19°C", "condition": "Mild & Pleasant", "icon": "cloud-sun"},
        "coordinates": {"lat": 35.0170, "lng": 135.6713},
        "entryFee": 18,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1528360983277-13d401cdc186?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Togetsukyo Moon-Crossing Bridge", "Tenryu-ji UNESCO Temple", "Iwatayama Monkey Park", "Sagano Romantic Train"],
        "ticketTiers": [
            {"id": "kyo-std", "name": "Bamboo Trail & Tenryu-ji Temple Pass", "price": 18, "desc": "Standard admission to grove path and famous zen landscape garden"},
            {"id": "kyo-fast", "name": "Skip-the-Queue + Audio Heritage Tour", "price": 32, "desc": "Express access with curated 12-chapter cultural storytelling companion"},
            {"id": "kyo-vip", "name": "Early Bird Sunrise Rickshaw & Tea Experience", "price": 85, "desc": "Private jinrikisha carriage through empty morning paths + matcha session"}
        ],
        "nearbyHotels": [
            {
                "id": "h-kyo-1",
                "name": "Suiran Luxury Collection Hotel Kyoto",
                "stars": 5,
                "rating": 4.9,
                "distance": "0.3 km from bamboo grove entrance",
                "pricePerNight": 450,
                "image": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Private Onsen Hot Spring", "Riverside Kaiseki Dining", "Japanese Garden", "Traditional Yukatas"]
            },
            {
                "id": "h-kyo-2",
                "name": "Hoshinoya Kyoto Ryokan",
                "stars": 5,
                "rating": 4.95,
                "distance": "1.1 km (Accessible via boat shuttle)",
                "pricePerNight": 620,
                "image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Private Wooden Boat Transfer", "Floating Pavilion Lounge", "Forest Tea Salon", "Fine Dining"]
            },
            {
                "id": "h-kyo-3",
                "name": "The GrandWest Arashiyama",
                "stars": 4,
                "rating": 4.6,
                "distance": "0.7 km from Hankyu Arashiyama Station",
                "pricePerNight": 190,
                "image": "https://images.unsplash.com/photo-1566665797739-1674de7a421a?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Bicycle Rentals Included", "Family Suites with Tatami", "Modern Cafe & Bakery", "Free WiFi"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-kyo-1",
                "name": "Togetsukyo Moon-Crossing Bridge",
                "category": "Historic Landmark & Scenic River",
                "distance": "450 m (6 min walk)",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1536657464919-892534f60d6e?auto=format&fit=crop&w=800&q=80",
                "description": "400-year-old wooden bridge spanning the Katsura River with maple tree mountain backdrop."
            },
            {
                "id": "p-kyo-2",
                "name": "Iwatayama Monkey Park",
                "category": "Wildlife Sanctuary & City Lookout",
                "distance": "900 m (15 min uphill walk)",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
                "description": "Home to 120 free-roaming Japanese macaque snow monkeys overlooking the Kyoto basin."
            },
            {
                "id": "p-kyo-3",
                "name": "Okochi Sanso Villa & Zen Garden",
                "category": "Traditional Estate & Tea Garden",
                "distance": "200 m from Bamboo trail exit",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1528360983277-13d401cdc186?auto=format&fit=crop&w=800&q=80",
                "description": "Former residence of silent movie star Denjiro Okochi, featuring peaceful moss gardens."
            }
        ]
    },
    {
        "id": "banff-lake-louise",
        "name": "Banff National Park & Lake Louise",
        "city": "Alberta",
        "country": "Canada",
        "region": "Americas",
        "category": "Mountains & Adventure",
        "rating": 4.96,
        "reviewsCount": 4200,
        "priceLevel": "$$$",
        "tagline": "Turquoise glacial waters framed by soaring rugged peaks of the Canadian Rockies",
        "description": "Canada's first national park is a UNESCO World Heritage site of awe-inspiring wilderness. Lake Louise is celebrated worldwide for its surreal vibrant turquoise water, fed by glacial silt, set against Mount Victoria and the majestic Victoria Glacier.",
        "bestTimeToVisit": "June - September (Hiking & Canoeing) or Dec - March (Skiing)",
        "weather": {"temp": "16°C", "condition": "Crisp Alpine Clear", "icon": "cloud-sun"},
        "coordinates": {"lat": 51.4254, "lng": -116.1773},
        "entryFee": 30,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Moraine Lake & Valley of Ten Peaks", "Fairmont Chateau Lake Louise", "Lake Agnes Historic Teahouse", "Plain of Six Glaciers Trail"],
        "ticketTiers": [
            {"id": "banff-std", "name": "Banff Parks Discovery Pass", "price": 30, "desc": "Full-day park vehicle & trail admission pass with park map"},
            {"id": "banff-canoe", "name": "Glacial Canoe Rental & Shuttle Package", "price": 75, "desc": "Lake Louise priority shuttle bus pass + 1-hour red canoe rental on the lake"},
            {"id": "banff-gondola", "name": "Banff Alpine Gondola & Skywalk Pass", "price": 62, "desc": "Summit gondola ticket to Sulphur Mountain boardwalk with 360° mountain vistas"}
        ],
        "nearbyHotels": [
            {
                "id": "h-bnf-1",
                "name": "Fairmont Chateau Lake Louise",
                "stars": 5,
                "rating": 4.9,
                "distance": "Direct lakeside frontage (0 km)",
                "pricePerNight": 520,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Glacier View Rooms", "Heated Indoor Pool & Spa", "5 On-site Alpine Restaurants", "Ski Concierge"]
            },
            {
                "id": "h-bnf-2",
                "name": "Post Hotel & Spa Lake Louise",
                "stars": 4,
                "rating": 4.8,
                "distance": "3.5 km from the lake",
                "pricePerNight": 340,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Rustic Pine Fireplaces", "Award-Winning Wine Cellar", "Saltwater Pool", "Free Shuttle"]
            },
            {
                "id": "h-bnf-3",
                "name": "Lake Louise Inn",
                "stars": 3,
                "rating": 4.4,
                "distance": "4 km from lakeshore",
                "pricePerNight": 175,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Hot Tubs Under Pines", "Pizza & Pub Eatery", "Heated Ski Lockers", "Pet Friendly"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-bnf-1",
                "name": "Moraine Lake & Ten Peaks",
                "category": "Glacial Lake & Viewpoint",
                "distance": "14 km scenic shuttle ride",
                "rating": 5.0,
                "image": "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?auto=format&fit=crop&w=800&q=80",
                "description": "Deep cobalt glacial waters featured on the Canadian twenty-dollar bill."
            },
            {
                "id": "p-bnf-2",
                "name": "Lake Agnes Teahouse Trail",
                "category": "Mountain Hike & Forest Tea House",
                "distance": "3.6 km hike from Lake Louise",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
                "description": "Charming 1905 log teahouse perched 2,135m high serving freshly baked scones and teas."
            },
            {
                "id": "p-bnf-3",
                "name": "Johnston Canyon Ice & Falls",
                "category": "Limestone Canyon & Waterfalls",
                "distance": "32 km along Bow Valley Parkway",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&w=800&q=80",
                "description": "Suspended canyon catwalks tracing roaring turquoise waterfalls through limestone chasms."
            }
        ]
    },
    {
        "id": "taj-mahal-agra",
        "name": "Taj Mahal & Mehtab Bagh Gardens",
        "city": "Agra",
        "country": "India",
        "region": "Asia",
        "category": "Historical Heritage & Wonder",
        "rating": 4.94,
        "reviewsCount": 5120,
        "priceLevel": "$",
        "tagline": "The eternal white marble monument of love and Mughal architectural perfection",
        "description": "An immense mausoleum of white ivory marble commissioned in 1632 by the Mughal emperor Shah Jahan to house the tomb of his favorite wife, Mumtaz Mahal. Renowned as the jewel of Muslim art in India and one of the universally admired masterpieces of the world's heritage.",
        "bestTimeToVisit": "October to March (Pleasant weather & crisp sunrise mist)",
        "weather": {"temp": "26°C", "condition": "Golden Sunlight", "icon": "sun"},
        "coordinates": {"lat": 27.1751, "lng": 78.0421},
        "entryFee": 15,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1587135941948-670b381f08ce?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Sunrise Marble Reflections", "Yamuna Riverside Courtyard", "Mehtab Bagh Moonlit Garden", "Agra Fort Mughal Palaces"],
        "ticketTiers": [
            {"id": "taj-std", "name": "Monument & Garden Admission Pass", "price": 15, "desc": "Standard entry to monument grounds, outer courtyards and charbagh gardens"},
            {"id": "taj-express", "name": "Mausoleum Main Dome + Fast-Track Entry", "price": 24, "desc": "Express gate security pass with access inside the main dome cenotaph and shoe covers"},
            {"id": "taj-sunrise", "name": "VIP Sunrise Guided Tour with Heritage Historian", "price": 45, "desc": "First light 5:45 AM private entry with certified ASI historian and golf cart transfer"}
        ],
        "nearbyHotels": [
            {
                "id": "h-taj-1",
                "name": "The Oberoi Amarvilas Agra",
                "stars": 5,
                "rating": 4.97,
                "distance": "600 m from Taj East Gate",
                "pricePerNight": 510,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Unobstructed Taj Views from Every Room", "Royal Mughal Spa", "Moorish Courtyard Pool", "Private Golf Cart Drop"]
            },
            {
                "id": "h-taj-2",
                "name": "ITC Mughal, A Luxury Collection Resort",
                "stars": 5,
                "rating": 4.7,
                "distance": "2.8 km from Taj Mahal",
                "pricePerNight": 160,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["35 Acres of Sprawling Gardens", "Kaya Kalp Royal Spa", "Peshawri Dining", "Tennis Courts"]
            },
            {
                "id": "h-taj-3",
                "name": "Tajview, Agra - IHCL SeleQtions",
                "stars": 4,
                "rating": 4.5,
                "distance": "2.1 km from Taj Mahal",
                "pricePerNight": 95,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Rooftop Cafe with Taj Views", "Swimming Pool", "Heritage Architecture", "Complimentary Breakfast"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-taj-1",
                "name": "Mehtab Bagh (Moonlight Garden)",
                "category": "Historic Charbagh & Sunset Point",
                "distance": "1.2 km directly across Yamuna river",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=800&q=80",
                "description": "Mughal garden perfectly aligned with the Taj across the river for magical sunset photography."
            },
            {
                "id": "p-taj-2",
                "name": "Agra Fort (Red Sandstone Citadel)",
                "category": "UNESCO World Heritage Fort",
                "distance": "2.5 km (8 min drive)",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1587135941948-670b381f08ce?auto=format&fit=crop&w=800&q=80",
                "description": "Massive 16th-century Mughal fortress of red sandstone with courtyards and royal chambers."
            },
            {
                "id": "p-taj-3",
                "name": "Fatehpur Sikri Imperial City",
                "category": "Ghost City & Mughal Architecture",
                "distance": "36 km day trip excursion",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=800&q=80",
                "description": "Preserved 16th-century deserted imperial capital founded by Akbar the Great."
            }
        ]
    },
    {
        "id": "amalfi-positano",
        "name": "Amalfi Coast & Positano",
        "city": "Salerno",
        "country": "Italy",
        "region": "Europe",
        "category": "Islands & Coast",
        "rating": 4.93,
        "reviewsCount": 3890,
        "priceLevel": "$$$$",
        "tagline": "Pastel villages tumbling into sapphire waters alongside lemon groves and coastal cliffs",
        "description": "A vertical dreamscape where colorful pastel houses cling to cliff faces dropping dramatically into the Tyrrhenian Sea. Celebrated for sparkling waters, terraced lemon orchards, world-class Mediterranean dining, and enchanting coastal drives.",
        "bestTimeToVisit": "May to October (Sun bathing & Mediterranean boat tours)",
        "weather": {"temp": "27°C", "condition": "Warm Coastal Sunshine", "icon": "sun"},
        "coordinates": {"lat": 40.6281, "lng": 14.4850},
        "entryFee": 20,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Spiaggia Grande Beach", "Path of the Gods (Sentiero degli Dei)", "Ravello Villa Rufolo Gardens", "Capri Blue Grotto Day Sail"],
        "ticketTiers": [
            {"id": "amf-std", "name": "Coast Ferry Hopper Day Pass", "price": 28, "desc": "Unlimited hop-on hop-off ferry boat ticket between Positano, Amalfi, and Minori"},
            {"id": "amf-gods", "name": "Path of the Gods Guided Trek + Lunch", "price": 65, "desc": "Expert alpine-coastal guide along mountain cliffs ending with farmhouse cheese & wine"},
            {"id": "amf-boat", "name": "Capri & Emerald Grotto Yacht Tour", "price": 145, "desc": "Full-day luxury Italian speedboat cruise with swimming stops, prosecco, and snorkeling"}
        ],
        "nearbyHotels": [
            {
                "id": "h-amf-1",
                "name": "Le Sirenuse Positano",
                "stars": 5,
                "rating": 4.96,
                "distance": "Heart of Positano cliffs (0.1 km)",
                "pricePerNight": 780,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Champagne & Oyster Bar", "Pool Terrace with Cliffside Views", "Michelin-starred La Sponda", "Private Vintage Wooden Boat"]
            },
            {
                "id": "h-amf-2",
                "name": "Hotel Poseidon Positano",
                "stars": 4,
                "rating": 4.8,
                "distance": "0.3 km from beach center",
                "pricePerNight": 420,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Heated Outdoor Pool", "Il Tridente Restaurant", "Rooftop Solarium", "Free Continental Breakfast"]
            },
            {
                "id": "h-amf-3",
                "name": "Villa Franca Positano",
                "stars": 5,
                "rating": 4.9,
                "distance": "0.5 km uphill panoramic",
                "pricePerNight": 610,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["360° Sky Bar", "Spa & Wellness Hammam", "Shuttle Service to Pier", "Luxury Suites"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-amf-1",
                "name": "Sentiero degli Dei (Path of the Gods)",
                "category": "Cliffside Hiking Trail",
                "distance": "Trailhead at Bomerano (8 km)",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
                "description": "Heavenly trail walking high above the clouds overlooking the entire Amalfi peninsula and Capri."
            },
            {
                "id": "p-amf-2",
                "name": "Villa Rufolo & Ravello Gardens",
                "category": "Historic Villa & Botanical Vista",
                "distance": "12 km up in the hills",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=800&q=80",
                "description": "Incredible cascading terrace gardens that inspired composer Richard Wagner."
            },
            {
                "id": "p-amf-3",
                "name": "Fiordo di Furore",
                "category": "Hidden Fjord & Secluded Cove",
                "distance": "7 km down coastal road",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
                "description": "A deep rocky coastal fissure bridged overhead, sheltering a tiny fishing village beach."
            }
        ]
    },
    {
        "id": "machu-picchu-peru",
        "name": "Machu Picchu & The Sacred Valley",
        "city": "Cusco",
        "country": "Peru",
        "region": "Americas",
        "category": "Historical Heritage & Wonder",
        "rating": 4.97,
        "reviewsCount": 4680,
        "priceLevel": "$$$",
        "tagline": "The legendary lost citadel of the Incas perched amidst cloud-draped Andean peaks",
        "description": "Built in the 15th century and abandoned during the Spanish conquest, Machu Picchu remained hidden to the outside world until 1911. Its sophisticated dry-stone walls fuse huge blocks without mortar, offering mystical views of the Huayna Picchu mountain rising behind.",
        "bestTimeToVisit": "May to October (Dry Andean winter season)",
        "weather": {"temp": "18°C", "condition": "Misty Cloud Forest", "icon": "cloud"},
        "coordinates": {"lat": -13.1631, "lng": -72.5450},
        "entryFee": 45,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1589802829985-817e51171b92?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1509299349698-dd22323b5963?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Temple of the Sun", "Intihuatana Sundial Stone", "Huayna Picchu Summit Hike", "Sun Gate (Inti Punku)"],
        "ticketTiers": [
            {"id": "mp-circuit2", "name": "Classic Circuit 2 Citadel Entry", "price": 45, "desc": "Official pass covering the panoramic upper terrace and main temple sectors"},
            {"id": "mp-huayna", "name": "Citadel Entry + Huayna Picchu Climb", "price": 70, "desc": "Citadel admission plus steep climbing permit for the iconic rear peak and Moon Temple"},
            {"id": "mp-full", "name": "All-Inclusive Expedition: Vistadome Train + Bus + Guide", "price": 185, "desc": "Panoramic glass-roof train from Cusco/Ollanta, roundtrip mountain bus, and personal private guide"}
        ],
        "nearbyHotels": [
            {
                "id": "h-mp-1",
                "name": "Sanctuary Lodge, A Belmond Hotel",
                "stars": 5,
                "rating": 4.95,
                "distance": "Directly adjacent to Citadel Gates (0 m)",
                "pricePerNight": 890,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Immediate Gate Access", "Orchid Gardens", "Tinkuy Andean Cuisine", "Shaman Blessing Ceremony"]
            },
            {
                "id": "h-mp-2",
                "name": "Inkaterra Machu Picchu Pueblo Hotel",
                "stars": 5,
                "rating": 4.9,
                "distance": "Aguas Calientes (6 km bus to citadel)",
                "pricePerNight": 440,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["12 Acres of Cloud Forest", "Spectacled Bear Sanctuary", "Andean Spa with Eucalyptus", "River View Casitas"]
            },
            {
                "id": "h-mp-3",
                "name": "Tierra Viva Machu Picchu",
                "stars": 4,
                "rating": 4.6,
                "distance": "Aguas Calientes riverside (5.8 km)",
                "pricePerNight": 160,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Buffet Breakfast from 5 AM", "Mountain Views", "Train Station Porter", "Free Oxygen Bar"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-mp-1",
                "name": "Sun Gate (Inti Punku)",
                "category": "Inca Trail Vantage Point",
                "distance": "2 km hike from citadel ruins",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=800&q=80",
                "description": "Historic mountain pass where hikers finishing the 4-day Inca Trail get their first glimpse of Machu Picchu."
            },
            {
                "id": "p-mp-2",
                "name": "Maras Salt Mines (Salineras)",
                "category": "Pre-Incan Evaporation Ponds",
                "distance": "Sacred Valley excursion (42 km)",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1589802829985-817e51171b92?auto=format&fit=crop&w=800&q=80",
                "description": "Over 3,000 terraced geometric ponds extracting pink Andean salt since ancient times."
            },
            {
                "id": "p-mp-3",
                "name": "Moray Concentric Terraces",
                "category": "Inca Agricultural Laboratory",
                "distance": "Sacred Valley (48 km)",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1509299349698-dd22323b5963?auto=format&fit=crop&w=800&q=80",
                "description": "Mysterious amphitheater-like circular depressions creating varying microclimates."
            }
        ]
    },
    {
        "id": "bali-ubud-tegallalang",
        "name": "Ubud & Tegallalang Rice Terraces",
        "city": "Bali",
        "country": "Indonesia",
        "region": "Asia",
        "category": "Tropical & Spiritual",
        "rating": 4.91,
        "reviewsCount": 3310,
        "priceLevel": "$",
        "tagline": "Verdant emerald stepped hills, sacred water temples, and traditional Balinese culture",
        "description": "Tegallalang forms the most iconic emerald landscape of Bali, utilizing the traditional subak cooperative irrigation system developed in the 8th century. Surrounded by jungle valleys, sacred monkey sanctuaries, artisan wood carving villages, and tranquil yoga retreats.",
        "bestTimeToVisit": "April to October (Dry season with sunny days)",
        "weather": {"temp": "28°C", "condition": "Tropical Warmth", "icon": "sun"},
        "coordinates": {"lat": -8.4343, "lng": 115.2798},
        "entryFee": 10,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1555400038-63f5ba517a47?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Alas Harum Jungle Swings", "Sacred Monkey Forest Sanctuary", "Tirta Empul Holy Water Temple", "Campuhan Ridge Nature Walk"],
        "ticketTiers": [
            {"id": "bali-std", "name": "Terrace Walk & Subak Heritage Ticket", "price": 10, "desc": "Access to walk along stepped rice ridges and view traditional irrigation bridges"},
            {"id": "bali-swing", "name": "Extreme Jungle Swing & Sky Walk Combo", "price": 28, "desc": "Admission + single high swing flight over the canyon canopy and bird-nest photo spots"},
            {"id": "bali-day", "name": "Full-Day Ubud Spiritual & Waterfalls Tour", "price": 60, "desc": "Private car with driver visiting Monkey Forest, Tirta Empul purification, and Tegenungan Falls"}
        ],
        "nearbyHotels": [
            {
                "id": "h-bal-1",
                "name": "Mandapa, a Ritz-Carlton Reserve",
                "stars": 5,
                "rating": 4.98,
                "distance": "Ayung River Valley (4.2 km)",
                "pricePerNight": 750,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Private Patih (Butler) Service", "Ayung Riverfront Villas", "Organic Permaculture Farm", "Holistic Wellness Spa"]
            },
            {
                "id": "h-bal-2",
                "name": "Komaneka at Bisma Ubud",
                "stars": 5,
                "rating": 4.9,
                "distance": "Ubud Center (6 km to terraces)",
                "pricePerNight": 290,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["33-Meter Hilltop Lap Pool", "Rainforest Canopy Views", "Afternoon Balinese Tea Included", "Free Town Shuttle"]
            },
            {
                "id": "h-bal-3",
                "name": "Adiwana Resort Jetan",
                "stars": 4,
                "rating": 4.7,
                "distance": "1.5 km from Tegallalang terraces",
                "pricePerNight": 140,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Infinity Valley Pool", "Tejas Ayurvedic Spa", "Floating Breakfast Available", "Yoga Deck"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-bal-1",
                "name": "Sacred Monkey Forest Sanctuary",
                "category": "Nature Reserve & Hindu Temples",
                "distance": "9 km south in central Ubud",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=800&q=80",
                "description": "Lush jungle sanctuary housing over 1,000 long-tailed macaques among moss-covered 14th-century shrines."
            },
            {
                "id": "p-bal-2",
                "name": "Tirta Empul Holy Spring Water Temple",
                "category": "Sacred Hindu Purification Springs",
                "distance": "5.5 km northeast",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1555400038-63f5ba517a47?auto=format&fit=crop&w=800&q=80",
                "description": "Legendary crystal-clear spring pools where pilgrims partake in the Melukat spiritual cleansing ritual."
            },
            {
                "id": "p-bal-3",
                "name": "Campuhan Ridge Walk",
                "category": "Scenic Hilltop Trek",
                "distance": "8 km southwest",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
                "description": "A sweeping grassy ridge trail between two rivers offering lush panoramas of Ubud's river gorges."
            }
        ]
    },
    {
        "id": "swiss-alps-matterhorn",
        "name": "Zermatt & The Matterhorn",
        "city": "Valais",
        "country": "Switzerland",
        "region": "Europe",
        "category": "Mountains & Adventure",
        "rating": 4.98,
        "reviewsCount": 3540,
        "priceLevel": "$$$$",
        "tagline": "The legendary pyramid tooth of the Alps crowned with perpetual snow and glacier lakes",
        "description": "Rising 4,478 meters above sea level, the jagged pyramid peak of the Matterhorn is one of the most photographed mountains on Earth. The car-free alpine village of Zermatt below offers world-class skiing, scenic cogwheel railways, and crystal-clear reflection lakes.",
        "bestTimeToVisit": "July - Sept (Alpine wildflower hikes) & Dec - April (World cup skiing)",
        "weather": {"temp": "12°C", "condition": "Alpine Breeze", "icon": "cloud-sun"},
        "coordinates": {"lat": 45.9765, "lng": 7.7491},
        "entryFee": 35,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1502784444187-359ac186c5bb?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Gornergrat Cogwheel Train (3,089m)", "Riffelsee Matterhorn Reflection Lake", "Matterhorn Glacier Paradise (3,883m)", "Car-Free Alpine Village"],
        "ticketTiers": [
            {"id": "sw-gorner", "name": "Gornergrat Bahn Summit Cogwheel Pass", "price": 68, "desc": "Roundtrip historic electric mountain railway to 3,135m summit platform with 29 four-thousander peaks"},
            {"id": "sw-glacier", "name": "Matterhorn Glacier Paradise 360° Pass", "price": 95, "desc": "Highest cable car in Europe, glacier ice palace walk-through, and summit cinema lounge"},
            {"id": "sw-5lakes", "name": "5 Lakes Walk & Sunnegga Funicular", "price": 42, "desc": "Sunnegga underground train access for the famous alpine reflection lakes hike"}
        ],
        "nearbyHotels": [
            {
                "id": "h-sw-1",
                "name": "The Omnia Mountain Lodge",
                "stars": 5,
                "rating": 4.97,
                "distance": "Elevated rock above Zermatt center (0.3 km)",
                "pricePerNight": 690,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Indoor/Outdoor Pool Facing Matterhorn", "Finnish Sauna & Steam Bath", "Fireplace Lounges", "Michelin Dining"]
            },
            {
                "id": "h-sw-2",
                "name": "Grand Hotel Zermatterhof",
                "stars": 5,
                "rating": 4.88,
                "distance": "0.1 km from Zermatt Bahnhofstrasse",
                "pricePerNight": 540,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Horse-Drawn Carriage Pickup", "Vita Borni Alpine Spa", "Smokers Lounge", "Ski School Desk"]
            },
            {
                "id": "h-sw-3",
                "name": "Hotel Butterfly, BW Signature Collection",
                "stars": 3,
                "rating": 4.5,
                "distance": "0.2 km from Gornergrat Train Station",
                "pricePerNight": 210,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Traditional Swiss Fondue Dinners", "Finnish Sauna", "Mountain Balconies", "Free High-Speed WiFi"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-sw-1",
                "name": "Riffelsee Alpine Lake",
                "category": "Glacial Reflection Tarn",
                "distance": "Rotenboden station (10 min stroll)",
                "rating": 5.0,
                "image": "https://images.unsplash.com/photo-1502784444187-359ac186c5bb?auto=format&fit=crop&w=800&q=80",
                "description": "Still, crystal-clear alpine waters casting a mirror-perfect inverted reflection of the Matterhorn."
            },
            {
                "id": "p-sw-2",
                "name": "Gorner Gorge (Gornerschlucht)",
                "category": "Glacial Chasm & Wooden Catwalks",
                "distance": "1.5 km walk from village",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
                "description": "Dramatic wooden walkways pinned to towering rock walls over rushing turquoise glacial rapids."
            },
            {
                "id": "p-sw-3",
                "name": "Hinterdorf Old Village Quarter",
                "category": "Historic 16th-Century Wooden Chalets",
                "distance": "In Zermatt center",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=800&q=80",
                "description": "Ancient larch-wood barns and storehouses perched on circular flat stone pillars designed to deter mice."
            }
        ]
    },
    {
        "id": "paris-eiffel-tower",
        "name": "Eiffel Tower & The Seine River",
        "city": "Paris",
        "country": "France",
        "region": "Europe",
        "category": "Urban Heritage & Romance",
        "rating": 4.90,
        "reviewsCount": 6800,
        "priceLevel": "$$$",
        "tagline": "The City of Light's iconic iron lady soaring above Champ de Mars and river boulevards",
        "description": "Designed by Gustave Eiffel for the 1889 World's Fair, the Eiffel Tower remains one of the world's most recognizable symbols. At dusk, thousands of golden bulbs illuminate the 330-meter spire, sparkling every hour on the hour over the glittering Seine.",
        "bestTimeToVisit": "April to June & September to November",
        "weather": {"temp": "21°C", "condition": "Gentle Breeze", "icon": "cloud-sun"},
        "coordinates": {"lat": 48.8584, "lng": 2.2945},
        "entryFee": 32,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1549144511-f099e773c147?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Summit Observation Deck (276m)", "Champ de Mars Garden Picnics", "Seine River Bateaux-Mouches Cruise", "Trocadéro Photo Esplanade"],
        "ticketTiers": [
            {"id": "par-2nd", "name": "Second Floor Panoramic Lift Pass", "price": 24, "desc": "Elevator access to 2nd floor with telescopes, glass floor, and city vistas"},
            {"id": "par-summit", "name": "Full Summit Elevator Fast-Track Pass", "price": 38, "desc": "Priority access right up to the highest 276m summit deck and Gustave Eiffel's restored office"},
            {"id": "par-combo", "name": "Summit Pass + Seine Sunset Champagne Cruise", "price": 68, "desc": "Complete Paris experience: Summit entry plus 1-hour cruise with flute of chilled champagne"}
        ],
        "nearbyHotels": [
            {
                "id": "h-par-1",
                "name": "Shangri-La Paris",
                "stars": 5,
                "rating": 4.96,
                "distance": "0.6 km across the Pont d'Iéna",
                "pricePerNight": 950,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Prince Roland Bonaparte's Palace", "Private Terraces with Direct Eiffel View", "Michelin-starred Shang Palace", "Chi Spa & Pool"]
            },
            {
                "id": "h-par-2",
                "name": "Pullman Paris Tour Eiffel",
                "stars": 4,
                "rating": 4.7,
                "distance": "0.3 km (3 min walk)",
                "pricePerNight": 340,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Balconies Facing Eiffel Spire", "FRAME Brasserie & Organic Garden", "Fitness Lounge", "Metro Proximity"]
            },
            {
                "id": "h-par-3",
                "name": "Hôtel Relais Bosquet Paris",
                "stars": 3,
                "rating": 4.6,
                "distance": "0.8 km near Rue Cler market street",
                "pricePerNight": 190,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Courtyard Garden Patio", "French Bakery Breakfast", "Quiet Rue Cler Neighborhood", "Free High-Speed Wi-Fi"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-par-1",
                "name": "Place du Trocadéro",
                "category": "Fountain Plaza & Iconic Vantage Point",
                "distance": "500 m across the Seine",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
                "description": "The premier high marble esplanade overlooking the Warsaw fountains and Eiffel Tower."
            },
            {
                "id": "p-par-2",
                "name": "Rue Cler Market Street",
                "category": "Artisan Food & Cafe Promenade",
                "distance": "750 m east",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1549144511-f099e773c147?auto=format&fit=crop&w=800&q=80",
                "description": "Quintessential pedestrian cobblestone avenue of fromageries, boulangeries, and outdoor bistros."
            },
            {
                "id": "p-par-3",
                "name": "Musée d'Orsay",
                "category": "Impressionist Art & Beaux-Arts Railway Station",
                "distance": "2.4 km along the Seine embankment",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=800&q=80",
                "description": "World-famous former railway terminus housing masterpiece paintings by Monet, Van Gogh, and Renoir."
            }
        ]
    },
    {
        "id": "maldives-ari-atoll",
        "name": "Ari Atoll & Coral Reefs",
        "city": "South Ari Atoll",
        "country": "Maldives",
        "region": "Asia",
        "category": "Islands & Coast",
        "rating": 4.99,
        "reviewsCount": 2180,
        "priceLevel": "$$$$",
        "tagline": "Crystal lagoons, private overwater bungalows, and year-round whale shark encounters",
        "description": "A tropical marine wonderland consisting of over 105 small coral islands encircled by glowing turquoise lagoons and barrier reefs. South Ari Atoll is celebrated as one of the very few locations on the planet where gentle whale sharks and manta rays can be observed year-round in their natural habitat.",
        "bestTimeToVisit": "November to April (Dry northeast monsoon with calm turquoise seas)",
        "weather": {"temp": "30°C", "condition": "Tropical Paradise", "icon": "sun"},
        "coordinates": {"lat": 3.6667, "lng": 72.8333},
        "entryFee": 50,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Overwater Villa Deck Stargazing", "Whale Shark Snorkel Safaris", "Fluorescent Night Coral Diving", "Sandbank Private Dining"],
        "ticketTiers": [
            {"id": "mld-whaleshark", "name": "Whale Shark & Manta Ray Snorkel Safari", "price": 95, "desc": "Guided speedboat expedition into Marine Protected Area with marine biologist and GoPro videos"},
            {"id": "mld-sunset", "name": "Traditional Dhoni Sunset Dolphin Cruise", "price": 60, "desc": "Cruise into Indian Ocean sunset on handcrafted Maldivian wooden dhoni with fruit & bubbly"},
            {"id": "mld-sandbank", "name": "Exclusive Private Castaway Sandbank Picnic", "price": 140, "desc": "4-hour drop-off on secluded powdery white sandbank surrounded by 360° turquoise lagoon with lunch"}
        ],
        "nearbyHotels": [
            {
                "id": "h-mld-1",
                "name": "LUX* South Ari Atoll Resort & Villas",
                "stars": 5,
                "rating": 4.97,
                "distance": "On island lagoon (0 km)",
                "pricePerNight": 850,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Direct Lagoon Access Steps", "8 World-Class Restaurants", "Overwater Spa Pavilions", "PADI 5-Star Dive Center"]
            },
            {
                "id": "h-mld-2",
                "name": "Conrad Maldives Rangali Island",
                "stars": 5,
                "rating": 4.94,
                "distance": "South Ari Atoll (5 km via boat)",
                "pricePerNight": 920,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Ithaa Undersea Restaurant (5m below)", "Twin Island Retreat", "Private Glass-Floor Pavilions", "Wine Cellar"]
            },
            {
                "id": "h-mld-3",
                "name": "Vilamendhoo Island Resort & Spa",
                "stars": 4,
                "rating": 4.75,
                "distance": "South Ari Atoll (8 km via boat)",
                "pricePerNight": 360,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Spectacular House Reef for Snorkeling", "Overwater Sunset Suites", "All-Inclusive Dining", "Infinity Beach Pool"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-mld-1",
                "name": "South Ari Marine Protected Area (SAMPA)",
                "category": "Whale Shark & Manta Ray Reserve",
                "distance": "Surrounding waters",
                "rating": 5.0,
                "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
                "description": "Global biodiversity sanctuary protected for gentle 10-meter whale sharks feeding near the surface."
            },
            {
                "id": "p-mld-2",
                "name": "Dhigurah Island & Long Beach Spit",
                "category": "Inhabited Island & Pristine Sand Spit",
                "distance": "12 km boat transfer",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
                "description": "Stunning 3-kilometer slender tropical sandbank island with friendly local guesthouses and jungle paths."
            },
            {
                "id": "p-mld-3",
                "name": "Kudarah Thila Underwater Pinnacle",
                "category": "World-Class Scuba Diving Site",
                "distance": "4 km offshore",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=800&q=80",
                "description": "Sunken submarine pinnacle covered in soft pink coral trees and clouds of yellow snapper."
            }
        ]
    },
    {
        "id": "grand-canyon-south-rim",
        "name": "Grand Canyon & South Rim Vistas",
        "city": "Arizona",
        "country": "USA",
        "region": "Americas",
        "category": "Mountains & Adventure",
        "rating": 4.96,
        "reviewsCount": 7400,
        "priceLevel": "$$",
        "tagline": "Two billion years of Earth's geological majesty carved by the wild Colorado River",
        "description": "Measuring 446 kilometers long and up to 29 kilometers wide with a mile-deep chasm, the Grand Canyon overwhelms the senses. The South Rim provides breathtaking cliff viewpoints, the historic Bright Angel trail descending to the canyon floor, and fiery copper sunsets.",
        "bestTimeToVisit": "March to May and September to November",
        "weather": {"temp": "23°C", "condition": "Desert Clear Sky", "icon": "sun"},
        "coordinates": {"lat": 36.0544, "lng": -112.1401},
        "entryFee": 35,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1474044159687-1ee9f3a51722?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1474044159687-1ee9f3a51722?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Mather Point Sunrise Overlook", "Bright Angel Canyon Hike", "Desert View Watchtower", "Helicopter Canyon Flight"],
        "ticketTiers": [
            {"id": "gc-std", "name": "National Park Vehicle & Trail Pass", "price": 35, "desc": "7-day access pass for all park shuttle buses, rim walks, and visitor centers"},
            {"id": "gc-ranger", "name": "Rim Walk with National Park Geologist", "price": 50, "desc": "2.5 hour guided geological trek along the Rim Trail uncovering ancient fossil layers"},
            {"id": "gc-heli", "name": "Imperial 45-Min Helicopter Canyon Flight", "price": 220, "desc": "Breathtaking flight over the Dragon Corridor and North Rim through the canyon's deepest gorges"}
        ],
        "nearbyHotels": [
            {
                "id": "h-gc-1",
                "name": "El Tovar Hotel Grand Canyon",
                "stars": 4,
                "rating": 4.75,
                "distance": "Directly perched on South Rim cliff edge (0 m)",
                "pricePerNight": 380,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["1905 Historic Stone Architecture", "Canyon View Dining Room", "Teddy Roosevelt Suite", "Rim Trail Footstep Access"]
            },
            {
                "id": "h-gc-2",
                "name": "The Grand Hotel at the Grand Canyon",
                "stars": 4,
                "rating": 4.6,
                "distance": "Tusayan (10 km to South Rim gate)",
                "pricePerNight": 220,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Indoor Heated Pool & Hot Tub", "Canyon Star Steakhouse", "Live Western Music", "Park Shuttle Stop"]
            },
            {
                "id": "h-gc-3",
                "name": "Bright Angel Lodge & Cabins",
                "stars": 3,
                "rating": 4.5,
                "distance": "On the Rim near Bright Angel Trailhead",
                "pricePerNight": 160,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Historic Mary Colter Fireplace", "Canyon Fountain Ice Cream", "Trailhead Proximity", "Rustic Log Cabins"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-gc-1",
                "name": "Desert View Watchtower & Mary Colter Vista",
                "category": "Stone Watchtower & East Rim Overlook",
                "distance": "35 km along Desert View Drive",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1474044159687-1ee9f3a51722?auto=format&fit=crop&w=800&q=80",
                "description": "1932 stone tower designed after ancient Ancestral Puebloan towers with inner Hopi murals."
            },
            {
                "id": "p-gc-2",
                "name": "Horseshoe Bend Overlook",
                "category": "Meandering Canyon Bend & 1,000ft Drop",
                "distance": "Page, AZ (180 km day excursion)",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
                "description": "Sensational 270-degree horseshoe-shaped bend of the Colorado River cutting through sandstone cliffs."
            },
            {
                "id": "p-gc-3",
                "name": "Hermit's Rest & Scenic Rim Overlooks",
                "category": "Historical Stone Shelter & Views",
                "distance": "11 km west via park shuttle",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
                "description": "Serene stone grotto with rustic hearth perched right on the westernmost South Rim promontory."
            }
        ]
    },
    {
        "id": "pyramids-giza-egypt",
        "name": "The Great Pyramids of Giza & Sphinx",
        "city": "Cairo",
        "country": "Egypt",
        "region": "Middle East & Africa",
        "category": "Historical Heritage & Wonder",
        "rating": 4.94,
        "reviewsCount": 5900,
        "priceLevel": "$$",
        "tagline": "The last standing Wonder of the Ancient World rising silently from golden desert sands",
        "description": "Built around 2560 BC as eternal resting places for pharaohs Khufu, Khafre, and Menkaure. Guarded by the monumental lion-bodied Great Sphinx, the Giza plateau represents one of human civilization's greatest architectural and mathematical triumphs.",
        "bestTimeToVisit": "October to April (Cool winter desert weather)",
        "weather": {"temp": "25°C", "condition": "Golden Desert Sun", "icon": "sun"},
        "coordinates": {"lat": 29.9792, "lng": 31.1342},
        "entryFee": 20,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1568322445389-f64ac2515020?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["Great Pyramid of Khufu Grand Gallery", "The Enigmatic Great Sphinx", "Panoramic Sunset Camel Caravan", "Grand Egyptian Museum (GEM)"],
        "ticketTiers": [
            {"id": "gz-std", "name": "Giza Plateau & Sphinx General Pass", "price": 20, "desc": "Standard admission to the entire archaeological plateau, valley temple, and Sphinx enclosure"},
            {"id": "gz-inside", "name": "Inside Khufu Pyramid King's Chamber Pass", "price": 45, "desc": "Special interior climbing pass up the ascending passageway into the granite burial room"},
            {"id": "gz-vip", "name": "Sunset Camel Safari + Egyptologist Private Tour", "price": 85, "desc": "2-hour sunset camel ride to remote desert dune panorama with certified university Egyptologist"}
        ],
        "nearbyHotels": [
            {
                "id": "h-gz-1",
                "name": "Marriott Mena House, Cairo",
                "stars": 5,
                "rating": 4.93,
                "distance": "Directly facing Great Pyramid (0.4 km)",
                "pricePerNight": 410,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Direct Balcony Views of Khufu Pyramid", "40 Acres of Palm Oasis Gardens", "139 Pavilion Fine Dining", "Oasis Pool"]
            },
            {
                "id": "h-gz-2",
                "name": "Steigenberger Pyramids Cairo",
                "stars": 5,
                "rating": 4.7,
                "distance": "2.3 km from Giza Entrance",
                "pricePerNight": 185,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Pyramid View Pool Terrace", "Egyptian Lotus Spa", "GEM Museum Proximity", "Airport Shuttle"]
            },
            {
                "id": "h-gz-3",
                "name": "Pyramids Eyes Hotel Giza",
                "stars": 3,
                "rating": 4.6,
                "distance": "0.8 km near Sphinx Gate",
                "pricePerNight": 65,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Rooftop Sunset Lounge & Hookah", "Free Bedouin Tea & Breakfast", "Friendly Local Hosts", "Tour Desk"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-gz-1",
                "name": "Grand Egyptian Museum (GEM)",
                "category": "Mega Museum of Antiquities",
                "distance": "2 km north of Giza Plateau",
                "rating": 4.95,
                "image": "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?auto=format&fit=crop&w=800&q=80",
                "description": "The largest archaeological museum in the world housing the complete King Tutankhamun collection."
            },
            {
                "id": "p-gz-2",
                "name": "Saqqara & Step Pyramid of Djoser",
                "category": "Ancient Necropolis & First Pyramid",
                "distance": "15 km south (25 min drive)",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1568322445389-f64ac2515020?auto=format&fit=crop&w=800&q=80",
                "description": "Dating back 4,700 years, the world's oldest monumental stone building designed by Imhotep."
            },
            {
                "id": "p-gz-3",
                "name": "Khan el-Khalili Historic Bazaar",
                "category": "14th-Century Medieval Souk & Spice Market",
                "distance": "16 km into Old Islamic Cairo",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=800&q=80",
                "description": "Labyrinth of brass lanterns, aromatic spices, silver filigree, and historic El Fishawy tea house."
            }
        ]
    },
    {
        "id": "petra-rose-city",
        "name": "Petra The Rose-Red City",
        "city": "Wadi Musa",
        "country": "Jordan",
        "region": "Middle East & Africa",
        "category": "Historical Heritage & Wonder",
        "rating": 4.96,
        "reviewsCount": 3800,
        "priceLevel": "$$$",
        "tagline": "A mystical Nabataean metropolis carved into blushing pink sandstone canyon walls",
        "description": "Half as old as time, Petra was the thriving desert capital of the Nabataean kingdom over 2,000 years ago. Approached through the narrow Siq canyon fissure, visitors emerge suddenly before the breathtaking 40-meter-high carved Treasury facade glowing rose-pink.",
        "bestTimeToVisit": "March to May & September to November",
        "weather": {"temp": "22°C", "condition": "Desert Breeze", "icon": "sun"},
        "coordinates": {"lat": 30.3285, "lng": 35.4444},
        "entryFee": 70,
        "currency": "USD",
        "heroImage": "https://images.unsplash.com/photo-1579606032822-8356f966144e?auto=format&fit=crop&w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1579606032822-8356f966144e?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1568322445389-f64ac2515020?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1000&q=80",
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80"
        ],
        "highlights": ["The Siq Narrow Gorge", "Al-Khazneh (The Treasury)", "Ad-Deir (The Monastery) 800-Step Climb", "Petra by Night (1,500 Candles)"],
        "ticketTiers": [
            {"id": "pt-std", "name": "Petra 1-Day Archaeological Pass", "price": 70, "desc": "Full-day official admission to the Siq, Treasury, Street of Facades, and Royal Tombs"},
            {"id": "pt-night", "name": "Treasury by Candlelight Night Pass", "price": 28, "desc": "Magical nighttime walk through the candlelit Siq with traditional Bedouin flute music"},
            {"id": "pt-monastery", "name": "All-Day Guided Hike to Ad-Deir Monastery", "price": 110, "desc": "Expert local Bedouin guide to climb the 850 cliff-carved rock steps up to the colossal mountain Monastery"}
        ],
        "nearbyHotels": [
            {
                "id": "h-pt-1",
                "name": "Mövenpick Resort Petra",
                "stars": 5,
                "rating": 4.88,
                "distance": "Directly at Petra Visitor Center Gate (50 m)",
                "pricePerNight": 290,
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Direct Gate Frontage", "Oriental Roof Garden", "Al Iwan Middle Eastern Dining", "Outdoor Heated Pool"]
            },
            {
                "id": "h-pt-2",
                "name": "Petra Bubble Luxotel",
                "stars": 5,
                "rating": 4.92,
                "distance": "Wadi Musa Hills (9 km with shuttle)",
                "pricePerNight": 380,
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Transparent Stargazing Bubble Domes", "Private Hot Tub on Deck", "Bedouin Grill Buffet Included", "Desert Mountain Panoramas"]
            },
            {
                "id": "h-pt-3",
                "name": "Petra Guest House Hotel",
                "stars": 4,
                "rating": 4.7,
                "distance": "At Petra Main Gate entrance",
                "pricePerNight": 170,
                "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
                "amenities": ["Famous Cave Bar (1st-century tomb)", "Direct Trailhead Access", "Piazza Terrace", "Free Wi-Fi"]
            }
        ],
        "nearbyPlaces": [
            {
                "id": "p-pt-1",
                "name": "Ad-Deir (The Monastery)",
                "category": "Colossal Mountain Monolithic Monument",
                "distance": "850 rock steps above city center",
                "rating": 4.95,
                "image": "https://images.unsplash.com/photo-1579606032822-8356f966144e?auto=format&fit=crop&w=800&q=80",
                "description": "Larger than the Treasury at 50 meters wide, tucked high in mountain heights with sweeping views over the Arabah valley."
            },
            {
                "id": "p-pt-2",
                "name": "Little Petra (Siq al-Barid)",
                "category": "Nabataean Caravanserai & Suburb",
                "distance": "9 km north of Petra",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1568322445389-f64ac2515020?auto=format&fit=crop&w=800&q=80",
                "description": "Mini canyon preserving rare ancient painted Hellenistic ceiling frescoes of grapevines and cupid."
            },
            {
                "id": "p-pt-3",
                "name": "Wadi Rum Protected Desert",
                "category": "Valley of the Moon Mars-like Wilderness",
                "distance": "100 km south (1.5 hr drive)",
                "rating": 5.0,
                "image": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=800&q=80",
                "description": "Towering red granite monoliths and sand dunes where Lawrence of Arabia and The Martian were filmed."
            }
        ]
    }
]

with open(os.path.join("data", "destinations.json"), "w", encoding="utf-8") as f:
    json.dump(destinations, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(destinations)} destinations.")
