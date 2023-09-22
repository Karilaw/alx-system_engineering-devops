# manifest kills a process named 'killmenow' using exec resource
# and 'pkill'

exec { 'kill_process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
