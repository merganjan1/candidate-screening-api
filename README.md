🧠 Candidate Screening Platform API

FastAPI va MongoDB asosida qurilgan backend API. Ushbu loyiha recruiterlar uchun job posting yaratish, kandidat arizalarini qabul qilish, avtomatik scoring va AI yordamida kandidatni Backend yoki AI/ML yo‘nalishiga mosligini aniqlash imkonini beradi.

🚀 Texnologiyalar

FastAPI – REST API

MongoDB – NoSQL ma’lumotlar bazasi

Motor – Async MongoDB driver

JWT Authentication – xavfsiz login/register

Pydantic – data validation

HuggingFace Transformers – lokal AI model

Uvicorn – ASGI server

📂 Loyiha tuzilmasi
candidate-screening-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── auth/
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── utils.py
│   │
│   ├── jobs/
│   │   ├── router.py
│   │   └── schemas.py
│   │
│   ├── candidates/
│   │   ├── router.py
│   │   └── schemas.py
│   │
│   └── ai/
│       └── classifier.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md

⚙️ O‘rnatish
1️⃣ Repository’ni clone qilish
git clone https://github.com/your-username/candidate-screening-api.git
cd candidate-screening-api

2️⃣ Virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Dependency’larni o‘rnatish
pip install -r requirements.txt

4️⃣ MongoDB ishga tushirish
mongod

🔐 Environment sozlamalari

.env fayl yarating:

MONGO_URI=mongodb://localhost:27017
DB_NAME=candidate_db
JWT_SECRET=supersecretkey
JWT_ALGORITHM=HS256

▶️ Serverni ishga tushirish
uvicorn app.main:app --reload


Server:
👉 http://127.0.0.1:8000

Swagger UI:
👉 http://127.0.0.1:8000/docs

🔑 Authentication

POST /auth/register – foydalanuvchi ro‘yxatdan o‘tish

POST /auth/login – login va JWT token olish

JWT token protected endpoint’larda talab qilinadi.

💼 Job Posting

POST /jobs/ – yangi job yaratish

GET /jobs/ – barcha job’larni ko‘rish

👤 Candidate Application

POST /candidates/ – kandidat ariza topshiradi

Resume va skill’lar asosida avtomatik score hisoblanadi

🤖 AI Classification

Loyiha lokal Transformer model ishlatadi va kandidatni quyidagi yo‘nalishlardan biriga tavsiya qiladi:

Backend Department

AI / ML Department

Model app/ai/classifier.py ichida joylashgan.

📌 Eslatma

Loyiha Backend Engineer (Mid-Level) texnik topshirig‘i asosida bajarilgan

Frontend mavjud emas (faqat API)

AI model internetga chiqmasdan, lokal ishlaydi