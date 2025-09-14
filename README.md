#  Note App (Flask + MySQL + Docker)

This is a simple **Note-Taking Web Application** built using:
- [Flask](https://flask.palletsprojects.com/) (Python backend)
- [MySQL](https://www.mysql.com/) (Database)
- [Docker](https://www.docker.com/) & Docker Compose (Containerization)

---

##  Features
- Add and view notes through a simple frontend.
- Notes are stored in a MySQL database.
- Persistent storage using Docker volumes.
- Ready to deploy anywhere with Docker Compose.

---

##  Project Structure
note-app/
│── app.py # Flask application
│── Dockerfile # Docker image for Flask app
│── docker-compose.yml # Orchestrates Flask + MySQL containers
│── requirements.txt # Python dependencies
│── templates/ # HTML templates (frontend)
│ └── index.html

---

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/note-app.git
cd note-app
2. Start the application
docker-compose up -d --build
3. Access the app
Open http://localhost:8080
 in your browser.
Database Access
From inside the MySQL container:
docker exec -it my-sql-db mysql -u ziad -p notesdb

Or run SQL query directly:
نسخ الكود
docker exec -it my-sql-db mysql -u ziad -p -e "USE notesdb; SELECT * FROM notes;"
🗂 Volumes

The MySQL data is persisted inside a Docker volume:

db_data → /var/lib/mysql

So your notes will not be lost even if the container is removed.
Notes

The app currently runs in Flask development mode.

For production, consider using Gunicorn or uWSGI behind NGINX.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/69b7f911-c9ba-4a29-b87f-6faca88884f3" />


🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.


