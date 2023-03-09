#RegEX#
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

Metacharacters
Metacharacters are characters with a special meaning:
[]	A set of characters
\	Signals a special sequence (can also be used to escape special characters)
.	Any character (except newline character)
^	Starts with
$	Ends with
*	Zero or more occurrences
+	One or more occurrences
?	Zero or one occurrences
{}	Exactly the specified number of occurrences
|	Either or	
() Capture and group

example:
Starts with The and ends with Spain

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

RegEx Functions:
findall - returns a list containing all matches

Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
