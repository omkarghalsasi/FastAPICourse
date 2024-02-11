# FastAPICourse
Intro to python fast api

#Installation 
## make virtual env
python3 -m venv fastapi-tutorial-venv
source fastapi-tutorial-venv/bin/activate
pip3 install uvicorn fastapi

#Start the server
uvicorn main:app --reload 
# filename:instanceoffastapi

# docs endpoing
/docs
/redoc

## Get method
Path Parameters
@app.get('/blog/{id}')
Predefined Values
enums
Query Parameters

## Order is important in path methods in get path functions