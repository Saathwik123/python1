import re
 

s = 'GeeksforGeeks: A computer science what for geeks'
 

match = re.search(r'what', s)
 

print('Start Index:', match.start())

print('End Index:', match.end())
