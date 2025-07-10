from fastapi import APIRouter

router = APIRouter()

# Example route
@router.get("/recipes/test")
def test_recipes():
    return {"message": "Recipes endpoint is working!"}