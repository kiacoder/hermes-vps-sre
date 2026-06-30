#!/usr/bin/env bash
# setup.sh — Automated Hermes Agent setup script for the VPS SRE tutorial
set -e

echo "🧙‍♂️ Welcome to the Ron Weasley SRE Setup Wizard! 🧙‍♂️"
echo "--------------------------------------------------"

# Ask for the required configuration parameters
read -rp "🔑 Enter your Gemini API Key: " GEMINI_API_KEY
read -rp "🤖 Enter your Telegram Bot Token: " TELEGRAM_BOT_TOKEN
read -rp "👤 Enter your Telegram User ID (allowed user): " TELEGRAM_ALLOWED_USERS
read -rp "📂 Enter your Project absolute path (default: /var/www/my-project): " PROJECT_PATH
PROJECT_PATH=${PROJECT_PATH:-/var/www/my-project}
read -rp "⚙️ Enter your systemd Service Name (default: my-project): " SERVICE_NAME
SERVICE_NAME=${SERVICE_NAME:-my-project}

echo ""
echo "🚀 Starting automated deployment for project: $SERVICE_NAME..."

# 1. Move configuration directory for security (run-as www-data)
echo "📦 Configuring directory ownership and permissions..."
if [ -d /root/.hermes ]; then
    cp -r /root/.hermes /var/www/.hermes
fi
mkdir -p /var/www/.hermes

# 2. Copy and customize config.yaml and SOUL.md personality
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
cp "$SCRIPT_DIR/config.yaml" /var/www/.hermes/config.yaml

echo "📝 Customizing agent personality bindings..."
sed -e "s|{{PROJECT_PATH}}|$PROJECT_PATH|g" \
    -e "s|{{SERVICE_NAME}}|$SERVICE_NAME|g" \
    "$SCRIPT_DIR/SOUL.md" > /var/www/.hermes/SOUL.md

# 3. Create the secure .env file
echo "🔐 Creating secure .env configuration..."
cat << EOF > /var/www/.hermes/.env
GEMINI_API_KEY="$GEMINI_API_KEY"
TELEGRAM_BOT_TOKEN="$TELEGRAM_BOT_TOKEN"
TELEGRAM_ALLOWED_USERS="$TELEGRAM_ALLOWED_USERS"
PYTHONUNBUFFERED=1
EOF

# Ensure www-data permissions
chown -R www-data:www-data /var/www/.hermes

# 4. Deploy sudoers policy
echo "🛡️ Deploying sudoers diagnostic permissions..."
sed "s|{{SERVICE_NAME}}|$SERVICE_NAME|g" "$SCRIPT_DIR/sudoers.d_template" > /etc/sudoers.d/www-data-$SERVICE_NAME
chmod 0440 /etc/sudoers.d/www-data-$SERVICE_NAME
visudo -cf /etc/sudoers.d/www-data-$SERVICE_NAME

# 5. Install and launch gateway daemon
echo "⚙️ Registering and launching system service..."
# Supply automated answers (n to starting now in wizard, y to running on boot) to the service installer
hermes gateway install --system --run-as-user www-data <<EOF
n
y
EOF

# Reload and start service
systemctl daemon-reload
systemctl start hermes-gateway
systemctl status hermes-gateway --no-pager

echo ""
echo "✨ Full Hermes Daemon deployed successfully! Ron Weasley is now active on Telegram! 🧙‍♂️📱"
