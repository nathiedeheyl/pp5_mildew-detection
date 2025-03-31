# Mildew Detection in Cherry Leaves

## Project Overview

![Am I Responsive Hero Image](assets/images/hero_image.png)

The Mildew Detection project is a data science and machine learning project developed as part of the "Predictive Analytics" specialization for the Code Institute final portfolio project. The project employs a machine learning model to differentiate between two image categories: healthy cherry leaves and those infected with powdery mildew.

The business context involves a client in the agri-food sector facing challenges with powdery mildew infections on their crops. Currently, disease detection is conducted manually, a process that is both labor-intensive and time-consuming. To enhance efficiency and reliability, this project proposes an ML-based solution that automates the identification of infected leaves from images.
By implementing this model, the client can reduce resource expenditures, streamline disease detection, and ensure a more accurate and timely response to infections.

The project is deployed as a Streamlit app on Render. You can access the live version here: [insert link].

## Dataset

The dataset used in this project is obtained from Kaggle ([See Kaggle Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)). It consists of over 4,000 images collected from the client’s cherry tree plantations. These images belong to two distinct categories:
* **Healthy Leaves**: Cherry leaves with no visible signs of disease
* **Infected Leaves**: Leaves affected by powdery mildew, a fungal infection that appears as a white, powder-like coating on the surface of the leaves

**Dataset Relevance to Business Understanding**

The client is concerned that the outbreak may be impacting crop quality. By analyzing a dataset containing real-world images of healthy and infected leaves, the project ensures the model learns to distinguish between the two categories effectively

The dataset consists of image files categorized into separate directories (/healthy; /powdery_mildew) for supervised machine learning tasks.

This dataset is used for achieving the project objectives, as it provides the necessary visual features to train a Convolutional Neural Network model to classify cherry leaves with high accuracy.

## Business Requirements

The client has outlined two key Business Requirements: 
- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
- 3 - The criteria for the performance goal of the predictions has been agreed on a degree of 97% accuracy.

**Aligning Business Requirements with the Dataset**

The primary objective of this project is to develop a machine learning model capable of detecting powdery mildew in cherry leaves from uploaded photographs. This will replace the current manual inspection process. By automating disease detection, the client aims to reduce operational costs, improve treatment efficiency, and maintain crop quality.

Since the dataset contains a balanced representation of both healthy and diseased leaves, it allows for effective training and testing of a classification model.

![Class Distribution Figure](assets/images/readme1_classdistrib.png)

Key stakeholders for this project include the agricultural business (Farmy & Foods) and their customers, who rely on high-quality produce.

By using this dataset, the project aligns with the CRISP-DM "Business Understanding" phase, ensuring that the machine learning solution is directly driven by the client’s problem statement and business needs.

## Hypothesis

### Hypothesis: Visual Differentiation Between Healthy and Infected Leaves

Hypothesis One is that cherry leaves affected by powdery mildew show distinct visual characteristics compared to healthy leaves, making it possible to differentiate them through image analysis. For instance, infected leaves are expected to display light, irregular spots, in contrast to the general green color of healthy leaves.

#### Validation

To test Hypothesis One, the average image and variability for each class ('healthy' and infected with 'powdery mildew') is generated to highlight dividing patterns.

![Average and Variability per class Image](assets/images/readme3_avrnvar1.png)

![Average and Variability per class Image](assets/images/readme3_avrnvar2.png)

These visualizations confirm that powdery mildew leaves typically reveal a speckled pattern not present in healthy leaves, supporting the hypothesis. The ML model trained on this dataset also achieves high predictive accuracy (99%), validating that these differences are significant enough for automated classification.

## Rationale to Map Business Requirements to Data Visualisations and ML Tasks

To ensure the machine learning solution aligns with business needs, each business requirement is linked to specific data visualizations and ml tasks.

### User Stories & Mapping

| Business Requirement | User Story | Data Visualisation | ML Task |
|----------------------|------------|--------------------|---------|
| **R1: Visually differentiate a healthy cherry leaf from one with powdery mildew** | As a **data scientist (client)**, I want to **compare healthy and infected leaves visually**, so that I can **understand the features that distinguish a healthy from a diseased leaf**. | Compute and plot the size of the average image, visualize class distributions, plot average and variability of images per label, image montage | Feature extraction (the CNN model learns the features that are specific to healthy and diseased leaves to distinguish them) |
| **R2: Predict if a cherry leaf is healthy or infected** | As a **manager (client)**, I want to **automate disease detection from images**, so that I can **take action to protect crops and save on cost for ressources**. | Image augmentation plots (to ensure the dataset has diverse image data for the model to learn from and prevent overfitting) | Model training, hyperparameter tuning (e.g. adjusting batch size), dropout layers |
| **R3: Ensure high model accuracy (97%)** | As a **business owner (client)**, I want a **highly accurate disease detection model**, so that I can **reduce losses and improve efficiency of the detection process**. | Model evaluation plots (learning curves: accuracy/loss) | Model evaluation on test set, Model evaluation on new random data |

