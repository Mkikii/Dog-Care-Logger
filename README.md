# Dog Care Logger

A command-line dog care management application built with Python, SQLAlchemy, and Click. Easily manage dog profiles, kennel locations, care types, and log care events.

**Author:** James Kamau

## Overview

Dog Care Logger helps dog care facilities streamline operations by tracking dogs, managing kennel locations, defining care activities, and logging events. It uses Python, SQLAlchemy ORM, and Click for a modern CLI and database experience.

## Features

- **Dog Management:** Add, view, update, and delete dog profiles (breed, birth date, notes).
- **Location Management:** Track kennel locations and population.
- **Care Type Management:** Define care activities and intervals.
- **Care Event Logging:** Record care activities for each dog.
- **CRUD Operations:** Full create, read, update, and delete support.
- **Data Validation:** Robust input validation and error handling.
- **SQLite Database:** Efficient local storage.
- **User-Friendly CLI:** Intuitive, color-coded menus and prompts.

## Technologies

- Python 3.8+
- SQLAlchemy (ORM)
- Click (CLI framework)
- SQLite (database)
- DateTime (date/time handling)

## Project Structure

```
Dog-Care-Logger/
├── Models.py          # SQLAlchemy models
├── CRUD.py            # Database operations
├── main.py            # CLI entry point
├── dogs.db            # SQLite database (generated)
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup Steps

1. Clone or download the project.
2. Navigate to the directory:
  ```bash
  cd Dog-Care-Logger
  ```
3. Install dependencies:
  ```bash
  pip install sqlalchemy click
  ```
4. Initialize the database:
  ```bash
  python Models.py
  ```
5. Run the application:
  ```bash
  python main.py
  ```

## Usage

Start the CLI:
```bash
python main.py
```

### Main Menu

1. **Dog Management**
  - Add, find, view, delete dog profiles
2. **Location Management**
  - Add, find, view, delete locations
3. **Care Type Management**
  - Add, find, view, delete care types
4. **Care Event Management**
  - Add, find, view, delete care events

### Data Input Format

- **Dates:** `YYYY-MM-DD` (e.g., `2025-08-15`)
- **Date-Time:** `YYYY-MM-DD HH:MM:SS` (e.g., `2025-08-15 14:30:00`)
- **IDs:** Integer values

## Database Schema

### Dogs Table
```sql
CREATE TABLE Dogs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  name VARCHAR(50) NOT NULL UNIQUE,
  breed VARCHAR(100) NOT NULL,
  date_of_birth DATETIME NOT NULL,
  location_id INTEGER NOT NULL,
  last_attended_to DATETIME,
  notes TEXT,
  FOREIGN KEY (location_id) REFERENCES Locations(id)
);
```

### Locations Table
```sql
CREATE TABLE Locations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  kennel_number INTEGER NOT NULL UNIQUE,
  population INTEGER
);
```

### Care_types Table
```sql
CREATE TABLE Care_types (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE,
  description TEXT,
  default_interval_days INTEGER
);
```

### Care_events Table
```sql
CREATE TABLE Care_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE,
  dog_id INTEGER NOT NULL,
  care_type_id INTEGER,
  performed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  details TEXT,
  notes TEXT,
  FOREIGN KEY (dog_id) REFERENCES Dogs(id),
  FOREIGN KEY (care_type_id) REFERENCES Care_types(id)
);
```

## API Reference (CRUD Functions)

### Dog Operations

- `add_new_Dog(created_at, name, breed, date_of_birth, location_id, last_attended_to, notes)` - Create new dog profile
- `find_dog_by_id(dog_id)` - Retrieve dog by ID
- `find_all_dogs()` - Get all dogs
- `delete_dog_by_id(dog_id)` - Delete dog profile

### Location Operations

- `add_new_Location(kennel_number, population)` - Create new location
- `find_location_by_id(location_id)` - Retrieve location by ID
- `find_all_locations()` - Get all locations
- `delete_location_by_id(location_id)` - Delete location

### Care Type Operations

- `add_new_Care_Type(name, description, default_interval_days)` - Create new care type
- `find_care_type_by_id(care_type_id)` - Retrieve care type by ID
- `find_all_care_types()` - Get all care types
- `delete_care_type_by_id(care_type_id)` - Delete care type

### Care Event Operations

- `add_new_Care_Event(dog_id, name, care_type_id, performed_at, details, notes)` - Create new care event
- `find_care_event_by_id(care_event_id)` - Retrieve care event by ID
- `find_all_care_events()` - Get all care events
- `delete_care_event_by_id(care_event_id)` - Delete care event

## Example Usage

### Adding a New Dog

Select "1 DOG MANAGEMENT" from main menu

Choose "1 Add new dog profile"

Enter dog details:

- Name: Max
- Breed: Golden Retriever
- D.O.B: 2023-05-15
- Time created: 2025-08-15 10:00:00
- Last attended: 2025-08-15 10:00:00
- Notes: Friendly and energetic
- Location ID: 1

### Logging a Care Event

Select "4 CARE EVENT MANAGEMENT"

Choose "1 Add new care event"

Enter event details:

- Name: Morning Walk
- Performed at: 2025-08-15 08:30:00
- Details: 30-minute walk around the park
- Notes: Good behavior on leash
- Dog ID: 1
- Care Type ID: 1
- Location ID: 1

## Error Handling

The application includes comprehensive error handling for:

- Invalid date formats
- Non-existent IDs
- Database constraint violations
- Invalid user inputs
- Type validation errors
- SQLite datetime object requirements

## Common Issues and Solutions

### Database Connection Issues

```bash
# If you encounter database connection problems:
rm dogs.db
python Models.py
```

### Module Not Found Errors

```bash
# Ensure all dependencies are installed:
pip install --upgrade sqlalchemy click
```

### Date Format Errors

Use exact format: YYYY-MM-DD for dates

Use exact format: YYYY-MM-DD HH:MM:SS for datetime

## Development

### Adding New Features

- Update database models in Models.py
- Add CRUD operations in CRUD.py
- Implement CLI interface in main.py
- Test thoroughly with various inputs

### Database Migrations

For schema changes, use Alembic migrations:

```bash
pip install alembic
alembic init migrations
```

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

- GitHub: @JamesKamau-5773
- Email: [Your Email Address]

## Contributing

- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Commit your changes (`git commit -m 'Add amazing feature'`)
- Push to the branch (`git push origin feature/amazing-feature`)
- Open a Pull Request

## Future Enhancements

- Web interface using Flask/Django
- User authentication and authorization
- Reporting and analytics features
- Email notifications for care schedules
- Mobile application interface
- Integration with veterinary APIs
- Image upload for dog profiles

## License

MIT License

Copyright © 2025 James Kamau

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

If you find this project useful, please give it a star on GitHub!
