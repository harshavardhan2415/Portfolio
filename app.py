import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# ------------ PAGE CONFIG ------------
st.set_page_config(page_title="Harshavardhan Portfolio", page_icon="💼", layout="wide")

# ------------ LOTTIE LOADER ------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------------ LOTTIE FILES ------------
hero_anim = load_lottie("https://lottie.host/38eec7b0-9f83-4a3e-ae7c-e34f6121c4e2/9DbO2He9DR.json")
skills_anim = load_lottie("https://lottie.host/70627c12-d4db-4093-9ed7-446d70a3f3d0/eyrPXYYFiH.json")
projects_anim = load_lottie("https://lottie.host/bfe9bc7b-e3f3-469f-8ed5-41c876aa64dc/7vwv4A5D6k.json")

# ------------ CSS STYLE ------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700&display=swap');

    html, body, .stApp {
        font-family: 'Urbanist', sans-serif;
        background: url('https://images.unsplash.com/photo-1542281286-9e0a16bb7366') no-repeat center center fixed;
        background-size: cover;
        color: white;
    }

    .glass {
        background: rgba(0, 0, 0, 0.5);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0,0,0,0.2);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
    }

    h1, h2, h3, h4 {
        color: #ffffff;
    }

    a {
        color: #56c7ff;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    .profile-pic {
        border-radius: 50%;
        width: 180px;
        margin-top: -30px;
        border: 4px solid white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    }

    </style>
""", unsafe_allow_html=True)

# ------------ HEADER ------------
st.markdown("<br>", unsafe_allow_html=True)
cols = st.columns([1, 3])
with cols[0]:
    try:
        image = Image.open("profile.jpg")
        st.image(image, use_column_width=False, width=180, output_format='auto')
    except:
        st.warning("profile.jpg not found. Please place it in the same directory.")
with cols[1]:
    st.title("Sheelam Harshavardhan")
    st.markdown("**Machine Learning & Deep Learning Enthusiast**")
    st.markdown("📍 Hyderabad | ✉️ harshavardhansheelam@gmail.com | ☎️ +91 94916 35633")
    st.markdown("[GitHub](https://github.com/harshavardhan2415) | [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) | [LeetCode](https://leetcode.com/harshavardhan2415)")

# ------------ HERO ANIMATION ------------
if hero_anim:
    st_lottie(hero_anim, height=220, key="hero_anim")

# ------------ TABS ------------
tab1, tab2, tab3, tab4 = st.tabs(["🧠 About", "🛠️ Skills", "📁 Projects", "📜 Certifications"])

# ------------ ABOUT ------------
with tab1:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🧠 About Me")
    st.write("""
        I’m currently pursuing a B.Tech in Electronics & Communication Engineering at NIT Andhra Pradesh. 
        Passionate about artificial intelligence and solving real-world problems using ML & DL.

        I enjoy building recommendation systems, neural networks, and working on innovative data projects.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------ SKILLS ------------
with tab2:
    if skills_anim:
        st_lottie(skills_anim, height=200, key="skills_anim")
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🛠️ Skills")

    st.subheader("Languages")
    st.write("Python, C++, Java")

    st.subheader("Libraries & Frameworks")
    st.write("TensorFlow, Keras, Scikit-learn, NumPy, Pandas")

    st.subheader("Tools")
    st.write("Git, Jupyter Notebook, VS Code")

    st.subheader("Soft Skills")
    st.write("Critical Thinking, Teamwork, Fast Learning")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------ PROJECTS ------------
with tab3:
    if projects_anim:
        st_lottie(projects_anim, height=200, key="proj_anim")
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("📁 Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎬 Movie Recommendation System")
        st.caption("Python | Pandas | Scikit-learn")
        st.write("Content-based + collaborative filtering engine using cosine similarity.")
        st.markdown("[🔗 GitHub](https://github.com/harshavardhan2415/movie-recommender)")

    with col2:
        st.subheader("📚 Book Recommendation System")
        st.caption("Python | Keras | TensorFlow")
        st.write("Artificial Neural Network powered personalized recommender.")
        st.markdown("[🔗 GitHub](https://github.com/harshavardhan2415/book-recommender)")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------ CERTIFICATIONS ------------
with tab4:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("📜 Certifications")
    st.markdown("- ✅ **Database Management Systems** — NPTEL")
    st.markdown("- ✅ **AI for Everyone** — Coursera")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------ FOOTER ------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center style='color:gray;'>© 2025 Sheelam Harshavardhan</center>", unsafe_allow_html=True)
