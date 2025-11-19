#!/usr/bin/env python3
"""Insert test data into the database"""

from app import create_app
from app.models.user import UserModel
from app.models.amenity import AmenityModel
from app.models.place import PlaceModel
from app.persistence.repository import SQLAlchemyRepository
from datetime import datetime
import uuid

app = create_app()

with app.app_context():
    user_repo = SQLAlchemyRepository(UserModel)
    amenity_repo = SQLAlchemyRepository(AmenityModel)
    place_repo = SQLAlchemyRepository(PlaceModel)
    
    # Check if admin already exists
    existing_admin = user_repo.get_by_attribute('email', 'admin@hbnb.io')
    
    if not existing_admin:
        print("Creating admin user...")
        # Create admin user with hashed password
        admin = UserModel(
            id='36c9050e-ddd3-4c3b-9731-9f487208bbc1',
            first_name='Admin',
            last_name='HBnB',
            email='admin@hbnb.io',
            is_admin=True
        )
        admin.hash_password('admin1234')  # Hash the password
        user_repo.add(admin)
        print(f"Admin user created: {admin.email}")
    else:
        print("Admin user already exists")
        admin = existing_admin
    
    # Check if regular user exists
    existing_user = user_repo.get_by_attribute('email', 'user@hbnb.io')
    
    if not existing_user:
        print("Creating regular user...")
        user = UserModel(
            id='36c9050e-ddd3-4c3b-9731-9f487208bbc2',
            first_name='User',
            last_name='HBnB',
            email='user@hbnb.io',
            is_admin=False
        )
        user.hash_password('user1234')  # Hash the password
        user_repo.add(user)
        print(f"Regular user created: {user.email}")
    else:
        print("Regular user already exists")
        user = existing_user
    
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
            'price': 90.00,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'owner_id': admin.id,
            'amenity_ids': [amenities[0].id, amenities[2].id, amenities[3].id]  # WiFi, AC, Kitchen
        },
        {
            'title': 'Beachfront Villa in Miami',
            'description': 'Luxurious villa right on the beach with private pool and stunning ocean views. Ideal for a relaxing vacation.',
            'price': 350.00,
            'latitude': 25.7617,
            'longitude': -80.1918,
            'owner_id': admin.id,
            'amenity_ids': [amenities[0].id, amenities[1].id, amenities[2].id, amenities[4].id]  # WiFi, Pool, AC, Parking
        },
        {
            'title': 'Mountain Cabin in Colorado',
            'description': 'Rustic cabin surrounded by nature with breathtaking mountain views. Great for hiking enthusiasts.',
            'price': 45.00,
            'latitude': 39.7392,
            'longitude': -104.9903,
            'owner_id': user.id,
            'amenity_ids': [amenities[0].id, amenities[3].id, amenities[4].id]  # WiFi, Kitchen, Parking
        },
        {
            'title': 'Modern Loft in New York',
            'description': 'Stylish loft in Manhattan with contemporary design and close to all major attractions.',
            'price': 200.00,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'owner_id': user.id,
            'amenity_ids': [amenities[0].id, amenities[2].id]  # WiFi, AC
        },
        {
            'title': 'Charming Cottage in London',
            'description': 'Quaint cottage in a quiet neighborhood with easy access to public transport and city center.',
            'price': 9.00,
            'latitude': 51.5074,
            'longitude': -0.1278,
            'owner_id': admin.id,
            'amenity_ids': [amenities[0].id, amenities[3].id]  # WiFi, Kitchen
        },
    ]
    
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
            print(f"Place created: {place.title} (${place.price}/night) with {len(place_amenities)} amenities")
        else:
            print(f"Place already exists: {existing_place.title}")
    
    print("\nTest data insertion completed!")
    print("\nYou can now login with:")
    print("  Email: admin@hbnb.io")
    print("  Password: admin1234")
    print("  OR")
    print("  Email: user@hbnb.io")
    print("  Password: user1234")
