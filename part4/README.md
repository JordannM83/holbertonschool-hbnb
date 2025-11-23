# Part 4: Web Application Frontend

## Overview
This is the frontend implementation for the HBnB (HolbertonBnB) application. It provides a user interface for browsing places, viewing details, logging in, and submitting reviews.

## Project Structure
```
part4/
├── index.html                      # Home page - List of places
├── login.html                      # Login form
├── place.html                      # Place details page with reviews
├── add_review.html                 # Standalone page to add a review
├── styles.css                      # Main stylesheet
├── scripts.js                      # JavaScript functionality
├── images/                         # Directory for images
│   ├── logo.png                   # Application logo
│   ├── icon.png                   # Favicon
│   ├── place1.jpg                 # Sample place images
│   ├── place2.jpg
│   ├── place3.jpg
│   └── place4.jpg
├── README.md                       # This file
├── IMPLEMENTATION_SUMMARY.md       # Detailed implementation notes
├── TESTING_GUIDE.md                # Testing instructions
├── REQUIREMENTS_VERIFICATION.md    # Requirements checklist
└── test_index.sh                   # Automated test script
```

## Pages

### 1. index.html - List of Places
**Features:**
- Displays all available places as cards
- **Authentication-based UI**: Login link shows only when NOT logged in
- **Client-side price filtering**: Filter places by price without page reload
  - Options: All, Up to $10, Up to $50, Up to $100
- Each card shows:
  - Place title
  - Price per night (dynamic from API)
  - Description snippet
  - "View Details" button
- Responsive grid layout
- Fetches data from API with JWT authentication support

**Implementation Highlights:**
- JWT token checked on page load from cookies
- Places fetched dynamically via Fetch API
- Filter dropdown with instant results (no reload)
- Field names match API: `title`, `price`, `description`

### 2. login.html - Login Form
- Email and password input fields
- Form validation
- Stores authentication token in cookies
- Redirects to home page upon successful login

### 3. place.html - Place Details
- Displays comprehensive place information:
  - Place title
  - Host information (owner)
  - Price per night
  - Description
  - List of amenities
- Shows all reviews for the place
- Includes inline review form (visible only for logged-in users)
- Each review displays:
  - User name
  - Rating (stars)
  - Comment

### 4. add_review.html - Add Review Form
- Standalone page for adding reviews
- Accessible only to authenticated users
- Contains:
  - Text area for review comment
  - Rating dropdown (1-5 stars)
  - Submit button
- Redirects to place details after submission

## Features

