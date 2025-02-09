import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")

x = st.slider("Select a value for x", 0, 100)
st.write(f"x = {x}")

import matplotlib.pyplot as plt
import numpy as np

y = np.sin(x * np.pi / 50)  # Example calculation
plt.plot(x, y)
st.pyplot(plt)  # Display the plot