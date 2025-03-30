import streamlit as st

def project_hypothesis_body():
    """
    Display project hypothesis, observations, and final validation
    """
    
    st.write("### Project Hypothesis and Validation")

    st.success(
        "**Hypothesis:** Cherry leaves affected by powdery mildew show distinctive visual characteristics "
        "compared to healthy leaves, making it possible to differentiate them through image analysis. "
        "Infected leaves are expected to display light, irregular spots, in contrast to the general green color of healthy leaves.\n\n"
        "**Validation:** To test this hypothesis, average images and variability images were generated for each class ('healthy' and 'powdery mildew'). "
        "These visualizations confirm that infected leaves typically reveal a dotted pattern not present in healthy leaves, supporting the hypothesis. "
        "Additionally, the ML model trained on this dataset achieves a high predictive accuracy, further validating that these differences "
        "are significant enough for automated classification."
        )
