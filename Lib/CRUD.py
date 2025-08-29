from Models import Dogs, Locations, Care_types, Care_events, session

#add new Dog
def add_new_Dog (created_at, name, breed, date_of_birth, location_id,  last_attended_to,  notes):
  new_dog = Dogs(created_at = created_at, name = name, breed = breed, date_of_birth = date_of_birth, location_id = location_id,   last_attended_to = last_attended_to, notes = notes )
  session.add(new_dog)
  session.commit()
  return new_dog


#add new Location
def add_new_Location ( kennel_number, population): 

  new_location = Locations (kennel_number =kennel_number, population = population) 
  session.add(new_location)
  session.commit()
  return new_location

#add new Care Type
def add_new_Care_Type (name, description, default_interval_days ):
  new_care_type = Care_types (name = name, description = description, default_interval_days = default_interval_days)
  session.add(new_care_type)
  session.commit()
  return new_care_type

#add new Care Event
def add_new_Care_Event (dog_id, name , care_type_id, perfomed_at, details, notes):
  new_care_event = Care_events (dog_id = dog_id, name = name, care_type_id = care_type_id,perfomed_at = perfomed_at, details = details, notes = notes  )
  session.add(new_care_event)
  session.commit()
  return new_care_event

