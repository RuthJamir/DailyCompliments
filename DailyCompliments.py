import streamlit as st
import random

st.set_page_config(page_title="Daily Compliment", page_icon="💌")

st.markdown(
    """
    <style>
    .stApp { 
        background: linear-gradient(to bottom, #ffe6eb, #fff5f7);
        font-family: "Comic Sans MS", cursive, sans-serif;
        text-align: center;
    }

    .title-text {
         color: #d6336c;  /* red */
         font-size: 45px;
         font-weight: bold;
         text-align: center;
         margin-bottom: 30px;
    }

    div.stButton > button:first-child {
        background-color: #ff4d6d;
        color: white;   /* fixed typo: 'while' → 'white' */
        font-size: 20px;
        font-weight: bold;
        border: none;
        width: 350px;
        height: 100px;
        border-radius: 20px;
        cursor: pointer;
    }
    div.stButton > button:first-child:hover {
        background-color:  #e63950;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title-text'>💖 Daily Compliments For You 💖</div>", unsafe_allow_html=True)

compliments = [
    "Loving you makes my heart skip a beat 💓",
    "I am so proud of you!",
    "🌸 You are the sweetest man I have ever met",
    "Your kisses are the only medicine that can heal this sick heart of mine 💕",
    "Life feels better with you in it 🌈",
    "You've got a smile that lights up the world 🌸",
    "I am so grateful to have you in my life 💌",
    "You are a handsome Angami Man 😍",
    "I like your brain very much 🧠",
    "You are an amazing human being blessed so much by God ✨",
    " Even over text, you are adorable",
    " I promise i will always be by your side. Well, except when I'm underneath you",
    " I love how honest, hardworking and capable you are",
    " You make me feel safe. Thank you my love",
]

gifs = [
    "https://i.gifer.com/1FaM.gif",
    "https://i.gifer.com/Pak.gif",
    "https://i.gifer.com/4GZ9.gif",
    "https://i.gifer.com/JSJ.gif",
    "https://i.gifer.com/zq2.gif",
    "https://i.gifer.com/7Uu.gif",
    "https://i.gifer.com/7cIs.gif",
    "https://i.gifer.com/40OU.gif",
    "https://i.gifer.com/3IU0.gif",
    "https://i.gifer.com/YtyM.gif",
    "https://i.gifer.com/XE3i.gif",
    "https://i.gifer.com/5Jy1.gif",
    "https://i.gifer.com/Y3in.gif",
    "https://i.gifer.com/DWhH.gif",
    "https://i.gifer.com/WS2c.gif",
]
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Click me ❤"):
        compliment = random.choice(compliments)
        gif = random.choice(gifs)
        st.markdown(
            f"<div style='font-size:20px; color:#d6336c; text-align:center; margin-top:20px;'>{compliment}</div>",
            unsafe_allow_html=True
        )
        st.image(gif, use_container_width=True)


st.markdown(
    "<hr><p style='color:gray; text-align:center;'>Made with 💖 just for you</p>",
    unsafe_allow_html=True
)