To meet the business requirements effectively, the following steps are necessary:
* The prepared dataset should provide representative images of both healthy and infected leaves, as well as visualizations showing variations within each category (image montage, average image, class distribution plot, average and variability per label plot, image augmentation)
* The model must accurately classify leaves as healthy or infected with powdery mildew (Model validation and evaluation)
* The system should process images uploaded on the dashboard by the client efficiently
* Predictions should be generated quickly to facilitate real-time decision-making
* The output should be easy to understand for both technical and non-technical users

## ML Business Case

**Business Case for each Machine Learning task:**

1 - _The aim behind the predictive analytics task_

The current process of manual leaf inspection is time-consuming and difficult to scale. It requires specific knowledge and expertise, which causes high costs in human resources and their training. This process is prone to error and inconsistency.

The goal of this machine learning model is to automate the detection of powdery mildew in cherry leaves using image classification. This replaces the current process of manual leaf inspection. By automating the process, the client can reduce the cost of human labour, ressources and improve the efficienty and accuracy of the inspection process. The ml model also makes classification decisions analytically transparent.

2 - _The learning method_

This project uses a Convolutional Neural Network trained from scratch. A convolutional neural networks is ideal for the task of image classification because it automatically learns patterns and details (e.g. edges, textures or shapes) that help the model recognize the difference between healthy and powdery mildew infected leaves.

3 - _The ideal outcome for the process_

The model should achieve at least 97% classification accuracy on test data.

4 - _Success/failure metrics_

4.1 - _Success:_
* Test set accuracy ≥ 97%
* Learning curves show stable exponential curve without overfitting

4.2 - _Failure:_
* Test accuracy below 97%
* Indication to overfitting: Large gap between training and validation learning curve
* Model struggles to differentiate between healthy and powdery mildew infected leaves

5 - _Model output and its relevance for the user_

* The model takes an input image and outputs the predicted class probability for either "healthy" or "infected" with powdery mildew.
* Since the `softmax` activation function is used to create and train the model, the client can see the confidence of the model in predicting whether the cherry leaf is healthy or infected.
* The higher the probability, the more confident the model is in its classification.
* This allows the client in the agricultural industry to quickly assess the health of the cherry leaves on their plantation and make informed decisions about crop protection.

6 - _Heuristics and training data used_

6.1 - **Data Augmentation**

To improve generalization and prevent overfitting, the dataset was augmented using the following transformations:
* Rotation range = 20 degree
  * Help the model recognize leaves from different orientations
* Width and height shift of 10%
  * Simulate variations in image positioning
* 10 % shear and zoom range
  * For perspective distortions and size variations
* Horizontal and vertical flip
  * For different leaf angles
* Fill mode set to ‘nearest’
  * Fill in missing pixels when shifting or rotating images
* Rescale 1:255
  * Normalize pixel values for better model performance

6.2 - **Dataset Splitting**

The dataset was split into three subsets:
* Training Set = 70%
* Validation Set = 10%
* Test Set = 20%

## Dashboard Design

1 - The Project Summary page: This page has important information about the background and origin of the project and the problem it's aiming to solve. Also included on the summary page are the business requirements set in agreement with the customer, which define a successful project, and a link to the README file for further information.

![Dashboard Design 1](assets/images/dashbaord_design1.png)

2 - The app page "Image visualizer": Important information for the user is displayed on this page. The customer and ultimately the user of the project site can see in more detail what image data the model is based on. Three checkboxes collapse information and example pictures of the average and variability images, the visual differences between the average images of both classes, and an image montage to show a random sample of image data that the model has been trained and validated on. To obtain the image montage, the user has to select one of the two labels from a dropdown menu and click the button saying 'Create Montage'. Loading can take a short moment. On top of the image montage, the user gets an info message with a brief explanation on how those performed actions help to meet business requirement 1.

![Dashboard Design 2](assets/images/dashbaord_design2.png)

![Dashboard Design 3](assets/images/dashbaord_design3.png)

![Dashboard Design 4](assets/images/dashbaord_design4.png)

The image montage shows a total of 3 colums with 8 rows selecting image data from all the subdirectories of the label selected:

![Dashboard Design 5](assets/images/dashbaord_design5.png)

3 - Mildew Detector page: The heart of the project. This is the tool that the client was looking for to improve their overall business, and with the successful implementation of this tool, business requirement 2 is met, by which the client can determine whether a cherry leaf is healthy or infected with powdery mildew by relying on the model's prediction.

![Dashboard Design 6](assets/images/dashbaord_design6.png)

The user can either click the 'Browse files' button or drag and drop their image file onto the uploading field. 

![Dashboard Design 7](assets/images/dashbaord_design7.png)

On the dashboard will then be displayed the uploaded image, along with a clear feedback statement on the predicted label of the image uploaded image, as well as a bar chart showcasing the probability of this class prediction by the model:

