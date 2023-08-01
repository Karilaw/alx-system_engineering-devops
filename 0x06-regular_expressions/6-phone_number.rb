#!/usr/bin/env ruby
if ARGV.length != 1
  puts "Usage: ./6-phone_number.rb <string>"
  exit
end
string = ARGV[0]
regex = /\A\d{10}\z/
matches = string.scan(regex)
puts matches.join
