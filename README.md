# ☁️ **GCP Virtual Machine Setup — LLMOps StudyBuddy**

In this stage, we deploy our environment to **Google Cloud Platform (GCP)** using a **Compute Engine Virtual Machine (VM)** and install the **Docker Engine**.
This setup provides a reliable cloud-based environment for building, testing, and running the **LLMOps StudyBuddy** system inside containers.

## 🧭 **Step 1 — Launch a GCP VM**

1. Log into or sign up for **Google Cloud Platform**:
   [https://cloud.google.com/](https://cloud.google.com/)
2. Search for **Compute Engine** in the GCP console and go to **VM instances**.
3. Click **+ Create instance**.

### Machine Configuration

Keep all defaults **except** for the *Machine type*.
Change it to:

```
e2-standard-4 (4 vCPU, 2 core, 16 GB memory)
```

under the **Standard** tab.

### OS and Storage

Under **OS and storage**, click **Change** and select the options shown below:

<p align="center">
  <img src="img/vm_setup/change_os.png" alt="Change OS Settings in GCP" width="100%">
</p>

### Networking

Under **Networking → Firewall**, enable:

* Allow HTTP traffic
* Allow HTTPS traffic
* Allow Load Balancer Health Checks

Also ensure **IP forwarding** is switched on.

Click **Create** to launch the instance.

When ready, click **SSH** under *Connect* to open a terminal.

## ⚙️ **Step 2 — Install Docker Engine**

Visit the official Docker documentation:
[https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)

Scroll to **“Install using the apt repository”** and run the commands under **1. Set up Docker’s apt repository**:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker's repository:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

Then scroll to **2. Install the Docker packages** and run only:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify installation:

```bash
sudo docker run hello-world
```

Expected output begins with:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## 🧪 **Step 3 — Enable Docker for Your User**

Visit:
[https://docs.docker.com/engine/install/linux-postinstall/](https://docs.docker.com/engine/install/linux-postinstall/)

Run:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

Then enable Docker on boot:

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

You should see output confirming activation.

## ✅ **Step 4 — Confirm Installation**

Check Docker version:

```bash
docker version
```

Typical output includes both the **Client** and **Server** sections, confirming that Docker Engine is running on your VM.

Your **Docker Engine** is now installed and configured on your **GCP VM**, ready to support deployment of the **LLMOps StudyBuddy** project.