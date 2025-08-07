import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# --------- CONFIG -----------
st.set_page_config(
    page_title="Sheelam Harshavardhan",
    page_icon="💼",
    layout="wide"
)

# --------- BACKGROUND & STYLE -----------
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(120deg, #f0f4fd 0%, #e0e7ff 100%);
    }
    .section-title {
        color: #134e6f;
        margin-top: 15px;
    }
    .section-card {
        background: rgba(255,255,255,0.94);
        border-radius: 10px;
        box-shadow: 0 2px 12px rgba(34,60,80,0.14);
        margin-bottom: 18px;
        padding: 25px 37px 25px 37px;
    }
    .sidebar .sidebar-content {background: #2940d3;}
    </style>
""", unsafe_allow_html=True)

# --------- LOTTIE ANIMATION FN -----------
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example Lottie URLs
lottie_about = load_lottieurl("https://lottie.host/36bebdfd-719f-4e63-be29-c6044dcee81e/cMLp4GJSw2.json") # developer animation
lottie_education = load_lottieurl("https://lottie.host/8f6e9784-77bf-4cca-bbdd-c426dc764f19/gKXyAyNncc.json") # graduation hat
lottie_skills = load_lottieurl("https://lottie.host/086a7eb7-5815-46e2-9468-824f18e02dce/h2afOtwocy.json") # skill gear
lottie_projects = load_lottieurl("https://lottie.host/3ef7981d-a730-47ba-82ad-71bc9c2e2b9c/iX8jGWDbCA.json") # working
lottie_certificate = load_lottieurl("https://lottie.host/aa581e0e-cc93-4a8e-83b6-39d7fca314c9/vWqEXuDEDn.json") # certificate

# --------- SIDEBAR ----------
st.sidebar.image("profile.jpg", width=100, caption="Sheelam Harshavardhan")
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "About Me",
        "Education",
        "Skills",
        "Projects",
        "Certifications"
    ]
)

# --------- HEADER & ANIMATION -----------
def about_me_section():
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_about, speed=1, width=120, height=120)
        try:
            st.image("profile.jpg", width=150)
        except Exception:
            st.empty()
    with col2:
        st.header("Sheelam Harshavardhan")
        st.subheader("Aspiring Machine Learning & Deep Learning Engineer")
        st.markdown("""
            📍 Hyderabad, India  
            📞 +91 94916 35633  
            ✉️ harshavardhansheelam@gmail.com  
        """)
        st.markdown("""
        [GitHub](https://github.com/harshavardhan2415) &nbsp; | &nbsp;
        [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) &nbsp; | &nbsp;
        [LeetCode](https://leetcode.com/harshavardhan2415)  
        """, unsafe_allow_html=True)
    st.markdown("***")

def education_section():
    col1, col2 = st.columns([1,4])
    with col1:
        st_lottie(lottie_education, speed=1, width=80, height=80)
    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🎓 Education")
        st.markdown("**National Institute of Technology, Andhra Pradesh**  \n"
                    "B.Tech in Electronics and Communication Engineering (Expected 2026)  \n"
                    "CGPA: **8.6**")
        st.markdown('</div>', unsafe_allow_html=True)

def skills_section():
    col1, col2 = st.columns([1,9])
    with col1:
        st_lottie(lottie_skills, speed=1, width=80, height=80)
    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Skills")
        sc1, sc2 = st.columns(2)
        with sc1:
            st.markdown("**Programming:**\n- C++\n- Python\n- Java")
            st.markdown("**Tools:**\n- Git\n- VS Code\n- Jupyter")
        with sc2:
            st.markdown("**Concepts:**\n- Data Structures\n- OOP\n- DBMS\n- Software Engineering")
            st.markdown("**Soft Skills:**\n- Problem Solving\n- Critical Thinking\n- Fast Learner\n- Collaborative")
        st.markdown('</div>', unsafe_allow_html=True)

def projects_section():
    col1, col2 = st.columns([1,4])
    with col1:
        st_lottie(lottie_projects, speed=1, width=80, height=80)
    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 💼 Projects")
        st.markdown("""
        **📽️ Movie Recommendation System**  
        *Python, Pandas, Scikit-Learn*  
        - Content-based and collaborative filtering using cosine similarity for recommendations.

        **📚 Book Recommendation System**  
        *Python, Keras, TensorFlow*  
        - Neural Network model for personalized book suggestions.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

def certifications_section():
    col1, col2 = st.columns([1,4])
    with col1:
        st_lottie(lottie_certificate, speed=1, width=80, height=80)
    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🎖️ Certifications")
        st.markdown("- Database Management Systems (DBMS) – NPTEL")
        st.markdown('</div>', unsafe_allow_html=True)

def footer():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:grey;'>© 2025 Sheelam Harshavardhan</p>",
        unsafe_allow_html=True
    )

# --------- PAGE ROUTER ----------
if section == "About Me":
    about_me_section()
elif section == "Education":
    about_me_section()
    education_section()
elif section == "Skills":
    about_me_section()
    skills_section()
elif section == "Projects":
    about_me_section()
    projects_section()
elif section == "Certifications":
    about_me_section()
    certifications_section()

footer()
