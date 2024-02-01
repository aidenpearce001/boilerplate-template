from fastapi import FastAPI, Request, HTTPException
import httpx

app = FastAPI()

OPA_URL = "http://opa-service:8181"  # URL of your OPA service

@app.middleware("http")
async def opa_authorization(request: Request, call_next):
    # Extract token or user info from the request
    token = request.headers.get("Authorization")

    # Prepare input for OPA
    input_data = {
        "input": {
            "user": token,  # or parsed user information
            "path": request.url.path,
            "method": request.method
        }
    }

    # Query OPA
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{OPA_URL}/v1/data/your_policy_name/allow", json=input_data)
        opa_response = response.json()

    # Check OPA's decision
    if not opa_response.get("result"):
        raise HTTPException(status_code=403, detail="Access Denied")

    response = await call_next(request)
    return response