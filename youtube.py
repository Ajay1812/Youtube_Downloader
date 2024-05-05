from pytube import YouTube
import time
import streamlit as st
import speech_recognition as sr
from moviepy.editor import *
import os

st.header("YouTube Video Downloader 📽️")

url = st.text_input("Enter a video URL..")


def download_audio(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(only_audio = True, file_extension='webm').first() # webm, mp4
        streams.download(output_path=save_path)
    except Exception as e:
        print("Error: ", e)

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        # thumb_url = yt.thumbnail_url
        # st.image(thumb_url)
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        # print("Video Downloaded Successfully!")
        
    except Exception as e:
        print("Error: ", e)

def audio_to_text():
    r = sr.Recognizer()
    # audio = download_audio(url,save_path)
    audio_file = []
    file = os.listdir('Downloads')
    for i in file:
        if i.endswith('.mp4'):
            clip = VideoFileClip(i)
            clip.audio("out_audio.wav")
            audio_file.append(clip)
    with sr.AudioFile(f'{audio_file}') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            st.write('Converting audio transcripts into text ...')
            st.write(text)
        except Exception as e:
            print("Error: ", e)


save_path = "/Users/ajay/Documents/Personal/projects/Automation/YouTube Downloader/Downloads"

col1, col2 = st.columns(2)
with col1:

    if st.button("Download Video", type="primary"):
        with st.spinner(text='In progress'):
            time.sleep(0.2)
            download_video(url,save_path)
            st.success("Thanks! The Video was Downloaded")

with col2:
    if st.button("Download Audio", type="secondary"):
        with st.spinner(text='In progress'):
            time.sleep(0.2)
            download_audio(url,save_path)
            st.success("Thanks! The Audio was Downloaded")

if st.button("Summary", type="secondary"):
        with st.spinner(text='In progress'):
            time.sleep(0.2)
            audio_to_text()
            st.success("Thanks! Here's the Summary.")