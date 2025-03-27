import streamlit as st

def project_summary_body():
    """
    Display summary of the project and its objectives
    """
    
    st.title("Project Summary: Cherry Leaf Powdery Mildew Detector")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects many plants, including cherry trees.\n"
        f"* It appears as white, powdery spots on leaves. When those spots spread they can significantly reduce plant health.\n"
        f"* Finding the disease early is important to stop it from spreading and to keep the crops healthy.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains images of cherry leaves labeled as 'healthy' or infected with 'powdery_mildew'.\n"
        f"* The machine learning model was trained with these images to detect the disease."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/nathiedeheyl/pp5_mildew-detection/blob/main/README.md)."
    )

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client wants a study to visually differentiate healthy and with powdery mildew infected cherry leaves.\n"
        f"* 2 - The client needs an automated tool to classify cherry leaf images as healthy or infected with powdery mildew."
    )
