# kill the process killmenow
exec {'pkill':
	command => 'pkill killmenow',
	path 	=> '/usr/bin',
	}
