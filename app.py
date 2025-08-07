import streamlit as st
from streamlit_lottie import st_lottie
import requests

# PAGE CONFIG
st.set_page_config(page_title="Harshavardhan | ML Portfolio", layout="wide", page_icon="🤖")

# LOAD LOTTIE FUNCTION
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ANIMATIONS
anim_hero = load_lottie("https://lottie.host/f9cc089d-e720-4db9-8fbd-65eb7292c38f/7KR7xvDf7x.json")
anim_skills = load_lottie("https://lottie.host/4ac11ac8-40fd-4b5f-a748-10f35de5c5f7/DQ1Of2oPCZ.json")
anim_projects = load_lottie("https://lottie.host/bfe9bc7b-e3f3-469f-8ed5-41c876aa64dc/7vwv4A5D6k.json")

# CUSTOM STYLES
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background: #121212;
    color: #ffffff;
}

.container {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 2rem;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

a {
    color: #56C7FF;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st_lottie(anim_hero, height=250, key="hero")

st.title("Sheelam Harshavardhan")
st.subheader("Machine Learning & Deep Learning Enthusiast")
st.write("📍 Hyderabad, India | ✉️ harshavardhansheelam@gmail.com | ☎️ +91 94916 35633")
st.markdown("[GitHub](https://github.com/harshavardhan2415) | [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) | [LeetCode](https://leetcode.com/harshavardhan2415)")

# NAVIGATION TABS
tab1, tab2, tab3, tab4 = st.tabs(["🧠 About", "🛠️ Skills", "📁 Projects", "📜 Certifications"])

# ABOUT
with tab1:
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.header("👨‍💻 About Me")
    st.write("""
        I’m a B.Tech student at NIT Andhra Pradesh, specializing in Electronics & Communication Engineering.
        I have a strong interest in Artificial Intelligence, particularly Machine Learning and Deep Learning.

        My work spans multiple projects that leverage neural networks, recommendation engines, and real-world applications.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# SKILLS
with tab2:
    st_lottie(anim_skills, height=200, key="skills")
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.header("🛠️ Skills")
    
    st.subheader("Languages")
    st.write("Python, C++, Java")

    st.subheader("Libraries & Frameworks")
    st.write("NumPy, Pandas, Scikit-learn, TensorFlow, Keras")

    st.subheader("Other Tools")
    st.write("Git, Jupyter, VS Code")

    st.subheader("Soft Skills")
    st.write("Fast Learner, Collaborative, Critical Thinker")
    st.markdown("</div>", unsafe_allow_html=True)

# PROJECTS
with tab3:
    st_lottie(anim_projects, height=200, key="projects")
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.header("📁 Projects")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎬 Movie Recommendation System")
        st.caption("Python | Pandas | Scikit-learn")
        st.write("A content-based and collaborative filtering model using cosine similarity.")
        st.markdown("[View on GitHub](https://github.com/harshavardhan2415/movie-recommender)")

    with col2:
        st.subheader("📚 Book Recommendation System")
        st.caption("Python | Keras | TensorFlow")
        st.write("ANN-based personalized recommendation engine for books.")
        st.markdown("[View on GitHub](https://github.com/harshavardhan2415/book-recommender)")

    st.markdown("</div>", unsafe_allow_html=True)

# CERTIFICATIONS
with tab4:
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.header("📜 Certifications")
    st.markdown("- ✅ Database Management Systems — NPTEL")
    st.markdown("- ✅ AI for Everyone — Coursera")
    st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("<center style='color:gray;'>© 2025 Sheelam Harshavardhan</center>", unsafe_allow_html=True)
