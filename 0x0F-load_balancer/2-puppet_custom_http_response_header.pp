# Creates a custom HTTP header response
package { 'nginx':
  ensure => 'installed',
}

exec { 'set_custom_header':
command => '/usr/bin/sed -i "/server_name _;/a     add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default'
 provider => shell,
}

service { 'nginx':
  ensure  => running,
  restart => true,
}
