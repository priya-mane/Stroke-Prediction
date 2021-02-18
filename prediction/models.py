from django.db import models
import joblib
import numpy as np
from joblib import dump, load
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import logging
import sys


# Create your models here.


class User:
    def __init__(self, Gender, Age, Hypertension, Heart_disease, Ever_married, Work_type, Residence_type, Avg_glucose_level, Bmi, Smoking_status):
        self.gender = Gender
        self.age = Age
        self.hypertension = Hypertension
        self.heart_disease = Heart_disease
        self.ever_married = Ever_married
        self.work_type = Work_type
        self.Residence_type = Residence_type
        self.avg_glucose_level = Avg_glucose_level
        self.bmi = Bmi
        self.smoking_status = Smoking_status

    def get_one_hot_encoders(self, encoder_file_name):
        encoders = []
        for file_name in encoder_file_name:
            clf = load(file_name)
            encoders.append(clf)
        return encoders

    def model(self):
        one_hot_features = ['gender', 'ever_married',
                            'work_type', 'Residence_type']

        smoking_label_encoder = load('ml_models/smoking_label_encoder.joblib')

        clf = load('ml_models/classifier.joblib')

        encoders = self.get_one_hot_encoders(
            ['ml_models/' + f + '.joblib' for f in one_hot_features])

        smoking = smoking_label_encoder.transform([self.smoking_status])

        input_list = [self.age, self.hypertension, self.heart_disease,
                      self.avg_glucose_level, self.bmi, smoking[0]]

        ans = []

        input_cat_features = [self.gender, self.ever_married,
                              self.work_type, self.Residence_type]

        for i in range(0, len(one_hot_features)):
            enc = encoders[i]
            val = enc.transform(
                np.array(input_cat_features[i]).reshape(-1, 1)).toarray()[0].tolist()
            ans.append(val)

        result = sum(ans, [])

        input_list = input_list + result

        y_pred = clf.predict(np.array(input_list).reshape(1, -1))
        prob = clf.predict_proba(
            np.array(input_list).reshape(1, -1))[:, y_pred[0]][0]

        return y_pred[0], prob
