import streamlit as st

# load script for page
from app_pages.project_summary import project_summary_body

# create an instance for the app
app = MultiPage(app_name="Mildew Detector")

# app page on dashboard
app.add_page("Project Summary", project_summary_body)

app.run()