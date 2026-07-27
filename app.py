import os
import sys
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from xgboost import data
from src.logger import logging
from src.exception import CustomException
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=int(request.form.get('reading_score')),
                writing_score=int(request.form.get('writing_score'))
             )
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            predict_pipeline = PredictPipeline()
            preds = predict_pipeline.predict(features=pred_df)
            return render_template('home.html', prediction_text="The predicted result is {}".format(preds[0]))
        except Exception as e:
            logging.error(e)
            raise CustomException(e, sys)
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
