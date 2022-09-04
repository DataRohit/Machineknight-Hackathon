# Machineknight Hackathon Project

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

### The API for the model has been hosted using Heroku.<br/>View the Interactive API playground by clicking the link - [Mahineknight-house-price](https://machineknight-house-price.herokuapp.com/)