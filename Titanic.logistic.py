# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""

import pandas as pd
import streamlit as st 
from sklearn.linear_model import LogisticRegression
import pickle as pickle

st.title('Model Deployment: Prediction of survival')

st.sidebar.header('User Input Parameters')

def user_input_features():
    Pclass= st.sidebar.selectbox('Class',('1','2','3'))
    Sex= st.sidebar.selectbox('Sex',('0','1'))
    Age= st.sidebar.number_input('Insert Age')
    SibSp = st.sidebar.selectbox('SibSp',('0','1','2','3'))
    Parch= st.sidebar.selectbox('Parch',('0','1','2','3','4','5','6'))
    Fare= st.sidebar.number_input('Insert Fare')
    Embarked= st.sidebar.selectbox('Embarked',('0','1','2'))
    
   
    
    data= {'Pclass':Pclass,
            'Sex':Sex,
            'Age':Age,
            'SibSp':SibSp,
            'Parch':Parch,
            'Fare':Fare,
            'Embarked':Embarked}

    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

loaded_model=pickle.load(open("C:\\Users\\hp\\Desktop\\EXCELR\\Assignments\\Titanic.pkl",'rb'))
''' Sex: Female-0
         Male-1

    Embarked: C-0
              Q-1
              S-2'''

prediction = loaded_model.predict(df)
prediction_proba = loaded_model.predict_proba(df)

   

st.subheader('Predicted Result')
if prediction==0:
    st.write("Person will not survive")
else:
    st.write("Person will survive")
             

st.subheader('Prediction Probability')
st.write(prediction_proba)
