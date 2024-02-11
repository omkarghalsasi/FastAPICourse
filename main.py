from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'hello world!'

@app.get('/hello')
def index2():
    return 'Hi'

@app.get('/hellojson')
def index3():
    return {"message": "hello"}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {"message": f'blog with id {id}'}

