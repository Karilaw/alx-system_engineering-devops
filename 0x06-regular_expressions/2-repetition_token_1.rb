#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./2-repetition_token_1.rb <string>"
  exit
end

string = ARGV[0]
regex = /hb?tn/
matches = string.scan(regex)
puts matches.join
