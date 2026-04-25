# 🔐 Doctolab - AWS Cloud Security Architecture

![Doctolab Architecture](architecture/4.png)

> Defense-in-depth architecture for a healthcare application handling 
sensitive data (PII).  
> Built to demonstrate **protection, detection, centralization and 
automated response** in AWS.

---

## 📌 Overview

**Doctolab** is a cloud security project simulating a medical application 
managing sensitive patient data (RGPD context).

The goal is to design a secure AWS architecture capable of:

- Protecting critical resources
- Detecting sensitive data exposure
- Centralizing security findings
- Triggering automated, human-readable alerts

---

## ⚡ Quick Highlights

- 🔐 Defense-in-depth AWS architecture  
- 🧠 Sensitive data detection with **Amazon Macie**  
- 📊 Centralized security posture with **Security Hub (SOC vision)**  
- ⚙️ Automated alerting pipeline (**EventBridge → Lambda → SNS**)  
- 🛡️ Web protection with **AWS WAF** (SQLi, XSS blocked)  
- ☁️ Infrastructure deployed using **CloudFormation (IaC)**  

---

## 🏗️ Architecture

- **CloudFront + AWS WAF** → Edge protection against web attacks (SQLi, 
XSS, brute force)  
- **VPC (public/private subnets)** → Network segmentation  
- **Bastion Host** → Secure administrative access (SSH restricted IP)  
- **EC2 (private)** → Application layer  
- **RDS PostgreSQL (private)** → Database (no internet exposure)  
- **S3 (private)** → Storage of sensitive documents  
- **NAT Gateway** → Outbound-only internet access  
- **VPC Gateway Endpoint (S3)** → Private communication without internet  

---

## 🔐 Security Approach

This project implements a **defense-in-depth strategy**:

- Web protection → WAF filtering malicious traffic  
- Network isolation → VPC, subnets, Security Groups, NACL  
- Data protection → S3 + RDS (no public exposure)  
- Detection → Amazon Macie  
- Centralization → AWS Security Hub  
- Automation → EventBridge + Lambda + SNS  

---

## 🚨 Detection & Alerting Pipeline

1. Sensitive data uploaded to S3  
2. **Amazon Macie** detects sensitive content  
3. Event sent to **EventBridge**  
4. **Lambda** processes and formats the alert  
5. **SNS** sends a human-readable notification  

👉 Result:  
From a silent data exposure → to a **real-time actionable alert**

---

## 🛡️ Security Validation

Simulated attacks:

- ❌ SQL Injection → blocked by AWS WAF  
- ❌ XSS → blocked by AWS WAF  

👉 Attacks are filtered **before reaching the application**

---

## ⚡ Results

- ✅ Automated detection of sensitive data  
- ✅ Reduced incident response time (**MTTR**)  
- ✅ Centralized security visibility  
- ✅ Real-time alerting  
- ✅ Reduced risk of undetected data exposure  

---

## 💼 Business Value

- 🔐 Reduced risk of sensitive data leakage (RGPD compliance)  
- ⚡ Faster incident detection and response  
- 👁️ Improved visibility of security posture  
- 🤖 Shift from reactive to proactive security  

---

## 🚀 Infrastructure as Code

The entire infrastructure is deployed using **AWS CloudFormation**.

- Reproducible deployment  
- Reduced manual errors  
- Structured and scalable architecture  

---

## 🚀 How to Deploy (Example)

```bash
aws cloudformation deploy \
  --template-file cloudformation/network.yaml \
  --stack-name doctolab-network
