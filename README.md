# 🧙‍♂️ Nous Hermes VPS Agent Setup (Ron Weasley SRE)

[English Version](#english) | [نسخه فارسی](#farsi)

---

<a name="english"></a>
## 🇬🇧 English Documentation

This repository contains all the configuration files, security policies, and simulation scripts used in the video tutorial on setting up **Nous Hermes** as an autonomous SRE agent on a Linux VPS.

### 📁 Repository Structure
*   `config.yaml` — Configured to run direct Gemini API (fast, low-cost token execution).
*   `SOUL.md` — The custom system prompt shaping the agent's personality as **Ron Weasley (Muggle IT Specialist)**.
*   `env.example` — A template for your API keys and secure Telegram allowed-user restrictions.
*   `sudoers.d_template` — The security policy granting passwordless `systemctl restart` access for your daemon.
*   `inject_error.py` — Script to simulate a live Django NameError typo (500 Error).
*   `restore_code.py` — Script to instantly recover from the simulated error.

### 🚀 Simplified 3-Step VPS Installation Guide
1. **Install Hermes Agent**:
   ```bash
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --non-interactive --skip-setup
   ```
2. **Download this Repository**:
   ```bash
   git clone https://github.com/kiacoder/hermes-vps-sre.git /tmp/hermes-sre
   ```
3. **Run the Setup Wizard**:
   ```bash
   bash /tmp/hermes-sre/setup.sh
   ```
   *The setup script will ask for your Gemini API Key, Telegram Bot Token, and allowed User ID. It will then automatically configure files, set permission controls, deploy the sudoers security policy, and start the system service!*

---

<a name="farsi"></a>
## 🇮🇷 راهنمای فارسی

این مخزن شامل تمام فایل‌های پیکربندی، سیاست‌های امنیتی و اسکریپت‌های شبیه‌سازی است که در ویدیوی آموزشی راه‌اندازی **Nous Hermes** به عنوان یک ایجنت خودمختار SRE (پشتیبان سرور) روی سرور مجازی لینوکس استفاده شده است.

### 📁 ساختار فایل‌های پروژه
*   `config.yaml` — پیکربندی برای اجرای مستقیم API جمینای (اجرای سریع و ارزان).
*   `SOUL.md` — دستورالعمل سیستم (پرامپت) برای شکل‌دهی شخصیت ایجنت به عنوان **رون ویزلی (متخصص آی‌تی مشنگ‌ها!)**.
*   `env.example` — قالب کلیدهای API و ایدی‌های مجاز تلگرام جهت امنیت ربات.
*   `sudoers.d_template` — سیاست امنیتی برای اعطای دسترسی ری‌استارت سرویس جنگو بدون نیاز به رمز عبور.
*   `inject_error.py` — اسکریپت شبیه‌سازی خطای جنگو (خطای ۵۰۰).
*   `restore_code.py` — اسکریپت بازیابی سریع کدها به حالت عادی.

### 🚀 راهنمای نصب ۳ مرحله‌ای روی سرور
1. **نصب ایجنت هرمس**:
   ```bash
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --non-interactive --skip-setup
   ```
2. **دانلود قالب‌ها و ابزارهای پروژه**:
   ```bash
   git clone https://github.com/kiacoder/hermes-vps-sre.git /tmp/hermes-sre
   ```
3. **اجرای جادوگر نصب خودکار**:
   ```bash
   bash /tmp/hermes-sre/setup.sh
   ```
   *اسکریپت نصب از شما کلید API جمینای، توکن ربات تلگرام و آیدی تلگرام شما را می‌پرسد و سپس تمام فایل‌ها را تنظیم کرده، سطوح دسترسی را اعمال می‌کند و سرویس پس‌زمینه را راه‌اندازی می‌کند!*

---

## 💥 Simulating a Crash / شبیه‌سازی خطا
To trigger the live SRE repair demonstration during video recordings:
```bash
python3 /var/www/hamrahvision/inject_error.py
sudo systemctl restart hamrahvision
```
Then message your Telegram bot: *"The homepage is down, please check the error and restart hamrahvision."*

---

## 📺 Follow the Channels / دنبال کردن شبکه‌ها
*   **YouTube (English)**: [@HesabAgent](https://www.youtube.com/@HesabAgent)
*   **Aparat (Persian)**: [Kia_coder](https://www.aparat.com/Kia_coder)

