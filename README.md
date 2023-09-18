# msd-assignment
msd-assignment based on kubernates

### Updated `README.md`:

```markdown
# msd-assignment

This repository contains a microservice that fetches the current price of Bitcoin in EUR and CZK. The microservice is containerized using Docker and can be deployed to a Kubernetes cluster using Helm.

## Microservice

The microservice is written in Python using the Flask framework. It fetches the Bitcoin price from the provided CoinDesk URLs and returns the data in a JSON format.

### Running the Microservice Locally

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the microservice:
   ```bash
   python app.py
   ```

3. Access the service at `http://localhost:5000/btc-price`.

## Docker

A `Dockerfile` is provided to containerize the microservice.

### Building the Docker Image

```bash
docker build -t your_dockerhub_username/btc-price-service .
```

### Running the Docker Container

```bash
docker run -p 5000:5000 your_dockerhub_username/btc-price-service
```

## Kubernetes Deployment using Helm

A Helm chart named `btc-price-service` is provided for deploying the microservice to a Kubernetes cluster.

### Deploying the Microservice

1. Build and push the Docker image to Docker Hub (as mentioned above).

2. Install the Helm chart:
   ```bash
   helm install btc-price-service ./btc-price-service
   ```

3. Access the service using `curl` or a browser:
   ```bash
   curl http://<SERVICE_IP>/btc-price
   ```

Replace `<SERVICE_IP>` with the IP address of the btc-price-service.

## License

This project is open-source and available under the MIT License.

```

You can replace the existing content of your `README.md` with the content provided above. This will give a comprehensive overview of the microservice, its containerization, and deployment instructions.

Once you've updated the `README.md`, commit and push the changes to your GitHub repository. This will ensure that anyone accessing your repository will have a clear understanding of how to run and deploy the microservice.