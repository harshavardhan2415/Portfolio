import streamlit as st
from PIL import Image

# ---------- CONFIGURATION ----------
st.set_page_config(page_title="Sheelam Harshavardhan | Portfolio", page_icon="📄", layout="wide")

# ---------- PROFILE PHOTO ----------
profile_pic = "profile.jpg"  # Replace with a hosted URL or local file in your repo

# ---------- HEADER ----------
with st.container():
    st.markdown("<h1 style='text-align: center;'>📄 Sheelam Harshavardhan</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: grey;'>Aspiring Machine Learning & Deep Learning Engineer</h4>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(profile_pic, width=180)

    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; font-size: 18px;'>
        📍 Hyderabad, India &nbsp; | &nbsp; 📞 +91 94916 35633 &nbsp; | &nbsp; ✉️ harshavardhansheelam@gmail.com  
        <br><br>
        🔗 
        <a href='https://github.com/harshavardhan2415' target='_blank'>GitHub</a> | 
        <a href='https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7' target='_blank'>LinkedIn</a> | 
        <a href='https://leetcode.com/harshavardhan2415' target='_blank'>LeetCode</a>
    </div>
    """, unsafe_allow_html=True)

# ---------- EDUCATION ----------
with st.container():
    st.write("---")
    st.header("🎓 Education")
    st.markdown("""
    **National Institute of Technology, Andhra Pradesh**  
    B.Tech in Electronics and Communication Engineering (Expected 2026)  
    CGPA: **8.6**
    """)

# ---------- SKILLS ----------
with st.container():
    st.write("---")
    st.header("🛠️ Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Programming")
        st.markdown("- C++\n- Python\n- Java")

        st.subheader("Tools")
        st.markdown("- Git\n- VS Code\n- Jupyter Notebook")

    with col2:
        st.subheader("Concepts")
        st.markdown("- Data Structures & Algorithms\n- OOP\n- DBMS\n- Software Engineering")

        st.subheader("Soft Skills")
        st.markdown("- Problem Solving\n- Critical Thinking\n- Fast Learner\n- Collaborative")

# ---------- PROJECTS ----------
with st.container():
    st.write("---")
    st.header("📂 Projects")

    st.markdown("""
    ### 📽️ Movie Recommendation System  
    *Tech: Python, Pandas, Scikit-Learn*  
    Developed a content-based and collaborative filtering model using cosine similarity to suggest movies.

    ---

    ### 📚 Book Recommendation System  
    *Tech: Python, Keras, TensorFlow*  
    Implemented an ANN to provide personalized book suggestions based on user preferences.
    """)

# ---------- CERTIFICATIONS ----------
with st.container():
    st.write("---")
    st.header("🎖️ Certifications")
    st.markdown("- ✅ Database Management Systems (DBMS) – NPTEL")

# ---------- FOOTER ----------
with st.container():
    st.write("---")
    st.markdown("<div style='text-align: center; color: grey;'>© 2025 Sheelam Harshavardhan</div>", unsafe_allow_html=True)
