# using strace to etermine the error

exec {'new word':
    command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    provider => shell,
}
