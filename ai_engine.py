import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def configure_genai(api_key):
    """Configures the Gemini API with the provided key."""
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        print(f"Error configuring API: {e}")
        return False

def generate_plan(user_profile, api_key):
    """
    Generates a workout and diet plan using Gemini API.
    
    Args:
        user_profile (dict): Dictionary containing details like:
            - name, age, gender, weight, height, bmi, bmi_category
            - fitness_goal, activity_level
            - dietary_pref, cuisine_type, budget_level
        api_key (str): The Google Gemini API key.
        
    Returns:
        str: The generated plan (markdown format) or an error message.
    """
    if not api_key:
        return "Error: API Key is missing."

    # Configure API
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-flash-latest')
    except Exception as e:
        return f"Error configuring API: {str(e)}"

    # Construct the Prompt
    prompt = f"""
    Act as a professional Fitness Trainer and Nutritionist. Create a personalized "Student-Centric Workout & Diet Plan" for the following student:

    **User Profile:**
    - **Name:** {user_profile.get('name')}
    - **Age:** {user_profile.get('age')} years
    - **Gender:** {user_profile.get('gender')}
    - **Weight:** {user_profile.get('weight')} kg
    - **Height:** {user_profile.get('height')} cm
    - **BMI:** {user_profile.get('bmi')} ({user_profile.get('bmi_category')})

    **Goals & Preferences:**
    - **Fitness Goal:** {user_profile.get('fitness_goal')}
    - **Activity Level:** {user_profile.get('activity_level')}
    - **Dietary Preference:** {user_profile.get('dietary_pref')}
    - **Preferred Cuisine:** {user_profile.get('cuisine_type')}
    - **Budget:** {user_profile.get('budget_level')} (Crucial: Keep it student-friendly!)

    **Requirements:**
    1. **Workout Plan:**
       - Create a weekly schedule (Mon-Sun).
       - Focus on exercises that are suitable for their goal and activity level.
       - Consider they are a student (time-efficient routines).
       - If budget is low, suggest home workouts or minimal equipment.
    
    2. **Diet Plan:**
       - Create a daily meal framework (Breakfast, Lunch, Snack, Dinner).
       - STRICTLY follow the "{user_profile.get('cuisine_type')}" cuisine and "{user_profile.get('dietary_pref')}" preference.
       - Focus on low-cost, nutritious ingredients available in local markets.
       - Include estimated calorie counts for meals.

    3. **Tips:**
       - Give 3 specific tips for maintaining consistency as a busy student.
       
    **Output Format:**
    - Use clean Markdown formatting.
    - Use bold headings for sections.
    - Use tables for the Workout Schedule.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"
