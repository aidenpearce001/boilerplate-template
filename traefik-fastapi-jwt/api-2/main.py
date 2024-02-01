from fastapi import FastAPI

app = FastAPI()

@app.get("/api-2")
async def api_2_endpoint():
    return {"message": "Access granted to API-2"}