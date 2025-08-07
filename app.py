import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Portfolio | Sheelam Harshavardhan", page_icon="🧠", layout="wide")

# -------- LOAD LOTTIE --------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -------- LOTTIE ANIMATIONS --------
lottie_about = load_lottieurl("https://lottie.host/5f417a62-f4f6-4944-9c02-45c4c2e88f14/U3sFgD7mMy.json")
lottie_skills = load_lottieurl("https://lottie.host/b12c1f01-c2e2-4fcb-8a8c-fb0f4890f89f/cHBB7BcozI.json")
lottie_projects = load_lottieurl("https://lottie.host/cd229d4f-5a02-44cb-a36b-3a4a36b43213/lF1FWHo3Na.json")
lottie_cert = load_lottieurl("https://lottie.host/b4bc31b2-4f8a-4f58-9a36-d2ad2b8f4ddc/B8Y14j8fPT.json")

# -------- CUSTOM CSS --------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Roboto&display=swap');

html, body, .stApp {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to right, #eef2f3, #8e9eab);
    color: #222;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    color: #1f2937;
}

.section {
    background: white;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.07);
    margin-bottom: 30px;
}

.lottie {
    margin-bottom: -20px;
}

.project-box {
    border: 1px solid #e5e7eb;
    padding: 16px;
    border-radius: 10px;
    background: #fafafa;
    transition: 0.3s ease;
}
.project-box:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 16px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.image("profile.jpg", width=100)
section = st.sidebar.radio("📍 Navigate", ["About", "Skills", "Projects", "Certifications"])

# -------- ABOUT --------
if section == "About":
    st_lottie(lottie_about, height=200, key="about")
    with st.container():
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.header("👋 Hi, I'm Sheelam Harshavardhan")
        st.subheader("Aspiring ML & Deep Learning Engineer | NIT Andhra Pradesh")
        st.write("Passionate about crafting intelligent systems that make lives easier. Constantly exploring ML, DL, and AI to push boundaries.")
        st.write("📍 Hyderabad, India")
        st.write("[GitHub](https://github.com/harshavardhan2415) | [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) | [LeetCode](https://leetcode.com/harshavardhan2415)")
        st.markdown("</div>", unsafe_allow_html=True)

# -------- SKILLS --------
if section == "Skills":
    st_lottie(lottie_skills, height=180, key="skills")
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🛠️ Skills Overview")

    st.subheader("Languages")
    st.write("Python, C++, Java")

    st.subheader("Libraries & Tools")
    st.write("NumPy, Pandas, TensorFlow, Keras, Scikit-learn, Git, Jupyter")

    st.subheader("Soft Skills")
    st.write("Problem Solving, Fast Learner, Team Collaboration")
    st.markdown("</div>", unsafe_allow_html=True)

# -------- PROJECTS --------
if section == "Projects":
    st_lottie(lottie_projects, height=200, key="projects")
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("📂 Projects")

    project_data = [
        {
            "title": "🎬 Movie Recommendation System",
            "desc": "Built a content-based and collaborative filtering model using cosine similarity to suggest movies.",
            "tools": "Python, Pandas, Scikit-learn",
            "github": "https://github.com/harshavardhan2415/movie-recommender"
        },
        {
            "title": "📚 Book Recommendation System",
            "desc": "Built a personalized book recommendation engine using a neural network.",
            "tools": "Python, TensorFlow, Keras",
            "github": "https://github.com/harshavardhan2415/book-recommender"
        }
    ]

    for proj in project_data:
        st.markdown(f"""
        <div class="project-box">
            <h4>{proj['title']}</h4>
            <p>{proj['desc']}</p>
            <small><b>Tools:</b> {proj['tools']}</small><br>
            <a href="{proj['github']}" target="_blank">🔗 GitHub Repo</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -------- CERTIFICATIONS --------
if section == "Certifications":
    st_lottie(lottie_cert, height=200, key="certs")
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🎖️ Certifications")
    st.markdown("- 📘 **Database Management Systems** — NPTEL")
    st.markdown("- 🤖 **AI for Everyone** — Coursera (optional)")
    st.markdown("</div>", unsafe_allow_html=True)

# -------- FOOTER --------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center style='color:gray;'>© 2025 Sheelam Harshavardhan</center>", unsafe_allow_html=True)
