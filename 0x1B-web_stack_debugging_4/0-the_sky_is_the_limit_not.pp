# increases the amount of traffic
# increases the UNLIMIT
exec { 'fix --for-nginx':
  # modify UNLIMIT
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # specify the path
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'restart-nginx':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
  # specify the path
  path    => '/etc/init.d/',
}
