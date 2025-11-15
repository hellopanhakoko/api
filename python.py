from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

NEW_API_URL = "https://mengtopup.shop/api/check_payment?md5={md5}"


@app.get("/check!payment")
async def check_payment():
    target_url = NEW_API_URL

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(target_url)
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/dev")
async def dev():
    return {"dev": "made@by@panha"}


@app.get("/infor")
async def infor():
    return {"infor": "trueid26"}
