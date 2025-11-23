#!/usr/bin/env python3
"""Insert test data into the database"""

from app import create_app
from app.models.user import UserModel
from app.models.amenity import AmenityModel
from app.models.place import PlaceModel
from app.models.review import ReviewModel
from app.persistence.repository import SQLAlchemyRepository
from datetime import datetime
import uuid

app = create_app()

with app.app_context():
    user_repo = SQLAlchemyRepository(UserModel)
    amenity_repo = SQLAlchemyRepository(AmenityModel)
    place_repo = SQLAlchemyRepository(PlaceModel)
    review_repo = SQLAlchemyRepository(ReviewModel)
    
    # Create users with different names
    users_data = [
        {
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'email': 'alice@hbnb.io',
            'password': 'alice1234',
            'is_admin': True
        },
        {
            'first_name': 'Bob',
            'last_name': 'Smith',
            'email': 'bob@hbnb.io',
            'password': 'bob1234',
            'is_admin': False
        },
        {
            'first_name': 'Charlie',
            'last_name': 'Brown',
            'email': 'charlie@hbnb.io',
            'password': 'charlie1234',
            'is_admin': False
        },
        {
            'first_name': 'Diana',
            'last_name': 'Martinez',
            'email': 'diana@hbnb.io',
            'password': 'diana1234',
            'is_admin': False
        },
        {
            'first_name': 'Emma',
            'last_name': 'Wilson',
            'email': 'emma@hbnb.io',
            'password': 'emma1234',
            'is_admin': False
        }
    ]
    
    users = []
    for user_data in users_data:
        existing_user = user_repo.get_by_attribute('email', user_data['email'])
        if not existing_user:
            password = user_data.pop('password')
            user = UserModel(**user_data)
            user.hash_password(password)
            user_repo.add(user)
            users.append(user)
            print(f"User created: {user.first_name} {user.last_name} ({user.email})")
        else:
            users.append(existing_user)
            print(f"User already exists: {existing_user.first_name} {existing_user.last_name}")
    
    # Create amenities
    amenities_data = [
        {'id': '2767d121-c1b4-4d16-a816-0f5113ab06d0', 'name': 'WiFi'},
        {'id': 'bcf813cf-1fd0-4a7f-b69d-d4167331aaa1', 'name': 'Swimming Pool'},
        {'id': '32561383-c728-4ba3-9fd2-cb7ceab79fca', 'name': 'Air Conditioning'},
        {'id': str(uuid.uuid4()), 'name': 'Kitchen'},
        {'id': str(uuid.uuid4()), 'name': 'Parking'},
    ]
    
    amenities = []
    for amenity_data in amenities_data:
        existing_amenity = amenity_repo.get_by_attribute('name', amenity_data['name'])
        if not existing_amenity:
            amenity = AmenityModel(id=amenity_data['id'], name=amenity_data['name'])
            amenity_repo.add(amenity)
            amenities.append(amenity)
            print(f"Amenity created: {amenity.name}")
        else:
            amenities.append(existing_amenity)
            print(f"Amenity already exists: {existing_amenity.name}")
    
    # Create sample places
    places_data = [
        {
            'title': 'Cozy Apartment in Paris',
            'description': 'Beautiful apartment in the heart of Paris with amazing views of the Eiffel Tower. Perfect for couples or small families.',
            'price': 95.00,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'owner_id': users[0].id,  # Alice
            'amenity_ids': [amenities[0].id, amenities[2].id, amenities[3].id]  # WiFi, AC, Kitchen
        },
        {
            'title': 'Beachfront Villa in Miami',
            'description': 'Luxurious villa right on the beach with private pool and stunning ocean views. Ideal for a relaxing vacation.',
            'price': 350.00,
            'latitude': 25.7617,
            'longitude': -80.1918,
            'owner_id': users[0].id,  # Alice
            'amenity_ids': [amenities[0].id, amenities[1].id, amenities[2].id, amenities[4].id]  # WiFi, Pool, AC, Parking
        },
        {
            'title': 'Mountain Cabin in Colorado',
            'description': 'Rustic cabin surrounded by nature with breathtaking mountain views. Great for hiking enthusiasts.',
            'price': 45.00,
            'latitude': 39.7392,
            'longitude': -104.9903,
            'owner_id': users[1].id,  # Bob
            'amenity_ids': [amenities[0].id, amenities[3].id, amenities[4].id]  # WiFi, Kitchen, Parking
        },
        {
            'title': 'Modern Loft in New York',
            'description': 'Stylish loft in Manhattan with contemporary design and close to all major attractions.',
            'price': 200.00,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'owner_id': users[1].id,  # Bob
            'amenity_ids': [amenities[0].id, amenities[2].id]  # WiFi, AC
        },
        {
            'title': 'Charming Cottage in London',
            'description': 'Quaint cottage in a quiet neighborhood with easy access to public transport and city center.',
            'price': 9.00,
            'latitude': 51.5074,
            'longitude': -0.1278,
            'owner_id': users[0].id,  # Alice
            'amenity_ids': [amenities[0].id, amenities[3].id]  # WiFi, Kitchen
        },
    ]
    
    places = []
    for place_data in places_data:
        existing_place = place_repo.get_by_attribute('title', place_data['title'])
        if not existing_place:
            # Get amenity objects before creating place
            amenity_ids = place_data.pop('amenity_ids')
            place_amenities = [amenity_repo.get(aid) for aid in amenity_ids]
            
            # Create place with amenities assigned
            place = PlaceModel(**place_data)
            place.amenities = place_amenities
            
            # Add to database
            place_repo.add(place)
            places.append(place)
            print(f"Place created: {place.title} (${place.price}/night) with {len(place_amenities)} amenities")
        else:
            places.append(existing_place)
            print(f"Place already exists: {existing_place.title}")
    
    # Create sample reviews
    reviews_data = [
        {
            'place_id': places[0].id,  # Paris Apartment
            'user_id': users[1].id,    # Bob reviews Alice's place
            'text': 'Amazing apartment with stunning views! The location is perfect for exploring Paris.',
            'rating': 5
        },
        {
            'place_id': places[0].id,  # Paris Apartment
            'user_id': users[2].id,    # Charlie reviews Alice's place
            'text': 'Great place, very clean and comfortable. Highly recommend!',
            'rating': 5
        },
        {
            'place_id': places[1].id,  # Miami Villa
            'user_id': users[3].id,    # Diana reviews Alice's place
            'text': 'Absolutely beautiful villa! The pool and beach access are incredible.',
            'rating': 5
        },
        {
            'place_id': places[2].id,  # Colorado Cabin
            'user_id': users[0].id,    # Alice reviews Bob's place
            'text': 'Perfect getaway for nature lovers. The mountain views are breathtaking!',
            'rating': 5
        },
        {
            'place_id': places[2].id,  # Colorado Cabin
            'user_id': users[4].id,    # Emma reviews Bob's place
            'text': 'Cozy and rustic, exactly what we were looking for. Great hiking trails nearby.',
            'rating': 4
        },
        {
            'place_id': places[3].id,  # New York Loft
            'user_id': users[2].id,    # Charlie reviews Bob's place
            'text': 'Modern and stylish loft in a great location. Walking distance to everything!',
            'rating': 5
        },
        {
            'place_id': places[4].id,  # London Cottage
            'user_id': users[3].id,    # Diana reviews Alice's place
            'text': 'Charming cottage in a quiet area. Easy to get around London from here.',
            'rating': 4
        }
    ]
    
    for review_data in reviews_data:
        # Check if review already exists
        existing_reviews = [r for r in review_repo.get_all() 
                          if r.place_id == review_data['place_id'] and r.user_id == review_data['user_id']]
        if not existing_reviews:
            review = ReviewModel(**review_data)
            review_repo.add(review)
            print(f"Review created: {users[[u.id for u in users].index(review_data['user_id'])].first_name} reviewed {places[[p.id for p in places].index(review_data['place_id'])].title}")
        else:
            print(f"Review already exists")
    
    print("\nTest data insertion completed!")
    print("\n5 users created with different names")
    print("5 places created with amenities")
    print("7 reviews added across multiple places")
    print("\nYou can login with any of these accounts:")
    print("  Alice (admin): alice@hbnb.io / alice1234")
    print("  Bob: bob@hbnb.io / bob1234")
    print("  Charlie: charlie@hbnb.io / charlie1234")
    print("  Diana: diana@hbnb.io / diana1234")
    print("  Emma: emma@hbnb.io / emma1234")
