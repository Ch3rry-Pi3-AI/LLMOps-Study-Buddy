# 🔗 **GitHub Integration and Firewall Configuration — LLMOps StudyBuddy**

In this stage, we connect the **LLMOps StudyBuddy** GitHub repository to the **Google Cloud Platform (GCP) Virtual Machine**, allowing direct version-control operations from the VM.
We also configure a **firewall rule** to ensure the VM can communicate securely with GitHub and external services.

## 🧭 Step 1 — Clone the GitHub Repository

Go to your project’s GitHub repository.
Click the green **“<> Code”** dropdown and copy the **HTTPS URL** of the repository.

Example:

```
https://github.com/Ch3rry-Pi3-AI/LLMOps-StudyBuddy.git
```

In your GCP VM terminal, run:

```bash
git clone https://github.com/Ch3rry-Pi3-AI/LLMOps-StudyBuddy.git
```

(Replace the URL above with your actual repository link.)

Navigate into the cloned directory:

```bash
cd LLMOps-StudyBuddy
```

You are now inside your project folder on the VM.

## ⚙️ Step 2 — Configure Git Identity

Set your Git identity so commits made from the VM are correctly attributed to you:

```bash
git config --global user.email "the_rfc@hotmai.co.uk"
git config --global user.name "Roger J. Campbell"
```

Verify the configuration:

```bash
git config --list
```

You should see your email and username listed.

## 🔑 Step 3 — Generate a GitHub Personal Access Token

1. Go to **GitHub → Settings**

2. Scroll to **Developer Settings**

3. Click **Personal access tokens → Tokens (classic)**

4. Select **Generate new token (classic)**

5. Name it something like `studybuddy-ci`

6. Select the following scopes:

   * `repo`
   * `workflow`
   * `admin:org`
   * `admin:public_key`
   * `admin:repo_hook`
   * `admin:org_hook`

7. Click **Generate token**

⚠️ Copy the token immediately — GitHub will not show it again.

## 🚀 Step 4 — Authenticate and Pull from GitHub

Use your token when pulling or pushing from the VM.

```bash
git pull origin main
```

When prompted:

* **Username:** your GitHub username
* **Password:** your personal access token

You are now authenticated.

## 🔥 Step 5 — Create a GCP Firewall Rule

Next, configure a firewall rule to ensure your VM can communicate externally (e.g., GitHub, Docker Hub, package registries).

1. In the **Google Cloud Console**, search for **Network Security**
2. Under **Cloud NGFW**, click **Firewall rule → + Create firewall policy**
3. Set the **Policy name** to:

```
allow-studybuddy
```

4. Configure:

| Field               | Setting                      |
| ------------------- | ---------------------------- |
| Targets             | All instances in the network |
| Source IPv4 ranges  | `0.0.0.0/0`                  |
| Protocols and ports | Allow all                    |

5. Click **Create**

Your firewall policy now allows full outbound communication between your VM and GitHub.

## ✅ In Summary

You have now successfully:

* Cloned the **LLMOps StudyBuddy** repository onto your GCP VM
* Configured Git identity for version control
* Created a GitHub personal access token for secure authentication
* Set up a GCP firewall rule allowing full outbound communication

Your VM is now fully connected to GitHub and ready for Docker builds, Kubernetes deployment, CI/CD, and further development of the StudyBuddy system.
