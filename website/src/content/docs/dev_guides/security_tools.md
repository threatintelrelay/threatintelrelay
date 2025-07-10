---
title: Dev Security Tools
description: Secure development tools for the Threat Intel Relay project.
---

## Introduction

Security is a core part of how we build, ship, and operate software. This section outlines the security controls and best practices integrated into our development workflow. These measures help us catch issues early, protect our users and data, and streamline our path to production.

You’ll find details on secure coding, dependency management, secrets detection, container and supply chain security, and more. Most controls are automated or enforced in CI/CD—others are best practices to keep in mind as you work. Security is a shared responsibility. With these controls, we make it easy for everyone to contribute to a secure product without slowing down development.

If you have questions or spot an opportunity for improvement, your feedback is always welcome!

---

## Security Controls & Tools Overview

| Area                        | Technology / Tool         | What It Does                                    |
|-----------------------------|--------------------------|-------------------------------------------------|
| **Static Code Analysis**    | Bandit                   | Detects code-level security bugs and bad patterns  |
| **Secrets Scanning**        | git-secrets, TruffleHog, Gitleaks | Prevents sensitive secrets in code/repos   |
| **Dependency Scanning**     | Dependabot               | Finds vulnerabilities in 3rd-party libraries     |
| **Container Image Scanning**| Trivy, Grype, Clair      | Finds OS/app vuln in Docker images               |
| **SBOM Generation**         | Syft                     | Produces a Software Bill of Materials for images |
| **Artifact Signing**        | Cosign                   | Signs images and SBOMs to prevent tampering      |
| **Policy Enforcement**      | Kyverno                  | Blocks unsigned or non-compliant images in K8s   |
| **Runtime Threat Detection**| Falco, kube-bench        | Alerts on suspicious behavior or misconfigs      |
| **Infra as Code Security**  | Checkov, kube-score      | Scans YAML/Helm/Terraform for misconfigurations  |

---

## Details & Developer Guidance

## 1. Static Code Analysis

### **Bandit**

- **What is it?**  
  Bandit is a static analysis tool that inspects Python code for common security issues and coding mistakes.

- **Why do we use it?**  
  To catch potential security flaws in Python code before they make it to production.

- **How to work with it:**  
  - Bandit runs automatically in CI for all pushes and PRs.
  - You can run it locally:
    ```sh
    pip install -r src/test-requirements.txt # from the root directory
    bandit -c src/api/bandit.yaml -r src/api # run bandit on FastAPI code
    bandit -c src/pipelines/bandit.yaml -r src/pipelines # run bandit on Airflow code
    ```
  - Review Bandit output, fix flagged issues, and re-run as needed.
  - bandit.yaml files are included in the two python apps to denote files/directories that bandit should not check. (e.g. tests) There are only a few good reasons to add to this, if you need to do so, please include detailed explaination in your PR.

---

### **Semgrep**

- **What is it?**  
  Semgrep is a fast, open-source static analysis tool that supports many languages (including Python, YAML, and configs).

- **Why do we use it?**  
  To detect insecure coding patterns, misconfigurations, and enforce custom rules.

- **How to work with it:**  
  - Semgrep runs in CI on PRs.
  - You can use it locally:
    ```sh
    semgrep --config=auto .
    ```
  - Address any issues in your PR before merging.

---

## 2. Secrets Scanning

### **git-secrets**

- **What is it?**  
  git-secrets prevents you from committing passwords, API keys, or other sensitive information to git repositories.

- **Why do we use it?**  
  To block accidental exposure of secrets and credentials in our codebase.

- **How to work with it:**  
  - Install locally:
    ```sh
    git secrets --install
    ```
  - CI will reject commits with secrets. If you see an error, remove the offending secret before pushing.

---

### **TruffleHog**

- **What is it?**  
  TruffleHog scans git repositories for secrets, high-entropy strings, and credentials.

- **Why do we use it?**  
  To detect secrets that may already exist in version history.

- **How to work with it:**  
  - TruffleHog runs as a periodic scan in CI.
  - If notified about a secret, follow incident response steps (rotate the secret, scrub git history if needed).

---

### **Gitleaks**

- **What is it?**  
  Gitleaks is a fast, flexible tool for detecting hardcoded secrets in git repos.

- **Why do we use it?**  
  For ongoing scanning to ensure secrets don’t get committed in the future.

- **How to work with it:**  
  - Gitleaks runs in CI on every PR.
  - Resolve any flagged issues before merge.

---

## 3. Dependency Scanning

### **Dependabot**

- **What is it?**  
  Dependabot automatically scans our dependencies and opens pull requests to update insecure packages.