### Required Features
- **Header**: Contains logo and login/logout button
- **Footer**: Displays copyright information
- **Navigation Bar**: Links to Home and Login pages
- **Place Cards**: Display places with proper styling (margin: 20px, padding: 10px, border: 1px solid #ddd, border-radius: 10px)
- **Review Cards**: Display reviews with proper styling (same as place cards)
- **Authentication**: Login functionality with token-based session management
- **Responsive Design**: Works on desktop and mobile devices

### Design Specifications
- **Fixed Parameters** (as required):
  - Margin: 20px for cards
  - Padding: 10px for cards
  - Border: 1px solid #ddd for cards
  - Border Radius: 10px for cards

## CSS Classes Used

### Required Classes:
- `.logo` - Application logo in header
- `.login-button` - Login/logout button
- `.place-card` - Individual place card
- `.details-button` - Button to view place details
- `.place-details` - Container for place details
- `.place-info` - Place information section
- `.review-card` - Individual review card
- `.add-review` - Add review form container
- `.form` - Form styling

## Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.x installed
- Virtual environment set up in part3/hbnb

### Quick Start

**Simply run the startup script:**
```bash
cd test
./start_servers.sh
```

This script will automatically:
1. Stop any existing servers
2. Free up ports 5000 and 8080
3. Reset the database places
4. Insert test data (users, amenities, and 5 sample places)
5. Start the backend server (Flask) on port 5000
6. Start the frontend server (HTTP) on port 8080

Once completed, access the application at: **http://127.0.0.1:8080**

### Test Credentials
- Alice (admin): alice@hbnb.io / alice1234
- Bob: bob@hbnb.io / bob1234
- Charlie: charlie@hbnb.io / charlie1234
- Diana: diana@hbnb.io / diana1234
- Emma: emma@hbnb.io / emma1234

### Stopping the Servers
```bash
pkill -f 'python run.py' && pkill -f 'python3 -m http.server 8080'
```

### Manual Setup (Alternative)

If you prefer to start services manually:

1. **Start the Backend Server**:
```bash
cd ../part3/hbnb
source venv/bin/activate
python run.py
# Server starts on http://127.0.0.1:5000
```

2. **Start the Frontend Server**:
```bash
cd ../../part4
python3 -m http.server 8080
# Server starts on http://127.0.0.1:8080
```

3. **Insert Test Data** (if needed):
```bash
cd test
cp insert_test_data.py ../part3/hbnb/
cd ../part3/hbnb
source venv/bin/activate
python insert_test_data.py
```

### Usage

1. **Access the Application**: 
   - Open http://127.0.0.1:8080 in your browser
   - The home page shows all available places from the API

2. **Filter Places by Price**:
   - Use the dropdown to select a price range
   - Options: All, Up to $10, Up to $50, Up to $100
   - Results update instantly without page reload

3. **Login**: 
   - Click the "Login" button in the header
   - Use test credentials
   - After login, the login link changes to "Logout"

4. **View Place Details**: 
   - Click "View Details" on any place card
   - See full information including amenities and reviews

5. **Add Review** (requires login):
   - Visit a place details page while logged in
   - Use the inline form at the bottom to add a review
   - Include rating (1-5) and comment
   - Note: You cannot review your own places

6. **Logout**: 
   - Click the "Logout" button in the header
   - The button will change back to "Login"

## Technical Details

### JavaScript Functionality
- **Authentication**: Cookie-based JWT token session management
- **Dynamic Content**: Places fetched from API endpoint `/api/v1/places/`
- **Client-Side Filtering**: Price filter with instant results (no page reload)
- **Form Handling**: Login and review submission with validation
- **URL Parameters**: Place details page reads place ID from URL
- **Responsive UI**: Login link visibility changes based on auth state
- **API Integration**: Full REST API integration with authentication headers

### Key Functions
- `getCookie(name)` - Retrieves cookie value by name
- `checkAuthentication()` - Verifies JWT token presence
- `updateLoginButton()` - Shows/hides login link based on auth
- `fetchPlaces(token)` - Fetches places from API
- `displayPlaces(places)` - Renders place cards dynamically
- `filterPlacesByPrice(maxPrice)` - Client-side filtering without reload

### API Endpoints Used
- **GET /api/v1/auth/login** - User authentication
- **GET /api/v1/places/** - List all places
- **GET /api/v1/places/{id}** - Get place details
- **GET /api/v1/places/{id}/reviews** - Get place reviews
- **POST /api/v1/reviews/** - Submit new review

### Data Flow
1. Page loads → Check authentication → Show/hide login link
2. Fetch places from API → Display as cards
3. User selects filter → Filter results client-side (instant)
4. User clicks "View Details" → Navigate to place.html with ID
5. User logs in → Store JWT → Hide login link → Fetch with auth

### Data Structure
The application uses sample data stored in JavaScript:
- **Places**: Array of place objects with id, name, price, description, host, image, and amenities
- **Reviews**: Object mapping place IDs to arrays of review objects

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Uses ES6+ JavaScript features
- CSS Grid and Flexbox for layouts

## Customization

### Changing Colors
Edit the color values in `styles.css`:
- Primary color: `#3498db` (blue)
- Dark background: `#2c3e50` (dark gray)
- Accent color: `#27ae60` (green)

### Adding Real Data
Replace the sample data in `scripts.js`:
1. Connect to your backend API
2. Fetch places and reviews from API endpoints
3. Update the data structures accordingly

### Adding More Pages
Follow the existing pattern:
1. Create new HTML file with header, nav, main, and footer
2. Add relevant sections with appropriate classes
3. Add JavaScript functionality in `scripts.js`

## Requirements Met

### Part 4 Objectives
- **Main page displays list of all places** from API
- **Fetch places data from API** using Fetch API with JWT authentication
- **Client-side filtering by price** without page reload
- **Login link visibility** based on authentication state:
  - Shows when user is NOT authenticated
  - Hides when user IS authenticated
- **Dynamic content population** using JavaScript DOM manipulation
- **Cookie-based authentication** with JWT tokens
- **Event listeners** for price filter dropdown
- **Authorization headers** included in API requests

### Original Requirements
- Semantic HTML5 elements used throughout
- Login form with email and password fields
- List of places displayed as cards
- Place details page with comprehensive information
- Add review form (both inline and standalone)
- Required CSS classes implemented
- Fixed parameters (margin, padding, border, border-radius) applied
- Responsive design
- Header with logo and login button
- Footer with copyright
- Navigation bar with links

## Documentation

For more detailed information, see:
- **IMPLEMENTATION_SUMMARY.md** - Complete implementation details
- **TESTING_GUIDE.md** - Step-by-step testing instructions
- **REQUIREMENTS_VERIFICATION.md** - Requirements checklist with code examples

## Credits
- Design: HolbertonSchool
- Implementation: Jordann Miso
- Images: Placeholder images

## License
© 2024 HBnB. All rights reserved.
