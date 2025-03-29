import streamlit as st


def project_summary_body():
    """
    Display summary of the project and its objectives
    """

    st.title("Project Summary: The Powdery Mildew Detector for Cherry Leaves")

    st.info("""
    **General Information**
    - Powdery mildew is a fungal disease that affects many plants,
            including cherry trees.
    - It appears as white, powdery spots on leaves. When those spots
            spread, they can significantly reduce plant health.
    - Finding the disease early is important to stop it from spreading
            and to keep the crops healthy.

    **Project Dataset**
    - The dataset contains images of cherry leaves labeled as 'healthy'
            or infected with 'powdery_mildew'.
    - The machine learning model was trained with these images to detect
            the disease.
    """)

    st.write(
        "- For additional information, please visit and **read** the "
        "[Project README file](https://github.com/nathiedeheyl/"
        "pp5_mildew-detection/blob/main/README.md)."
    )

    st.success("""
        The project has 3 business requirements:\n
        1. The client wants a study to visually differentiate healthy and
               with powdery mildew infected cherry leaves.\n
        2. The client needs an automated tool to classify cherry leaf images
               as healthy or infected with powdery mildew.\n
        3. The performance goal of the predictions has been agreed on a
               degree of 97% accuracy.
    """)
