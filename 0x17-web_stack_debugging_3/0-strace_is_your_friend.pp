# Fix wordpress issue using puppet

exec { 'fix-wp-err':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
}
