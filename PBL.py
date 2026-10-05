import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def student_performance_prediction(df):

    # Features
    X = df[[
        "Python",
        "DBMS",
        "CN",
        "Maths",
        "OS",
        "Attendance"
    ]]

    # Target
    y = df["Result"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Random Forest Model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Accuracy
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = accuracy_score(y_test, y_pred)

    print("Random Forest Train Accuracy:", train_accuracy)
    print("Random Forest Test Accuracy:", test_accuracy)

    return model


if __name__ == "__main__":

    data = pd.read_csv("Student_Performance.csv")
    student_performance_prediction(data)
