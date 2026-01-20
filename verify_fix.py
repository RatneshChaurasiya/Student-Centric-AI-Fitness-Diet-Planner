import ai_engine
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

profile = {
    "name": "Test Student",
    "age": 20,
    "gender": "Female",
    "weight": 60,
    "height": 170,
    "bmi": 20.7,
    "bmi_category": "Normal Weight",
    "fitness_goal": "Maintain Fitness",
    "activity_level": "Moderately Active",
    "dietary_pref": "Vegetarian",
    "cuisine_type": "Indian",
    "budget_level": "Low"
}

print("Testing generate_plan...")
result = ai_engine.generate_plan(profile, api_key)
if result.startswith("Error"):
    print("FAILED:", result)
else:
    print("SUCCESS: Plan generated (first 100 chars):")
    print(result[:100])
