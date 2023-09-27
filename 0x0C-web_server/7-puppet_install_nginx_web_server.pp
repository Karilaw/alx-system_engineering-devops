# This Puppet manifest installs Nginx, configures a redirection from /redirect_me, and sets up a custom 404 page

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/redirection':
    ensure  => file,
    content => "server {
      listen 80;
      server_name _;
      location / {
        try_files \$uri \$uri/ =404;
      }
      location /redirect_me {
        return 301 https://www.example.com;
      }
    }",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => absent,
    force  => true,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/redirection':
    ensure => link,
    target => '/etc/nginx/sites-available/redirection',
    require => File['/etc/nginx/sites-available/redirection'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/redirection'],
  }
}

include nginx
