# fix nginx error

exec { 'fix-nginx-err':
  command => 'sed -i s/15/4096/g /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
