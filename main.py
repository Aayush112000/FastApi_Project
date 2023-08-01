from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


conn = MongoClient('mongodb+srv://aayushgajera2000:sLhTGxrqv5Ma19oA@cluster0.z8ju6y2.mongodb.net/test')

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find_one({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id": doc[_id],
            "note": doc["note"]
        } )
    return templates.TemplateResponse("index.html",{"request":request, newDocs:newDocs  })

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str| None = None):
    return {"item_id": item_id, "q":q}
