import mlflow
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train(data_path, k):
    # Load Wine dataset
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train KNN model
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Evaluate the model
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Log parameters, metrics, and model
    mlflow.log_param("k_neighbors", k)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(knn, "model")

if __name__ == "__main__":
    # Parse command-line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default="data/wine.csv")
    parser.add_argument("--k", type=int, default=3)
    args = parser.parse_args()

    # Start MLflow run
    with mlflow.start_run():
        train(args.data_path, args.k)
