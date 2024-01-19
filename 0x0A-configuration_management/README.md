# 0x0A. Configuration management

# Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

Puppet 5 Docs

Install puppet-lint
$ gem install puppet-lint

#Tasks
0. Create a file
Using Puppet, create a file in /tmp.
Requirements:
File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet
1. Install a package
Using Puppet, install flask from pip3.
Requirements:
Install flask
Version must be 2.1.0
2. Execute a command
Using Puppet, create a manifest that kills a process named killmenow.
Requirements:
Must use the exec Puppet resource
Must use pkill

