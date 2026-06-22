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

## 🚀 Step-by-Step VPS Installation Guide

### 1. Install Hermes Agent
Run the official Nous Hermes installer in non-interactive mode:
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --non-interactive --skip-setup
```

### 2. Move Configuration for Security
Move the settings folder to the web daemon's home directory so it runs under a non-root user (`www-data`):
```bash
cp -r /root/.hermes /var/www/.hermes
chown -R www-data:www-data /var/www/.hermes
```

### 3. Apply Configuration Files
Copy the customized `config.yaml`, `SOUL.md`, and `.env` templates from this repository into `/var/www/.hermes/` (be sure to fill in your `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`, and `GEMINI_API_KEY` in `.env`).

### 4. Set Up Sudoers Policy
Copy the `sudoers.d_template` to `/etc/sudoers.d/www-data-hamrahvision` and set permissions:
```bash
chmod 0440 /etc/sudoers.d/www-data-hamrahvision
visudo -cf /etc/sudoers.d/www-data-hamrahvision
```

### 5. Install & Start Gateway Daemon
Install and start the system service to keep the Telegram bot running in the background:
```bash
hermes gateway install --system --run-as-user www-data
# Answer 'n' to starting immediately, 'y' to starting automatically on boot.

# Start the system daemon:
sudo systemctl start hermes-gateway
sudo systemctl status hermes-gateway
```

### 6. Simulating a Crash
To trigger the live repair simulation:
```bash
python3 /var/www/hamrahvision/inject_error.py
sudo systemctl restart hamrahvision
```
Then message your bot: *"The homepage is down, please check the error and restart hamrahvision."*
