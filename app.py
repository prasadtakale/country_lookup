from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Summary, Counter, generate_latest, REGISTRY
import requests

app = Flask(__name__)

# Define a Prometheus summary metric for API request duration
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Define a Prometheus counter metric for API requests
API_REQUESTS = Counter('api_requests_total', 'Total API requests')

# Function to fetch travel advisory data for a given country code
@app.route('/lookup', methods=['POST'])
@REQUEST_TIME.time()
def lookup():
    try:
        data = request.get_json()
        country_code = data.get('countryCode')
        if not country_code:
            return jsonify({"error": "Missing 'countryCode' in the request body"}), 400

        print
        country_codes = country_code.split(',')
        results = {}
        for country_code in country_codes:
            api_url = f"https://www.travel-advisory.info/api?countrycode={country_code.strip()}"
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            advisory_data = response.json()
            results[country_code] = advisory_data

        return jsonify(results)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error fetching data for {country_code}: {str(e)}"}), 500

# Prometheus metrics endpoint
@app.route('/metrics')
def metrics():
    return generate_latest()

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

