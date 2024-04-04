# Setup the web servers for the deployment of web_static

exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}

exec {'install-nginx':
  command => '/usr/bin/env apt-get -y install nginx',
}

exec {'create-web_static-dir':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}

exec {'create-web_static-shared-dir':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}

exec {'create-index-html':
  command => '/usr/bin/env echo "<html>
 <head>
 </head>
 <body>
   Holberton School
 </body>
</html>" > /data/web_static/releases/test/index.html',
}

exec {'create-symbolic-link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}

exec {'configure-nginx':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

exec {'set-ownership':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}

exec {'restart-nginx':
  command => '/usr/bin/env service nginx restart',
}
