# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Python Data Visualizations
#
#    - I will first create my own sample data to check if the packages are working properly then the fun with real data begins!

import pandas as pd
import numpy as np


# +
# I will take the courses I am currently taking at my university as a sample data
course_details=np.array([["SECT-M5201", "Advanced Development","SECT-4221","Enterprise Application Developement",7.00],
                ["SECT-M4451", "Machine Learning and big data","SECT-4451","Machine Learning and big data",5.00],
                ["SECT-M4181", "System Modeling","SECT-4181","Requirement Engineering and architectire",7.00],
                ["SECT-M4141", "High performance computing","SECT-4141","Fundamentals of distributed systems",7.00],
                ["SECT-M4231", "Software project management","SECT-4231","Software Project Management",5.00]])

column_lables= ["Module Code", "Module Name", "Course Code", "Course Title", "ECTS"]
# -

course_table = pd.DataFrame(data= course_details, columns=column_lables)

course_table

# - Loading a .csv dataset

car_financing_dataset= "../data/car_financing.csv"
car_financing_dataframe= pd.read_csv(car_financing_dataset)

car_financing_dataframe

# - Loading a .xlsx dataset

car_financing_dataset= "../data/car_financing.xlsx"
car_financing_dataframe= pd.read_excel(car_financing_dataset)

car_financing_dataframe

# - Let's check the datatypes for each columns in the given dataset

car_financing_dataframe.dtypes

#checking the first 5 rows
car_financing_dataframe.head()

# checking the last 5 rows
car_financing_dataframe.tail()

#checking the number of rows an columns
car_financing_dataframe.shape

# # Slicing the dataset

#Let's isolate the car type and the starting balance into a separate dataframe
ct_sb= car_financing_dataframe[["car_type","Starting Balance"]]


ct_sb.head()

# - Panda Series

# +

car_type_series= car_financing_dataframe['car_type'][0:10]
# -

car_type_series

# The offical way to visualize this would be by using the loc attribute
car_financing_dataframe.loc[:,["car_type","Starting Balance"]][0:10] 

# # Filtering the Dataset

# - Checking the different values there are for a specific column

car_financing_dataframe[["car_type"]].value_counts()

# - Filtering data for a particular car_type

# +
#Let's say we just want VW Golf R type cars from the dataset

vw_filter= car_financing_dataframe['car_type']=="VW Golf R"


# -

vw_filter.head()

car_financing_dataframe.loc[vw_filter,:][0:10]


