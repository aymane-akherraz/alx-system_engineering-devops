# Increase the user limit for holberton-user

exec { 'change-os-conf-for-holberton-user':
  command => 'sed -i "/holberton/s/5/50/; /holberton/s/4/40/" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}
