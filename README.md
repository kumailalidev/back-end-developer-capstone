# **Back-End Developer Capstone**
## **Little Lemon Web Application 🍋**
<br>

### **Description**:
This capstone project is part of **Back-End Developer Capstone** course offered by **Meta** on Coursera and covers building a capstone project in Django, specifically building an API for the Little Lemon restaurant using the Django REST Framework.
<br>
<br>

## **Setup**

### **1. Setup and activate python virtual environment (Windows)**
```bash
python -m venv .venv
.\Scripts\activate
```
### **2. Install dependencies**
```bash
pip install requirements
```
### **3. Setup MySQL database**
Open `.\litlelemon\littlelemon\settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS' : {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```
Replace `database_name`, with the database you created, `username`, and `password` with MySQL user and password.
<br>

### **4. Perform migrations**
```bash
cd .\littlelemon\
python manage.py makemigrations
python manage.py migrate
```
<br>

### **5. Start Django server**
```
python manage.py runserver
```
