import streamlit as st

def main():
    st.set_page_config(
        page_title="Cherry Leaf Powdery Mildew Detector",
        page_icon="🍒",
    )

    st.title("Cherry Leaf Powdery Mildew Detection")
    st.write("""
    This application uses a CNN model to detect powdery mildew in cherry leaves.
    I will add a sidebar to browse through different pages.
    """)

if __name__ == "__main__":
    main()