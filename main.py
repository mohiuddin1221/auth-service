from fastapi import FastAPI
from src.user.router import router
from src.user import listeners


app = FastAPI()
app.include_router(router)


@app.get("/")
def health():
    return {"status": "Healthy"}
