import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# --------------- CONFIG ---------------
st.set_page_config(
    page_title="Sheelam Harshavardhan",
    page_icon="💼",
    layout="wide"
)

# ------------- FLEXIBLE THEME (CSS) -------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg,#e4e9fd 0%, #cfd9df 99%);
        min-height: 100vh;
        font-family: 'Segoe UI', sans-serif;
    }
    .portfolio-header {
        margin-top: 25px;
        margin-bottom: 10px;
        color: #113452;
    }
    .section-card {
        border-radius: 14px;
        margin-bottom: 28px;
        box-shadow: 0 4px 32px rgba(35,111,161,.11);
        background: rgba(255,255,255,0.86);
        padding: 37px 40px 35px 40px;
        transition: box-shadow 0.22s;
    }
    .section-card:hover {
        box-shadow: 0 6px 32px rgba(21,75,214,.16);
        transform: translateY(-4px) scale(1.01);
    }
    .card-image {
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 2px 10px rgba(34,60,80,.07);
    }
    .project-tag {
        display: inline-block;
        background: #e0eaef;
        color: #134e6f;
        border-radius: 6px;
        font-size: 0.9em;
        padding: 3px 11px;
        margin-right: 8px;
        margin-bottom: 4px;
    }
    .timeline {
        border-left: 3.5px solid #235ed5;
        margin: 18px 0 18px 16px;
        padding-left: 24px;
    }
    .timeline-event {
        margin-bottom: 19px;
        color: #152447;
    }
    hr {
        border: none;
        height: 1.5px;
        background: linear-gradient(60deg,#296ed3,rgba(255,255,255,0));
        margin: 30px 0 17px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ------------- LOTTIE ANIMATION -------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_dev = load_lottieurl("https://lottie.host/36bebdfd-719f-4e63-be29-c6044dcee81e/cMLp4GJSw2.json")
lottie_edu = load_lottieurl("https://lottie.host/8f6e9784-77bf-4cca-bbdd-c426dc764f19/gKXyAyNncc.json")
lottie_skill = load_lottieurl("https://lottie.host/086a7eb7-5815-46e2-9468-824f18e02dce/h2afOtwocy.json")
lottie_proj = load_lottieurl("https://lottie.host/3ef7981d-a730-47ba-82ad-71bc9c2e2b9c/iX8jGWDbCA.json")
lottie_cert = load_lottieurl("https://lottie.host/aa581e0e-cc93-4a8e-83b6-39d7fca314c9/vWqEXuDEDn.json")

# ------------- SIDEBAR NAVIGATION -------------
st.sidebar.image("profile.jpg", width=90, caption="Sheelam Harshavardhan")
main_section = st.sidebar.radio(
    "Navigate",
    ["About", "Career & Education", "Skills", "Projects", "Certifications"]
)

# ------------- HEADER SECTION -------------
if main_section == "About":
    col1, col2 = st.columns([1, 3])
    with col1:
        st_lottie(lottie_dev, width=120, key="about_anim")
        st.image("profile.jpg", width=120)
    with col2:
        st.markdown("<h1 class='portfolio-header'>Sheelam Harshavardhan</h1>", unsafe_allow_html=True)
        st.write("**Aspiring Machine Learning & Deep Learning Engineer**")
        st.write("📍 Hyderabad, India &nbsp; | &nbsp; 📞 +91 94916 35633 &nbsp; | &nbsp; ✉️ harshavardhansheelam@gmail.com", unsafe_allow_html=True)
        st.write("[GitHub](https://github.com/harshavardhan2415) &nbsp; | &nbsp; [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) &nbsp; | &nbsp; [LeetCode](https://leetcode.com/harshavardhan2415)", unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.08em;color:#2d2d2d;padding-left:10px;">Driven by curiosity and commitment to impactful tech! Building projects that shape smarter solutions for tomorrow.</div>', unsafe_allow_html=True)

# ------------- TIMELINE: CAREER & EDUCATION -------------
if main_section == "Career & Education":
    st_lottie(lottie_edu, width=80, key="edu_anim")
    with st.container():
        st.markdown('<div class="section-card timeline">', unsafe_allow_html=True)
        st.markdown("### 🎓 Education / Career Timeline")
        st.write("""
            <div class="timeline-event"><b>2022–2026 (expected)</b>: <span style="color:#235ed5">National Institute of Technology, Andhra Pradesh</span><br>
            B.Tech, Electronics & Communication Engineering<br>
            CGPA: <b>8.6</b></div>
            <div class="timeline-event"><b>2021</b>: Completed Higher Secondary (Class XII)</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ------------- EXPANDABLE SKILLS SECTION -------------
if main_section == "Skills":
    st_lottie(lottie_skill, width=80, key="skill_anim")
    with st.container():
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Key Skills (Click to Expand)")
        with st.expander("Programming Languages"):
            st.markdown("C++, Python, Java")
        with st.expander("Tools"):
            st.markdown("Git, VS Code, Jupyter")
        with st.expander("Core Concepts"):
            st.markdown("Data Structures, OOP, DBMS, Software Engineering")
        with st.expander("Soft Skills"):
            st.markdown("Problem Solving, Critical Thinking, Fast Learner, Collaborative")
        st.markdown('</div>', unsafe_allow_html=True)

# ------------- ADVANCED PROJECT CARDS -------------
if main_section == "Projects":
    st_lottie(lottie_proj, width=80, key="proj_anim")
    project_data = [
        {
            "title": "Movie Recommendation System",
            "image": "project_movie.jpg",      # supply your own image
            "tags": ["Python", "Pandas", "Scikit-Learn"],
            "desc": "Built a content-based and collaborative filtering model using cosine similarity to suggest movies.",
            "github": "https://github.com/yourname/movie-recommender"
        },
        {
            "title": "Book Recommendation System",
            "image": "project_book.jpg",      # supply your own image
            "tags": ["Python", "Keras", "TensorFlow"],
            "desc": "Artificial Neural Network for personalized book suggestions.",
            "github": "https://github.com/yourname/book-recommender"
        }
    ]
    for proj in project_data:
        with st.container():
            col1, col2 = st.columns([1,3])
            with col1:
                st.image(proj["image"], width=90, caption="")
            with col2:
                st.markdown(f"<b>{proj['title']}</b>", unsafe_allow_html=True)
                st.markdown("".join([f"<span class='project-tag'>{tag}</span>" for tag in proj["tags"]]), unsafe_allow_html=True)
                st.caption(proj["desc"])
                st.markdown(f"[See on GitHub]({proj['github']})", unsafe_allow_html=True)

# ------------- CERTIFICATIONS WITH ANIMATION -------------
if main_section == "Certifications":
    st_lottie(lottie_cert, width=80, key="cert_anim")
    with st.container():
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🎖️ Certifications")
        st.markdown("- Database Management Systems (DBMS) — NPTEL")
        st.markdown('</div>', unsafe_allow_html=True)

# ------------- FOOTER -------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:grey;'>© 2025 Sheelam Harshavardhan</p>", unsafe_allow_html=True)
