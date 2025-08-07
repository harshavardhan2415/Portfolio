import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import base64
import json

# === Page configuration ===
st.set_page_config(page_title="Sheelam Portfolio", layout="wide", page_icon="💼")

# === CSS styling ===
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
body, .stApp {background: linear-gradient(to right,#0c0c0f,#003d5b); color: white; font-family: 'Inter';}
.card {background: rgba(255,255,255,0.1); padding:2rem; border-radius:12px; margin-bottom:2rem; backdrop-filter: blur(10px);}
.profile {border-radius:50%; width:150px; border:3px solid white;}
</style>
""", unsafe_allow_html=True)

# === Load Lottie animation safely ===
def load_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

hero_anim = load_lottie("https://lottie.host/.../hero.json")
skills_anim = load_lottie("https://lottie.host/.../skills.json")

# === Header ===
col1, col2 = st.columns([1,4])
with col1:
    try:
        img = Image.open("profile.jpg")
        st.image(img, width=150, use_column_width=False)
    except:
        st.warning("Place profile.jpg in current folder.")
with col2:
    st.title("Sheelam Harshavardhan")
    st.write("Aspiring ML & Deep Learning Engineer") 
    st.write("📍 Hyderabad | ✉️ harshavardhansheelam@gmail.com")

if hero_anim:
    st_lottie(hero_anim, height=200)

# === Tabs: About / Skills / Projects / Timeline / Chatbot? / Resume / Contact ===
tabs = st.tabs(["About", "Skills", "Projects", "Timeline", "Resume", "Contact"])
bio = open("bio.txt", encoding="utf-8").read() if st.sidebar.button("🔄 Load bio") else ""

with tabs[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("About Me")
    st.write(bio or "Add your intro in `bio.txt` and click ➡️")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    if skills_anim:
        st_lottie(skills_anim, height=150)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Skills")
    st.write("- Python, C++, Java\n- TensorFlow, Keras, Scikit‑learn, Pandas\n- Git, VS Code, Jupyter\n- Soft Skills: Problem solving, teamwork")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Projects")
    st.markdown("**Movie Recommendation System**  
Python • Scikit‑learn • cosine similarity  
[GitHub](https://github.com/harshavardhan2415/movie-recommender)")
    st.markdown("**Book Recommendation System**  
Python • TensorFlow • Keras  
[GitHub](https://github.com/harshavardhan2415/book-recommender)")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Career Snapshot")
    # Use external JSON timeline file
    timeline_json = json.load(open("timeline.json"))
    st.write(timeline_json)  # replace with streamlit_timeline.timeline import if available
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Resume")
    with open("resume.pdf","rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        iframe = f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="600px"></iframe>'
        st.markdown(iframe, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[5]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Contact Me")
    st.markdown(f"""
<form action="https://formsubmit.co/harshavardhansheelam@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your name" required><br>
<input type="email" name="email" placeholder="Your email" required><br>
<textarea name="message" placeholder="Your message" required></textarea><br>
<button type="submit">Send</button>
</form>
""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
