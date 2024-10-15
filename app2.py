# -*- coding: utf-8 -*-
"""app2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14mqOvcpMEmIvLhSf449SvsSpBbpdMUsq
"""

import streamlit as st

# Streamlit app to accept name input and display it
def greet_user():
    # Create an input text box for the user's name
    name = st.text_input("Please enter your name:")

    # Check if the user has entered a name
    if name:
        # Display a greeting message with the user's name
        st.write(f"Hello, {name}! Welcome to the app.")

# Run the app
if __name__ == '__main__':
    greet_user()