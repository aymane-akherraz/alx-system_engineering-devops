# Creates a custom HTTP header response

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => installed,
  require => Exec['update system']
}

exec { 'set_custom_header':
  command => '/usr/bin/sudo sed -i "/server_name _;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default'
}

service { 'nginx':
  ensure  => running,
  restart => true,
}
