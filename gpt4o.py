import streamlit as st
import openai

# Set up OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

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
                client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
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
