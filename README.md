Certainly! Below is a sample README file (`README.md`) for your application. You can adapt and use it as a template for your project's README file:

---

# Country Code Lookup Service

The Country Code Lookup Service is a simple CLI tool and RESTful API for quickly looking up country codes to expedite the processing of expense reports. It leverages data from an external API and provides functionality to retrieve country names based on country codes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
  - [CLI Usage](#cli-usage)
  - [REST API Usage](#rest-api-usage)
- [Docker Container](#docker-container)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [License](#license)

## Features

- Look up country names based on country codes.
- Retrieve information about the health and status of the external API.
- Convert country names to country codes.
- Docker containerization for easy deployment.
- Kubernetes support for scaling and management.

## Installation

### Requirements

Before you begin, ensure you have the following prerequisites:

- Python 3.x
- pip (Python package manager)
- Docker (for containerization)
- kubectl (for Kubernetes deployment)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-url/country-code-lookup.git
   ```

2. Navigate to the project directory:

   ```bash
   cd country-code-lookup
   ```

3. Install the required Python packages using `pip` and the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### CLI Usage

You can use the CLI tool to look up country names, check the health of the service, and perform diagnostics.

To look up a country name by country code (e.g., 'AU'):

```bash
python country_lookup.py lookup --countryCode=AU
```

To check the health of the service:

```bash
python country_lookup.py health
```

To perform diagnostics on the external API:

```bash
python country_lookup.py diag
```

### REST API Usage

The service provides a RESTful API for country code lookup. You can use HTTP requests to interact with the service.

- To look up a country name by country code, make a POST request to `http://<service-url>/lookup` with a JSON payload containing the `countryCode`:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"countryCode":"AU"}' http://<service-url>/lookup
  ```

- To check the health of the service, make a GET request to `http://<service-url>/health`:

  ```bash
  curl http://<service-url>/health
  ```

- To perform diagnostics on the external API, make a GET request to `http://<service-url>/diag`:

  ```bash
  curl http://<service-url>/diag
  ```

## Docker Container

You can run the service in a Docker container. To build the Docker image, use the following command:

```bash
docker build -t country-code-lookup:latest .
```

To run the container:

```bash
docker run -p 5000:5000 country-code-lookup:latest
```

## Kubernetes Deployment

To deploy the service to a local Kubernetes cluster, follow these steps:

1. Create a local Kubernetes cluster on your workstation using tools like Minikube or Docker Desktop.

2. Deploy the service to the cluster:

   ```bash
   kubectl apply -f deployment.yaml
   ```

3. Expose the service as a NodePort or LoadBalancer service depending on your setup.

## Monitoring

Prometheus metrics are exposed at `http://<service-url>/metrics`. You can configure Prometheus to scrape these metrics for monitoring.

## Contributing

Contributions to this project are welcome. To contribute, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---

Please replace `<service-url>` with the actual URL where your service is running. Customize the README file further to provide specific information about your application and setup.