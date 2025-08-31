import click
from datetime import datetime
from CRUD import (add_new_Dog, add_new_Location, add_new_Care_Type, add_new_Care_Event,
delete_dog_by_id, delete_location_by_id, delete_care_type_by_id, delete_care_event_by_id,
find_dog_by_id, find_location_by_id, find_care_type_by_id, find_care_event_by_id,
find_all_dogs, find_all_locations, find_all_care_types, find_all_care_events)


while True:
    try:
        click.clear()
        click.secho("Welcome to Dog Care Logger", fg='green', bold=True)
        click.secho(
            "where every walk, woof, and wellness check gets its moment in the sun!", fg='cyan')
        click.secho("Select an Option to Proceed", fg='yellow', bold=True)

        click.secho("1 DOG MANAGEMENT", fg='yellow')
        click.secho("2 LOCATION MANAGEMENT", fg='yellow')
        click.secho("3 CARE TYPE MANAGEMENT", fg='yellow')
        click.secho("4 CARE EVENT MANAGEMENT", fg='yellow')
        click.secho("0 EXIT APPLICATION", fg='red')

        user_input = click.prompt("Select option", type=int)

        if user_input == 0:
            click.secho(
                "Thank you for using Dog Care Logger! Goodbye!", fg='green')
            break

        elif user_input == 1:
            click.secho("DOG MANAGEMENT OPTIONS", fg='green', bold=True)
            click.secho("1 Add new dog profile", fg='yellow')
            click.secho("2 Find dog by id", fg='yellow')
            click.secho("3 Find all dogs", fg='yellow')
            click.secho("4 Delete dog profile", fg='yellow')
            click.secho("5 Back to main menu", fg='red')

            dog_management_option = click.prompt(
                "Select Dog management option", type=int)

            if dog_management_option == 1:
                click.secho("ADD NEW DOG PROFILE", fg='green', bold=True)
                name = click.prompt("Dog's name")
                breed = click.prompt("Dog's breed")
                date_of_birth_str = click.prompt("Dog's D.O.B (YYYY-MM-DD)")
                date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
                created_at_str = click.prompt("Time created (YYYY-MM-DD HH:MM:SS)")
                created_at = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S")
                last_attended_to_str = click.prompt(
                    "Last time the dog was attended to (YYYY-MM-DD HH:MM:SS)")
                last_attended_to = datetime.strptime(last_attended_to_str, "%Y-%m-%d %H:%M:%S")
                notes = click.prompt("Leave a note")
                location_id = click.prompt("Location ID", type=int)

                add_new_Dog(created_at, name, breed, date_of_birth,
            location_id, last_attended_to, notes)
                click.secho(f'Dog {name} added successfully!', fg='green')

            elif dog_management_option == 2:
                click.secho("FIND DOG BY ID", fg='green', bold=True)
                dog_id = click.prompt("Enter dog ID", type=int)
                dog = find_dog_by_id(dog_id)
                if dog:
                    click.secho(
                        f'Found Dog: {dog.name} (Breed: {dog.breed}, DOB: {dog.date_of_birth})', fg='green')
                else:
                    click.secho("Dog not found", fg='red')

            elif dog_management_option == 3:
                click.secho("FIND ALL DOGS", fg='green', bold=True)
                dogs = find_all_dogs()
                for dog in dogs:
                    click.secho(
                        f'ID: {dog.id} | Name: {dog.name} | Breed: {dog.breed} | DOB: {dog.date_of_birth}', fg='yellow')

            elif dog_management_option == 4:
                click.secho("DELETE DOG", fg='green', bold=True)
                dog_id = click.prompt("Enter dog ID to delete", type=int)
                if click.confirm("Are you sure you want to delete this dog?"):
                    delete_dog_by_id(dog_id)
                    click.secho("Profile deleted successfully!", fg='green')
                else:
                    click.secho("Deletion cancelled", fg='yellow')

            elif dog_management_option == 5:
                continue

            else:
                click.secho("Invalid option!", fg='red')

        elif user_input == 2:
            click.secho("LOCATION MANAGEMENT OPTIONS", fg='green', bold=True)
            click.secho("1 Add new location", fg='yellow')        
            click.secho("2 Find location by id", fg='yellow')
            click.secho("3 Find all locations", fg='yellow')
            click.secho("4 Delete location", fg='yellow')
            click.secho("5 Back to main menu", fg='red')

            location_management = click.prompt(
                "Select location management option", type=int)

            if location_management == 1:
                click.secho("ADD NEW LOCATION", fg='green', bold=True)
                kennel_number = click.prompt("Kennel number")
                population = click.prompt("Population", type=int)
                add_new_Location(kennel_number, population)
                click.secho("Location added successfully!", fg='green')

            elif location_management == 2:
                click.secho("FIND LOCATION BY ID", fg='green', bold=True)
                location_id = click.prompt("Enter location ID", type=int)
                location = find_location_by_id(location_id)
                if location:
                    click.secho(
                        f"Found location: Kennel {location.kennel_number}, Population: {location.population}", fg='green')
                else:
                    click.secho("Location not found", fg='red')

            elif location_management == 3:
                click.secho("FIND ALL LOCATIONS", fg='green', bold=True)
                locations = find_all_locations()
                for location in locations:
                    click.secho(
                        f'ID: {location.id} | Kennel: {location.kennel_number} | Population: {location.population}', fg='yellow')

            elif location_management == 4:
                click.secho("DELETE LOCATION", fg='green', bold=True)
                location_id = click.prompt(
                    "Enter location ID to delete", type=int)
                if click.confirm("Are you sure you want to delete this location?"):
                    delete_location_by_id(location_id)
                    click.secho("Location deleted successfully!", fg='green')
                else:
                    click.secho("Deletion cancelled", fg='yellow')

            elif location_management == 5:
                continue

            else:
                click.secho("Invalid option!", fg='red')

        elif user_input == 3:
            click.secho("CARE TYPE MANAGEMENT OPTIONS", fg='green', bold=True)
            click.secho("1 Add new care type", fg='yellow')
            click.secho("2 Find care type by id", fg='yellow')
            click.secho("3 Find all care types", fg='yellow')
            click.secho("4 Delete care type", fg='yellow')
            click.secho("5 Back to main menu", fg='red')

            care_type_management = click.prompt(
                "Select care type management option", type=int)

            if care_type_management == 1:
                click.secho("ADD NEW CARE TYPE", fg='green', bold=True)
                name = click.prompt("Care type name")
                description = click.prompt("Enter description")
                default_interval_days = click.prompt(
                    "Enter default interval days", type=int)

                add_new_Care_Type(name, description, default_interval_days)
                click.secho(
                    f"Care type '{name}' added successfully!", fg='green')

            elif care_type_management == 2:
                click.secho("FIND CARE TYPE BY ID", fg='green', bold=True)
                care_type_id = click.prompt("Enter care type ID", type=int)
                care_type = find_care_type_by_id(care_type_id)
                if care_type:
                    click.secho(
                        f"Found care type: {care_type.name} (Description: {care_type.description}, Interval: {care_type.default_interval_days} days)", fg='green')
                else:
                    click.secho("Care type not found", fg='red')

            elif care_type_management == 3:
                click.secho("FIND ALL CARE TYPES", fg='green', bold=True)
                care_types = find_all_care_types()
                for care_type in care_types:
                    click.secho(
                        f'ID: {care_type.id} | Name: {care_type.name} | Description: {care_type.description} | Interval: {care_type.default_interval_days} days', fg='yellow')

            elif care_type_management == 4:
                click.secho("DELETE CARE TYPE", fg='green', bold=True)
                care_type_id = click.prompt(
                    "Enter care type ID to delete", type=int)
                if click.confirm("Are you sure you want to delete this care type?"):
                    delete_care_type_by_id(care_type_id)
                    click.secho("Care type deleted successfully!", fg='green')
                else:
                    click.secho("Deletion cancelled", fg='yellow')

            elif care_type_management == 5:
                continue

            else:
                click.secho("Invalid option!", fg='red')

        elif user_input == 4:
            click.secho("CARE EVENT MANAGEMENT OPTIONS", fg='green', bold=True)
            click.secho("1 Add new care event", fg='yellow')
            click.secho("2 Find care event by id", fg='yellow')
            click.secho("3 Find all care events", fg='yellow')
            click.secho("4 Delete care event", fg='yellow')
            click.secho("5 Back to main menu", fg='red')

            care_event_management = click.prompt(
                "Select care event management option", type=int)

            if care_event_management == 1:
                click.secho("ADD NEW CARE EVENT", fg='green', bold=True)
                name = click.prompt("Enter name of event")
                performed_at = click.prompt(
                    "Enter date and time when event was performed  (YYYY-MM-DD HH:MM:SS)")
                details = click.prompt(
                    "Enter details", default="", show_default=False)
                notes = click.prompt(
                    "Do you have anything to note?", default="", show_default=False)
                dog_id = click.prompt("Enter dog ID", type=int)
                care_type_id = click.prompt("Enter care type ID", type=int)
                

                add_new_Care_Event(name, performed_at, details,
                                   notes, dog_id, care_type_id,)
                click.secho(
                    f"Care event '{name}' added successfully!", fg='green')

            elif care_event_management == 2:
                click.secho("FIND CARE EVENT BY ID", fg='green', bold=True)
                care_event_id = click.prompt("Enter care event ID", type=int)
                care_event = find_care_event_by_id(care_event_id)
                if care_event:
                    click.secho(
                        f"Found care event: {care_event.name} (Performed at: {care_event.performed_at}, Details: {care_event.details})", fg='green')
                else:
                    click.secho("Care event not found", fg='red')

            elif care_event_management == 3:
                click.secho("FIND ALL CARE EVENTS", fg='green', bold=True)
                care_events = find_all_care_events()
                for care_event in care_events:
                    click.secho(
                        f'ID: {care_event.id} | Name: {care_event.name} | Performed at: {care_event.performed_at} | Details: {care_event.details}', fg='yellow')

            elif care_event_management == 4:
                click.secho("DELETE CARE EVENT", fg='green', bold=True)
                care_event_id = click.prompt(
                    "Enter care event ID to delete", type=int)
                if click.confirm("Are you sure you want to delete this care event?"):
                    delete_care_event_by_id(care_event_id)
                    click.secho("Care event deleted successfully!", fg='green')
                else:
                    click.secho("Deletion cancelled", fg='yellow')

            elif care_event_management == 5:
                continue

            else:
                click.secho("Invalid option!", fg='red')

        else:
            click.secho("Invalid option! Please select 0-4.", fg='red')

    except ValueError:
        click.secho("Please enter a valid number!", fg='red')
    except Exception as e:
        click.secho(f"An error occurred: {str(e)}", fg='red')

    click.prompt("\nPress Enter to continue...",
                 default='', show_default=False)
