# Part 4: Web Application Frontend

## Overview
This is the frontend implementation for the HBnB (HolbertonBnB) application. It provides a user interface for browsing places, viewing details, logging in, and submitting reviews.

## Project Structure
```
part4/
├── index.html           # Home page - List of places
├── login.html           # Login form
├── place.html           # Place details page with reviews
├── add_review.html      # Standalone page to add a review
├── styles.css           # Main stylesheet
├── scripts.js           # JavaScript functionality
├── images/              # Directory for images
│   ├── logo.png        # Application logo
│   ├── icon.png        # Favicon
│   ├── place1.jpg      # Sample place images
│   ├── place2.jpg
│   ├── place3.jpg
│   └── place4.jpg
└── README.md           # This file
```

## Pages

### 1. index.html - List of Places
- Displays all available places as cards
- Each card shows:
  - Place image
  - Place name
  - Price per night
  - "View Details" button
- Responsive grid layout

### 2. login.html - Login Form
- Email and password input fields
- Form validation
- Stores authentication token in cookies
- Redirects to home page upon successful login

### 3. place.html - Place Details
- Displays comprehensive place information:
  - Place name
  - Host information
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

### Required Features ✓
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

- **Flexible Parameters** (customizable):
  - Color Palette: Blue (#3498db), Dark Gray (#2c3e50), Green (#27ae60)
  - Font: Arial, sans-serif
  - Images: Placeholder images provided
  - Favicon: icon.png included

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
- A local web server (optional but recommended)

### Installation

1. Navigate to the part4 directory:
```bash
cd part4
```

2. Add images to the `images/` directory:
   - `logo.png` - Your application logo
   - `icon.png` - Your favicon
   - `place1.jpg`, `place2.jpg`, etc. - Place images

3. Open the application:
   - Option 1: Open `index.html` directly in your browser
   - Option 2: Use a local web server:
     ```bash
     # Using Python 3
     python3 -m http.server 8000
     
     # Then visit: http://localhost:8000
     ```

### Usage

1. **Browse Places**: Open `index.html` to see all available places
2. **View Details**: Click "View Details" on any place card
3. **Login**: Click the "Login" button in the header
   - Enter any email and password to simulate login
4. **Add Review**: 
   - After logging in, visit a place details page
   - Use the inline form at the bottom, OR
   - Navigate to `add_review.html?place_id=1` (replace 1 with place ID)
5. **Logout**: Click the "Logout" button in the header

## Technical Details

### JavaScript Functionality
- **Authentication**: Cookie-based session management
- **Dynamic Content**: Places and reviews loaded from JavaScript arrays
- **Form Handling**: Login and review submission with validation
- **URL Parameters**: Place details page reads place ID from URL
- **Responsive UI**: Login button text changes based on auth state

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

✓ Semantic HTML5 elements used throughout
✓ Login form with email and password fields
✓ List of places displayed as cards
✓ Place details page with comprehensive information
✓ Add review form (both inline and standalone)
✓ Required CSS classes implemented
✓ Fixed parameters (margin, padding, border, border-radius) applied
✓ Responsive design
✓ Header with logo and login button
✓ Footer with copyright
✓ Navigation bar with links

## Future Enhancements
- Connect to real backend API
- Add user registration
- Implement search and filter functionality
- Add booking functionality
- Include image galleries
- Add user profiles
- Implement real-time updates

## Credits
- Design: HolbertonSchool
- Implementation: [Your Name]
- Images: Placeholder images (replace with your own)

## License
© 2024 HBnB. All rights reserved.
