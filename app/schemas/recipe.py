from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class RecipeCreate(BaseModel):
    title: str = Field(..., example="Spaghetti Carbonara")
    ingredients: List[str] = Field(..., example=["spaghetti", "eggs", "cheese", "pancetta", "pepper"])
    instructions: str = Field(..., example="Cook spaghetti...")

class RecipeOut(BaseModel):
    id: int
    title: str
    ingredients: List[str]
    instructions: str
    created_at: datetime

    class Config:
        orm_mode = True