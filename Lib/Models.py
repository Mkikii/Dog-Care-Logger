from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine = create_engine("sqlite:///dogs.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)



class Dogs(Base):
    __tablename__ = "Dogs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now)
    name = Column(String(50), nullable=False, unique=True)
    breed = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    location_id = Column(Integer, ForeignKey('Locations.id'), nullable=False)
    last_attended_to = Column(DateTime)
    notes = Column(Text)

    location = relationship('Locations', back_populates='dogs')
    care_events = relationship('Care_events', back_populates='dog')
    
    @property
    def validated_name(self):
        return self.name
    
    @validated_name.setter
    def validated_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty")
        if len(value) > 50:
            raise ValueError("Name cannot exceed 50 characters")
        self.name = value.strip()
        
       

class Locations(Base):
    __tablename__ = "Locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    kennel_number = Column(Integer, unique=True, nullable=False)
    population = Column(Integer)

    dogs = relationship('Dogs', back_populates='location')
    

class Care_types(Base):
    __tablename__ = "Care_types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text)
    default_interval_days = Column(Integer)

    care_events = relationship('Care_events', back_populates='care_type')    
    
    @property
    def validated_name(self):
        return self.name
    
    @validated_name.setter
    def validated_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty")
        if len(value) > 50:
            raise ValueError("Name cannot exceed 50 characters")
        self.name = value.strip()




class Care_events(Base):
    __tablename__ = "Care_events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column (String (50), nullable = False, unique = True)
    dog_id = Column(Integer, ForeignKey('Dogs.id'), nullable=False)
    care_type_id = Column(Integer, ForeignKey('Care_types.id'))
    perfomed_at = Column(DateTime, default=datetime.now)
    details = Column(Text)
    notes = Column(Text)

    dog = relationship('Dogs', back_populates='care_events')
    care_type = relationship('Care_types', back_populates='care_events')


def create_database():
    Base.metadata.create_all(engine)
    print("Database and Tables created successfully")

if __name__ == "__main__":
    create_database()
    

Base.metadata.create_all(bind=engine)


session = Session()    