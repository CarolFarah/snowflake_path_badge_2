import streamlit
import pandas as pd
import requests

streamlit.title('My Parents New Health Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueerry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list = my_fruits_list.set_index('Fruit')



# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index))
fruits_to_show = my_fruits_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
# Display the table on the page.



fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response)
