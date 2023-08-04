#!/usr/bin/env ruby
# a script only matching capital letters

string = "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream"
result = string.scan(/[A-Z]/)
puts result.join
# => ILOVESYSADMIN
