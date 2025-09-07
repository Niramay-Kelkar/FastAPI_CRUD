# FastAPI MySQL CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with **FastAPI** and **MySQL** using SQLAlchemy ORM.

---

## 🚀 Features
- FastAPI for building high-performance APIs
- SQLAlchemy ORM for database interaction
- MySQL as the database backend
- Pydantic schemas for request/response validation
- Uvicorn for ASGI server

---

## 📂 Project Structure

```
.
├── database.py     # Database connection and session management
├── main.py         # FastAPI app entrypoint & API endpoints
├── models.py       # SQLAlchemy models (database tables)
├── schemas.py      # Pydantic schemas (request/response models)
├── requirements.txt # Python dependencies
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2️⃣ Create & activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start MySQL server
Make sure MySQL is running and accessible.

Create the database (if not already created):
```sql
CREATE DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Update **`database.py`** with your MySQL username and password.

---

## ▶️ Run the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at:  
👉 http://127.0.0.1:8000

Interactive API docs:  
👉 http://127.0.0.1:8000/docs

---

## 📌 Example API Endpoints

- **Create students** → `POST /students/`
- **Get all students** → `GET /students/`
- **Get single student** → `GET /students/{student_id}`
- **Update student** → `PUT /students/{student_id}`
- **Delete student** → `DELETE /students/{student_id}`

---

## 📦 Requirements

Dependencies are listed in `requirements.txt`:
```
fastapi
uvicorn
sqlalchemy
pymysql
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Development Notes
- Update `database.py` with correct DB credentials
- Run `Base.metadata.create_all(bind=engine)` to create tables
- Use `.venv` for isolation
- Test endpoints using Swagger UI or Postman

---

## 📜 License
This project is licensed under the MIT License.
