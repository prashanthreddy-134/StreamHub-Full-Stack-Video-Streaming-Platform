# ðŸŽ¬ StreamHub â€“ Full-Stack Video Streaming Platform

<p align="center">
  A Django-based video streaming and sharing platform where users can upload, watch, manage, and interact with videos.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.2-green?logo=django" alt="Django">
  <img src="https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql" alt="MySQL">
  <img src="https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Status-Development-success" alt="Status">
</p>

---

## ðŸ“Œ Project Overview

**StreamHub** is a full-stack video streaming and sharing web application developed using Python and Django.

The platform allows users to create accounts, manage channels, upload videos, watch content, interact with other users, and organize videos into playlists.

StreamHub provides a video-sharing experience with features such as video playback, search, comments, likes, dislikes, channel subscriptions, watch history, and creator analytics.

The project demonstrates the development of a database-driven web application using Django, MySQL, frontend technologies, and user authentication.

## âœ¨ Features

### ðŸ” User Authentication
- User registration.
- Secure login and logout.
- Session-based authentication.
- Authenticated access to protected features.
- User-specific content and activity.

### ðŸ“¹ Video Management
- Upload videos.
- Add video titles and descriptions.
- Upload video thumbnails.
- Watch uploaded videos.
- Manage published videos.
- Delete videos.
- Display video information and view counts.

### â–¶ï¸ Video Playback
- HTML5 video player.
- Play and pause controls.
- Video seeking and playback controls.
- Video thumbnail preview.
- Watch progress tracking.
- Watch history.

### ðŸ‘¤ Channel Management
- Create a channel.
- Display channel information.
- View channel videos.
- Manage your own channel.
- Subscribe to other channels.
- Display subscriber counts.

### ðŸ‘ User Engagement
- Like videos.
- Dislike videos.
- Add comments.
- Display comments.
- Track video views.
- Prevent unauthorized interactions.

### ðŸ“‚ Playlist Management
- Create playlists.
- Set playlist visibility.
- Add videos to playlists.
- View playlist details.
- Organize videos into collections.

### ðŸ”Ž Search and Discovery
- Search videos.
- Browse video categories.
- Explore published videos.
- View related video recommendations.

### ðŸ“Š Creator Dashboard
- View uploaded videos.
- Monitor video views.
- Access creator analytics.
- Manage published content.

### ðŸ•’ Watch History
- Track watched videos.
- Maintain user watch history.
- Track playback progress.

### ðŸ“± Responsive Interface
- Bootstrap 5 layout.
- Responsive navigation.
- Video cards and thumbnails.
- Mobile-friendly interface.
- Interactive frontend components.

---

## ðŸ› ï¸ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Backend programming |
| Django 4.2 | Web application framework |
| MySQL 8.0 | Relational database |
| HTML5 | Web page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive frontend |
| JavaScript | Frontend interactions |
| Django ORM | Database operations |
| Django Authentication | User authentication |
| HTML5 Video | Video playback |
| Git and GitHub | Version control |

---

## ðŸ—ï¸ Application Architecture

StreamHub follows a Django-based application architecture.

