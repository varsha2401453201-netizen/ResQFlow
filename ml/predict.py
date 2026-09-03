import joblib
import pandas as pd

# Load trained model and preprocessor
model = joblib.load("ml/model/hgb_flood_model.pkl")
preprocessor = joblib.load("ml/model/flood_preprocessor.pkl")

print("Model and preprocessor loaded successfully!")
print("Model type:", type(model))
print("Number of model iterations:", model.n_iter_)


def predict_flood(
    state,
    district,
    month,
    day,
    rainfall,
    rainfall_3day,
    rainfall_7day,
    historical_flood_count_10yr
):

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "State": state,
        "District": district,
        "month": month,
        "Day": day,
        "Rainfall": rainfall,
        "rainfall_3day": rainfall_3day,
        "rainfall_7day": rainfall_7day,
        "historical_flood_count_10yr": historical_flood_count_10yr
    }])

    # Convert numeric columns to float
    numeric_columns = [
        "month",
        "Day",
        "Rainfall",
        "rainfall_3day",
        "rainfall_7day",
        "historical_flood_count_10yr"
    ]

    input_data[numeric_columns] = input_data[numeric_columns].astype(float)

    # Preprocess the input
    input_processed = preprocessor.transform(input_data)

    # HGB requires dense data
    if hasattr(input_processed, "toarray"):
        input_processed = input_processed.toarray()

    # Get flood probability
    probability = model.predict_proba(input_processed)[0][1]

    # Threshold = 0.20
    prediction = 1 if probability >= 0.20 else 0

    # Risk level
    if probability >= 0.50:
        risk = "High Risk"
    elif probability >= 0.20:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return {
        "State": state,
        "District": district,
        "Flood Probability": float(round(probability * 100, 2)),
        "Prediction": "Flood" if prediction == 1 else "No Flood",
        "Risk Level": risk
    }


# Test prediction
if __name__ == "__main__":
    result = predict_flood(
        "andhra pradesh",
        "guntur",
        7,
        15,
        200,
        500,
        800,
        3
    )

    print(result)