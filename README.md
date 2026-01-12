# Django Personal Website 🌐

Bu loyiha **Django framework** yordamida yaratilgan shaxsiy veb-sayt.  
Sayt **database ishlatmaydi**, **Django Admin panel yo‘q** va **static folder ishlatilmagan**.

Barcha kontent:
- HTML template’lar orqali render qilinadi
- GitHub’dan olinadigan ma’lumotlarga tayangan

---

## 🚀 Texnologiyalar
- Python 3.x
- Django 5.2
- HTML
- Virtual Environment (venv)
- GitHub Raw Content / API

---

## 📌 Muhim eslatmalar
- ❌ Database ishlatilmaydi (default SQLite mavjud, lekin foydalanilmaydi)
- ❌ Django Admin panel ishlatilmaydi
- ❌ `static/` papkasi yo‘q
- ✅ Kontent template va tashqi manbalardan olinadi
- ✅ Loyiha **content-based personal website**

---

## ⚙️ O‘rnatish (Local)
```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
````

Brauzerda oching:

```
http://127.0.0.1:8000/
```

---

## 🔐 Environment variables

Loyiha `.env` fayl orqali boshqariladi. Namuna `.env.sample` faylda mavjud.

### `.env.sample`

```env
SECRET_KEY=your_secret_key_here
DEBUG_MODE=production/development

GITHUB_BASE_URL=https://raw.githubusercontent.com/your-username/your-repo/main
CACHE_TIMEOUT=86400
```

`.env` fayl yarating:

```bash
cp .env.sample .env
```

> ⚠️ `.env` fayl **GitHub’ga yuklanmasligi kerak** (`.gitignore` ichida mavjud)

---

## 📁 Loyihaning tuzilishi

```
django-personal-website/
├── core/           # django-admin startproject
├── blog/           # django-admin startapp
├── templates/      # barcha HTML sahifalar
├── .env            # environment variables
├── .env.sample     # .env uchun namuna
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 requirements.txt

`requirements.txt` faylda loyiha uchun zarur bo‘lgan **Python paketlari** ro‘yxati mavjud.
Ular `pip install -r requirements.txt` orqali o‘rnatiladi.

---

## 🛠 Development holati

Loyiha **minimalistik va database-free** yondashuv asosida ishlab chiqilgan.

Rejalashtirilgan:

* GitHub’dan dynamic kontent olish
* Caching mexanizmlarini yaxshilash
* Production deployment

---

## 👤 Muallif

**Mehroj Saparov**

GitHub: [https://github.com/mehroj-saparov-io](https://github.com/mehroj-saparov-io)
