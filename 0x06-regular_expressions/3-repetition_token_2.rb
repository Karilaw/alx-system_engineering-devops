#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./3-repetition_token_2.rb <string>"
  exit
end

string = ARGV[0]
regex = /hbt+n/
matches = string.scan(regex)
puts matches.join
