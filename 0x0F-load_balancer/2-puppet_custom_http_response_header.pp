# Creates a custom HTTP header response
exec { 'command':
  command => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
}
