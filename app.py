import streamlit as st
from PIL import Image

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Sheelam Harshavardhan",
    page_icon="💼",
    layout="wide"
)

# ---------- COLOR & STYLE ----------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .section-title {
        color: #003566;
        margin-top: 15px;
        color: #003566;
    }
    .section-card {
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 15px;
        padding: 25px 37px 25px 37px;
    }
    ul {
        margin: 0;
        padding-left: 1.2em;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
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

# ---------- HEADER (at top) ----------
def about_me_section():
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            st.image("profile.jpg", width=160)
        except Exception:
            st.empty()  # If image not found
    with col2:
        st.header("Sheelam Harshavardhan")
        st.subheader("Aspiring Machine Learning & Deep Learning Engineer")
        st.markdown("""
        <small>
            📍 Hyderabad, India  &nbsp; | &nbsp;
            📞 +91 94916 35633  &nbsp; | &nbsp;
            ✉️ harshavardhansheelam@gmail.com  
        </small>
        """, unsafe_allow_html=True)
        st.markdown("""
        [GitHub](https://github.com/harshavardhan2415) &nbsp; | &nbsp;
        [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) &nbsp; | &nbsp;
        [LeetCode](https://leetcode.com/harshavardhan2415)  
        """, unsafe_allow_html=True)
    st.markdown("***")

def education_section():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🎓 Education")
    st.markdown("**National Institute of Technology, Andhra Pradesh**  \n"
                "B.Tech in Electronics and Communication Engineering (Expected 2026)  \n"
                "CGPA: **8.6**")
    st.markdown('</div>', unsafe_allow_html=True)

def skills_section():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🛠️ Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Programming:**")
        st.markdown("- C++\n- Python\n- Java")
        st.markdown("**Tools:**")
        st.markdown("- Git\n- VS Code\n- Jupyter")
    with col2:
        st.markdown("**Concepts:**")
        st.markdown("- Data Structures\n- OOP\n- DBMS\n- Software Engineering")
        st.markdown("**Soft Skills:**")
        st.markdown("- Problem Solving\n- Critical Thinking\n- Fast Learner\n- Collaborative")
    st.markdown('</div>', unsafe_allow_html=True)

def projects_section():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 💼 Projects")

    st.markdown("""
    **📽️ Movie Recommendation System**  
    *Python, Pandas, Scikit-Learn*  
    - Built a content-based and collaborative filtering model using cosine similarity to suggest movies.

    **📚 Book Recommendation System**  
    *Python, Keras, TensorFlow*  
    - Implemented an Artificial Neural Network to provide personalized book suggestions.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def certifications_section():
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

# ---------- PAGE ROUTER ----------
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
