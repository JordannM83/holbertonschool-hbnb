# HBnB - Holberton Project

## Project Description

HBnB is an accommodation rental application developed as part of the Holberton School curriculum. This project implements a complete web application with REST API, business logic layer, and database persistence.

## Objectives

Development of a complete web application following best practices:

- **Layered Architecture**: Separation between presentation, business logic, and data persistence
- **REST API**: RESTful interface with Flask-RESTX
- **UML Modeling**: Technical documentation with UML diagrams
- **Design Patterns**: Repository and Facade patterns
- **Authentication**: JWT-based authentication with password hashing
- **Database**: SQLAlchemy ORM with SQLite

## Architecture

Layered architecture implementation:

```
HBnB Application
├── Presentation Layer (REST API with Flask-RESTX)
├── Business Logic Layer (Models and Facade)
├── Persistence Layer (Repository Pattern)
└── Database Layer (SQLAlchemy with SQLite)
```

## Project Structure

```
holbertonschool-hbnb/
├── README.md                                    # This file
├── .gitignore                                   # Git ignore file
├── part1/                                      # Phase 1 - Design and modeling
│   ├── README.md                              # Part 1 documentation
│   ├── high-level_package_diagram.mmd        # High-level package diagram
│   ├── business_logic_layer_diagram.mmd      # Business Logic layer diagram
│   ├── sequence_api_call_user.mmd            # Sequence diagram - Users
│   ├── sequence_api_call_place.mmd           # Sequence diagram - Places
│   ├── sequence_api_call_review.mmd          # Sequence diagram - Reviews
│   └── sequence_api_call_request_list.mmd    # Sequence diagram - Lists
├── part2/                                      # Phase 2 - Implementation with in-memory storage
│   └── hbnb/                                  # Main application
│       ├── app/                               # Application package
│       │   ├── api/v1/                       # REST API endpoints
│       │   ├── models/                       # Data models
│       │   ├── services/                     # Business logic (Facade)
│       │   └── persistence/                  # In-memory persistence layer
│       ├── tests/                             # Test suite
│       ├── config.py                         # Application configuration
│       ├── run.py                            # Application entry point
│       ├── requirements.txt                  # Python dependencies
│       └── README.md                         # Part 2 documentation
├── part3/                                      # Phase 3 - Database and Authentication
│   └── hbnb/                                  # Main application
│       ├── venv/                              # Python virtual environment (create here)
│       ├── app/                               # Application package
│       │   ├── api/v1/                       # REST API endpoints with auth
│       │   ├── models/                       # SQLAlchemy models
│       │   ├── services/                     # Business logic (Facade)
│       │   └── persistence/                  # SQLAlchemy repository
│       ├── instance/                          # Database directory
│       │   └── development.db                # SQLite database file
│       ├── sql/                               # SQL schema files
│       ├── tests/                             # Test suite (51 API + 28 model + 7 persistence tests)
│       ├── init_db.py                        # Database initialization
│       ├── config.py                         # Configuration with SQLAlchemy
│       ├── run.py                            # Application entry point
│       ├── requirements.txt                  # Python dependencies
│       ├── hbnb_database_er_diagram.mmd      # Database ER diagram
│       └── README.md                         # Part 3 documentation
└── part4/                                      # Phase 4 - Frontend Web Application
    ├── index.html                             # Home page with places list
    ├── login.html                             # Login page
    ├── place.html                             # Place details page
    ├── add_review.html                        # Add review page
    ├── styles.css                             # Application styles
    ├── scripts.js                             # JavaScript functionality
    ├── images/                                # Image assets
    ├── test/                                  # Test scripts and utilities
    │   ├── start_servers.sh                  # Automated startup script
    │   ├── insert_test_data.py               # Database population script
    │   └── reset_places.py                   # Database reset script
    └── README.md                              # Part 4 documentation
```

## Implemented Features

### User Management
- User creation with validation
- Email uniqueness validation
- Password hashing with Bcrypt
- User authentication with JWT tokens
- User profile management (CRUD operations)

### Accommodation Management
- Place creation with validation
- Owner assignment and validation
- Price and location validation (latitude/longitude bounds)
- Place-amenity relationships (many-to-many)
- Place data retrieval and updates

