# Creates a custom HTTP header response
package { 'nginx':
  ensure => installed,
}

exec { 'set_custom_header':
  command => '/usr/bin/sudo sed -i "/server_name _;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default'
}

service { 'nginx':
  ensure  => running,
  restart => true,
}
