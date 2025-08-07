import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests

# Page settings
st.set_page_config(page_title="Harshavardhan | Portfolio", layout="wide", page_icon="💼")

# Load Lottie Animations
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animations
hero_anim = load_lottie("https://lottie.host/4f55d82a-6cc5-47d1-96a9-8456ce83f3f7/LgcK5AeuJr.json")
skills_anim = load_lottie("https://lottie.host/36313538-b37b-468e-b1e2-e2d539a5d258/fESDwclEz4.json")
project_anim = load_lottie("https://lottie.host/6dc60503-0b60-4e7e-b64e-1be17e06d4de/QmoaW6XtDo.json")

# Fonts & Background
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');
    
    html, body, .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }

    .container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }

    .profile-pic {
        border-radius: 50%;
        border: 3px solid white;
        width: 160px;
        margin-top: -10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }

    a {
        color: #56c7ff;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    h1, h2, h3 {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION ----
col1, col2 = st.columns([1, 3])
with col1:
    try:
        profile_img = Image.open("profile.jpg")
        st.image(profile_img, use_column_width=False, width=160)
    except:
        st.warning("Missing profile.jpg")

with col2:
    st.title("Sheelam Harshavardhan")
    st.subheader("ML & Deep Learning Enthusiast")
    st.write("📍 Hyderabad | ✉️ harshavardhansheelam@gmail.com | ☎️ +91 94916 35633")
    st.markdown("[GitHub](https://github.com/harshavardhan2415) | [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) | [LeetCode](https://leetcode.com/harshavardhan2415)")

if hero_anim:
    st_lottie(hero_anim, height=200)

# ---- NAVIGATION ----
tab1, tab2, tab3, tab4 = st.tabs(["👤 About", "🛠 Skills", "📂 Projects", "📜 Certifications"])

# ---- ABOUT ----
with tab1:
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.header("👤 About Me")
    st.write("""
        I'm a B.Tech student at NIT Andhra Pradesh (2022–2026) majoring in Electronics & Communication Engineering.

        My passion lies in building real-world applications using Machine Learning, Deep Learning, and Neural Networks. Whether it's recommendation systems, automation, or AI-driven tools, I enjoy solving meaningful problems with data.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- SKILLS ----
with tab2:
    if skills_anim:
        st_lottie(skills_anim, height=180)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.header("🛠 Skills")
    st.subheader("Languages")
    st.write("Python, C++, Java")

    st.subheader("Libraries & Frameworks")
    st.write("TensorFlow, Keras, Scikit-learn, Pandas, NumPy")

    st.subheader("Tools")
    st.write("Git, VS Code, Jupyter")

    st.subheader("Soft Skills")
    st.write("Problem Solving, Critical Thinking, Teamwork")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- PROJECTS ----
with tab3:
    if project_anim:
        st_lottie(project_anim, height=180)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.header("📂 Projects")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎬 Movie Recommendation System")
        st.caption("Python | Pandas | Scikit-learn")
        st.write("Built a content-based and collaborative filtering model using cosine similarity.")
        st.markdown("[🔗 GitHub](https://github.com/harshavardhan2415/movie-recommender)")

    with col2:
        st.subheader("📚 Book Recommendation System")
        st.caption("Python | Keras | TensorFlow")
        st.write("A neural-network-based recommender for personalized book suggestions.")
        st.markdown("[🔗 GitHub](https://github.com/harshavardhan2415/book-recommender)")

    st.markdown('</div>', unsafe_allow_html=True)

# ---- CERTIFICATIONS ----
with tab4:
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.header("📜 Certifications")
    st.markdown("- ✅ **Database Management Systems** — NPTEL")
    st.markdown("- ✅ **AI for Everyone** — Coursera")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("---")
st.markdown("<center style='color:gray;'>© 2025 Sheelam Harshavardhan</center>", unsafe_allow_html=True)
