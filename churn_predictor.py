def predict_churn(input_data):
    model = joblib.load("churn_model.pkl")
    prediction = model.predict([input_data])
    return "Will Churn" if prediction[0] == 1 else "Will Stay"
