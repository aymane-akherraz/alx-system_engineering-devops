# Installs and configures an Nginx server
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file_line { 'nginx_redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => "\tlocation = /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}",
  match  => 'location = /redirect_me {',
  after  => 'root /var/www/html;',
}

service { 'nginx':
  ensure  => running,
  restart => true,
}
