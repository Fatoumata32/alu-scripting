#!/usr/bin/env ruby
if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit 1
end

input_string = ARGV[0]

pattern = /School/

result = ""

input_string.scan(pattern) { |match| result += match }

puts result
