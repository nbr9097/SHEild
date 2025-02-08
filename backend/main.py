from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.alert import router as alert_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(auth_router, prefix="/api/auth")
app.include_router(alert_router, prefix="/api/alert")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)