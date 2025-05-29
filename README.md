# Club Membership Application

This is a Django application for managing club memberships. Users can log in, view their enrolled activities, check their membership status, and log out.

## Features

- User authentication (login/logout)
- Dashboard displaying enrolled activities
- Membership status indication
- Activity enrollment

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd club_membership
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Visit the login page to authenticate.
- After logging in, users will be redirected to their dashboard where they can see their enrolled activities and membership status.
- Users can log out using the provided option on the dashboard.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.