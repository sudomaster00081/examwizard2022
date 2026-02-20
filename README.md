
# Django Docker Project

## Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Quick Start

1. **Ensure your `.env` file is configured** (see root directory).
2. **Build and run the containers:**
   ```bash
   docker-compose up --build
   ```
   *This automatically waits for the database, runs migrations, and creates a superuser if `DEBUG=True`.*

3. **Access the application:**
   - **Web:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - **Admin:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
     - **Username:** `admin`
     - **Password:** `adminpassword123`
     *(Configured in `docker-compose.yml`)*

## Stop the Project
```bash
docker-compose down
```

## Reset Database (Optional)
To wipe all data and start fresh:
```bash
docker-compose down -v
docker-compose up --build
```