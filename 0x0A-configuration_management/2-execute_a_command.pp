# Use exec to kill the process killmenow
exec {'kill-killmenow':
	command => 'pkill killmenow',
	path 	=> '/usr/bin';
	}
