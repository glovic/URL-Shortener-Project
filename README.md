# URL Shortener

## Tagline
**Simplifying links for better web navigation.**

## Project Description
The URL Shortener project simplifies long URLs, making them easier to share and manage. It provides users with the ability to generate short, memorable links that redirect to the original, longer URLs. The project is built using Flask for the backend and a simple HTML/CSS/JavaScript frontend.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Features
- Shorten long URLs to simple, memorable links.
- Redirect users from short URLs to the original URLs.
- User-friendly interface for generating and copying short URLs.
- Custom short URLs.

## Technologies Used
### Backend
- **Framework**: Flask
- **Database**: PostgreSQL
- **Libraries**: Flask-RESTful, SQLAlchemy

### Frontend
- **Languages**: HTML, CSS, JavaScript

## Installation
### Prerequisites
- Python 3.x
- PostgreSQL

### Steps
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. **Create a Virtual Environment and Activate it:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```sh
    pip install Flask Flask-RESTful SQLAlchemy psycopg2
    ```

4. **Setup PostgreSQL:**
    Create a new database and update the database URI in `app.py`:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/yourdatabase'
    ```

5. **Initialize the Database:**
    ```sh
    python app.py
    ```

6. **Run the Application:**
    ```sh
    python app.py
    ```

### Running the Application
- Navigate to `http://localhost:5000` to access the landing page.

## Usage
### Shorten a URL
1. Paste the long URL in the input box on the landing page.
2. Click the "Shorten" button.
3. You will be redirected to a page with the shortened URL.

### Copy the Shortened URL
1. On the redirected page, click the "Copy" button to copy the shortened URL to your clipboard.

## File Structure
```plaintext
url-shortener/
│
├── app.py                 # Main backend application
├── templates/
│   ├── index.html         # Landing page for URL input
│   ├── copy_page.html     # Page to display the shortened URL
├── static/
│   ├── css/
│   │   └── styles.css     # CSS for the frontend
│   └── js/
│       └── script.js      # JavaScript for the frontend
├── README.md              # This file
└── requirements.txt       # Python dependencies

