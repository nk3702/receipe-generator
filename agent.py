from pydantic import BaseModel, Field
from pydantic_ai import Agent
import os
from dotenv import load_dotenv

load_dotenv()

class Input(BaseModel):
    ingredients: str = Field(description="Comma-separated ingredients")

class Output(BaseModel):
    recipe_title: str = Field(description="Recipe title")
    steps: list[str] = Field(description="Step-by-step instructions")
    additional_tips: str = Field(description="Extra tips")

agent = Agent(
    model='openrouter:meta-llama/llama-3.1-8b-instruct',  # Free model
    api_key=os.getenv('OPENROUTER_API_KEY'),
    output_type=Output,
    instructions='Generate a simple, healthy recipe using the given ingredients. Be creative.'
)

async def generate_recipe(ingredients: str):
    input_data = Input(ingredients=ingredients)
    try:
        result = await agent.run(input_data)
        return result.output
    except Exception as e:
        return {"error": str(e)}  # Fallback