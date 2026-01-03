import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("RetinaRisk AI")

# Sidebar
with st.sidebar:
    st.header("Patient Data")
    p_id = st.text_input("ID", "PT-001")
    name = st.text_input("Name", "Test Patient")
    age = st.number_input("Age", 0, 100, 50)

# Main Action
if st.button("Check Connectivity"):
    try:
        # Note: We use the container name 'backend' to talk inside Docker
        res = requests.post(
            "http://backend:8000/analyze", 
            json={"id": p_id, "name": name, "age": age}
        )
        st.success(res.json())
    except Exception as e:
        st.error(f"Error: {e}")