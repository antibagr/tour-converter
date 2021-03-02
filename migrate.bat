@echo off
python skillready\manage.py makemigrations
python skillready\manage.py migrate
