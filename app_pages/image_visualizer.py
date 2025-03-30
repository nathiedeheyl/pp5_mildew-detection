import streamlit as st
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def image_visualizer_body():
    """
    Display visualization options of cherry leaf images:
    * Average and Variability Images
    * Difference between averages images
    * Image Montage
    """

    st.write("### Cherry Leaf Image Visualizer")

    st.info(
        "* This tool helps explore cherry leaf images and visualize "
        "patterns related to powdery mildew."
        )

    version = 'v1'
    if st.checkbox("Average and Variability Images"):

        avg_infected = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png"
            )
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.image(
            avg_infected,
            caption='Infected Leaf - Average and Variability'
            )
        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')

        st.write(
            "These images show the average image of powdery mildew infected "
            "and healthy leaves. Differences in aspects like color or shape "
            "help the model to distinguish between the two classes."
            )

        st.write("---")

    if st.checkbox("Difference Between Average Images"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.image(
            diff_between_avgs,
            caption='Difference between Average Images'
            )

        st.write("""
            These images show how the average image of a healthy leaf 
            and average image of a with powdery mildew infected leaf 
            differ on average. \n
            This is helpful for feature extraction.
            """)

        st.write("---")

    if st.checkbox("Image Montage"):
        st.write(
                "* To create or refresh the montage, click on the "
                "'Create Montage' button"
                )
        my_data_dir = 'inputs/mildew_dataset/cherry-leaves'

        # Get only real directories in validation folder
        # exclude hidden system files
        validation_dir = os.path.join(my_data_dir, "validation")
        labels = [
            d
            for d in os.listdir(validation_dir)
            if os.path.isdir(os.path.join(validation_dir, d))
            ]

        label_to_display = st.selectbox("Select Label", options=labels)

        if st.button("Create Montage"):

            st.write(
                "The image montage shows a sample of the diversity "
                "of images per category (label) in the dataset."
                )

            image_montage(
                dir_path=os.path.join(my_data_dir, "validation"),
                label_to_display=label_to_display,
                nrows=8,
                ncols=3,
                figsize=(10, 25)
                )

        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """
    Generate and display a montage of images from validation image dataset
    """
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # Filter images per label
    if label_to_display in labels:

        # Get list of images in selected folder
        # check if montage space > subset size
        images_list = os.listdir(os.path.join(dir_path, label_to_display))

        # Check if montage size is valid
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            st.write(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} images in your subset, "
                f"but you requested a montage with {nrows * ncols} spaces."
            )
            return

        # Create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # Create a figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(nrows * ncols):
            img = imread(os.path.join(dir_path, label_to_display, img_idx[x]))
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px"
                )
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        st.error("The selected label does not exist.")
        st.error(f"Available labels: {labels}")
