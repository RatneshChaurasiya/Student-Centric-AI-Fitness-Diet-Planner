import os
from dotenv import load_dotenv
import streamlit as st
import utils
import ai_engine

load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="AI Fitness & Diet Planner",
    page_icon="💪",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("💪 Student-Centric AI Fitness & Diet Planner")
    st.markdown("### Personalized routines that fit your student life and budget.")

    # Sidebar for Inputs
    st.sidebar.header("Your Profile")
    
    name = st.sidebar.text_input("Name", "Student")
    age = st.sidebar.number_input("Age", 16, 60, 20)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.sidebar.number_input("Weight (kg)", 40.0, 150.0, 60.0)
    height = st.sidebar.number_input("Height (cm)", 140.0, 220.0, 170.0)
    
    # Calculate BMI
    bmi = utils.calculate_bmi(weight, height)
    bmi_category = utils.get_bmi_category(bmi)
    st.sidebar.info(f"**BMI:** {bmi} ({bmi_category})")
    
    # API Key Handling (Prioritize .env, fallback to user input)
    env_api_key = os.getenv("GEMINI_API_KEY")
    
    if env_api_key:
        api_key = env_api_key
        st.sidebar.success("✅ System API Key Active")
    else:
        st.sidebar.warning("System Key not found.")
        st.sidebar.info("Enter your personal API Key to generate plans.")
        api_key = st.sidebar.text_input("Gemini API Key", type="password")

    # Main Content Area
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Preferences")
        fitness_goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintain Fitness", "Increase Stamina"])
        activity_level = st.select_slider("Activity Level", options=["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
        
    with col2:
        st.subheader("Constraints")
        dietary_pref = st.selectbox("Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Eggetarian"])
        cuisine_type = st.selectbox("Preferred Cuisine", ["Indian", "Western", "Mediterranean", "Asian"])
        budget_level = st.select_slider("Budget Level", options=["Low (Student Friendly)", "Medium", "High"])

    if st.button("Generate My Plan"):
        if not api_key:
            st.error("Please enter your Google Gemini API Key in the sidebar.")
        else:
            with st.spinner("Generating your personalized student plan... This may take a few seconds."):
                # Prepare User Profile
                user_profile = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "weight": weight,
                    "height": height,
                    "bmi": bmi,
                    "bmi_category": bmi_category,
                    "fitness_goal": fitness_goal,
                    "activity_level": activity_level,
                    "dietary_pref": dietary_pref,
                    "cuisine_type": cuisine_type,
                    "budget_level": budget_level
                }
                
                # Call AI Engine
                plan = ai_engine.generate_plan(user_profile, api_key)
                
                # Display Result
                st.markdown("---")
                st.subheader(f"🎉 Your Personalized Plan, {name}!")
                st.markdown(plan)

if __name__ == "__main__":
    main()
