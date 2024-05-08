# Fix wordpress issue using puppet
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template("<%= File.read('/var/www/html/wp-settings.php').gsub(\"require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );\", \"require_once( ABSPATH . WPINC . '/class-wp-locale.php' );\") %>"),
