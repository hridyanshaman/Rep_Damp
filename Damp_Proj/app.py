import streamlit as st
from ozon3.ozon3 import get_city_air  # assuming function exists in ozon3.py

st.set_page_config(page_title="Ozon3 - Air Quality Dashboard", page_icon="🌍", layout="wide")
st.title("🌍 Ozon3 Air Quality Dashboard")

city = st.text_input("Enter City Name", placeholder="e.g., Delhi")

if city:
    try:
        data = get_city_air(city)
        st.success(f"Air Quality data for {city}:")
        st.json(data)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
