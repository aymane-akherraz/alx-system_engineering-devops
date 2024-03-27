# Installs and configures an Nginx server
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => "Hello World!",
}

file_line { 'nginx_redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'root /var/www/html;',
}

service { 'nginx':
  ensure  => running,
  restart => true,
}
