import streamlit as st
import datetime
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#st.title('Hello World')

#take input from user
#name = st.text_input('Enter your name')
#st.write('Hello', name)

#Demo of dropdown box in streamlit
#option = st.selectbox('Which number do you like best?', [1, 2, 3, 4, 5])
#st.write('You selected:', option)

#Demo of radio button in streamlit
#option = st.radio('Which number do you like best?', [1, 2, 3, 4, 5])
#st.write('You selected:', option)

#Demo of checkbox in streamlit
#if st.checkbox('Show/Hide'):
#   st.write('Showing or Hiding Widget')

#Demo of slider in streamlit
#age = st.slider('How old are you?', 0, 130, 25)
#st.write('I am:', age, 'years old')

#Demo of button in streamlit
#if st.button('Say Hello'):
#    st.write('Hello')

#Demo of textarea in streamlit
#message = st.text_area('Enter your message')
#st.write('You entered:', message)

#Demo of date input in streamlit
#today = st.date_input('Today is:', datetime.datetime.now())
#st.write('Today is:', today)

#Demo of time input in streamlit
#time = st.time_input('The time is:', datetime.time())
#st.write('The time is:', time)
#st.write('Current time is:', datetime.datetime.now())

#Demo of file uploader in streamlit & display the uploaded file in a csv
#uploaded_file = st.file_uploader('Choose a file', type = ['csv'])
#if uploaded_file is not None:
#    data = pd.read_csv(uploaded_file)
#    st.write(data)

#Demo of progress bar in streamlit
#my_bar = st.progress(0)
#for precentage_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(precentage_complete + 1)

#Demo of sidebar in streamlit
#st.sidebar.write('This is a sidebar')
#st.sidebar.button('Press me')

#Demo of expander in streamlit
#with st.expander('See more'):
#    st.write('This is hidden by default')

#Demo of columns in streamlit
#col1, col2, col3 = st.columns(3)
#col1.write('This is column 1')
#col2.write('This is column 2')
#col3.write('This is column 3')

#Demo of plot in streamlit
#x = np.random.randn(100)
#fig, ax = plt.subplots()
#ax.hist(x, bins = 20)
#st.pyplot(fig)

#Demo of image in streamlit
#image = Image.open("C:/Users/Chetana/OneDrive/Pictures/Screenshots 1/Screenshot (30).png")
#st.image(image, caption = 'Genshin Event', use_column_width = True)

#Demo of yt video in streamlit
#st.video('video link here')

#Demo of local video in streamlit
st.video("C:/Users/Chetana/Videos/Captures/Wuthering Waves   2024-07-24 12-58-24.mp4", 'r')

#CSS or HTML
#st.markup('')