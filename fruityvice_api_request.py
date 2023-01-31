import requests

fruitvice_response1 = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response)
