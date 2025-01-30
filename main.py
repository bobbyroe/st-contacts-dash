import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Contacts Dashboard", page_icon="☎️", layout="wide")

st.title("☎️ CONTACTS & LEADS")

st.logo(image="images/t-mobile-logo.png", 
        icon_image="images/t-logo.png")
@st.cache_data
def load_data():
    data = pd.read_csv('./data/customer_list_extended.csv')
    return data

data = load_data()
all_job_levels = data['job level'].value_counts()
def select_all_jobs():
    st.session_state.job_level = all_job_levels.keys().tolist()
with st.sidebar:
    job_level_selection = st.multiselect("Job Level", all_job_levels.keys().tolist(), default=all_job_levels.keys().tolist(), key="job_level")
    st.button("Select All", on_click=select_all_jobs)


colA, colB, colC = st.columns([1, 1, 2])

filtered_data = data[data['job level'].isin(job_level_selection)]
total_items = filtered_data.shape[0]
num_businesses = filtered_data['company'].nunique()
job_levels = filtered_data['job level'].value_counts()

colA.metric("Total contacts", total_items, border=True)
colB.metric("Businesses", num_businesses, border=True)
pie_chart = px.pie(job_levels, 
                   title="Job Levels", 
                   names=job_levels.index,
                   labels="fff",
                   values="count", height=300)
colC.write(pie_chart)
st.dataframe(filtered_data)

colA, colB = st.columns(2)

# colA.write(job_level_selection)
earth_image = Image.open('./images/earth.png')
colB.image(earth_image, caption="EARF", width=400)