@echo off
uvicorn skillready.asgi:application --reload --reload-dir skillready --app-dir skillready
