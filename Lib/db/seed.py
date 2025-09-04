from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Lib.Models import Dogs, Locations, Care_types, Care_events
from datetime import datetime

engine = create_engine('sqlite:///dogs.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    try:
        session.query(Care_events).delete()
        session.query(Dogs).delete()
        session.query(Care_types).delete()
        session.query(Locations).delete()
        session.commit()

        locations = [
            Locations(kennel_number=111, population=5),
            Locations(kennel_number=112, population=5),
            Locations(kennel_number=113, population=5),
            Locations(kennel_number=114, population=5)
        ]
        
        session.add_all(locations)
        session.commit()
        
        care_types = [
            Care_types(name="Exercise", description="consists of walks, playtime (fetch, tag of war), purposeful activities (running, swimming, hiking)", default_interval_days=1),
            Care_types(name="Vet care", description="Consists of vaccinations, parasite prevention, routine checkup and sick care", default_interval_days=0),
            Care_types(name="Therapies", description="consists of physical therapy, acupuncture, massage", default_interval_days=1)
        ]
        
        session.add_all(care_types)
        session.commit()

        dogs = [
            Dogs(
                created_at=datetime(2025, 8, 4, 8, 5, 12), 
                name="Guten", 
                breed="German Shepherd", 
                date_of_birth=datetime(2025, 8, 4).date(), 
                location_id=1, 
                last_attended_to=datetime(2025, 8, 4, 8, 5, 12), 
                notes="born with no abnormalities"
            ),
            Dogs(
                created_at=datetime(2025, 8, 7, 10, 6, 12), 
                name="Snow", 
                breed="Pitbull", 
                date_of_birth=datetime(2025, 8, 7).date(), 
                location_id=2, 
                last_attended_to=datetime(2025, 8, 4, 8, 5, 12), 
                notes="needs special attention"
            ),
            Dogs(
                created_at=datetime(2025, 8, 8, 9, 8, 12), 
                name="Khalisi", 
                breed="husky", 
                date_of_birth=datetime(2025, 8, 4).date(), 
                location_id=1, 
                last_attended_to=datetime(2025, 8, 4, 5, 5, 12), 
                notes="new born, keep warm"
            ),
            Dogs(
                created_at=datetime(2025, 8, 12, 4, 10, 12), 
                name="Groot", 
                breed="chiwawa", 
                date_of_birth=datetime(2025, 8, 1).date(), 
                location_id=3, 
                last_attended_to=datetime(2025, 8, 12, 8, 5, 12), 
                notes="born with no abnormalities"
            ),
            Dogs(
                created_at=datetime(2025, 8, 2, 8, 15, 12), 
                name="Bizzy", 
                breed="German Shepherd", 
                date_of_birth=datetime(2025, 8, 1).date(), 
                location_id=2, 
                last_attended_to=datetime(2025, 8, 12, 8, 5, 12), 
                notes="has a huge appetite, give supplements"
            )
        ]

        session.add_all(dogs)
        session.commit()
        
        care_events = [
            Care_events(
                dog_id=1, 
                name="walk", 
                care_type_id=1,
                perfomed_at=datetime(2025, 8, 12, 8, 5, 12), 
                details="take the dog for a 2hr walk", 
                notes="have breaks in between"
            ),
            Care_events(
                dog_id=2, 
                name="playtime", 
                care_type_id=1,
                perfomed_at=datetime(2025, 8, 12, 11, 5, 12), 
                details="let the dog play for 2hrs", 
                notes="choose the toys from the collection"
            ),
            Care_events(
                dog_id=4, 
                name="massage", 
                care_type_id=3,
                perfomed_at=datetime(2025, 8, 12, 8, 5, 12), 
                details="let the masseuse give a 3hr massage", 
                notes="you have the option of using hot stones. he can take it"
            )
        ]
        
        session.add_all(care_events)
        session.commit()
        
        print("Database seeded successfully!")
        
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()