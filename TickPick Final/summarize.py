import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "KEY"

# Streamlit app
def spmain():
    st.title("Text-Shorty")

    # Text input
    text = st.text_area("Enter text to make it easier for you..", height=200)

    # Button to generate summary
    if st.button("Generate "):
            # Generate summary using OpenAI API
            summary = generate_summary(text)
            st.markdown("## Your Personalised Content")
            st.write(summary)
            # st.warning("Please enter text to summarize.")

def generate_summary(text):
    # Use the OpenAI API to generate a summary
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=100,
        temperature=0.3,
        top_p=1.0,
        n=1,
        stop=None,
        echo=False
    )
    summary = response.choices[0].text.strip()
    return summary
if __name__ == "__main__":
    spmain()
