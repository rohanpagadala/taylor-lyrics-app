import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests

st.title("🎤 Taylor Swift Lyrics Visualizer")

song_title = st.text_input("Enter a Taylor Swift Song Title:")

def fetch_lyrics_lyricsovh(artist, title):
    try:
        url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("lyrics")
        else:
            return None
    except Exception:
        return None

if song_title:
    lyrics = fetch_lyrics_lyricsovh("Taylor Swift", song_title)
    if lyrics:
        st.subheader("🎶 Lyrics")
        st.text_area("Lyrics", lyrics, height=300)

        st.subheader("☁️ Word Cloud")
        wc = WordCloud(width=800, height=400, background_color="white", collocations=False).generate(lyrics)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.error("Lyrics not found for this song. Try another title.")
