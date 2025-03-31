import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    predictions_probabilities
                                                    )


def mildew_detector_body():
    """
    Mildew detection model page for analyzing individual cherry leaf samples.
    """

    st.info("""
        * This tool helps determine whether a given cherry leaf is
        infected with powdery mildew or not.
        """)

    st.write(
        f"* You can upload images of cherry leaves for live prediction. "
        f"If you need sample images, visit the dataset source "
        f"[here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
        )

    st.write("---")

    images_buffer = st.file_uploader(
        'Upload cherry leaf images. You may select more than one.',
        type='png',
        accept_multiple_files=True
        )

    if images_buffer:
        df_report = pd.DataFrame([])

        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Cherry Leaf Sample: **{image.name}**")

            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=f"Image Size: {img_array.shape[1]}px width x "
                        f"{img_array.shape[0]}px height"
                    )

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                                resized_img, version=version
                                )

            predictions_probabilities(pred_proba, pred_class)

            df_report = df_report._append(
                {"Name": image.name, "Result": pred_class},
                ignore_index=True
                )

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(
                        download_dataframe_as_csv(df_report),
                        unsafe_allow_html=True
                        )
