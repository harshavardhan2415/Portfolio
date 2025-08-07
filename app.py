import streamlit as st
from PIL import Image
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Sheelam Harshavardhan", page_icon="💼", layout="wide")

# ---------- CUSTOM CSS FOR ANIMATIONS ----------
st.markdown("""
    <style>
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        .fade-in {
            animation: fadeIn 1.2s ease-in;
        }
        .project-card {
            border: 1px solid #e0e0e0;
            padding: 20px;
            border-radius: 10px;
            transition: all 0.3s ease;
            background-color: #fafafa;
        }
        .project-card:hover {
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# ---------- LOAD PROFILE PHOTO ----------
profile_pic = "profile.jpg"  # Replace with image URL or keep it in your repo

# ---------- HEADER SECTION ----------
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(profile_pic, width=160)
    with col2:
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        st.title("Sheelam Harshavardhan")
        st.subheader("🚀 Aspiring ML & Deep Learning Engineer")
        st.markdown("""
        📍 Hyderabad, India  
        📞 +91 94916 35633  
        ✉️ harshavardhansheelam@gmail.com  
        🔗 [GitHub](https://github.com/harshavardhan2415) | 
        [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) | 
        [LeetCode](https://leetcode.com/harshavardhan2415)
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- ANIMATED DIVIDER ----------
st.markdown("<hr class='fade-in'>", unsafe_allow_html=True)

# ---------- EDUCATION ----------
with st.container():
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("🎓 Education")
    st.markdown("""
    **National Institute of Technology, Andhra Pradesh**  
    B.Tech in Electronics and Communication Engineering (Expected 2026)  
    CGPA: **8.6**
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SKILLS ----------
with st.container():
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("🧠 Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Languages")
        st.markdown("- C++\n- Python\n- Java")
        st.subheader("Tools")
        st.markdown("- Git\n- VS Code\n- Jupyter")

    with col2:
        st.subheader("Concepts")
        st.markdown("- Data Structures\n- OOP\n- DBMS\n- Software Engineering")
        st.subheader("Soft Skills")
        st.markdown("- Critical Thinking\n- Problem Solving\n- Teamwork")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- PROJECTS ----------
with st.container():
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("💼 Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='project-card'>
            <h4>📽️ Movie Recommendation System</h4>
            <p><strong>Tech:</strong> Python, Pandas, Scikit-Learn</p>
            <p>Built a content-based and collaborative filtering model using cosine similarity to suggest movies.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='project-card'>
            <h4>📚 Book Recommendation System</h4>
            <p><strong>Tech:</strong> Python, Keras, TensorFlow</p>
            <p>Implemented an Artificial Neural Network to provide personalized book suggestions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- CERTIFICATIONS ----------
with st.container():
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("🎖️ Certifications")
    st.markdown("- ✅ Database Management Systems (DBMS) – NPTEL")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>© 2025 Sheelam Harshavardhan</p>", unsafe_allow_html=True)
