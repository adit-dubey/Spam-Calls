# Spam Calls Detector

## Overview

The Spam Calls Detector is a Django-based project that allows users to register, manage their profiles, and search for phone numbers. Users can also mark contacts as spam, and the app provides a spam likelihood score based on a user's contact list.

## Features

- **User Registration & Profile Management**: Users can sign up, manage their profiles, and update their details.
- **Search Functionality**: Search for people by name or phone number. View details and spam likelihood based on the user's contact list.
- **Spam Detection**: Mark contacts as spam, and the app will compute and display the likelihood of a phone number being spam.
- **Custom Management Commands**: Includes a custom command to populate the database with random sample data for testing purposes.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django 4.x
- A PostgreSQL or SQLite database (or another supported database)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/adit-dubey/Spam-Calls.git
    cd Spam-Calls
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Set Up the Database:**

    Update your `settings.py` with your database configurations.

    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Populate the Database with Sample Data:**

    Use the custom management command to add random sample data to your database:

    ```bash
    python manage.py test_db
    ```

### Usage

Once the server is running, you can:

- Register a new account
- Search for contacts by name or phone number
- Mark numbers as spam
- View the spam likelihood for a number

### Running Tests

To run tests, use the following command:

```bash
python manage.py test
