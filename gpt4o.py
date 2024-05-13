import streamlit as st
import openai
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Your API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to get GPT response using GPT-4
def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4",  # Use "gpt-4" for the GPT-4 model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            stop=None
        )
        logging.info("GPT-4 response received successfully")
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error getting GPT-4 response: {e}")
        return "There was an error getting the response."

# Streamlit app setup
st.title("Family GPT Assistant")

# User input
user_input = st.text_input("Ask a question:")
if user_input:
    # Construct the prompt with the same context and formatting as used in the Playground
    prompt = f"Family members: Ada Solario, Bucky Solario, Mando Solario, Kayla Solario, Savanah Solario, Marj Stice, Nichole Payne, Sheree Solario, Chris Solario.\n\n{user_input}"
    response = get_gpt_response(prompt)
    st.write(response)
