import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Set the title of the dashboard
st.title("Poultry Management System")

# Sidebar
st.sidebar.header('Dashboard')
st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max'))
st.sidebar.subheader('Donut chart ')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))
st.sidebar.subheader('Line chart ')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)


# Create two columns for the body
col1, col2 = st.columns([3, 2])

# Column 1: Video and Table
with col1:
    # Display the video
    st.video("chicken.mp4", start_time=0, loop=True,)

    # Create a sample table
    data = {'ID': [1, 2, 3],
            'Name': ['Chicken 1', 'Chicken 2', 'Chicken 3'],
            'Age': [2, 3, 1]}
    df = pd.DataFrame(data)

    # Display the table
    st.write("## Chicken Information")
    st.table(df)

# Column 2: Disease Detection and Chart
with col2:
    # Check if disease is detected
    disease_detected = True  # Replace with your detection logic

    if disease_detected:
        # Display the detected disease
        st.write("## Disease Detection")
        st.write("Disease Detected: Avian Influenza")
        st.image("fecal_image.jpg", caption="Fecal Matter Image")

    # Create a sample chart
    st.write("## Light Duration")
    values = np.random.randint(0, 60, 50)  # Random values for demonstration
    threshold = 40

    # Plot the chart
    fig, ax = plt.subplots()
    ax.plot(values, color='blue')  # Start with blue color

    # Highlight values above the threshold
    above_threshold = [val if val > threshold else None for val in values]
    ax.plot(above_threshold, 'ro')

    # Set the chart title and labels
    ax.set_title("Light Duration")
    ax.set_xlabel("Time")
    ax.set_ylabel("Light Status")

    # Change line color to red when value exceeds 40
    if any(val > threshold for val in values):
        ax.lines[0].set_color('red')

    # Display the chart
    st.pyplot(fig)

    # Calculate percentage of time light is above 40
    percentage_above_threshold = (sum(val > threshold for val in values) / len(values)) * 100
    st.write("## Light Usage")
    st.write(f"Percentage of time light is above 40%: {percentage_above_threshold:.2f}%")
