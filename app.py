import streamlit as st
import os
import google.generativeai as genai
import re
from dotenv import load_dotenv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load NLTK resources
nltk.download('vader_lexicon', quiet=True)
sid = SentimentIntensityAnalyzer()

# Load API key from environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    response.resolve()  # Wait for the complete response
    return response

def analyze_politeness(text):
    sentiment_score = sid.polarity_scores(text)
    return sentiment_score['pos']

# Initializing Streamlit
st.set_page_config(page_title="Negotiation Session")
st.header("Gemini LLM Application")

# Initializing chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input handling
input_text = st.text_input("Input:", key="input")
submit = st.button("Bargain")

MIN_PRICE = 50
MAX_PRICE = 150

def extract_number_from_text(text):
    # Extract number from input sentence using regex
    numbers = re.findall(r'\d+', text)
    return int(numbers[0]) if numbers else None

if submit and input_text:
    user_price = extract_number_from_text(input_text)
    if user_price is None:
        st.write("Please provide a valid price in your input.")
    else:
        # Determine AI response based on user price and politeness
        if user_price < MIN_PRICE:
            if analyze_politeness(input_text) < 0.4:
                ai_prompt = f"The user is offering {user_price}, which is lower than the minimum price of {MIN_PRICE}. Respond firmly that the offer cannot be accepted."
            else:
                ai_prompt = f"The user is offering {user_price}, which is lower than the minimum price of {MIN_PRICE}. Respond politely that this offer cannot be accepted."
        elif user_price > MAX_PRICE:
            if analyze_politeness(input_text) < 0.4:
                ai_prompt = f"The user is offering {user_price}, which is higher than the maximum price of {MAX_PRICE}. Respond firmly, suggesting a lower price within the acceptable range."
            else:
                ai_prompt = f"The user is offering {user_price}, which is higher than the maximum price of {MAX_PRICE}. Respond politely, suggesting a lower price within the acceptable range."
        else:
            ai_prompt = f"The user is offering {user_price}. Respond to the offer directly without suggesting additional terms."

        # Get response from the Gemini LLM
        response = get_gemini_response(ai_prompt)

        # Combine the entire response text and display "Bot:" only once
        full_response = ''.join([chunk.text for chunk in response])

        # Append user and bot responses to chat history
        st.session_state['chat_history'].append(("YOU", input_text))
        st.session_state['chat_history'].append(("Bot", full_response))

# Display the chat history
st.subheader("HISTORY:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