```text
                 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                 â”‚       USER / BROWSER    â”‚
                 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                              â”‚
                              â–¼
                 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                 â”‚      FRONTEND UI        â”‚
                 â”‚ HTML, CSS, Bootstrap   â”‚
                 â”‚       JavaScript        â”‚
                 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                              â”‚
                              â–¼
                 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                 â”‚     DJANGO BACKEND      â”‚
                 â”‚                         â”‚
                 â”‚ Views and URLs          â”‚
                 â”‚ Authentication          â”‚
                 â”‚ Business Logic          â”‚
                 â”‚ Video Management        â”‚
                 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                              â”‚
                              â–¼
                 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                 â”‚       DJANGO ORM       â”‚
                 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                              â”‚
                              â–¼
                 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                 â”‚       MYSQL 8.0         â”‚
                 â”‚                         â”‚
                 â”‚ Users and Channels      â”‚
                 â”‚ Videos and Playlists    â”‚
                 â”‚ Comments and Reactions  â”‚
                 â”‚ Subscriptions/History   â”‚
                 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## ðŸ“ Project Structure

The project is organized into Django applications, templates, static assets, configuration files, and media storage.

```text
StreamHub-Full-Stack-Video-Streaming-Platform/
â”‚
â”œâ”€â”€ manage.py
â”‚
â”œâ”€â”€ .venv/
â”‚
â”œâ”€â”€ .env
â”œâ”€â”€ .gitignore
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ README.md
â”‚
â”œâ”€â”€ templates/
â”‚   â”œâ”€â”€ base.html
â”‚   â”œâ”€â”€ registration/
â”‚   â””â”€â”€ videos/
â”‚       â”œâ”€â”€ watch.html
â”‚       â”œâ”€â”€ playlists.html
â”‚       â””â”€â”€ ...
â”‚
â”œâ”€â”€ static/
â”‚   â”œâ”€â”€ css/
â”‚   â”‚   â””â”€â”€ style.css
â”‚   â””â”€â”€ js/
â”‚       â””â”€â”€ app.js
â”‚
â”œâ”€â”€ media/
â”‚   â”œâ”€â”€ videos/
â”‚   â””â”€â”€ thumbnails/
â”‚
â”œâ”€â”€ videos/
â”‚   â”œâ”€â”€ migrations/
â”‚   â”œâ”€â”€ models.py
â”‚   â”œâ”€â”€ views.py
â”‚   â”œâ”€â”€ forms.py
â”‚   â”œâ”€â”€ urls.py
â”‚   â””â”€â”€ ...
â”‚
â””â”€â”€ [Django project configuration directory]
    â”œâ”€â”€ settings.py
    â”œâ”€â”€ urls.py
    â”œâ”€â”€ asgi.py
    â””â”€â”€ wsgi.py
```

*Note: The structure above illustrates the main project components. Your actual repository may contain additional files and folders.*

---

## âš™ï¸ Installation and Setup

Follow these steps to run StreamHub locally.

### 1. Prerequisites

Install the following software:

- Python 3.11 or later.
- MySQL Server 8.0.
- Git.
- Visual Studio Code or another code editor.
- A modern web browser.

### 2. Clone the Repository

```bash
git clone https://github.com/prashanthreddy-134/StreamHub-Full-Stack-Video-Streaming-Platform.git
```

Navigate to the project directory:

```bash
cd StreamHub-Full-Stack-Video-Streaming-Platform
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install Dependencies

```bash
python -m pip install --upgrade pip
```

Install the project requirements:

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

Start your MySQL Server.

Open MySQL Workbench or the MySQL command-line client and create the database:

```sql
CREATE DATABASE video_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Create a database user:

```sql
CREATE USER 'video_user'@'localhost'
IDENTIFIED BY 'YOUR_DATABASE_PASSWORD';
```

Grant database permissions:

```sql
GRANT ALL PRIVILEGES ON video_db.*
TO 'video_user'@'localhost';

FLUSH PRIVILEGES;
```

Replace `YOUR_DATABASE_PASSWORD` with your own password.

### 6. Configure Environment Variables

Create a `.env` file in the project root.

Add the environment variables expected by your Django `settings.py`.

For example:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=video_db
DB_USER=video_user
DB_PASSWORD=YOUR_DATABASE_PASSWORD
DB_HOST=localhost
DB_PORT=3306
```

**Important:** Check the database and environment-variable configuration in your actual `settings.py`. The variable names in this example must match what your project reads. Never commit your real `.env` file or credentials to GitHub.

### 7. Apply Database Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 8. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the instructions to create your administrator account.

### 9. Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

**http://127.0.0.1:8000/**

Your local StreamHub application should now be accessible.

---

## ðŸŒ Application Pages

