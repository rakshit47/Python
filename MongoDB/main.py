from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def Home():
    return "Welcome back"