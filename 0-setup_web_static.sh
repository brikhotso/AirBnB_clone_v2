#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Update package index and install nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Fake HTML content
fake_html_content="<html>
  <head>
    <title>My_index</title>
  </head>
  <body>
    <h1>Hello, this is a fake HTML page!</h1>
  </body>
</html>"

# Create fake HTML file
echo "$fake_html_content" > /data/web_static/releases/test/index.html

# Remove symbolic link if exists and recreate
if [ -L "/data/web_static/current" ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership and group of /data directory
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
cat >/etc/nginx/sites-available/default <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root   /var/www/html;
    index  index.html;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
EOF

# Restart Nginx service
sudo service nginx restart
