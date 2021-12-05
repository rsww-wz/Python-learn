import re

string = "34h6ld3k5d956j9f5h9adss02fhing2kdw3h46"
spam = re.findall('(\d[a-z]){1,4}',string)
print(spam)
