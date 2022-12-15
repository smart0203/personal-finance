# Personal Financial App
Simple personal financial app developed by Django

### Technical Stacks
* Programming Language: **`Python 3.9`**
* Framework: **`Django 4.1.3`**

### Configuring and Running Site on Local

##### 1. First, Create virtualenv

```bash
virtualenv venv
```

##### 2. Activate virtualenv

```bash
source venv/bin/activate
```

##### 3. Install python packages

```bash
pip install -r requirements.txt
```

##### 4. Create `personal_finance/local_settings.py` from `personal_finance/local_settings.py.example`
##### (fill in proper values like DATABASES, EMAIL_BACKEND, and so on.)


##### 5. Run Database Migration
```bash
python manage.py migrate
```

##### 6. Create superuser
```bash
python manage.py createsuperuser
```

##### 7. Run Site locally
```bash
python manage.py runserver
```
