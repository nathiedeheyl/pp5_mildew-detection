# Mildew Detection in Cherry Leaves

## Project Overview

...

## ML Business Case

`"frame the business case using methods covered in the course"`

The current process of leaf inspection is time-consuming and difficult to scale. It requires specific knowledge and expertise, which causes high costs in human resources and their training. This process is prone to error and inconsistency.

Therefore, a machine learning project offers an attractive solution. The ml model automates the inspection and classification process which makes the process faster and scalable. It reduces labour costs and makes classification decisions analytically transparent. It improves accuracy.

Potential risks of a machine learning solution are the following: The model might not adjust to new data and have difficulties categorising deviations, e.g. mutations of the powdery mildew. Also, the size of the model might eventually increase, and its future cost has to be evaluated. Mitigation strategies are to continuously use adequate training data and augmentations, as well as implement data size limitations, e.g. reduce image size resolution.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis
### Hypothesis 1
Healthy and powdery mildew-infected cherry leaves have visual differences that can be quantified through image analysis, e.g. white blotches on infected leaves.
#### Validation 1
Compare average images, variability images, and visual features across the two classes (healthy and infected).

### Hypothesis 2
The ml model can identify a cherry leaf as either healthy or powdery mildew-infected with at least 97% accuracy.
#### Validation 2
Train a binary classification model and evaluate its accuracy on test data.

## Rationale to map business requirements to Data Visualisations and ML tasks

=> What exactly is the Rationale?

Map

| Business need | Data Visualisation | Technical implementation: ML task |
|---------------|--------------------|-----------------------------------|
|R1: Visually differentiate a healthy cherry leaf from one with powdery mildew | 1. Create average images [and other tasks, check walkthrough] for each class | Feature Engineering/Extraction = "figure out what features determine healthy or infected" |
| R2: Predict if a cherry leaf is healthy or infected | Plot class distribution | In case: image augmentation and for sure: hyperparameters |
| Model accuracy of 97% | ... | Model evaluation and performance comparison |

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

project/
├── app.py                 # Main application entry point
├── pages/                 # Additional pages for the multi-page app
│   ├── 1_project_summary.py
│   ├── 2_leaf_visualizer.py
│   ├── 3_ml_prediction.py
│   ├── 4_hypothesis.py
│   └── 5_model_performance.py
├── src/                   # Source code modules
│   ├── data_management.py         # Functions for data handling
│   ├── predictive_analysis.py     # Functions for model predictions
│   └── visualization.py           # Functions for data visualization
├── model/                 # Saved model files
│   └── cnn_model.h5       # Your trained CNN model
├── assets/                # Static assets
│   ├── sample_images/     # Sample images for download
│   └── css/               # Custom CSS styling
└── README.md              # Project documentation

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
