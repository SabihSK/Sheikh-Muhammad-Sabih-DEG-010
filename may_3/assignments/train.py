import fire
import mlflow
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.model_selection import train_test_split

def setup_knn_pipeline(k):
    knn = KNeighborsClassifier(n_neighbors=k)
    pipe = make_pipeline(StandardScaler(), knn)
    return pipe


def track_with_mlflow(model, X_test, Y_test, mlflow, model_metadata):
    mlflow.log_params(model_metadata)
    mlflow.log_metric("accuracy", model.score(X_test, Y_test))
    mlflow.sklearn.log_model(model, "knn", registered_model_name="sklearn_knn")

def main():
    df = datasets.load_wine()
    print(df)
    X_train, X_test, Y_train, Y_test = train_test_split(df.data, df.target, test_size=0.2)
    k_list = range(1, 10)
    for k in k_list:
        with mlflow.start_run():
            knn_pipe = setup_knn_pipeline(k)
            knn_pipe.fit(X_train, Y_train)
            model_metadata = {"k": k}
            track_with_mlflow(knn_pipe, X_test, Y_test, mlflow, model_metadata)

if __name__ == "__main__":
    fire.Fire(main)
