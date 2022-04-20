import streamlit as st
from PIL import Image

# Custom imports
from multipage import MultiPage
from pages import _1_general_dashboard, _2_segmentation_dashboard  # import your pages here


st.set_page_config(layout="wide")

image = Image.open('Demo_Project_multi_page_dashboard_Benbhk/top.png')
st.image(image)
st.title(" Multi-Page Dashboard ")
st.subheader(" Benjamin Barre - Demo Project ")
st.write('In this project, I realise :')
st.write('''- page 1 : a general dashboard.''')
st.write('''- page 2 : a customer segmentation and dashboard for every segmentation with a comparaison with the main dashboard.''')
st.write('The data comes from an online and offline sales company')
st.write("Link to the [github repo](https://github.com/Benjaminbhk/Demo_Project_multi_page_dashboard_Benbhk)")

st.write('''---''')

st.write("""
     ## Data Analysis
""")

# Create an instance of the app
app = MultiPage()

# Add all your applications (pages) here
app.add_page("Page 1 - Dashboard", _1_general_dashboard.app)
app.add_page("Page 2 - Segmentation dashboard", _2_segmentation_dashboard.app)

# The main app
app.run()
