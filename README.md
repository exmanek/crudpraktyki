# Flask CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built with Flask. The project was developed as part of a vocational internship at Pixel.

## Routes

### User Routes

#### POST /api/: Create New User  
**Request Body:**  
- `name` (string, required): The name of the user.  
- `surname` (string, required): The surname of the user.  
- `email` (string, required): The email of the user.  

**Response Body:**  
- `success` (boolean)  
- `data` (object): Contains the created user data.

---

#### GET /api/users: Get List of Users  
Returns a list of all users.  

**Response Body:**  
- `success` (boolean)  
- `data` (array): Each user object contains:  
  - `user_id` (integer)  
  - `name` (string)  
  - `surname` (string)  
  - `email` (string)  

---

#### GET /api/users/<user_id>: Get User by ID  
Retrieves user information by ID.  

**Response Body:**  
- `success` (boolean)  
- `data` (object): Contains user data.

---

#### PUT /api/users/<user_id>: Update User  
Updates user information by ID.  

**Request Body:**  
- `name` (string, optional): New name of the user.  
- `surname` (string, optional): New surname of the user.  
- `email` (string, optional): New email of the user.  

**Response Body:**  
- `success` (boolean)  
- `data` (object): Updated user data.

---

#### DELETE /api/users/<user_id>: Delete User  
Deletes a user by ID.  

**Response Body:**  
- `success` (boolean)  
- `data` (object): Empty object.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Technologies Used
Flask: Lightweight web framework for building the application.
Python 3.x: Programming language used for the backend logic.
Git: Version control for source code management.
