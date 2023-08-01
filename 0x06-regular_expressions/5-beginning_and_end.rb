#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./5-beginning_and_end.rb <string>"
  exit
end

string = ARGV[0]
regex = /\Ah.n\z/
matches = string.scan(regex)
puts matches.join
