import streamlit as st


# Manage multiple Streamlit pages in one app
class MultiPage:

    def __init__(self, app_name):
        self.app_name = app_name
        self.pages = []

        st.set_page_config(
          page_title="Cherry Leaf Powdery Mildew Detector",
          page_icon="🍒",
          )

    def add_page(self, title, func):
        """
        Add a new page to the app
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Run the multipage app
        """
        st.title("Cherry Leaf Powdery Mildew Detector")
        st.write(
            "Use the sidebar to navigate through the project"
            "details and tools."
            )
        page = st.sidebar.radio(
            'Page Navigation',
            self.pages,
            format_func=lambda page: page["title"]
            )
        page["function"]()
