import streamlit as st
# Debugging predictions on deployment step
import os


# Debugging
# Print current working directory
st.write("Current working directory:", os.getcwd())

# List files in output folder
# Make sure model is listed in those files
try:
    files = os.listdir("outputs/v1")
    st.write("Files in outputs/v1:", files)
except Exception as e:
    st.error(f"Could not list files in outputs/v1: {e}")


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
