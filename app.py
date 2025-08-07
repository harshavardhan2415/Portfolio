import streamlit as st
from PIL import Image

# ---------- CONFIG ----------
st.set_page_config(page_title="Sheelam Harshavardhan", page_icon="💼", layout="wide")

# ---------- COLORS & STYLE ----------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
header {
    background-color: #003566;
    padding: 30px;
    border-radius: 10px;
    color: white;
    text-align: center;
}
h1, h2, h3 {
    color: #003566;
}
.section {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
.card {
    background-color: #f1f3f6;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 15px;
}
a {
    color: #1a73e8;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
with st.container():
    st.markdown("<header>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("profile.jpg", width=150)  # Replace or comment this out if not using image
    with col2:
        st.markdown("## Sheelam Harshavardhan")
        st.markdown("### Aspiring Machine Learning & Deep Learning Engineer")
        st.markdown("""
        📍 Hyderabad, India  
        📞 +91 94916 35633  
        ✉️ harshavardhansheelam@gmail.com  
        🔗 [GitHub](https://github.com/harshavardhan2415) | 
        [LinkedIn](https://www.linkedin.com/in/sheelam-harshavardhan-4747092b7) | 
        [LeetCode](https://leetcode.com/harshavardhan2415)
        """)
    st.markdown("</header>", unsafe_allow_html=True)

# ---------- EDUCATION ----------
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🎓 Education")
    st.markdown("""
    **National Institute of Technology, Andhra Pradesh**  
    B.Tech in Electronics and Communication Engineering (Expected 2026)  
    CGPA: **8.6**
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SKILLS ----------
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🛠️ Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Programming")
        st.markdown("- C++\n- Python\n- Java")
        st.subheader("Tools")
        st.markdown("- Git\n- VS Code\n- Jupyter")

    with col2:
        st.subheader("Concepts")
        st.markdown("- Data Structures\n- OOP\n- DBMS\n- Software Engineering")
        st.subheader("Soft Skills")
        st.markdown("- Problem Solving\n- Critical Thinking\n- Fast Learner\n- Collaborative")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- PROJECTS ----------
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("💼 Projects")

    st.markdown("""
    <div class='card'>
    <h4>📽️ Movie Recommendation System</h4>
    <p><b>Tech:</b> Python, Pandas, Scikit-Learn</p>
    <p>Built a content-based and collaborative filtering model using cosine similarity to suggest movies.</p>
    </div>

    <div class='card'>
    <h4>📚 Book Recommendation System</h4>
    <p><b>Tech:</b> Python, Keras, TensorFlow</p>
    <p>Implemented an Artificial Neural Network to provide personalized book suggestions.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- CERTIFICATIONS ----------
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🎖️ Certifications")
    st.markdown("- Database Management Systems (DBMS) – NPTEL")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
with st.container():
    st.markdown("<p style='text-align:center; color: grey;'>© 2025 Sheelam Harshavardhan</p>", unsafe_allow_html=True)
