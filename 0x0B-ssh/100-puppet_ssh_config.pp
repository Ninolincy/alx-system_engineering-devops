# Client configuration file (w/ Puppet)

exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/authorized_keys',
  returns => [0,1],
}