```
# 🧘 Gravity Fitness Booking App 🏋️‍♀️

A Django-based web application for booking fitness classes like Yoga, Zumba, and HIIT. It includes user authentication, real-time slot tracking, phone number validation, and intelligent timezone handling.

Took 10 working hours to build this web application

---

## 📌 Features

- ✅ User registration and login
- 📅 Browse available fitness classes
- 📥 Book slots with live availability check
- 📱 Phone number-based user info (validated)
- 🌍 Timezone-aware class schedule display
- 💡 Smart UI: “Book Now”, “Full”, and “Booked” states
- 🔒 Secure with Django auth and CSRF protection
- 📸 Images auto-rendered from static or Unsplash fallback
- 🧭 Mobile-first responsive design (Bootstrap 5.3)

---

## 🛠️ Technologies Used

- Python 3.10+
- Django 4.x
- PostgreSQL (or SQLite for dev)
- Bootstrap 5.3
- HTML5 / CSS3
- JavaScript (for timezone detection)

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/yourusername/gravity-fitness.git
cd gravity-fitness

---

### 2. Create and Activate Virtual Environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

---

### 3. Install Requirements

pip install -r requirements.txt

---

### 4. Database Configuration

Default uses SQLite.  
For PostgreSQL, update the `DATABASES` section in `settings.py`:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gravity_fitness',
        'USER': 'gravity_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

---

### 5. Apply Migrations

python manage.py makemigrations  
python manage.py migrate

---

### 6. Create Superuser (for admin access)

python manage.py createsuperuser

---

### 7. Run the Development Server

python manage.py runserver

Visit: http://127.0.0.1:8000

---

Add sample classes via Django Admin
Navigate to:
http://127.0.0.1:8000/admin/
and add entries like:

Name	Instructor	Date/Time (IST)	Slots
Yoga	Priya Sharma	2025-06-10 07:00:00+05:30	15
Zumba	Alex Brown	2025-06-11 18:00:00+05:30	10
HIIT	John Miller	2025-06-12 08:00:00+05:30	8

## 🕐 Timezone Management

### Why?

Classes are created in **IST**, but users may view them from different timezones.

### How it works:

1. Django stores all datetimes in UTC (with `USE_TZ = True`)
2. IST (`Asia/Kolkata`) is set as the default timezone
3. User timezone is auto-detected via JS and stored in a cookie
4. Custom middleware reads this cookie and sets the timezone
5. Template filter `|localtime` is used to render in the correct local time

✅ Example: If a Yoga class is at 6:00 AM IST, and you're in New York, it shows as **7:30 PM (previous day)**.

---

## 🔐 Admin Panel

Visit http://127.0.0.1:8000/admin

- Manage users, fitness classes, and bookings
- Uses Django admin with custom filters

---

## 📱 Phone Number Validation

- Client-side validation (HTML5):
  - Required field
  - Must start with 6, 7, 8, or 9
  - Exactly 10 digits (or with optional +91)
- Stored in database under `Booking.phone`

---

## 🖼️ Class Images

- Looks for: `/static/images/classes/Yoga.jpeg`, etc.
- Fallbacks to Unsplash if not found:

<img src="{% static 'images/classes/Yoga.jpeg' %}"
     onerror="this.src='https://source.unsplash.com/400x200/?fitness,Yoga';">

---

## 🔧 To-Do (Enhancements)

- ✅ Email/OTP login
- 📅 Calendar view for booked slots
- 🔔 Reminder emails (Celery)
- 📊 User dashboard with stats
- 🧾 Payment gateway integration

---

## 🙋 Support

For bugs, feature requests, or contributions, feel free to raise an issue or pull request.


---

> Built by srikarkopanati
```
