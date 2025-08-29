from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Lib.Models import Dogs, Locations, Care_types, Care_events


engine = create_engine('sqlite:///dogs.db')
Session = sessionmaker(bind=engine)
session = Session()


def seed_database():
    # clear existing data
    session.query(Dogs).delete()
    session.query(Locations).delete()
    session.query(Care_types).delete()
    session.query(Care_events).delete()

    # create Dogs
    dogs = [
        Dogs(created_at="2025-08-04 08:05:12", name="Guten", breed="German Shepherd", date_of_birth="2025-08-04", location_id=1, last_attended_to="2025-08-04 08:05:12", notes="born with no abnomalities"),
        Dogs(created_at="2025-08-07 10:06:12", name="Snow", breed="Pitbull", date_of_birth="2025-08-07", location_id=2, last_attended_to="2025-08-04 08:05:12", notes="needs special attention"),
        Dogs(created_at="2025-08-08 09:08:12", name="Khalisi", breed="husky", date_of_birth="2025-08-04", location_id=1, last_attended_to="2025-08-04 05:05:12", notes="new born, keep warm"),
        Dogs(created_at="2025-08-12 04:10:12", name="Groot", breed="chiwawa", date_of_birth="2025-08-01", location_id=3, last_attended_to="2025-08-12 08:05:12", notes="born with no abnomalities"),
        Dogs(created_at="2025-08-02 08:15:12", name="Bizzy", breed="German Shepherd", date_of_birth="2025-08-01", location_id=2, last_attended_to="2025-08-12 08:05:12", notes="has a huge appetite, give suppliments")
    ]

    session.add_all(dogs)
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
        Care_types(name="Exersice", description="consists of walks, playtime (fetch, tag of war), purposeful activities (running, swimming, hiking)", default_interval_days=1),
        Care_types(name="Vet care", description="Consists of vaccinations, parasite prevention, routine checkup and sick care", default_interval_days=0),
        Care_types(name="Therapies", description="consists of physcal therapy, acupuncture, massage", default_interval_days=1)
    ]
    
    session.add_all(care_types)
    session.commit()
    
    care_events = [
        Care_events(dog_id=1, name="walk", care_type_id=2, perfomed_at="2025-08-12 08:05:12", details="take the dog for a 2hr walk", notes="have breaks in between"),
        Care_events(dog_id=2, name="playtime", care_type_id=2, perfomed_at="2025-08-12 11:05:12", details="let the dog play for  2hrs ", notes="choose the toys from the collection"),
        Care_events(dog_id=4, name="massage", care_type_id=3, perfomed_at="2025-08-12 08:05:12", details="let the massuse give a 3hr massage", notes="you have the optioin of using hot stones. he can take it")
    ]
    
    session.add_all(care_events)
    session.commit()