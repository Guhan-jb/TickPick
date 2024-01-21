import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import pysrt

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        st.error(f"Error: {str(e)}")

def get_subtitles(video_id):
    try:
        captions = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = pysrt.SubRipFile()
        for caption in captions:
            start = pysrt.SubRipTime.from_seconds(caption['start'])
            end = pysrt.SubRipTime.from_seconds(caption['start'] + caption['duration'])
            text = caption['text']
            subtitle = pysrt.SubRipItem(index=len(subtitles) + 1, start=start, end=end, text=text)
            subtitles.append(subtitle)
        return subtitles
    except Exception as e:
        st.error(f"Error: {str(e)}")

def display_transcript(transcript):
    for segment in transcript:
        st.write(f"{segment['text']}")

def display_subtitles(subtitles):
    for subtitle in subtitles:
        st.write(subtitle.text)

# Streamlit app
def youmain():
    st.title("You-Text")

    # User input
    video_id = st.text_input("Enter YouTube Video ID")

    if st.button("Get Transcript"):
        if video_id:
            transcript = get_transcript(video_id)
            if transcript:
                display_transcript(transcript)
        else:
            st.warning("Please enter a YouTube Video ID")

    if st.button("Get Subtitles"):
        if video_id:
            subtitles = get_subtitles(video_id)
            if subtitles:
                display_subtitles(subtitles)
        else:
            st.warning("Please enter a YouTube Video ID")

if __name__ == "__main__":
    youmain()
