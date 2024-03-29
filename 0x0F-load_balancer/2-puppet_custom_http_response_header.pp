# Creates a custom HTTP header response
exec { 'set_custom_header':
command => 'apt-get -y install nginx;
sudo sed -i "/server_name _;/a\        add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
service nginx restart',
 provider => shell,
}
