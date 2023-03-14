<<<<<<< HEAD

=======
>>>>>>> development_anusha
FROM python:3
RUN pip install Django
COPY . .
RUN python manage.py migrate
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
<<<<<<< HEAD

=======
>>>>>>> development_anusha
