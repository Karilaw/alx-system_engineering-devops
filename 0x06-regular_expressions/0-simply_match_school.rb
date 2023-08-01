#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <string>"
  exit
end

string = ARGV[0]
matches = string.scan(/School/)
puts matches.join
