#* is the important star metacharacter

import re
pattern = r"bread(eggs)*bread"

if re.match(pattern ,"breadeggsbread"):
    print("macth found")