- **Why do we use it?**  
  To stay ahead of known vulnerabilities in third-party libraries.

- **How to work with it:**  
  - Watch for PRs from Dependabot.
  - Review, test, and merge PRs to stay secure.

---

## 4. Container Image Scanning

### **Trivy**

- **What is it?**  
  Trivy scans Docker images for vulnerabilities in OS packages, language dependencies, and app configs.

- **Why do we use it?**  
  To catch vulnerabilities in our container images before they’re deployed.

- **How to work with it:**  
  - Trivy runs automatically in CI.
  - Run locally:
    ```sh
    trivy image <your_image>:<tag>
    ```
  - Address any critical findings before pushing images.

---

### **Grype**

- **What is it?**  
  Grype is a vulnerability scanner for container images and filesystems.

- **Why do we use it?**  
  For comprehensive and fast scanning of images as part of our build process.

- **How to work with it:**  
  - Grype runs as part of CI.
  - You can scan locally:
    ```sh
    grype <your_image>:<tag>
    ```
  - Review and remediate flagged vulnerabilities.

---

### **Clair**

- **What is it?**  
  Clair analyzes container images for known vulnerabilities and integrates with container registries.

- **Why do we use it?**  
  To ensure ongoing scanning of images after they’re pushed to the registry.

- **How to work with it:**  
  - No manual steps needed; alerts are sent if issues are found in registry images.

---

## 5. Software Bill of Materials (SBOM)

### **Syft**

- **What is it?**  
  Syft generates a Software Bill of Materials (SBOM) for containers and code projects.

- **Why do we use it?**  
  For transparency and compliance—so we always know what’s inside our images and can quickly assess exposure to new vulnerabilities.

- **How to work with it:**  
  - Syft runs in CI for every built image.
  - To use locally:
    ```sh
    syft <your_image>:<tag> -o cyclonedx-json > sbom.json
    ```
  - SBOM files are attached as build artifacts.

---

## 6. Artifact Signing

### **Cosign**

- **What is it?**  
  Cosign is a tool for signing and verifying container images and other artifacts using digital signatures.

- **Why do we use it?**  
  To ensure only trusted, unaltered images and artifacts are deployed to our environments.

- **How to work with it:**  
  - Cosign signs images and SBOMs as part of CI/CD.
  - You can verify signatures:
    ```sh
    cosign verify <your_image>:<tag>
    ```
  - Unsigned images are blocked from deployment by policy.

---

## 7. Kubernetes Policy Enforcement

### **Kyverno**

- **What is it?**  
  Kyverno is a Kubernetes-native policy engine for enforcing security, compliance, and best practices.

- **Why do we use it?**  
  To automate checks on resources in the cluster—blocking non-compliant, unsigned, or misconfigured workloads.

- **How to work with it:**  
  - Kyverno policies are maintained by the DevOps/security team.
  - You’ll receive feedback if your deployment violates a policy.
  - Review and adjust your manifests as guided by Kyverno feedback.

---

## 8. Runtime Threat Detection

### **Falco**

- **What is it?**  
  Falco is a runtime security tool that monitors system calls and detects suspicious behavior in containers and Kubernetes.

- **Why do we use it?**  
  For early warning on potential attacks or anomalous activity in production.

- **How to work with it:**  
  - No manual steps—Falco runs in the background.
  - Security/DevOps team will notify if investigation/action is needed.

---

### **kube-bench**

- **What is it?**  
  kube-bench checks if Kubernetes clusters meet the CIS security benchmarks.

- **Why do we use it?**  
  To validate that our cluster configuration follows industry security best practices.

- **How to work with it:**  
  - Periodic scans are run by the ops team.
  - If notified, follow up on configuration changes as recommended.

---

## 9. Infrastructure as Code Security

### **Checkov**

- **What is it?**  
  Checkov scans infrastructure-as-code files (Terraform, Kubernetes manifests, Helm charts) for misconfigurations and security issues.

- **Why do we use it?**  
  To catch mistakes in infrastructure code before they are deployed.

- **How to work with it:**  
  - Runs as part of CI for relevant code.
  - You can run locally:
    ```sh
    checkov -d .
    ```
  - Address any failed checks before merging.

---

### **kube-score**

- **What is it?**  
  kube-score analyzes Kubernetes object definitions for best practices and security.

- **Why do we use it?**  
  For fast, actionable feedback on Kubernetes manifest quality.

- **How to work with it:**  
  - Run locally before submitting manifests:
    ```sh
    kube-score score <file.yaml>
    ```
  - Fix reported issues for better reliability and security.

---

## Questions or Feedback?

Security is a team sport! If you notice something missing or have suggestions to improve these controls, reach out to the security or DevOps team.