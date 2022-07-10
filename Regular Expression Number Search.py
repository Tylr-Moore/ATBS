import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me at 415-555-1011 tomorrow, or 415-555-9999 for my office line.')) # mo = match objects
#mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow, or 415-555-9999 for my office line.') # mo = match objects
#print(mo.group())
