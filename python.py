from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

NEW_API_URL = "https://mengtopup.shop/api/check_payment?md5={md5}"

@app.get("/check_payment/{md5}")  # Changed to path parameter for md5
async def check_payment(md5: str):
    if not md5:
        raise HTTPException(status_code=400, detail="md5 parameter is required")
    
    target_url = NEW_API_URL.format(md5=md5)
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(target_url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"API error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

@app.get("/dev")
async def dev():
    return {"dev": "made@by@panha"}

@app.get("/infor")
async def infor():
    return {"infor": "trueid26"}
