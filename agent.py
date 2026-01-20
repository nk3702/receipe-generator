from pydantic import BaseModel, Field
from pydantic_ai import Agent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Input(BaseModel):
    ingredients: str = Field(description="Comma-separated list of available ingredients")

class Output(BaseModel):
    recipe_title: str = Field(description="A catchy title for the recipe")
    steps: list[str] = Field(description="Step-by-step cooking instructions")
    additional_tips: str = Field(description="Any extra cooking tips or variations")

# Initialize the AI agent – IMPORTANT: use openrouter: prefix
agent = Agent(
    model='qwen/qwen2.5-7b-instruct:free',  # ← This is the correct format
    output_type=Output,
    instructions=(
        "You MUST respond ONLY with valid JSON matching this exact structure - no extra text, no explanations, no markdown:\n"
    "{\n"
    '  "recipe_title": "short catchy title",\n'
    '  "steps": ["step 1", "step 2", ...],\n'
    '  "additional_tips": "optional tips or empty string"\n'
    "}\n"
    "Generate a simple, healthy recipe using ONLY the provided ingredients. "
    "Be concise and creative. Do NOT add any other text outside the JSON."
    )
)

async def generate_recipe(ingredients: str):
    """Run the AI agent to generate a recipe."""
    try:
        input_data = Input(ingredients=ingredients)
        result = await agent.run(input_data)
        return result.output  # Returns the structured Output model
    except Exception as e:
        return {"error": f"Failed to generate recipe: {str(e)}"}