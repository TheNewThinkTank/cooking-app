"""_summary_
"""

import requests
import streamlit as st

st.title("Nutrition App")

st.write(
    """
# Analyze the nutritional content of your meals
Created by Gustav C. Rasmussen. Powered by nutritionix
"""
)

ingredient = st.sidebar.text_input("Ingredient")
amount = st.sidebar.text_input("Amount")
unit = st.sidebar.text_input("Unit")


URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"

NUTRITIONIX_ID = st.secrets["NUTRITIONIX_ID"]
NUTRITIONIX_KEY = st.secrets["NUTRITIONIX_KEY"]

HEADER = "Content-Type: application/json,"
# f"x-app-id: {NUTRITIONIX_ID},"
# f"x-app-key: {NUTRITIONIX_KEY}"

BODY = {"query": f"{amount}{unit} of {ingredient}", "timezone": "US/Eastern"}


def get_facts():

    response = requests.post(
        URL,
        headers=HEADER,
        json=BODY,
    )

    return response.text
