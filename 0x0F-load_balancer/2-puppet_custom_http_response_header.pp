# This Puppet manifest installs Nginx and configures it to add a custom header 'X-Served-By' with the value of the hostname of the server.

class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/snippets/custom-header.conf':
    ensure  => file,
    content => "add_header X-Served-By \$hostname;",
    require => Package['nginx'],
  }

  exec { 'nginx_include_custom_header':
    command => "sed -i '/server_name _;/a include snippets/custom-header.conf;' /etc/nginx/sites-available/default",
    path    => ['/bin', '/usr/bin'],
    require => File['/etc/nginx/snippets/custom-header.conf'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => Exec['nginx_include_custom_header'],
  }
}

include nginx_custom_header
