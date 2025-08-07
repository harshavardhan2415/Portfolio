# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:10:26 2025

@author: harsh
"""

import streamlit as st
from PIL import Image

# ---------- CONFIG ----------
st.set_page_config(page_title="My Portfolio", page_icon="📁", layout="wide")

# ---------- HEADER ----------
with st.container():
    st.subheader("Hi, I'm Your Name 👋")
    st.title("A [Your Role] with a passion for building impactful projects.")
    st.write("Welcome to my portfolio. I love solving real-world problems with data, code, and creativity.")
    st.write("[Download Resume >](#)")  # <-- Add a real link

# ---------- ABOUT ----------
with st.container():
    st.write("---")
    st.header("About Me")
    st.write(
        """
        I'm a [Your Profession] with experience in:
        - Python, Machine Learning, Data Analysis
        - Streamlit, Flask, SQL
        - Git, Docker, AWS

        I enjoy working on end-to-end projects, from problem understanding to deployment.
        """
    )

# ---------- PROJECTS ----------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Project One")
        st.image("https://via.placeholder.com/300x200", use_column_width=True)
        st.write("Short description of project one.")
        st.write("[GitHub Repo](#)")

    with col2:
        st.subheader("Project Two")
        st.image("https://via.placeholder.com/300x200", use_column_width=True)
        st.write("Short description of project two.")
        st.write("[GitHub Repo](#)")

    with col3:
        st.subheader("Project Three")
        st.image("https://via.placeholder.com/300x200", use_column_width=True)
        st.write("Short description of project three.")
        st.write("[GitHub Repo](#)")

# ---------- CONTACT ----------
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here..." required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Optional styling
    st.markdown(
        """
        <style>
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            width: 300px;
        }
        input, textarea {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-family: sans-serif;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
