from fastapi import FastAPI
from routers import messages

app = FastAPI()

app.include_router(messages.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}