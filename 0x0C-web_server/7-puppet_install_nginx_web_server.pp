#configure server with puppet
#nginx_puppet_manifest.pip

#install Nginx package
package{'nginx':
    ensure => installed,
}

#ensure nginxis running and enabled
service { 'nginx' :
    ensure => running,
    enable => true,
    require => package['nginx'],
}
# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx_puppet_manifest/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Create Hello World HTML file
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  notify  => Service['nginx'],
}

# Redirect /redirect_me with a 301 Moved Permanently
nginx::resource::location { 'redirect_me':
  ensure    => present,
  server    => 'default',
  location  => '/redirect_me',
  type      => 'redirect',
  parameters => {
    'destination' => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
    'permanent'   => true,
  },
  require   => File['/etc/nginx/sites-available/default'],
}