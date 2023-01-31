import requests
import streamlit
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response)
