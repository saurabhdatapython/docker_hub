from trainingModel import trainModel
from training_Validation_Insertion import train_validation
import flask_monitoringdashboard as dashboard
from predictFromModel import prediction
path = r"C:\Users\Samsung\Desktop\Training_Batch_Files"
train_valObj = train_validation(path)  # object initialization

train_valObj.train_validation()  # calling the training_validation function

trainModelObj = trainModel()  # object initialization
trainModelObj.trainingModel()  # training the model for the files in the table