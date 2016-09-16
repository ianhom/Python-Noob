#!/usr/bin/python
# -*0- coding: UTF-8 -*-

for letter in 'Python':     # First Example
   if letter == 'o':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 3:
      break

print "End!"

# result
"""
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current variable value : 10
Current variable value : 9
Current variable value : 8
Current variable value : 7
Current variable value : 6
Current variable value : 5
Current variable value : 4
End!
"""
