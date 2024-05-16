# fix nginx error

exec { 'fix-nginx-err':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => 'shell'
}

exec { 'restart-nginx':
  command  => 'service nginx restart',
  provider => 'shell'
}
