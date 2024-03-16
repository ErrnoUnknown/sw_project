import streamlit as st
import pandas as pd
import numpy as np

st.title('This is a title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

def click_event():
    print('1')

st.button('Example Button', on_click=click_event)