### Amenity System
- Amenity creation and management
- Amenity-place associations
- Name validation and length constraints
- CRUD operations for amenities

### Review System
- Review creation with user and place validation
- Rating system (1-5 scale)
- Text validation
- Review retrieval and management
- CRUD operations for reviews

### Authentication and Security
- JWT token-based authentication
- Login endpoint with email/password validation
- Protected endpoints requiring valid tokens
- Password hashing with Bcrypt
- Role-based access control (is_admin flag)

### Database
- SQLAlchemy ORM with SQLite
- Database models with relationships
- One-to-many relationships (User-Places, User-Reviews, Place-Reviews)
- Many-to-many relationship (Place-Amenities)
- Database initialization script

## Development Status

### Part 1 - Design and Modeling (Completed)

**UML Diagrams:**
- High-level package diagram (Mermaid)
- Business Logic class diagram with entity relationships
- API call sequence diagrams (User, Place, Review, Request list)

**Architecture Decisions:**
- Layered architecture with clear separation of concerns
- Facade pattern for simplified API interface
- Repository pattern with interface abstraction
- Security approach with JWT and RBAC

**Flow Modeling:**
- User creation and authentication flows
- Place creation and search flows
- Review creation and validation flows
- Complete error handling scenarios

**Documentation:**
- Comprehensive technical documentation
- API contracts and endpoint specifications
- Non-functional requirements (performance, scalability, security)

### Part 2 - Implementation with In-Memory Storage (Completed)

**Business Logic Layer:**
- Complete model implementations (User, Place, Review, Amenity)
- BaseModel with UUID, timestamps, and common functionality
- Facade pattern for centralized business operations
- In-memory repository pattern with abstract interface
- Comprehensive data validation and error handling

**REST API:**
- Flask-RESTX based API with automatic documentation
- Complete CRUD operations for all entities
- Proper HTTP status codes and error handling
- API versioning (v1)
- Swagger UI interactive documentation

**Architecture Implementation:**
- Three-layer architecture (Presentation, Business Logic, Persistence)
- Repository pattern for data persistence abstraction
- Facade pattern for simplified layer communication
- Clear separation of concerns

**Testing:**
- 27 automated endpoint tests with 100% success rate
- Comprehensive validation testing (email format, coordinates, data types)
- Boundary and edge case testing
- Detailed test report documentation

### Part 3 - Database and Authentication (Completed)

**Database Integration:**
- SQLAlchemy ORM implementation with declarative models
- SQLite database (development.db) with production-ready schema
- Complete database models with relationships
- SQL schema files for reference and documentation
- Database initialization script (init_db.py)
- Database persistence validation across application restarts
- Entity-Relationship diagram (Mermaid)

**Authentication System:**
- JWT token-based authentication with Flask-JWT-Extended
- Secure login endpoint (/api/v1/auth/login)
- Protected endpoints with JWT verification
- Role-based access control (is_admin flag)
- Token generation and validation

**Security Features:**
- Bcrypt password hashing for all user passwords
- JWT token signing with secret key configuration
- Role-based authorization (user/admin roles)
- Ownership verification for resource modifications
- Secure credential storage

**Database Relationships:**
- User → Places (one-to-many)
- User → Reviews (one-to-many)
- Place → Reviews (one-to-many)
- Place ↔ Amenities (many-to-many via junction table)
- Unique constraints (email, user-place review)

**Repository Pattern:**
- SQLAlchemy repository implementation
- Specialized repositories (UserRepository with email lookup)
- Support for both in-memory and database storage
- Abstract repository interface for flexibility
- Proper session management with flush and refresh

**Testing:**
- 86 comprehensive tests (51 API + 28 model + 7 persistence tests)
- 100% success rate across all test suites
- Authentication and authorization testing
- Database relationship validation
- Database persistence across application restarts
- Ownership and access control verification

### Part 4 - Frontend Web Application (Completed)

**User Interface:**
- Complete frontend implementation with HTML5, CSS3, and JavaScript
- Responsive design with mobile and desktop support
- Dynamic content loading from REST API
- Client-side price filtering without page reload
- Authentication-based UI (login/logout button visibility)

