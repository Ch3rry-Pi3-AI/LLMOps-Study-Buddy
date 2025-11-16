# ⚙️ **Jenkins Setup on GCP VM using Docker-in-Docker (DinD) — LLMOps StudyBuddy**

In this stage, you will set up **Jenkins** on your **Google Cloud Platform (GCP) Virtual Machine** using a **Docker-in-Docker (DinD)** configuration.
This allows Jenkins to run inside a Docker container while still being able to interact with the host Docker daemon.
The result is a CI/CD engine capable of building images, pushing to registries, and orchestrating Kubernetes deployments for the **LLMOps StudyBuddy** project.

## 🧩 1️⃣ Ensure Jenkins Runs on the Same Network as Minikube

Run this inside your **GCP VM terminal**:

```bash
docker run -d --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(which docker):/usr/bin/docker \
  -u root \
  -e DOCKER_GID=$(getent group docker | cut -d: -f3) \
  --network minikube \
  jenkins/jenkins:lts
```

Verify containers:

```bash
docker ps
```

## 🧠 2️⃣ Retrieve the Jenkins Admin Password

```bash
docker logs jenkins
```

Look for a message containing a long auto-generated password such as:

```
bf98ea15f0664d158749e387bdd48970
```

Copy it.

## 🌐 3️⃣ Access Jenkins in Your Browser

1. Go to **VM Instances** in GCP
2. Copy your VM’s **External IP**
3. Open:

```
http://<YOUR_VM_EXTERNAL_IP>:8080
```

<p align="center">
  <img src="img/jenkins/admin_login.png" alt="Jenkins Admin Login" width="100%">
</p>

## 🧩 4️⃣ Install Plugins and Create Admin User

### Install Suggested Plugins

<p align="center">
  <img src="img/jenkins/install_plugins.png" alt="Jenkins Install Plugins" width="100%">
</p>

### Create Admin User

<p align="center">
  <img src="img/jenkins/create_admin_user.png" alt="Create Admin User" width="100%">
</p>

You will then see the dashboard:

<p align="center">
  <img src="img/jenkins/jenkins_dashboard.png" alt="Jenkins Dashboard" width="100%">
</p>

## 🔧 5️⃣ Install Required Jenkins Plugins

From Jenkins:

1. Manage Jenkins
2. Plugins
3. Available Plugins

Install:

* Docker
* Docker Pipeline

<p align="center">
  <img src="img/jenkins/install_docker_plugins.png" alt="Install Docker Plugins" width="100%">
</p>

Then install:

* Kubernetes

<p align="center">
  <img src="img/jenkins/install_kubernetes_plugin.png" alt="Install Kubernetes Plugin" width="100%">
</p>

## 🔁 6️⃣ Restart Jenkins

```bash
docker restart jenkins
```

## 🧱 7️⃣ Set Up Python Inside the Jenkins Container

Enter the container:

```bash
docker exec -it jenkins bash
```

Install Python 3 and tooling:

```bash
apt update -y
apt install -y python3
ln -s /usr/bin/python3 /usr/bin/python
apt install -y python3-pip
apt install -y python3-venv
exit
```

Restart Jenkins:

```bash
docker restart jenkins
```

## 🔐 8️⃣ Add GitHub Credentials in Jenkins

1. Manage Jenkins → **Credentials**
2. Open the **(global)** store

<p align="center">
  <img src="img/jenkins/add_credential.png" alt="Add Credential" width="100%">
</p>

3. Add credentials:

* Username: your GitHub username
* Password: your GitHub personal access token
* ID: `github-token`

<p align="center">
  <img src="img/jenkins/new_credential.png" alt="New GitHub Credential" width="100%">
</p>

Click **Create**.

## 🚀 9️⃣ Create a New Jenkins Pipeline

1. From the dashboard, choose **+ New Item**
2. Name it:

```
GITOPS PROJECT
```

3. Select **Pipeline** and click **OK**

<p align="center">
  <img src="img/jenkins/new_item.png" alt="New Pipeline Item" width="100%">
</p>

## 🧠 1️⃣0️⃣ Configure the Pipeline to Use GitHub

1. Scroll to the **Pipeline** section
2. Select **Pipeline script from SCM**
3. Set **SCM = Git**
4. Paste the GitHub repo URL
5. Select credentials: `github-token`
6. Change branch:

```
*/main
```

<p align="center">
  <img src="img/jenkins/item_config.png" alt="SCM Config" width="100%">
</p>

Click **Apply**, then **Save**.

## 🧩 1️⃣1️⃣ Generate a Jenkins Pipeline Script

1. On the pipeline page, click **Pipeline Syntax**
2. Select:

```
checkout: Check out from version control
```

3. Enter your repo URL, credentials, and branch
4. Click **Generate Pipeline Script**
5. Copy the generated Groovy snippet (for later in Jenkinsfile)


