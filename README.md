# Roses Disease Classification Project

## Overview
    The Roses Disease Classification project aims to develop a machine learning model to classify images of rose leaves into three categories: Black Spot, Downy Mildew, and Fresh Leaf. The project utilizes convolutional neural networks (CNNs) implemented using TensorFlow and Keras to achieve accurate classification. This README provides an overview of the project structure, components, and usage.
![upload_pic](https://github.com/kounima-zakaria/roses_disease_classification/assets/110348449/35018ab5-a543-4af3-b706-cbc691872932)
![result](https://github.com/kounima-zakaria/roses_disease_classification/assets/110348449/00947a7d-ade0-4f68-9a56-23a5e1f35220)



## Project Components

1. Dataset
The dataset consists of images of rose leaves categorized into three classes: **Black Spot**, **Downy Mildew**, and **Fresh Leaf**.
Images are organized into folders corresponding to their respective classes.

2. Augmented Dataset
Augmented dataset contains additional images generated through data augmentation techniques.
Data augmentation helps in improving model robustness and generalization by artificially increasing the diversity of the training dataset.

3. Training Notebook (training.ipynb)
The training notebook (training.ipynb) contains the code for loading the dataset, defining the model architecture, training the model, and evaluating its performance.
It includes *step-by-step* instructions and code snippets for each stage of the model development process.

4. API (api)
The API directory contains backend code for serving the trained model.
The API exposes endpoints for model inference, allowing users to classify images using HTTP requests.

5. Frontend (frontend)
The frontend directory contains code for the user interface.
It provides a web interface for users to interact with the model, upload images, and view classification results.

6. Test Images (test_images)
Test images directory contains sample images used for testing and validation purposes.
These images are used to evaluate the model's performance and verify classification accuracy.

7. Saved Model (Saved_model_version1)
The saved model directory contains the trained model serialized and saved in a format compatible with TensorFlow/Keras.
The saved model can be loaded and used for inference without retraining.

## Usage
### Dataset Preparation: Ensure that the dataset is properly organized in folders corresponding to each class.
#### Data Augmentation (Optional): Augment the dataset to increase its diversity and improve model performance if necessary.
### Model Training: Execute the training notebook (training.ipynb) to train the CNN model on the dataset.
### Model Evaluation: Evaluate the trained model's performance using test images and metrics provided in the training notebook.
### Backend Integration: Integrate the trained model into the backend API (api) to expose classification endpoints.
### Deployment: Deploy the backend API and frontend interface to a server or hosting platform for public access.

## Frontend Source Acknowledgement !!  

*The frontend source code used in this project is based on an existing template or framework that has been adapted for the Roses Disease Classification project. While the specific details of the original source may not be provided here, it's essential to acknowledge the original creators or contributors of the frontend code.*

### Source Attribution
The frontend source code used in this project is adapted from [insert name of template or framework]. The original source provides a foundation for building user interfaces and web applications, and its adaptation for the Roses Disease Classification project adds specific functionality related to image classification and interaction with the backend API.

### Features and Components
The adapted frontend includes the following features and components:

- User interface elements for uploading images
- Integration with backend API endpoints for image classification
- Display of classification results to users
- Responsive design for compatibility across different devices

### Acknowledgement
We extend our gratitude to the original creators or contributors of the frontend source code for providing a valuable resource that has been instrumental in the development of the Roses Disease Classification project. Their work serves as a foundation for building intuitive and user-friendly interfaces, enhancing the accessibility and usability of the project for its intended audience.
