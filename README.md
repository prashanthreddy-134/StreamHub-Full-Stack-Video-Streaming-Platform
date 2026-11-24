
# StreamHub - Full-Stack Video Streaming Platform

A Django-based video streaming and sharing application where users can create accounts, manage channels, upload videos, watch content, and interact with other users.

## Project Overview

StreamHub is a full-stack web application built with Python and Django. It provides video-sharing features alongside user accounts, channel management, playlists, engagement tools, watch history, and creator analytics.

The project uses MySQL for database storage and a responsive frontend built with HTML, CSS, Bootstrap, and JavaScript.

## Features

### 1. User Authentication
- User registration
- Secure login and logout
- Session-based authentication
- Protected access to account-specific features
- User-specific content and activity

### 2. Channel Management
- Create and manage creator channels
- View channel information
- Display uploaded videos
- Subscribe to channels
- View creator content

### 3. Video Management
- Upload videos
- Add video titles and descriptions
- Upload video thumbnails
- Browse available videos
- Search for videos
- Organize and manage video content

### 4. Video Playback
- Browser-based video player
- HTML5 video playback
- Video controls
- Related video suggestions
- Video viewing functionality

### 5. User Engagement
- Like videos
- Dislike videos
- Post comments
- View comments
- Subscribe to creators

### 6. Playlist Management
- Create playlists
- Add videos to playlists
- View playlist contents
- Organize videos into collections

### 7. Watch History
- Track watched videos
- View previously watched content
- Access watch history

### 8. Creator Dashboard
- Creator dashboard
- Video and channel activity information
- Creator analytics

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python |
| Web Framework | Django 4.2 |
| Database | MySQL 8.0 |
| Frontend | HTML5, CSS3 |
| UI Framework | Bootstrap 5 |
| Programming | JavaScript |
| Video Player | HTML5 Video Player |
| Version Control | Git and GitHub |

## Project Architecture

```text
                  STREAMHUB
                      |
          -------------------------
          |                       |
       FRONTEND                 BACKEND
          |                       |
    HTML / CSS / JS             Django
          |                       |
     Bootstrap 5              Django Views
          |                       |
    User Interface           Application Logic
                                  |
                         ------------------
                         |                |
                       Models           Forms
                         |                |
                         ------------------
                                  |
                              MySQL
                                  |
                         Database Storage
```

## Project Structure

```text
video-streaming-platform/
|
|-- manage.py
|-- requirements.txt
|-- .env.example
|-- .gitignore
|-- README.md
|
|-- video_stream/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|
|-- videos/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- templates/
|   |-- base.html
|   |-- registration/
|   |-- videos/
|
|-- static/
|   |-- css/
|   |-- js/
|
|-- media/
|   |-- channels/
|   |-- thumbnails/
|   |-- videos/
|
|-- .venv/
```

Note: `.venv/` and uploaded media are local development files and are excluded from GitHub.

## Requirements

Install the following software before running the project:

- Python 3.11 or compatible version
- MySQL Server 8.0
- Git
- Visual Studio Code or another code editor
- Modern web browser

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/prashanthreddy-134/StreamHub-Full-Stack-Video-Streaming-Platform.git
```

Navigate into the project directory:

```bash
cd StreamHub-Full-Stack-Video-Streaming-Platform
```

### Step 2: Create a Virtual Environment

For Windows PowerShell:

```powershell
py -3.11 -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL Database

Open MySQL and execute:

```sql
CREATE DATABASE video_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER 'video_user'@'localhost'
IDENTIFIED BY 'choose-a-strong-password';

GRANT ALL PRIVILEGES ON video_db.*
TO 'video_user'@'localhost';

FLUSH PRIVILEGES;
```

Replace the example password with your own strong MySQL password.

If you already have a MySQL account, you can configure the project to use that account instead.

### Step 5: Configure Environment Variables

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

Open `.env` and configure the following values:

```dotenv
SECRET_KEY=replace-with-a-long-random-secret
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_ENGINE=mysql
DB_NAME=video_db
DB_USER=video_user
DB_PASSWORD=your-local-mysql-password
DB_HOST=127.0.0.1
DB_PORT=3306
```

Important:
- Replace the example database password with your local MySQL password.
- Keep `.env` private.
- Never upload actual credentials to GitHub.
- The `.env` file is excluded through `.gitignore`.

### Step 6: Apply Database Migrations

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

### Step 7: Create an Administrator Account

Run:

```bash
python manage.py createsuperuser
```

Follow the instructions to create your administrator account.

### Step 8: Start the Development Server

Run:

```bash
python manage.py runserver
```

Open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

The StreamHub application will be available locally.

To stop the development server, press `CTRL + C`.

## Application Pages

| Page | URL |
|---|---|
| Home | http://127.0.0.1:8000/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Upload Video | http://127.0.0.1:8000/upload/ |
| Playlists | http://127.0.0.1:8000/playlists/ |
| Creator Dashboard | http://127.0.0.1:8000/dashboard/ |
| Watch History | http://127.0.0.1:8000/history/ |

Some pages require authentication.

## Database Description

The application uses MySQL to store its application data.

The database supports information related to:

- User accounts
- Creator channels
- Uploaded videos
- Video comments
- Likes and dislikes
- Channel subscriptions
- Playlists
- Watch history

The Django models define the database structure, while Django migrations manage database schema changes.

## Testing

Run the Django automated test suite:

```bash
python manage.py test
```

The project also includes a PowerShell helper script named `test.ps1`.

## Security Considerations

- Environment variables are used for sensitive configuration.
- The `.env` file is excluded from version control.
- The virtual environment is excluded from GitHub.
- Uploaded media files are excluded from the repository.
- Django authentication protects account-specific features.

For production deployment:

- Generate a strong and unique Django secret key.
- Set `DEBUG=False`.
- Configure the production domain in `ALLOWED_HOSTS`.
- Use a secure database password.
- Enable HTTPS.
- Configure persistent storage for uploaded media.
- Review file-upload validation and access controls.

Do not use the development secret key or development configuration in production.

## Deployment Status

The source code is published on GitHub.

GitHub repository:

https://github.com/prashanthreddy-134/StreamHub-Full-Stack-Video-Streaming-Platform

Publishing the source code does not automatically deploy the application. A public deployment requires a hosting provider, production database, environment variables, static-file configuration, and persistent media storage.

## Future Enhancements

Potential future improvements include:

- Adaptive bitrate video streaming
- Video transcoding
- Cloud-based media storage
- Improved content moderation
- Video recommendations
- Expanded automated testing
- Continuous integration and deployment
- Performance monitoring

These are proposed enhancements and are not claims about currently implemented functionality.

## Author

**Prashanth Reddy**

Information Science and Engineering Student

GitHub: https://github.com/prashanthreddy-134

## License

No open-source license is currently specified.

An appropriate license can be added if the project is intended for public reuse, modification, or distribution.
