from fastapi import FastAPI

app = FastAPI()

@app.get("/api-1")
async def api_1_endpoint():
    return {"message": "Access granted to API-1"}