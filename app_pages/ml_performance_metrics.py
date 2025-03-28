import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

def ml_performance_metrics():
    """
    Display model performance metrics: class label distribution, training history, test dataset evaluation, and business requirement conclusions
    """
    version = 'v1'

    # Performance metrics Section
    st.write("### Machine Learning Model Performance Dashboard")

    # Label distribution
    st.write("#### 1. Dataset Composition")
    st.write("About the distribution of image labels in the dataset:")
    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    
    st.write("---")

    # Model training history
    st.write("#### 2. Model Training Performance")
    col1, col2 = st.columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    # Test set performance
    st.write("#### 3. Model Generalization")
    test_eval = load_test_evaluation(version)
    st.dataframe(pd.DataFrame(test_eval, index=['Loss', 'Accuracy']))

    # Business conclusions Section
    st.write("### 4. Business Insights and Conclusions")

    # TODO: If possible, dynamically extract accuracy from 'test_eval'
    st.write("Conclusions of data analytics task to answer business requirements:")
    st.write(f"The model has a predictive accuracy of 99%, indicating that it meets business requirement #3.")
