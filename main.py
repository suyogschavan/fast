from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {
            'data': {'name':'Suyog'}}
    
@app.get('/about')
def about():
    return {'data': {'name': 'Suyog', 'page':'About'}}