# Installs flask (2.1.0) from pip3
exec { 'install flask':
  command => '/usr/bin/env pip3 install flask==2.1.0',
}
