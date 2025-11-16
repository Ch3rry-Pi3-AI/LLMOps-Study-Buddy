# 🧩 **Kubernetes Manifests — LLMOps StudyBuddy**

The `manifests/` folder contains the Kubernetes configuration files required to deploy the **StudyBuddy Streamlit application** to a Kubernetes cluster.

These manifests provide:

* A **Deployment** for running the StudyBuddy application
* A **Service** for exposing the app externally
* Support for securely loading environment variables through **Kubernetes Secrets**

This setup enables StudyBuddy to run on environments such as Minikube, KIND, AKS, GKE, and EKS.

## 📁 Folder Overview

```text
manifests/
├── deployment.yaml   # 🟦 Defines replicas, containers, and environment setup
└── service.yaml      # 🌐 Exposes the application via NodePort
```

# 🟦 `deployment.yaml` — Application Deployment

The Deployment configuration:

* Runs the StudyBuddy container image (`ch3rrypi3/studybuddy:<tag>`)
* Ensures two running replicas for resilience
* Exposes the container’s internal Streamlit port (`8501`)
* Loads the Groq API key from a Kubernetes Secret called `groq-api-secret`

Pods created here are labelled `app: llmops-app`, which the Service uses to route traffic.

# 🌐 `service.yaml` — External Access

The Service provides external access to the application using **NodePort**.

Traffic flow:

```
Client → NodePort → Port 80 (Service) → Port 8501 (container)
```

When using Minikube, you can automatically open the application in your browser via:

```bash
minikube service llmops-service
```

# 🚀 How to Deploy StudyBuddy to Kubernetes

From the root of the project:

```bash
kubectl apply -f manifests/
```

Check the deployment status:

```bash
kubectl get pods
kubectl get deployments
kubectl get svc
```

Once the Service is ready, the StudyBuddy UI will be available through the assigned NodePort.

# 🔐 Environment Variables (Important)

The Deployment expects a secret named:

```
groq-api-secret
```

containing:

```
GROQ_API_KEY
```

Create it using:

```bash
kubectl create secret generic groq-api-secret \
  --from-literal=GROQ_API_KEY="YOUR_API_KEY_HERE"
```

# ✅ Summary

The `manifests/` folder includes the Kubernetes resources needed to deploy and expose the StudyBuddy application. It provides:

* A scalable Deployment
* A Service for external access
* Secure secret handling
* A clean foundation for future components like autoscaling, ingress routing, or Helm charts