![Dashboard Design 8](assets/images/dashbaord_design8.png)

And finally, an analysis report with a link giving the option to download a report of the analyzed images: 

![Dashboard Design 9](assets/images/dashbaord_design9.png)

![Dashboard Design 91](assets/images/dashbaord_design91.png)

Clicking this link downloads a CSV file named using the moment's timestamp down to the second to create an individual file name.

![Dashboard Design 96](assets/images/dashbaord_design96.png)

4 - The Project Hypothesis page summarizes the project's hypothesis and it's validation.

![Dashboard Design 96](assets/images/dashbaord_design96.png)

5 - ML Performance Metrics page: To meet business requirement 3, the ml performance metrics page showcases what methods have been used to prepare, train, validate and evaluate the model. First, the label frequencies per splitted dataset (train, validation, test image dataset):

![Dashboard Design 93](assets/images/dashbaord_design93.png)

Second, the history of model training performance figures: 

![Dashboard Design 94](assets/images/dashbaord_design94.png)

Third, forth, and lastly - the generalized model loss and accuracy performance metrics as a table and conclusions, as well as conclusions to the business case: 

![Dashboard Design 95](assets/images/dashbaord_design95.png)

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Testing

### Python Code Validation

| App page | Screenshot before | Fixes | Screenshot validated |
|----------|-------------------|-------|----------------------|
| Project summary | ![pep8 validator image 1](assets/images/readme2_pep8-1.png) | fix small syntax errors and apply PEP8 formatting fixes | ![pep8 validator image 2](assets/images/readme2_pep8-2.png) |
| page_manager | ![pep8 validator image 3](assets/images/readme2_pep8-3.png) | fix small syntax errors and apply PEP8 formatting fixes | ![pep8 validator image 4](assets/images/readme2_pep8-4.png) |
| image_visualizer | ![pep8 validator image 5](assets/images/readme2_pep8-5.png) | fix small syntax errors and apply PEP8 formatting fixes | ![pep8 validator image 6](assets/images/readme2_pep8-6.png) |
| mildew_detector | ![pep8 validator image 7](assets/images/readme2_pep8-7.png) | fix small syntax errors and apply PEP8 formatting fixes | ![pep8 validator image 8](assets/images/readme2_pep8-8.png) |
| project_hypothesis | ![pep8 validator image 92](assets/images/readme2_pep8-92.png) | fix small syntax errors and apply PEP8 formatting fixes | ![pep8 validator image 93](assets/images/readme2_pep8-93.png) |
| ml_performance_metrics | ![pep8 validator image 9](assets/images/readme2_pep8-9.png) | fix small syntax errors and apply PEP8 formatting fixes | ![pep8 validator image 91](assets/images/readme2_pep8-91.png) |
| evaluate_clf | ![pep8 validator image 94](assets/images/readme2_pep8-94.png) | PEP8 formatting fix: new line at end of file missing | ![pep8 validator image 95](assets/images/readme2_pep8-95.png) |
| predictive_analytics | ![pep8 validator image 96](assets/images/readme2_pep8-96.png) | PEP8 formatting fix: new line at end of file missing | ![pep8 validator image 97](assets/images/readme2_pep8-97.png) |
| data_management | ![pep8 validator image 98](assets/images/readme2_pep8-98.png) | No fixes | - |
| page_manager | ![pep8 validator image 99](assets/images/readme2_pep8-99.png) | No fixes | - |
| app.py | ![pep8 validator image 991](assets/images/readme2_pep8-991.png) | PEP* formatting fix: new line at end of file missing | ![pep8 validator image 992](assets/images/readme2_pep8-992.png) |

### Manual testing

| Feature | Function | Screenshot | Manual Test Validation |
|---------|----------|------------|------------------------|
| Radio button side bar navigation menu | Site navigation: All sites accessible after clicking radio button | ![testing 1](assets/images/readme4_test1.png) | ✅ |
| Collapsible navigation side menu | Collapsible and responsive side bar navigation | ![testing 1](assets/images/readme4_test2.png) ![testing 1](assets/images/readme4_test3.png) | ✅ |
| Link to README file | Redirects to README file | ![testing 1](assets/images/readme4_test4.png) | ✅ |
| Three checkboxes for project image visualization | Collapse the information described | see Dashboard Design above | ✅ |
| Mildew Detector image file upload | Drag and drop or choose and select image files for live prediction | ![testing 1](assets/images/readme4_test5.png) | ✅ |
| Image live prediction | Predict class of uploaded image(s) and create downloadable csv file with results | - | ❌ |

### Image Size Reduction and Model Performance

While resizing images was considered as a possible optimization step, the model performed well at a resolution of 256×256 pixels, and deployment to GitHub was completed successfully without need for adjustments. As a result, resizing was not implemented in this version.

However, for future iterations, investigating the impact of smaller image sizes on model performance and training efficiency could be valuable – particularly if the dataset builds up over time. Optimizing image size may help ensure scalability while maintaining classification accuracy.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
