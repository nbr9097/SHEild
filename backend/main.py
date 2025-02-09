from fastapi import FastAPI
from routes.auth import router as auth_router
# from routes.alert import router as alert_router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()

app.include_router(auth_router, prefix="/api/auth")
# app.include_router(alert_router, prefix="/api/alert")

origins = [
   "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)