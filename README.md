# 🧙‍♂️ Nous Hermes VPS Agent Setup (Ron Weasley SRE)

This repository contains all the configuration files, security policies, and simulation scripts used in the video tutorial on setting up **Nous Hermes** as an autonomous SRE agent on a Linux VPS.

---

## 📁 Repository Structure

*   `config.yaml` — Configured to run direct Gemini API (fast, low-cost token execution).
*   `SOUL.md` — The custom system prompt shaping the agent's personality as **Ron Weasley (Muggle IT Specialist)**.
*   `env.example` — A template for your API keys and secure Telegram allowed-user restrictions.
*   `sudoers.d_template` — The security policy granting passwordless `systemctl restart` access for your daemon.
*   `inject_error.py` — Script to simulate a live Django NameError typo (500 Error).
*   `restore_code.py` — Script to instantly recover from the simulated error.

---

## 🚀 Simplified 3-Step VPS Installation Guide

### 1. Install Hermes Agent
Run the official Nous Hermes installer in non-interactive mode:
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --non-interactive --skip-setup
```

### 2. Download this Repository
Clone the repository templates to a temporary folder:
```bash
git clone https://github.com/kiacoder/hermes-vps-sre.git /tmp/hermes-sre
```

### 3. Run the Setup Wizard
Execute the automated wizard script to configure, secure, and start the daemon in one go:
```bash
bash /tmp/hermes-sre/setup.sh
```
*The script will ask for your Gemini API Key, Telegram Bot Token, and allowed User ID. It will then automatically configure files, set permission controls, deploy the sudoers security policy, and start the system service!*

---

## 💥 Simulating a Crash
To trigger the live SRE repair demonstration during video recordings:
```bash
python3 /var/www/hamrahvision/inject_error.py
sudo systemctl restart hamrahvision
```
Then message your Telegram bot: *"The homepage is down, please check the error and restart hamrahvision."*

---

## 📺 Follow the Tutorial
*   **YouTube (English)**: [@HesabAgent](https://www.youtube.com/@HesabAgent)
*   **Aparat (Persian)**: [Kia_coder](https://www.aparat.com/Kia_coder)

