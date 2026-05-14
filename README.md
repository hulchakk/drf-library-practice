# Library Service API

This project is a RESTful API for a library management system designed to automate the process of tracking books, borrowings, and users. It replaces outdated paper-based systems with a modern, digital solution.

## Features Implemented

The current version of the API includes the following core functionalities:

1. **Books Service**: Full CRUD (Create, Read, Update, Delete) operations for managing the library's book collection.
2. **User Management**: Registration and profile management endpoints for library customers.
3. **Authentication**: Secure access implemented via JWT (JSON Web Token) using `djangorestframework-simplejwt`.
4. **Permissions**: Granular access control where any user can view books, but only administrators can manage the inventory.
5. **Borrowing System**: Basic borrowing logic allowing authenticated users to create and view their borrowings.
6. **Filtering and Validation**:
* Validation to prevent borrowing books with zero inventory.
* Filtering of borrowings by `user_id` (for admins) and `is_active` status.



## Technologies Used

* Python
* Django
* Django REST Framework
* JWT Authentication
* SQLite (Development database)

## Installation and Setup

1. **Clone the repository**:
```bash
git clone <your-repository-url>
cd drf-library-practice

```


2. **Set up a virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# or
.venv\Scripts\activate     # Windows

```


3. **Install dependencies**:
```bash
pip install -r requirements.txt

```


4. **Run migrations**:
```bash
python manage.py migrate

```


5. **Start the server**:
```bash
python manage.py runserver

```



## API Documentation

Once the server is running, you can access the following primary endpoints:

### Users

* `POST /api/users/` - Register a new user.
* `POST /api/users/token/` - Obtain a JWT token.
* `GET /api/users/me/` - Retrieve personal profile information.

### Books

* `GET /api/books/` - List all books.
* `POST /api/books/` - Add a new book (Admin only).

### Borrowings

* `POST /api/borrowings/` - Create a new borrowing.
* `GET /api/borrowings/` - List borrowings (Filtered for regular users; full list for admins).
* `GET /api/borrowings/?is_active=true` - Filter active borrowings.

## Testing

The project includes unit and integration tests to ensure the reliability of the business logic. Run tests using:

```bash
python manage.py test

```