| Page | URL |
|---|---|
| Home | `/` |
| Registration | `/register/` |
| Login | `/accounts/login/` |
| Upload Video | `/upload/` |
| My Channel | `/my-channel/` |
| Playlists | `/playlists/` |
| Creator Dashboard | `/dashboard/` |
| Watch History | `/history/` |
| Django Admin | `/admin/` |

Some pages require authentication.

---

## ðŸ—„ï¸ Database

StreamHub uses MySQL 8.0 as its relational database.

The Django ORM manages database interactions and model relationships.

The database supports application information such as:

- User accounts.
- Channel information.
- Uploaded video details.
- Video thumbnails and media references.
- Comments and user reactions.
- Channel subscriptions.
- Playlists and playlist entries.
- Watch history and playback progress.

Database tables are managed through Django models and migrations.

---

## ðŸ”’ Security

The application uses Django's built-in security and authentication features.

Security practices include:

- Password hashing through Django authentication.
- CSRF protection for forms.
- Authentication checks for protected actions.
- Permission checks for user-owned content.
- Environment-based configuration for sensitive values.
- Database credentials kept outside source control.

Never upload database passwords, secret keys, private user data, or production credentials to a public repository.

---

## ðŸ§ª Testing

Run Django's system checks:

```bash
python manage.py check
```

Run database migrations:

```bash
python manage.py migrate
```

Run the Django test suite:

```bash
python manage.py test
```

Manually verify the following application workflows:

1. Register a new account.
2. Log in and log out.
3. Create a channel.
4. Upload a video and thumbnail.
5. Play, pause and seek through a video.
6. Search for videos.
7. Like and dislike videos.
8. Add and view comments.
9. Subscribe to another channel.
10. Create a playlist and save videos.
11. Check watch history.
12. Open the creator dashboard.

---

## ðŸ“¸ Screenshots

Screenshots of the working application should be added here.

Suggested screenshots:

| No. | Screenshot |
|---|---|
| 1 | StreamHub Home Page |
| 2 | User Registration and Login |
| 3 | Video Upload Page |
| 4 | Video Playback Page |
| 5 | Channel Page |
| 6 | Playlist Management |
| 7 | Comments and Reactions |
| 8 | Creator Dashboard |
| 9 | Watch History |
| 10 | Video Search Results |

Create a `screenshots` folder in the repository and add your actual application screenshots.

Example:

```text
screenshots/
â”œâ”€â”€ home.png
â”œâ”€â”€ login.png
â”œâ”€â”€ upload.png
â”œâ”€â”€ video-playback.png
â”œâ”€â”€ channel.png
â”œâ”€â”€ playlists.png
â”œâ”€â”€ comments.png
â”œâ”€â”€ dashboard.png
â””â”€â”€ history.png
```

After adding the images, display them here using Markdown:

```markdown
![StreamHub Home Page](screenshots/home.png)

![Video Playback](screenshots/video-playback.png)

![Creator Dashboard](screenshots/dashboard.png)
```

---

## ðŸš€ Future Enhancements

Potential improvements for future versions include:

- Adaptive bitrate streaming.
- Video transcoding and compression.
- Video recommendations.
- Real-time notifications.
- Advanced creator analytics.
- Video reporting and moderation.
- REST API integration.
- Cloud-based media storage.
- Improved video search and filtering.
- Deployment with production-grade infrastructure.

---

## ðŸ‘¨â€ðŸ’» Author

**Prashanth Reddy S**

Information Science and Engineering Student
Brindavan College of Engineering, Bengaluru

GitHub: [@prashanthreddy-134](https://github.com/prashanthreddy-134)

Project Repository: [StreamHub â€“ Full-Stack Video Streaming Platform](https://github.com/prashanthreddy-134/StreamHub-Full-Stack-Video-Streaming-Platform)

---

## ðŸ“„ License

This project is intended for educational and learning purposes.

A formal open-source license has not been specified. All rights remain with the project author unless a license is added to the repository.

---

## â­ Support

If you find this project useful, consider giving the repository a star on GitHub.

**StreamHub â€“ Watch. Share. Connect.**
