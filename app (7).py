import streamlit as st
import google.generativeai as palm

# Configure the API key
palm.configure(api_key="AIzaSyAYSUBWBve3AgCfrMZ1NEgsgbBGvk4mG0Q")

# Define the model to use
model_name = "models/text-bison-001"

def generate_career_pathway(user_interests, user_skills, career_goals):
    # Create a prompt for the generative AI model
    prompt = f"Provide personalized career guidance, job recommendations, and skill development resources based on user interests: {user_interests}, skills: {user_skills}, and career goals: {career_goals}."
    
    # Call the generative AI model
    response = palm.generate_text(model=model_name, prompt=prompt)
    
    return response.result

# Streamlit app
st.title("CareerMapper: AI-Powered Personal Career Mapping")

# Introduction text
st.markdown("""

CareerMapper is an innovative platform designed to provide personalized career mapping, guidance, and job recommendations based on individual interests, skills, and career goals. Leveraging the power of AI technology, CareerMapper assists users in navigating their career paths by analyzing their unique characteristics and providing tailored recommendations to help them achieve their professional aspirations. Whether users are exploring new career opportunities, seeking advancement in their current fields, or undergoing a career transition, CareerMapper offers personalized insights and resources to support their journey towards career success.

## Scenario 1: Career Exploration for Students
Students often face challenges when deciding on their future career paths. CareerMapper helps students explore various career options by analyzing their interests, skills, and aspirations. By inputting their academic interests, extracurricular activities, and desired career fields, students receive personalized career maps that highlight potential career paths, recommended educational pathways, and job opportunities. CareerMapper empowers students to make informed decisions about their future careers and pursue paths aligned with their interests and goals

## Scenario 2: Professional Development for Working Professionals
Working professionals seeking career advancement or considering a career change can benefit from CareerMapper's personalized career mapping capabilities. By inputting their current job role, skills, and career goals, professionals receive customized career maps that outline potential advancement opportunities, recommended skill development resources, and job market insights. Whether aiming for a promotion within their current organization or exploring new career paths, CareerMapper provides actionable insights to support professionals in achieving their career objectives.

## Scenario 3: Career Transition for Job Seekers
Job seekers undergoing career transitions often face uncertainty and challenges in navigating the job market. CareerMapper assists job seekers in identifying transferable skills, exploring alternative career paths, and accessing relevant job opportunities. By inputting their previous work experience, skills, and desired career fields, job seekers receive personalized career maps that highlight potential job roles, recommended training programs, and networking opportunities. CareerMapper empowers job seekers to navigate career transitions with confidence and pursue fulfilling career opportunities aligned with their aspirations.
""")

st.header("Enter Your Information")
user_interests = st.text_input("Interests", "e.g., programming, marketing, data analysis")
user_skills = st.text_input("Skills", "e.g., Python, communication, project management")
career_goals = st.text_input("Career Goals", "e.g., software engineer, digital marketer, business analyst")

if st.button("Get Career Advice"):
    if user_interests and user_skills and career_goals:
        with st.spinner("Generating personalized career advice..."):
            try:
                career_advice = generate_career_pathway(user_interests, user_skills, career_goals)
                st.success("Here is your personalized career advice!")
                st.write(career_advice)
            except Exception as e:
                st.error(f"Error generating career advice: {e}")
    else:
        st.error("Please provide all required information.")

