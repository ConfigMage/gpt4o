import streamlit as st
import openai
import os

# Set up OpenAI API key and assistant ID from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["GPT_ASSISTANT_ID"] = st.secrets["GPT_ASSISTANT_ID"]

# Configure OpenAI with the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("GPT_ASSISTANT_ID")

# Streamlit app
st.set_page_config(page_title="GPT Assistant Interface", page_icon="🤖")

st.title("GPT Assistant Interface")
st.write("Enter a prompt and get a response from your GPT model:")

# Input prompt
prompt = st.text_area("Prompt", "", height=150, help="Type your prompt here")

# When the "Get Response" button is pressed
if st.button("Get Response"):
    if prompt:
        with st.spinner('Getting response...'):
            try:
                # Call the OpenAI API with the prompt
                client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": f"You are a helpful assistant. Your assistant ID is {assistant_id}."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=150
                )
                # Display the response
                st.success("Response received:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")

st.write("Note: Make sure your API key and assistant ID are set in your environment variables.")
