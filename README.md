# Flask URL Shortener on Kubernetes

A secure, cloud-native URL shortener built with Flask and Redis, containerized with Docker, orchestrated with Kubernetes (Minikube), and integrated with modern DevOps practices including GitOps (Argo CD), security scanning (Trivy), and monitoring (Prometheus + Grafana).

---

## Features

-  Shorten long URLs into 6-character short links
-  Redirect short links to the original URLs
-  RESTful API with clean endpoints
-  Redis-based key-value store
-  Dockerized for portable deployment
-  Kubernetes deployment using Minikube
-  GitHub Actions + Trivy for CI security scanning
-  Ready for GitOps, Helm, and Observability

---

## Tech Stack

- Python 3.10 + Flask
- Redis
- Docker
- Kubernetes (Minikube)
- GitHub Actions
- Argo CD
- Trivy
- Prometheus + Grafana
- Helm

---

 ### Getting Started

## 1. Clone the Repository
```
git clone https://github.com/HackHunter8/flask-url-shortener.git
cd flask-url-shortener 
```

## 2. Run Locally (for testing)
```
pip install -r requirements.txt
python app.py
```

## 3. Dockerize and Push
```
docker build -t <your-dockerhub-username>/flask-url-shortener:latest .
docker push <your-dockerhub-username>/flask-url-shortener:latest
```

## 4. Deploy to Kubernetes (Minikube)
```
minikube start
kubectl create namespace url-shortener
kubectl apply -f k8s/redis-deployment.yaml -n url-shortener
kubectl apply -f k8s/web-deployment.yaml -n url-shortener
minikube service flask-service -n url-shortener
```

**CI/CD and Security Scanning**

GitHub Actions runs on push to main, using:
Docker logi
Buildx
Trivy vulnerability scanner
Docker push to Docker Hub

Secrets used:
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN

- Trivy scan blocks CI pipeline on critical vulnerabilities.


### Dev Log: Hurdles & Solutions

Docker Build + GitHub Actions
Issue: GitHub blocked push due to hardcoded secrets in ci.yml
Fix: Replaced credentials with GitHub Secrets (DOCKERHUB_USERNAME, DOCKERHUB_TOKEN)

Minikube 404 Error
Issue: Not Found when visiting minikube service URL
Fix: Minikube was stopped. Restarted it using minikube start, then re-applied deployments.

Git Filter Repo Error
Issue: git filter-repo command deleted all files unintentionally
Fix: Deleted local repo, re-cloned from GitHub, and recommitted clean version with safe secrets

Secret Scanning Blocks on GitHub
Issue: GitHub Push Protection blocked Docker token from being committed
Fix: Used secret references in workflow (${{ secrets.DOCKERHUB_TOKEN }}) instead of hardcoding values.


### Next Milestones
 GitHub Actions CI with Trivy
 Add Prometheus + Grafana for monitoring
 Create Helm chart
 Install Argo CD and enable GitOps

# Author
David Martins aka HackHunter8

# License
MIT License.





<img width="1440" alt="Screenshot 2025-05-24 at 4 03 29 pm" src="https://github.com/user-attachments/assets/3159bed0-5e26-4adc-981f-849f09469f78" />


<img width="1440" alt="Screenshot 2025-05-24 at 10 41 09 am" src="https://github.com/user-attachments/assets/87bca163-27cd-4e6e-a84b-a08320ab8997" />

<img width="1440" alt="Screenshot 2025-05-24 at 10 43 43 am" src="https://github.com/user-attachments/assets/d072ee56-8fcd-48f7-9ff2-e8659639ed93" />


<img width="1440" alt="Screenshot 2025-05-25 at 3 15 01 pm" src="https://github.com/user-attachments/assets/df9e0300-f955-4722-a68e-0dc6356a95c6" />

<img width="1440" alt="Screenshot 2025-05-24 at 1 12 47 pm" src="https://github.com/user-attachments/assets/951dcf5f-3af4-4a02-9da1-f4054589bc69" />


<img width="1440" alt="Screenshot 2025-05-25 at 3 02 37 pm" src="https://github.com/user-attachments/assets/36711149-6261-4ecd-84ce-9a57b8aeca5d" />

<img width="1440" alt="Screenshot 2025-05-24 at 10 19 12 am" src="https://github.com/user-attachments/assets/16b1b686-53b3-4c91-9e3f-3241180a6ff5" />







