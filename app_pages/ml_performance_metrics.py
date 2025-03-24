import streamlit as st

def ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    # labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    # st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    # st.write("---")

    # st.write("### Model History")
    # col1, col2 = st.columns(2)
    # with col1: 
    #     model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    #     st.image(model_acc, caption='Model Training Accuracy')
    # with col2:
    #     model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
    #     st.image(model_loss, caption='Model Training Losses')
    # st.write("---")

    # # reference to def load_test_evaluation(version) in src/machine_learning/evaluate_clf.py where load_test_evaluation is returned, function reference to src/data_management.py => def load_pkl_file(file_path) to load pickle file
    # st.write("### Generalised Performance on Test Set")
    # st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
