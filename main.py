# main.py
from fastapi import FastAPI
from app.routes import product
from app.config import settings
from app.models import product as product_model
from app.database import engine

# Create database tables
product_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

# Include routers
app.include_router(product.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI MVC API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)