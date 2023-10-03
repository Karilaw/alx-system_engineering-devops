# This Puppet manifest installs Nginx and configures it to add a custom header 'X-Served-By' with the value of the hostname of the server.

# Ensure nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure nginx service is running
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

# Configure nginx
file_line { 'listen 80':
  path => '/etc/nginx/sites-available/default',
  line => '    listen 80;',
  match => '^\s*listen 80 default_server;',
  require => Package['nginx'],
}

# Set up the Hello World page
file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
}

# Add the custom header to all location blocks in the default site configuration
exec { 'add custom header':
  command => "sudo sed -i \"/location /a\\\\\\\\tadd_header X-Served-By \$HOSTNAME;\" /etc/nginx/sites-available/default",
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
