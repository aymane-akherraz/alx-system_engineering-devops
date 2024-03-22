# Configures ssh to use the private key in ~/.ssh/school for authentication
file { '/etc/ssh/ssh_config':
  ensure  => present,
  mode    => '0600',
  content => "Host 52.86.133.238\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n"
}
