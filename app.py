from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Summary
import requests

app = Flask(__name__)

# Define a Prometheus summary metric for API request duration
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Function to fetch travel advisory data for a given country code
@app.route('/lookup', methods=['POST'])
@REQUEST_TIME.time()
def lookup():
    try:
        data = request.get_json()
        country_code = data.get('countryCode')
        if not country_code:
            return jsonify({"error": "Missing 'countryCode' in the request body"}), 400

        api_url = f"https://www.travel-advisory.info/api?countrycode={country_code}"

        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        advisory_data = response.json()
        return jsonify(advisory_data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error fetching data for {country_code}: {str(e)}"}), 500


# Health check route
@app.route('/health')
def health():
    return "Service is healthy"

# Diagnostics route to check the status of the external API
@app.route('/diag')
def diag():
    external_api_url = "https://www.travel-advisory.info/api"
    
    try:
        response = requests.get(external_api_url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        api_status = response.json()["api_status"]
        return jsonify(api_status)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error checking API status: {str(e)}"}), 500

if __name__ == '__main__':
    # Start Prometheus HTTP server for monitoring on port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