**Pages:**
- Home page with places listing and price filter
- Login page with JWT authentication
- Place details page with amenities and reviews
- Add review functionality (inline and standalone)

**JavaScript Features:**
- Cookie-based JWT session management
- Fetch API for REST API integration
- Dynamic DOM manipulation
- Form validation and submission
- URL parameter handling for navigation

**Integration:**
- Full REST API integration with Part 3 backend
- Authentication headers with JWT tokens
- Real-time data fetching from database
- Test data insertion scripts
- Automated startup script for development

## Documentation

- **[Part 1 Documentation](./part1/README.md)** - Design and modeling phase
- **[Part 2 Documentation](./part2/hbnb/README.md)** - Implementation with in-memory storage
- **[Part 3 Documentation](./part3/hbnb/README.md)** - Database and authentication implementation
- **[Part 4 Documentation](./part4/README.md)** - Frontend web application

## Technologies

**Backend:**
- Python 3.12
- Flask 3.x (Web framework)
- Flask-RESTX (REST API and automatic documentation)
- Flask-JWT-Extended (JWT authentication)
- Flask-Bcrypt (Password hashing)
- Flask-CORS (Cross-origin resource sharing)
- SQLAlchemy 2.x (ORM)
- Flask-SQLAlchemy (Flask-SQLAlchemy integration)

**Frontend:**
- HTML5 (Semantic markup)
- CSS3 (Grid, Flexbox, Custom properties)
- JavaScript ES6+ (Fetch API, DOM manipulation)

**Database:**
- SQLite (Development and Testing)

**Architecture Patterns:**
- Facade Pattern (Business Logic simplification)
- Repository Pattern (Data access abstraction)
- Layered Architecture (Separation of concerns)

**Documentation:**
- Mermaid for UML diagrams (class, sequence, ER diagrams)
- Swagger UI for interactive API documentation
- Markdown for technical documentation

**Testing:**
- Pytest (Unit and integration testing)
- Pytest-cov (Code coverage analysis)

**Code Quality:**
- PEP 8 compliant (Python)
- Semistandard compliant (JavaScript)
- W3C HTML5 and CSS3 validation
- Type hints for better code clarity
- Comprehensive validation and error handling

## API Endpoints

### Authentication (Part 3)
- `POST /api/v1/auth/login` - Login with email and password, returns JWT token
  - **Request:** `{ "email": "user@example.com", "password": "password" }`
  - **Response:** `{ "access_token": "jwt_token" }`
- `GET /api/v1/auth/protected` - Protected endpoint requiring valid JWT token
  - **Headers:** `Authorization: Bearer <token>`

### Users
- `POST /api/v1/users/` - Create a new user (registration for unauthenticated, admin creation when authenticated)
  - **Request:** `{ "first_name": "John", "last_name": "Doe", "email": "john@example.com", "password": "secure123" }`
- `GET /api/v1/users/` - Get all users (public fields for non-admin, all fields for admin)
- `GET /api/v1/users/<user_id>` - Get a specific user
- `PUT /api/v1/users/<user_id>` - Update a user (own profile or admin)
  - **Authentication:** Required (JWT)
  - **Authorization:** User can update own profile, admin can update any user

### Places
- `POST /api/v1/places/` - Create a new place
  - **Authentication:** Required (JWT)
  - **Request:** `{ "title": "Beach House", "description": "...", "price": 150.00, "latitude": 45.5, "longitude": -73.6, "owner_id": "user-uuid" }`
- `GET /api/v1/places/` - Get all places (public access)
- `GET /api/v1/places/<place_id>` - Get a specific place (public access)
- `PUT /api/v1/places/<place_id>` - Update a place
  - **Authentication:** Required (JWT)
  - **Authorization:** Owner or admin only
- `GET /api/v1/places/<place_id>/reviews` - Get all reviews for a place (public access)

### Reviews
- `POST /api/v1/reviews/` - Create a new review
  - **Authentication:** Required (JWT)
  - **Request:** `{ "text": "Great place!", "rating": 5, "user_id": "user-uuid", "place_id": "place-uuid" }`
