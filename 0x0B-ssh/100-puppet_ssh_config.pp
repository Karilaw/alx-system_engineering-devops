# Puppet manifest to configure SSH client

class ssh_client_config {
  file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => template('ssh/ssh_config.erb'),
  }
}

class ssh_disable_password_auth {
  file_line { 'Disable Password Authentication':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
  }
}

class ssh_set_identity_file {
  file_line { 'Set Identity File':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
  }
}

class ssh {
  include ssh_client_config
  include ssh_disable_password_auth
  include ssh_set_identity_file
}

include ssh
