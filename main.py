from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import generate_recipe
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Recipe Generator API - Haveloc Assignment")

# Allow frontend (Vite dev server + Vercel) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],  # * for testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecipeRequest(BaseModel):
    ingredients: str

@app.post("/generate_recipe")
async def get_recipe(request: RecipeRequest):
    """
    Endpoint to generate a recipe from user-provided ingredients.
    """
    if not request.ingredients.strip():
        raise HTTPException(status_code=400, detail="Ingredients cannot be empty")

    logger.info(f"Received request with ingredients: {request.ingredients}")

    try:
        result = await generate_recipe(request.ingredients)
        
        if "error" in result:
            logger.error(result["error"])
            raise HTTPException(status_code=500, detail=result["error"])
        
        logger.info("Recipe generated successfully")
        return result
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error - please try again later")

@app.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return {"status": "healthy", "message": "Backend is running"}

# Optional: run locally with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)