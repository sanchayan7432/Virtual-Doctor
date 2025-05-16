import streamlit as st
import google.generativeai as genai

# Step 1: Configure API key
genai.configure(api_key="AIzaSyB8MGZ5CQ2iqAsZOk3dWMa_VNaTXTJsKeg")  # Replace with your Gemini API key

# Step 2: Define the assistant model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=(
        "You are a certified medical doctor. Provide safe, clear diagnostic health advice "
        "and prescribe medicine recommendation with composition in a professional, precise and reassuring tone. "
        "Give pointwise response within 70 words."
    )
)

# Step 3: Session state to switch between pages
if "page" not in st.session_state:
    st.session_state.page = "front"  # Start on front page

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat()

# Function to show the front page
def show_front_page():
    st.title("HEALITICS MEDICAL ASSISTANT")
    st.image("Gemini_Generated_Image_jroozajroozajroo.jpeg", use_column_width=True)
    st.markdown("""
    🤖 Your AI-Powered Health Advisor
    - Ask about symptoms, get safe medical advice.
    - Receive medicine recommendations with composition.
    - Professional, precise, and concise responses.
    
    👉 Note: Always consult a human doctor for emergencies.

    """)
    if st.button("Enter Clinic"):
        st.session_state.page = "assistant"

# Function to show the assistant interface
def show_medical_assistant():
    st.title("👨‍⚕️ HEALITICS VIRTUAL ASSISTANT")
    st.image("Gemini_Generated_Image_8fcyhq8fcyhq8fcy.jpeg", use_column_width=True)
    st.markdown("Ask any health issues related question below:")

    user_input = st.text_input("Your Query", key="input")

    if st.button("Get Advice") and user_input:
        # Main doctor response
        response = st.session_state.chat.send_message(user_input)
        st.subheader("HEALITICS's Advice")
        st.write(response.text)

        # Summary generation
        summary_model = genai.GenerativeModel("gemini-2.0-flash")
        summary_prompt = f"Summarize this advice in 2 short sentences including disease and medicine needed\n{response.text}"
        summary_response = summary_model.generate_content(summary_prompt)

        st.subheader("🔍 Summary")
        st.write(summary_response.text)
        
        st.markdown("---")
        st.markdown("### 🛒 Need to buy medicine?")
        st.link_button("Go to Specific Medical Website", url="https://www.1mg.com")


    if st.button("⬅ Back to Home"):
        st.session_state.page = "front"

# Render the correct page based on state
if st.session_state.page == "front":
    show_front_page()
else:
    show_medical_assistant()
