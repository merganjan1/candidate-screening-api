# Candidate Screening API

FastAPI + MongoDB asosida qurilgan **Candidate Screening Platform API**. Ushbu backend recruiterlar uchun nomzodlarning CV (resume)larini saqlash, ko‘rish va token orqali himoyalangan endpointlar bilan ishlash imkonini beradi.

---

## 🚀 Texnologiyalar

* **FastAPI** – REST API
* **MongoDB** – Ma’lumotlar bazasi
* **Motor** – Async MongoDB driver
* **JWT (OAuth2 Password Flow)** – Authentication
* **Swagger UI** – API testlash

---

## 📦 Loyihani ishga tushirish

### 1️⃣ Repository’ni clone qilish

```bash
git clone <repo_url>
cd candidate-screening-api
```

### 2️⃣ Virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux / Mac
```

### 3️⃣ Dependency’larni o‘rnatish

```bash
pip install -r requirements.txt
```

### 4️⃣ MongoDB ishga tushirish

```bash
mongod
```

MongoDB default: `mongodb://localhost:27017`

### 5️⃣ Backend server

```bash
uvicorn app.main:app --reload
```

Server: [http://127.0.0.1:8000](http://127.0.0.1:8000)
Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔐 Authentication (JWT + Swagger OAuth)

### Register (ochiq endpoint)

`POST /auth/register`

```json
{
  "email": "test@mail.com",
  "password": "123456",
  "role": "recruiter"
}
```

### Login (OAuth2 Password Flow)

Swagger orqali:

1. `/docs` sahifasiga o‘ting
2. 🔒 **Authorize** tugmasini bosing
3. `username` → email
4. `password` → password
5. **Authorize**

Swagger avtomatik tokenni `Authorization` header’ga qo‘shadi.

---

## 📄 Resume API (Protected)

### Create Resume

`POST /resumes/`

```json
{
  "full_name": "Ali Valiyev",
  "email": "ali@mail.com",
  "skills": ["Python", "FastAPI", "MongoDB"],
  "experience": 2,
  "resume_text": "Backend developer with FastAPI and MongoDB experience"
}
```

### List Resumes

`GET /resumes/`

### Get Resume by ID

`GET /resumes/{resume_id}`

⚠️ Ushbu endpointlar **JWT token** talab qiladi.

---

## 🧠 Muhim Texnik Nuqtalar

* JWT **stateless authentication** ishlatadi
* Token `Authorization: Bearer <token>` orqali yuboriladi
* MongoDB `ObjectId` → `str()` qilib qaytariladi
* Swagger OAuth2 `OAuth2PasswordRequestForm` bilan integratsiya qilingan

---

## ✅ Holat

* Auth: ✅
* Swagger OAuth: ✅
* Resume CRUD: ✅
* MongoDB integration: ✅

---

