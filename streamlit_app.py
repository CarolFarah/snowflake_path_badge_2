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

streamlit.header('Fruitvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.text('Formato JSON')
streamlit.text(fruitvice_response.json())

streamlit.text('')
streamlit.text('')

streamlit.text('Formato texto')
streamlit.text(fruitvice_response.text)

streamlit.text('')
streamlit.write('')

streamlit.write('Dataframe')
fruitvice_normalized = pd.json_normalize(fruitvice_response.json())
streamlit.dataframe(fruitvice_normalized) 

