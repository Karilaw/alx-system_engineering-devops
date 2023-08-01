#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./4-repetition_token_3.rb <string>"
  exit
end

string = ARGV[0]
regex = /hbt*n/
matches = string.scan(regex)
puts matches.join
