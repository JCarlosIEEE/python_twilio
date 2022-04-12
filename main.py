from fastapi import FastAPI

app = FastAPI()

@app.get("/inicio")
async def root():
    return "Hello World!"