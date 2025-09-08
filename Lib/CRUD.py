from Models import Dogs, Locations, Care_types, Care_events, session

def add_new_Dog (session, created_at, name, breed, date_of_birth, location_id,  last_attended_to,  notes):
  new_dog = Dogs(created_at = created_at, name = name, breed = breed, date_of_birth = date_of_birth, location_id = location_id,   last_attended_to = last_attended_to, notes = notes )
  session.add(new_dog)
  session.commit()
  return new_dog


#add new Location
def add_new_Location ( session, kennel_number, population): 

  new_location = Locations (kennel_number =kennel_number, population = population) 
  session.add(new_location)
  session.commit()
  return new_location

#add new Care Type
def add_new_Care_Type (session, name, description, default_interval_days ):
  new_care_type = Care_types (name = name, description = description, default_interval_days = default_interval_days)
  session.add(new_care_type)
  session.commit()
  return new_care_type

#add new Care Event
def add_new_Care_Event (session, dog_id, name , care_type_id, perfomed_at, details, notes):
  new_care_event = Care_events (dog_id = dog_id, name = name, care_type_id = care_type_id,perfomed_at = perfomed_at, details = details, notes = notes  )
  session.add(new_care_event)
  session.commit()
  return new_care_event

#delete Dog
def delete_dog_by_id (session, dog_id):
  dog = session.query(Dogs).where(Dogs.id == dog_id).first()
  if dog:
    session.delete(dog)
    session.commit()

#delete Location
def delete_location_by_id (session, location_id):
  location = session.query(Locations).where(Locations.id == location_id).first()
  if location:
    session.delete(location)
    session.commit()    

#delete care_type
def delete_care_type_by_id (session, care_type_id):
  care_type = session.query(Care_types).where(Care_types.id == care_type_id).first()
  if care_type:
    session.delete(care_type)
    session.commit()

#delete care_event
def delete_care_event_by_id (session, care_event_id):
  care_event = session.query(Care_events).where(Care_events.id == care_event_id).first()
  if care_event:
    session.delete(care_event)
    session.commit() 


#find dog by id
def find_dog_by_id(session, dog_id):
  dog = session.query(Dogs).where(Dogs.id == dog_id).first()
  return dog

#find location by id 
def find_location_by_id(session, location_id):
  location = session.query(Locations).where(Locations.id == location_id).first()
  return location


#find care type by id    
def find_care_type_by_id(session, care_type_id ):
  care_type = session.query(Care_types).where(Care_types.id == care_type_id ).first()
  return care_type 


#find care event by id    
def find_care_event_by_id(session, care_event_id ):
  care_event = session.query(Care_events).where(Care_events.id == care_event_id ).first()
  return care_event 
   
#find all dogs
def find_all_dogs():
  dog = session.query(Dogs).all()
  return dog  

#find all locations
def find_all_locations():
  location = session.query(Locations).all()
  return location       
  

#find all care_types
def find_all_care_types():
  care_type = session.query(Care_types).all()
  return care_type

#find all care_events
def find_all_care_events():
  care_event = session.query(Care_events).all()
  return care_event

