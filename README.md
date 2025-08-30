# Dog Care Logger

#### A comprehensive dog care management application built using Python with SQLAlchemy and Click for managing dog care facilities, tracking dog profiles, and logging care events.

#### By **James Kamau**

## Description

Dog Care Logger is a command-line interface (CLI) application designed for dog care facilities to manage their operations efficiently. The application provides comprehensive functionality for tracking dogs, managing kennel locations, defining care types, and logging care events. Built with Python, SQLAlchemy ORM, and Click for the CLI interface, it demonstrates modern database management and command-line application development concepts.

## Features

- **Dog Management**: Create, view, and manage dog profiles with detailed information including breed, date of birth, and special notes
- **Location Management**: Track kennel locations with population counts and unique identifiers
- **Care Type Management**: Define different types of care activities with descriptions and default intervals
- **Care Event Logging**: Record and track all care activities performed for each dog
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for all entities
- **Data Validation**: Comprehensive input validation with proper error handling
- **SQLite Database**: Lightweight and efficient database storage using SQLite
- **User-Friendly CLI**: Intuitive command-line interface with color-coded menus and prompts
- **Database Migrations**: Alembic integration for schema management
- **Seed Data**: Pre-populated sample data for testing

## Technologies Used

- **Python 3.8+**: Core programming language
- **SQLAlchemy**: Object-Relational Mapping (ORM) for database operations
- **Click**: Python package for creating beautiful command-line interfaces
- **SQLite**: Lightweight database engine for data persistence
- **DateTime**: Python module for handling date and time operations
- **Alembic**: Database migration tool
- **Pipenv**: Python dependency management

## Project Structure
DOG-CARE-LOGGER/
├── alembic/ # Database migration scripts
├── Lib/ # Library modules
│ ├── pycache/ # Python cache files
│ ├── init.py # Package initialization
│ ├── CRUD.py # Database operations and CRUD functions
│ └── Models.py # SQLAlchemy database models and schema
├── db/ # Database-related files
│ └── seed.py # Database seeding script
├── pycache/ # Python cache files
├── vscode/ # VSCode configuration
├── venv/ # Virtual environment
├── dogs.db # SQLite database file
├── Dogs.db # Secondary database file (if any)
├── Main.py # Main CLI application entry point
├── alembic.ini # Alembic configuration
├── helpers.py # Utility functions
├── Pipfile # Pipenv dependency management
├── LICENSE # Project license
└── README.md # Project documentation

text

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Process

1. **Navigate to the project directory**:
  ```bash
  cd DOG-CARE-LOGGER
  ```
2. **Set up virtual environment (if using Pipenv):**
  ```bash
  pipenv install
  pipenv shell
  ```
  Or using regular virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install the required dependencies:**
  ```bash
  pip install sqlalchemy click alembic
  ```
4. **Initialize the database:**
  ```bash
  python Lib/Models.py
  ```
5. **Run database migrations (if needed):**
  ```bash
  alembic upgrade head
  ```
6. **Seed the database with sample data:**
  ```bash
  python db/seed.py
  ```
7. **Run the application:**
  ```bash
  python Main.py
  ```

## How to Use

### Starting the Application

Run the main script to start the interactive CLI:

```bash
python Main.py
```

### Main Menu Options

The application provides four main management areas:

- DOG MANAGEMENT - Manage dog profiles
- LOCATION MANAGEMENT - Manage kennel locations
- CARE TYPE MANAGEMENT - Define care activities
- CARE EVENT MANAGEMENT - Log care activities

### Database Operations

#### Running Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Revert migrations
alembic downgrade -1
```

#### Seeding Database

```bash
python db/seed.py
```

## Module Structure

### Lib/Models.py

Contains SQLAlchemy ORM models for:

- Dogs - Dog profiles and information
- Locations - Kennel locations and capacity
- Care_types - Types of care activities
- Care_events - Logged care activities

### Lib/CRUD.py

Contains CRUD operations for:

- Create, Read, Update, Delete operations
- Database session management
- Data validation and error handling

### Main.py

Main application entry point with:

- CLI interface using Click
- Menu navigation system
- User input handling
- Color-coded output

### db/seed.py

Database seeding script with:

- Sample dog data
- Pre-defined locations
- Care type definitions
- Example care events

## Database Schema

### Key Tables

**Dogs Table**  
id, name, breed, date_of_birth  
location_id, last_attended_to, notes  
Relationships with Locations and Care_events

**Locations Table**  
id, kennel_number, population  
Relationship with Dogs

**Care_types Table**  
id, name, description, default_interval_days  
Relationship with Care_events

**Care_events Table**  
id, name, dog_id, care_type_id  
performed_at, details, notes  
Relationships with Dogs and Care_types

## API Reference (CRUD Functions)

### Dog Operations (Lib/CRUD.py)

- add_new_Dog() - Create new dog profile
- find_dog_by_id() - Retrieve dog by ID
- find_all_dogs() - Get all dogs
- delete_dog_by_id() - Delete dog profile

### Location Operations

- add_new_Location() - Create new location
- find_location_by_id() - Retrieve location by ID
- find_all_locations() - Get all locations
- delete_location_by_id() - Delete location

### Care Type Operations

- add_new_Care_Type() - Create new care type
- find_care_type_by_id() - Retrieve care type by ID
- find_all_care_types() - Get all care types
- delete_care_type_by_id() - Delete care type

### Care Event Operations

- add_new_Care_Event() - Create new care event
- find_care_event_by_id() - Retrieve care event by ID
- find_all_care_events() - Get all care events
- delete_care_event_by_id() - Delete care event

## Development

### Running Tests

```bash
# Run specific module tests
python -m pytest tests/test_models.py
python -m pytest tests/test_crud.py
```

### Code Structure

```python
# Import modules correctly
from Lib.Models import Dogs, Locations, session
from Lib.CRUD import add_new_Dog, find_dog_by_id
```

### Adding New Features

- Update models in Lib/Models.py
- Add CRUD operations in Lib/CRUD.py
- Update CLI interface in Main.py
- Add migration scripts in alembic/versions/
- Test thoroughly

## Common Issues and Solutions

### Module Import Issues

```python
# Correct import syntax
from Lib import CRUD, Models
# or
from Lib.CRUD import add_new_Dog
```

### Database Migration Issues

```bash
# Reset and recreate database
rm dogs.db
alembic upgrade head
python db/seed.py
```

### Virtual Environment Issues

```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

GitHub: @JamesKamau-5773

## License

MIT License - See LICENSE file for details.

If you find this project useful, please give it a star on GitHub!