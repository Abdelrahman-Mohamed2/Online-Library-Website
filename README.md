# Online Library Website

The Online Library Website is a Django-based web application that allows users to browse, borrow, and manage books online. The system supports two types of users: **Admins** and **Users**, each with specific roles and features.

---

## Features

### Admin Features
- **Sign Up and Login**:
  - Admins can create an account by filling in a form with fields such as username, password, email, and selecting the `is_admin` option.
  - Login securely to access the admin dashboard.

- **Manage Books**:
  - Add new books with details such as ID, name, author, category, and description.
  - View a list of all available books.
  - Edit book details.
  - Delete books from the database.

### User Features
- **Sign Up and Login**:
  - Users can create an account by filling in a form with fields such as username, password, and email.
  - Login securely to access user-specific features.

- **Search and Borrow Books**:
  - Search for books by title, author, or category.
  - View a list of available books marked as "Available" or "Not Available" (if borrowed by another user).
  - View detailed book information on a separate book page.
  - Borrow books (only if marked as "Available").

- **View Borrowed Books**:
  - Users can view a personalized list of books they have borrowed.

### Shared Features
- **Dynamic Navigation Bar**:
  - The navigation bar dynamically updates based on the logged-in user type (Admin/User).
  - Accessible from all pages of the website.

---

## Getting Started

### Prerequisites
- Python 3.x
- Django Framework
- SQLite (default database)

### Installation
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/online-library.git
    cd online-library
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run Migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the Development Server**:
    ```sh
    python manage.py runserver
    ```

5. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Project Structure

```plaintext
online-library/
├── adm/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── library/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── user/
├── db.sqlite3
├── manage.py
