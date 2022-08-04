import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io 

st.set_page_config(layout="wide")

st.markdown("# CYBERSECURITY")

choose = option_menu(None, ["Home", "About", "Member", "Planning", "Result", "Contact"], 
                    icons=['house', 'upc-scan', 'lock', 'motherboard','shield-exclamation','cloud-upload', "list-task"], 
                    menu_icon="cast", default_index=0, orientation="horizontal",
                    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"}, 
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "green"},
    }
)

image = Image.open('infographicnotebook.png')

st.image(image, caption='cybersecurity')

st.markdown("""Cybersecurity Fundamentals: 
A Real-World Perspective explains detailed 
concepts within computer networks and computer security 
in an easy-to-understand way, 
making it the perfect introduction to the topic.""")


st.write("""The short definition of cybersecurity is, 
“The protection of software, hardware, 
and data resources connected and stored on the Internet is known as the cybersecurity”. 
From an individual to a large corporation, 
everybody is concerned about the security of their online data, software, and information.
The protection of the personal, financial data, 
commercial data, business-critical information, operational continuity, data integrity, 
and availability of online software services fall in the cybersecurity domain. 
Regulating the physical access and control- ling the malicious intrusion, 
allowing the authorized access, encrypting the valuable information, 
and safeguarding the privacy are the components of cybersecurity.
Cybersecurity is one of the most important domains in the field of information technology.
There are two spellings for it, “Cybersecurity” and “Cyber Security”. 
Cybersecurity is basically the name of standard practices that involve the people,
technology, and processes in an organiza- tion, in a team, 
or even in a stand-alone environment 
in which the computers with the valuable data are connected to the Internet or the Intranet. 
Cybersecurity deals with the different procedures that create an environment of full security.
""")

#with st.sidebar:
#    choose = option_menu("Menu", ["About", "Member", "Project Planning", "Project Result", "Contact"],
#                         icons=['house', 'upc-scan', 'lock', 'motherboard','shield-exclamation'],
#                         menu_icon="app-indicator", default_index=0, orientation="horizontal",
#                         styles={
#        "container": {"padding": "5!important", "background-color": "#fafafa"},
#        "icon": {"color": "green", "font-size": "25px"}, 
#        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#        "nav-link-selected": {"background-color": "#02ab21"},
#    }
    
#    ) 


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    path = "infographicnotebook.png"
    image = Image.open(path)

df = pd.DataFrame(px.data.gapminder())
clist = df['country'].unique()
country = st.sidebar.selectbox("Select a country:",clist)
st.header("Global Cybersecurity")
fig = px.line(df[df['country'] == country], 
    x = "year", y = "gdpPercap", title = country)
st.plotly_chart(fig)
