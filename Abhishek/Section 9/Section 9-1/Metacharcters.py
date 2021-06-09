#. is the most important dotmetacharacter

#import re
#pattern = r"gr.y" # the string should start with this name so that it returns true

#if re.match(pattern ,"agray"):
 #   print("match found")
#else:
 #   print("match not found")


import re 

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern , "AA1"):
    print("housenumber found")