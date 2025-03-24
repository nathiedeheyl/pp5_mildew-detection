import streamlit as st

def project_hypothesis_body():
    """
    Display project hypothesis, observations, and final validation
    """
    
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Hypothesis: Cherry leaves affected by powdery mildew exhibit distinct visual patterns, "
        f"e.g. white powdery spots, that clearly differentiate them from healthy leaves.\n\n"
        f"* Validation: The Image Montage (see 'Image Visualizer') reveals that leaves infected "
        f"with powdery mildew often display visible white patches. "
        f"However, the difference between average image of both classes analysis "
        f"does not clearly highlight distinct patterns to differentiate."
        )
