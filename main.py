from typifrom fastapi.templating import Jinja2Templatesng import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()


conn = MongoClient('mongodb+srv://aayushgajera2000:<password>@cluster0.z8ju6y2.mongodb.net/')



