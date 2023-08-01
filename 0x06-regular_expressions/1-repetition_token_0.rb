#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./1-repetition_token_0.rb <string>"
  exit
end

string = ARGV[0]
regex = /hbt{2,5}n/
matches = string.scan(regex)
puts matches.join
