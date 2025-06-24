import streamlit as st
import lyricsgenius
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Genius API token (Hardcoded - okay for personal projects, NOT recommended for public repos)
GENIUS_API_TOKEN = "ABI6WKLcMnboPJzrR4Vry-wOvqKQhLucHLceQd39xUQ35bK1F_DjQlLU5qVzkvh3"
genius = lyricsgenius.Genius(
    GENIUS_API_TOKEN,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"]
)

# Streamlit Page Setup
st.set_page_config(page_title="Taylor Swift Lyrics Visualizer", page_icon="🎤", layout="centered")
st.title("🎤 Sing with Streamlit: Taylor Swift Lyrics Visualizer")
st.write("Enter any Taylor Swift song title to get its lyrics and a word cloud!")

# User Input
song_title = st.text_input("Enter a Taylor Swift Song Title:")

# Main Logic
if song_title:
    try:
        with st.spinner("Fetching lyrics..."):
            song = genius.search_song(song_title, "Taylor Swift")

        if song and song.lyrics:
            st.subheader("🎶 Lyrics")
            st.text_area("Lyrics", song.lyrics, height=300)

            st.subheader("☁️ Word Cloud")
            wc = WordCloud(width=800, height=400, background_color='white', collocations=False).generate(song.lyrics)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wc, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.error("Lyrics not found. Try a different song title.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
