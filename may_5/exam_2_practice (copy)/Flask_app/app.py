from flask import Flask
import requests

app = Flask(__name__)

## 8000
@app.route("/sum/<int:number_1>/<int:number_2>/")
def main(number_1: int, number_2: int):
    url = f'http://0.0.0.0:8000/add/{number_1}/{number_2}/'  # Replace with your API endpoint URL
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()  # Convert the response to JSON
        return f"the is = {data}"  # Return the response data as the API response
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
    return {"sum is": url}

# @app.route('/api/')
# def get_api():
#     url = 'http://0.0.0.0:8000/add/4/4/'  # Replace with your API endpoint URL
#     return url
    
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception if the request was unsuccessful
#         data = response.json()  # Convert the response to JSON
#         return data  # Return the response data as the API response
#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
