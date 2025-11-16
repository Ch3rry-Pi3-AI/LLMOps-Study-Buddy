# 🐳 **Containerisation & Kubernetes Deployment — LLMOps StudyBuddy**

This branch introduces the **Docker containerisation layer** and **Kubernetes deployment configuration** for the LLMOps StudyBuddy project.

With these additions, the StudyBuddy Streamlit application can now be:

* Packaged into a reproducible Docker image
* Deployed on any Kubernetes cluster
* Exposed externally via a NodePort service
* Configured securely using Kubernetes Secrets

This marks the beginning of StudyBuddy’s production-ready infrastructure.

# 🐳 **Dockerfile**

A new `Dockerfile` has been added at the project root.
It defines a minimal, efficient Python 3.12 Streamlit image with:

* Clean environment setup
* System dependencies
* Editable install of the StudyBuddy package
* Proper port exposure (`8501`)
* A launch command for Streamlit

This enables portable, reproducible deployments of the StudyBuddy application.

# ☸️ **Kubernetes Manifests**

Inside the `manifests/` directory, two new files define the Kubernetes deployment workflow:

* `deployment.yaml` — defines replicas, container configuration, ports, and secret-based environment variables
* `service.yaml` — exposes the StudyBuddy app externally via NodePort

Together, these manifests allow you to run StudyBuddy on Minikube, KIND, GKE, AKS, or EKS.

# 🗂️ **Updated Project Structure**

Only the **new files** added in this branch are annotated below:

```text
LLMOPS-STUDY-BUDDY/
├── Dockerfile                         # 🐳 Container definition for StudyBuddy
├── manifests/
│   ├── deployment.yaml                # ☸️ Kubernetes Deployment for running the app
│   └── service.yaml                   # 🌐 NodePort Service exposing Streamlit
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── app.py
├── img/
│   └── streamlit/
│       ├── streamlit_app1.gif
│       └── streamlit_app2.gif
├── llmops_study_buddy.egg-info/
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── src/
    ├── common/
    ├── config/
    ├── models/
    ├── prompts/
    ├── llm/
    ├── generator/
    └── utils/
```

# 🚀 **How to Build and Run the Docker Image**

Build the image:

```bash
docker build -t studybuddy:latest .
```

Run the container:

```bash
docker run -p 8501:8501 studybuddy:latest
```

Then open:

```
http://localhost:8501
```

# ☸️ **How to Deploy StudyBuddy to Kubernetes**

Apply both manifests:

```bash
kubectl apply -f manifests/
```

Check pods and services:

```bash
kubectl get pods
kubectl get svc
```

On Minikube, open the app:

```bash
minikube service llmops-service
```

# 🔐 **Required Kubernetes Secret**

Your Deployment expects this secret:

```bash
kubectl create secret generic groq-api-secret \
  --from-literal=GROQ_API_KEY="YOUR_API_KEY_HERE"
```

# ✅ **In Summary**

This branch:

* Adds a production-ready **Dockerfile**
* Introduces complete **Kubernetes manifests**
* Enables cluster-ready deployment of StudyBuddy
* Provides external access through a NodePort service
* Lays the infrastructure foundation for scaling, CI/CD, and cloud deployments
