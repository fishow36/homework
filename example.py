import re

reg = r'\b«([а-я]+-[0-9]+)»\b'

mr = '«тяньгунь-8»'

if re.search(reg, mr) != None:
    print(mr)
