# Increasing the limit a nginx server can handle

exec { 'change nginx limit':
    command => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
    provider=> shell,
}