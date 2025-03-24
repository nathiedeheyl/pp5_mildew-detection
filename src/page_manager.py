import streamlit as st

# Manage multiple Streamlit pages in one app
class MultiPage:
    
    def __init__(self, app_name):
        self.app_name = app_name
        self.pages = []

    def add_page(self, title, func):
        """
        Add a new page to the app
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Run the multipage app
        """
        st.sidebar.title(self.app_name)
        page = st.sidebar.radio("Navigation", self.pages, format_func=lambda page: page["title"])
        page["function"]()
