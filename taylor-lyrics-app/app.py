import streamlit as st
import lyricsgenius
from wordcloud import WordCloud
import matplotlib.pyplot as plt

GENIUS_API_TOKEN = "b4ILDzRV3Y4dJzebvnmKZii52pf9n-k6ibUtuuPNa904aygDVTMravzFYZld8HF7"#I added extra digits to the api key to secure

genius = lyricsgenius.Genius(
    GENIUS_API_TOKEN,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True
)

st.set_page_config(page_title="Taylor Swift Lyrics Visualizer", layout="centered")
st.title("🎤 Taylor Swift Lyrics Visualizer")

song_title = st.text_input("Enter a Taylor Swift song title:")

if song_title:
    with st.spinner("Fetching lyrics..."):
        try:
            song = genius.search_song(song_title, artist="Taylor Swift")
            if song and song.lyrics:
                lyrics = song.lyrics

                # Show lyrics
                st.subheader("🎶 Lyrics")
                st.text_area("Lyrics", value=lyrics, height=300)

                # Generate word cloud
                st.subheader("☁️ Word Cloud")
                wordcloud = WordCloud(
                    width=800,
                    height=400,
                    background_color='white',
                    collocations=False
                ).generate(lyrics)

                fig, ax = plt.subplots(figsize=(10, 5))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis("off")
                st.pyplot(fig)

            else:
                st.error("Could not find lyrics. Try another song.")
        except Exception as e:
            st.error(f"Error: {e}")
