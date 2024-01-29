#automate the task of creating a custom HTTP header response
class { 'nginx':
    ensure => 'installed',
}

file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => 'present',
    content => "add_header X-Served-By $::hostname;",
    require => Class['nginx'],
    notify  => Service['nginx'],
}

service { 'nginx':
    ensure => 'running',
    enable => true,
}
