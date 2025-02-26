
python -m venv .venv

.\.venv\Scripts\activate

pip install django

django-admin startproject setup .

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'niuan.spolid@gmail.com'
EMAIL_HOST_PASSWORD = 'qlpv rgxv itln egwq'
