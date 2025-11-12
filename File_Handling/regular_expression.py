import re

test = "The quick brown fox jumps"

pattern = r"quick"

match = re.match(pattern, test)
if match:
    print("Match found", match.group())
else:
    print("No match found")



'''re.match() only checks for a match at the beginning of the string.

Your string starts with "The", not "quick".

Therefore, the pattern "quick" doesn’t match at the start.'''


