from fastapi import FastAPI

app = FastAPI()

@app.get('/users/me')
async def read_user_me():
    return {'user id:': 'The current User'}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user id': user_id}




