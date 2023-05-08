from fastapi import FastAPI
from pydantic import BaseModel  
from typing import Optional

app = FastAPI()

class Todos(BaseModel):
    title: str
    description: str
    done: bool

class updateTodo(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None

true = True 
false = False

todos = {
    1: {
        "title": "Read a book.",
        "description": "Read the art of not giving a ****",
        "Done": true
    },
    2: {
        "title": "Cycling",
        "description": "Cycle around gbk",
        "Done": false
    }
}
AmIdoneTodos = {
    1:
    {
    "title": "Read a book.",
    "description": "Read the art of not giving a ****",
    "Done": true
    }
}
@app.get("/todo/")
def todoPrint():
    return todos

@app.get("/get-todo/{todo_id}")
def get_todo(todo_id: int):
    return todos[todo_id]

@app.get("/get-todo-by-title/{todo_id}")
def get_todo(*, todo_id:int, title: Optional[str] = None, test:int):
    for todo_id in todos:
        if todos[todo_id]["title"] == title:
            return todos[todo_id]
    return {"Data": "Presence of such object was not detected"}

@app.post("/create-todo/{todo_id}")
def create_todo(todo_id: int, todo: Todos):
    if todo_id in todos:
        return {"Error:" "This todo is with us (The id already exists)"}
    
    todos[todo_id] = todo
    return todos[todo_id]

@app.put("/LeUpdate/{todo_id}")
def update_todo(todo_id:int, todo:updateTodo):
    if todo_id not in todos:
        return{"Error": "Presence of such object was not detected"}
    if todo.title != None: 
        todos[todo_id].title = todo.title
    if todo.description != None:
        todos[todo_id].description = todo.description
    if todo.done != None: 
        todos[todo_id].done = todo.done
    
    return todos[todo_id]

@app.delete("/byebye/{todo_id}")
def del_todo(todo_id:int):
    if todo_id not in todos:
        return {"Error": "What exists not cannot be unexisted"}
    del todos[todo_id]
    return {"Iz successfully gone"}