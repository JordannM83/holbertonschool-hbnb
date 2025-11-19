#!/usr/bin/env python3
"""Reset places and re-insert with amenities"""

from app import create_app
from app.models.place import PlaceModel
from app.persistence.repository import SQLAlchemyRepository

app = create_app()

with app.app_context():
    place_repo = SQLAlchemyRepository(PlaceModel)
    
    # Get all places
    all_places = place_repo.get_all()
    
    print(f"Deleting {len(all_places)} existing places...")
    for place in all_places:
        place_repo.delete(place.id)
    
    print("All places deleted. Run insert_test_data.py to re-insert with amenities.")
