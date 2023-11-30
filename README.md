

# Flask API for User Management

This Flask API provides a simple user management system, including user registration, login, and a secure endpoint with rate limiting. It uses a MySQL database for storing user data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- pip
- A MySQL database (local or remote)

### Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/ChaitanyaArora/Assignment.git
   ```
2. **Navigate to the project directory:**
   ```
   cd Assignment
   ```
3. **Install required packages:**
   ```
   pip install -r requirements.txt
   ```

### Configuring the Application

1. **Set up your database credentials:**
   - Edit the `.env` file to include your MySQL database URI.
   ```
   DATABASE_URL=mysql+pymysql://username:password@host:port/db_name
   ```

2. **Initialize the database:**
   - If you have migration scripts, run them to set up your database schema.

### Running the Application

1. **Start the Flask server:**
   ```
   flask run --host=0.0.0.0
   ```
   - The API will be available at `http://localhost:5000`.

## API Endpoints

### User Registration

- **URL:** `/register`
- **Method:** `POST`
- **Body:**
  - `username`: A unique username
  - `email`: User's email address
  - `password`: User's password
- **Success Response:**
  - **Code:** 201 (CREATED)
  - **Content:** `{"msg": "User registered successfully"}`

### User Login

- **URL:** `/login`
- **Method:** `POST`
- **Body:**
  - `username`: Registered username
  - `password`: User's password
- **Success Response:**
  - **Code:** 200 (OK)
  - **Content:** `{ "access_token": "<JWT_TOKEN>" }`

### Secure Endpoint

- **URL:** `/secure-endpoint`
- **Method:** `GET`
- **Authentication:** Required (JWT Token)
- **Rate Limit:** 5 requests per minute
- **Success Response:**
  - **Code:** 200 (OK)
  - **Content:** `{ "msg": "Accessed secure endpoint successfully" }`
