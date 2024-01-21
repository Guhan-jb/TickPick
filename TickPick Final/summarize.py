import streamlit as st
from openai import OpenAI

client = OpenAI(api_key='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')
# Streamlit app
def spmain():
    st.title("Text-Shorty")

    # Text input
    text = st.text_area("Enter text to make it easier for you..", height=200)

    # Button to generate summary
    if st.button("Generate "):
            # Generate summary using client API
            summary = generate_summary(text)
            st.markdown("## Your Personalised Content")
            st.write(summary)
            # st.warning("Please enter text to summarize.")

def generate_summary(text):
    # Use the client API to generate a summary
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Summerize this : "+text
    )
    summary = response.choices[0].text.strip()
    return summary
if __name__ == "__main__":
    spmain()
