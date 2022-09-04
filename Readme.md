# Machineknight Hackathon Project

#### Github Repo Link (For Complete Files and Folder) - [Fly to Repo](https://github.com/DataRohit/Machineknight-Hackathon)

## Problem Statement
Your frined is going to start a real estate business, and ask your help to **predict** the **house rents** in his regions. He gave you a **housing data** to work on. You decided to build a **machine learning model** that can predict the rent of house.
<br/>
Also your friend has no idea about ml and how to make predictions using ml model. So, you have to build an **api hosted front-end web app**, so that your friend can easily operate that.

## Task
You are give the **dataset of housing properties**. You task is to create a ML model that can predict the rent of house based on the given properties. Serve that **ML model using rest api**. You have to integrate both backend and frontend.
<br/>
**Train your model using train data and make predictions of teh test data**

## Installation
This project has two folders
 - One for Data Processing and Model Training and Testing 
 - Second for API

Both these folders have their seperate **requirement.txt** files.

#### Change directory to each of these folder and run the following commands step by step
```python
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
```
#### Note: Commands for command prompt

# Usage
One all the packages are installed you are ready to go.
 - For running the .ipynb file use google colab
   - For model training and testing auto-sklearn package has been used. Auto-sklearn package only supports linux based systems so use google colab.
   - Upload the the data files to runtime in colab.
   - Firstly run the code cell which install the auto-sklearn package as auto-sklearn asks for restart of Runtime.
   - One done you can Rull all the cell and get the output.
 - For running the API
   - The same problem here is that auto-sklearn does not support windows.
   - But other endpoints can be tested.
   - Change directory to the API folder.
   - Then run the following command ```uvicorn main:app --reload``` in the terminal to get the API started.

**Solution to the Auto-Sklearn Problem - Luckily the servers running Google Colab and Heroku (Used for API hosting) both use Linux based servers for hosting.**

## The API for the model has been hosted using Heroku.<br/>View the Interactive API playground by clicking the link - [Mahineknight-house-price](https://machineknight-house-price.herokuapp.com/)

# Requiremnts.txt
## Data Processing & Model Training
```python
pandas==1.4.4
auto-sklearn==0.14.7
```
## API
```python
fastapi==0.81.0
pandas==1.4.4
uvicorn==0.18.3
auto-sklearn==0.14.7
gunicorn==20.1.0
```

# Data Processing
### The following steps were followed in order to model the data in the desired format followed by training and testing of the model:
 1. Dropping `id`, `activation_data` and `locality` column from the data as they did not have much effect on the rent <br/>Model was trained and tested with and withot `locality` column the model performance did not seemed to be affected.
 2. `amenities` columns has stored in the form of stringified dictionary. Extracting that data and adding to original dataset.
 3. Dropping the repeated columns. Some columns which are present in data are also in amenities so Dropping them.
 4. All the features extracted from `amenities` are binary. So Assuming more the ammenities higher will be the price. So summing up all the amenities binary feature to make one single feature.
 5. Dropping the ineffective columns and preparing the data for encoding of categorical columns.
 6. Seperating the target and features from the data.
 7. Label Encoding the categorical columns and storing the trained encoder for each feature to be used in the API.
 8. Splitting the data into training and testing data form ML Model training and testing.
 9. Initializing and Training AutoSklearn Regressor. The same model was trained from 1Hr and 2Hr. The 2Hr model performed slightly better and thus was used for making the predictions.
 10. Custom function to calculate `RMSE`, `R2` and `Adjusted R2` score for checking the performance of the model.
 11. Saving the trained model and trained encoders.

# API - Working
#### Test the API (Open in Browser)  - https://machineknight-house-price.herokuapp.com/docs
### Base Path (https://machineknight-house-price.herokuapp.com/)
This base path is a path which supports GET request but it redirects to the `/docs` path which provides a GUI interface to test and play with the API. This path returns the HTML of the "/docs" page but works if the link is opened in Browser.
### Get Object Features (https://machineknight-house-price.herokuapp.com/get_features/object_features)
This past supports GET Request and it returns the Object / Categorical columns that are expected as Input and their expected values in the form of list.
### Get Number Features (https://machineknight-house-price.herokuapp.com/get_features/numerical_features)
This path supports GET Request and it return the Numerical columns that are expected as Input and their expected values in the form of list which is the range where the first value being the minimum and second being maximum. The max and min values was calculated from the complete data that was used for training and testing of the model.
### Predict House Rent (https://machineknight-house-price.herokuapp.com/predict/rent)
This path supports POST Request and it expects 18 different values as query parameters. Once successfully making the request without any error or fault values the model returns a dictionary of the the values that were given as the input and the predicted house rent.

# Screenshots
|    |    |
| ---| ---|
|![Screenshot](/images/FastAPI-Swagger-UI-1.png)| ![Screenshot](/images/FastAPI-Swagger-UI-2.png) |
|![Screenshot](/images/FastAPI-Swagger-UI-3.png)| ![Screenshot](/images/FastAPI-Swagger-UI-4.png) |