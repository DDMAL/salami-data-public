require 'find'
 
Find.find("/Users/blahblahblah/SALAMI_data_v1.2/data") do |f|
   if f.split(".")[-1]=="txt" then
       puts f
       system("ruby get_sections_sept_2012.rb #{f}")
   end
end