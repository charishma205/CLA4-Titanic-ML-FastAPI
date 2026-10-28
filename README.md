# ML Model Deployment Strategies and Model Serving using FastAPI

## 1. Project Overview

Machine Learning (ML) models are useful for making predictions from data. However, training a model alone is not sufficient. The trained model must be deployed so that users and applications can access its predictions.

This project, **ML Model Deployment Strategies and Model Serving using FastAPI**, demonstrates the process of training, saving, deploying, and serving a machine learning model.

The Titanic dataset is used to develop a classification model that predicts whether a passenger survived or not. The trained model is saved as a file and used for online, batch, and streaming inference.

FastAPI is used to create a REST API that allows users to interact with the trained model and obtain predictions.

## 2. Problem Statement

Machine learning models developed during experimentation are often limited to notebooks and local environments. To make these models useful in real-world applications, they must be deployed and made accessible through a suitable serving mechanism.

The objective of this project is to demonstrate different model inference strategies and deploy a trained classification model using FastAPI.

The system should support:
- Prediction for a single unseen record.
- Prediction for multiple records in batch.
- Processing records in a streaming manner.
- Serving predictions through REST API endpoints.
- Validating input data and handling invalid requests.

## 3. Objectives

The main objectives of this project are:

1. To train and evaluate a machine learning classification model using the Titanic dataset.
2. To save the trained model for future use.
3. To implement online inference for a single unseen record.
4. To implement batch inference for 20 unseen records.
5. To implement streaming inference for 10 records with a 1-second delay.
6. To develop a FastAPI application for serving machine learning predictions.
7. To create health-check and prediction endpoints.
8. To test the API using Swagger UI and a Python client.
9. To understand the practical workflow of machine learning model deployment.

## 4. Dataset Description

The project uses the Titanic dataset available on Kaggle.

The dataset contains information about passengers who travelled on the Titanic. It includes passenger details and the survival outcome.

The dataset is used to train a classification model that predicts the survival status of a passenger.

The data is preprocessed before training. The preprocessing and model pipeline are saved together so that the same transformations can be applied during inference.

**Dataset:** Kaggle Titanic Dataset  
**Target:** Survival prediction  
**Task Type:** Binary Classification

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Google Colab | Model development and execution |
| Pandas | Data loading and data manipulation |
| Scikit-learn | Data preprocessing, model training, and evaluation |
| Random Forest Classifier | Classification model |
| Pickle | Saving and loading the trained model |
| FastAPI | Creating REST API endpoints |
| Pydantic | Input data validation |
| Uvicorn | Running the FastAPI application |
| Requests | Sending HTTP requests to the API |
| GitHub | Source code storage and project sharing |

## 6. Methodology

The project follows the below workflow:

1. Load the Titanic dataset.
2. Perform data preprocessing.
3. Split the dataset into training and testing data.
4. Train the machine learning classification model.
5. Evaluate the model using suitable evaluation metrics.
6. Save the trained model as `model.pkl`.
7. Perform online inference.
8. Perform batch inference.
9. Perform streaming inference.
10. Develop the FastAPI application.
11. Test the API endpoints.
12. Observe and analyze the results.

## 7. Model Deployment Strategies

### 7.1 Online Inference

Online inference is used when a prediction is required for a single input record.

In this project, one unseen passenger record is provided to the trained model. The model processes the input and returns the predicted survival outcome.

**Use case:** Making an immediate prediction for an individual passenger.

### 7.2 Batch Inference

Batch inference is used when predictions are required for multiple records at the same time.

In this project, 20 unseen records are processed by the trained model. The predictions are generated and saved into a CSV file named `batch_predictions.csv`.

**Use case:** Processing a collection of records together.

### 7.3 Streaming Inference

Streaming inference processes records one after another as they arrive.

In this project, 10 records are processed sequentially with a 1-second delay between records. The prediction for each record is displayed during execution.

**Use case:** Demonstrating continuous or sequential processing of incoming records.

## 8. FastAPI Model Serving

FastAPI is a Python web framework used to create APIs. It allows the trained machine learning model to be accessed through HTTP requests.

The trained model is loaded into the FastAPI application. When a request is received, the input data is validated, passed to the model, and the prediction is returned as a response.

### API Endpoints

#### GET /health

This endpoint checks whether the API application is running.

**Expected response:**

    {
        "status": "API is running"
    }

#### POST /predict

This endpoint accepts passenger information and returns the predicted survival outcome.

The input is validated using Pydantic. If the input is valid, the model generates a prediction. If the input is invalid, the API returns a validation error.

## 9. API Testing

The FastAPI application is tested using Swagger UI and a Python client.

The following tests are performed:

- Health-check endpoint testing.
- Successful prediction using valid input.
- Validation testing using invalid input.
- API response status code verification.
- Prediction response verification.

Swagger UI provides an interactive interface to test the API endpoints.

## 10. Project Files

| File Name | Description |
|---|---|
| `model.pkl` | Saved machine learning model and preprocessing pipeline |
| `app.py` | FastAPI application containing the API endpoints |
| `client.py` | Python client used to send requests to the API |
| `batch_predictions.csv` | Output file containing batch inference results |
| `requirements.txt` | List of required Python packages |

## 11. Observations

The project demonstrates the process of deploying a trained machine learning model and serving predictions through different inference strategies.

The online inference, batch inference, and streaming inference tasks demonstrate how a model can process data in different ways.

The FastAPI application provides an interface for accessing the model through HTTP requests. The health-check endpoint verifies the application status, while the prediction endpoint returns model predictions.

Input validation helps identify invalid requests and improves the reliability of the API.

## 12. Advantages

- Demonstrates the complete machine learning deployment workflow.
- Supports single-record and multiple-record predictions.
- Provides an API interface for accessing model predictions.
- Uses input validation to handle invalid requests.
- Separates model training from model serving.
- Helps understand practical ML deployment concepts.

## 13. Conclusion

This project demonstrates the implementation of machine learning model deployment strategies and model serving using FastAPI.

A classification model is trained using the Titanic dataset and saved for future inference. Online, batch, and streaming inference strategies are implemented to demonstrate different ways of generating predictions.

The FastAPI application provides health-check and prediction endpoints, allowing the trained model to be accessed through HTTP requests.

Overall, this project provides practical experience in machine learning model development, deployment, API creation, input validation, and model serving.

## 14. Future Enhancements

- Deploy the FastAPI application on a cloud platform.
- Add logging and monitoring for API requests.
- Improve the model using additional features and hyperparameter tuning.
- Develop a simple web interface for users.
- Add automated testing for the API endpoints.

## 15. Author

**Project:** ML Model Deployment Strategies and Model Serving using FastAPI  
**Dataset:** Kaggle Titanic Dataset  
**Development Environment:** Google Colab  
**Repository:** GitHub
