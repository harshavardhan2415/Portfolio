import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Harshavardhan | Portfolio", page_icon="💼", layout="wide")

# Load profile image
profile_img = Image.open("profile.jpg")

# Load Lottie Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animation URLs
lottie_coding = load_lottieurl("https://lottie.host/086a7eb7-5815-46e2-9468-824f18e02dce/h2afOtwocy.json")
lottie_contact = load_lottieurl("https://lottie.host/aa581e0e-cc93-4a8e-83b6-39d7fca314c9/vWqEXuDEDn.json")

# --- CSS ---
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to right, #f1f4f9, #dff1ff);
        }
        h1, h2, h3 {
            color: #113452;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton>button {
            background-color: #1f77be;
            color: white;
            border-radius: 8px;
        }
        .tag {
            display: inline-block;
            background-color: #e0f0ff;
            color: #134e6f;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 2px 5px;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(profile_img, width=180)
    with col2:
        st.title("Sheelam Harshavardhan")
        st.subheader("Aspiring Machine Learning Engineer")
        st.write("📍 Hyderabad, India")
        st.write("📧 harshavardhansheelam@gmail.com")
        st.markdown("[🌐 GitHub](https://github.com/harshavardhan2415) | [🔗 LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7)")

# --- ANIMATION ---
with st.container():
    if lottie_coding:
        st_lottie(lottie_coding, height=200, key="coding")

# --- PROJECTS ---
with st.container():
    st.write("---")
    st.header("📁 Projects")
    st.markdown("##")

    st.markdown("""
    ### 🎬 Movie Recommendation System  
    Python • Scikit‑learn • Cosine Similarity  
    [GitHub Repo](https://github.com/harshavardhan2415/movie-recommender)
    """)

    st.markdown("""
    ### 📚 Book Recommendation System  
    Python • TensorFlow • Keras  
    [GitHub Repo](https://github.com/harshavardhan2415/book-recommender)
    """)

# --- SKILLS ---
with st.container():
    st.write("---")
    st.header("🛠️ Skills")
    st.markdown("##")
    st.markdown("#### Programming Languages")
    st.markdown('<span class="tag">Python</span><span class="tag">C++</span><span class="tag">Java</span>', unsafe_allow_html=True)
    st.markdown("#### Tools")
    st.markdown('<span class="tag">Git</span><span class="tag">VS Code</span><span class="tag">Jupyter</span>', unsafe_allow_html=True)
    st.markdown("#### Soft Skills")
    st.markdown('<span class="tag">Problem Solving</span><span class="tag">Fast Learner</span><span class="tag">Teamwork</span>', unsafe_allow_html=True)

# --- CONTACT ---
with st.container():
    st.write("---")
    st.header("📞 Contact")
    st.markdown("##")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Email: harshavardhansheelam@gmail.com")
        st.write("Phone: +91 94916 35633")
    with col2:
        if lottie_contact:
            st_lottie(lottie_contact, height=160, key="contact")

# --- FOOTER ---
st.write("---")
st.markdown("<center>© 2025 Sheelam Harshavardhan</center>", unsafe_allow_html=True)
