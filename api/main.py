from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
    response_template = {
        "msg": "Service up..",
        "status_code":200
    }
    return response_template