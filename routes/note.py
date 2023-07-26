from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()



@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    docs = conn.notes.notes.find_one({})
    newDocs = []
    for doc in docss:
        newDocs.append({
            "id":doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"],
        })
    return templates.TemplateResponse("item.html", {"request": request,newDocs:newDocs)


@note.post("/")
def add_note(note: Note ):
    print(note)
    inserted_note = conn.notes.notes.insert_one(dict(note))
    return noteEntity(inserted_note)

@note.post("/", response_class=HTMLResponse)
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if  formDict["important"] == 'on' else False
    note = conn.notes.notes.insert_one(formDict)
    return {"Success":True}
