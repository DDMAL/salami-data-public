files = Dir.glob("/Users/blahblahblah/salami-data-public/annotations/*/*.txt") 
files.each do |f|
   if f.split(".")[-1]=="txt" then
       puts f
       system("ruby get_sections_sept_2012.rb #{f}")
   end
end