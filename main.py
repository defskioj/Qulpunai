from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Подключаем статику (убедись, что папка static существует)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home():
    # Мы просто отдаем файл как он есть, без Jinja2
    return FileResponse("templates/index.html") 

@app.get("/catalog")
async def get_catalog():
    return FileResponse("templates/catalog.html")