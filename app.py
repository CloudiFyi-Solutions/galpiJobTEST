from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def call_azure_api_management(api_url, subscription_key, api_version="1.0"):
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Construct the API endpoint URL
    full_url = f"{api_url}?api-version={api_version}"

    try:
        # Make a GET request (or use requests.post for POST requests)
        response = requests.get(full_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": f"Failed to call API. Status Code: {response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Error making API call: {e}"}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input from the form
        # api_url = request.form.get("api_url")
        # subscription_key = request.form.get("subscription_key")
        api_url = "https://dctestingapim.azure-api.net/conference/speakers"
        subscription_key = "52e0c5ce97c240c29d0d6e9d5ff075d4"

        # Make API call
        api_response = call_azure_api_management(api_url, subscription_key)

        return render_template("index.html", api_response=api_response)

    return render_template("index.html", api_response=None)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=3000)
