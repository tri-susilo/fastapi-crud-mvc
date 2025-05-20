from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictFloat


class ProductBase(BaseModel):
    name : str = Field(..., min_length=1, max_length=100, description="Nama produk")
    description: Optional[str] = Field(None, min_length=1)
    price: StrictFloat = Field(..., gt=0)
    stock: Optional[int] = Field(0, ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock:int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True