- `GET /api/v1/reviews/` - Get all reviews (public access)
- `GET /api/v1/reviews/<review_id>` - Get a specific review (public access)
- `PUT /api/v1/reviews/<review_id>` - Update a review
  - **Authentication:** Required (JWT)
  - **Authorization:** Author or admin only
- `DELETE /api/v1/reviews/<review_id>` - Delete a review
  - **Authentication:** Required (JWT)
  - **Authorization:** Author or admin only

### Amenities
- `POST /api/v1/amenities/` - Create a new amenity
  - **Authentication:** Required (JWT)
  - **Authorization:** Admin only
  - **Request:** `{ "name": "WiFi" }`
- `GET /api/v1/amenities/` - Get all amenities (public access)
- `GET /api/v1/amenities/<amenity_id>` - Get a specific amenity (public access)
- `PUT /api/v1/amenities/<amenity_id>` - Update an amenity
  - **Authentication:** Required (JWT)
  - **Authorization:** Admin only

**Common HTTP Status Codes:**
- `200 OK` - Successful GET request
- `201 Created` - Successful POST request (resource created)
- `400 Bad Request` - Invalid data or validation error
- `401 Unauthorized` - Missing or invalid authentication token
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `409 Conflict` - Duplicate resource (e.g., email already exists)

All endpoints return JSON responses with appropriate HTTP status codes.

## About

Project developed as part of the Holberton School curriculum, applying software architecture concepts, web development, and programming best practices.

**Authors:**
- Part 1 (Design): Jordann Miso & Mickael Mur
- Parts 2-4 (Implementation): Jordann Miso

**Key Learning Outcomes:**
- Layered architecture design and implementation
- RESTful API development with Flask-RESTX
- Authentication and security with JWT and Bcrypt
- Database design and ORM with SQLAlchemy
- Frontend development with HTML5, CSS3, and JavaScript
- API integration with Fetch API
- Design patterns (Facade, Repository)
- Comprehensive testing strategies
- API documentation with Swagger

## Getting Started

### Quick Start (Part 4 - Full Application)

1. **Setup Virtual Environment**:
```bash
cd part3/hbnb
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Run the Application**:
```bash
cd ../../part4/test
./start_servers.sh
```

This automated script will:
- Stop existing servers and free ports
- Initialize the database
- Insert test data (5 users, 5 places with amenities, 7 reviews)
- Start backend server on port 5000
- Start frontend server on port 8080

3. **Access the Application**:
- Open http://127.0.0.1:8080 in your browser
- Test credentials:
  - Alice (admin): alice@hbnb.io / alice1234
  - Bob: bob@hbnb.io / bob1234
  - Charlie: charlie@hbnb.io / charlie1234
  - Diana: diana@hbnb.io / diana1234
  - Emma: emma@hbnb.io / emma1234

### Running Tests

**Part 3 API and Model Tests**:
```bash
cd part3/hbnb
source venv/bin/activate
python -m pytest tests/ -v
```

Test suites:
- `test_endpoint.py` - 51 API endpoint tests
- `test_core_classes.py` - 28 model validation tests
- `test_persistence.py` - 7 database persistence tests

Total: 86 tests, 100% success rate

### Manual Setup (Alternative)

If you prefer manual setup:

1. **Start Backend**:
```bash
cd part3/hbnb
source venv/bin/activate
python run.py
```

2. **Start Frontend** (new terminal):
```bash
cd part4
python3 -m http.server 8080
```

3. **Initialize Database** (first time only):
```bash
cd part3/hbnb
source venv/bin/activate
python init_db.py
```

### Project Parts Overview

1. **Part 1** - Architecture and design decisions with UML diagrams
2. **Part 2** - Backend implementation with in-memory storage
3. **Part 3** - Database integration with SQLAlchemy and JWT authentication
4. **Part 4** - Frontend web application with full API integration

Each part has detailed README files with specific setup instructions.

## Interactive API Documentation

Access the Swagger UI documentation when running the application:
- **Part 2:** `http://localhost:5000/api/v1/`
- **Part 3:** `http://localhost:5000/api/v1/`

The interactive documentation allows you to:
- Explore all available endpoints
- View request/response schemas
- Test API calls directly from the browser
- Understand authentication requirements

## License

This project is developed for educational purposes as part of the Holberton School program.
