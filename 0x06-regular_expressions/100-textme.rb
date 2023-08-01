#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$0} LOG_FILE"
  exit 1
end
log_file = File.open(ARGV[0], "r")

log_file.each_line do |line|
  sender = line.match(/\[from:(.+?)\]/)[1]
  receiver = line.match(/\[to:(.+?)\]/)[1]
  flags = line.match(/\[flags:(.+?)\]/)[1]
  puts "#{sender},#{receiver},#{flags}"
end
log_file.close

