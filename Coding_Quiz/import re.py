import re
p = re.compile('[a-zA-Z]')
m = p.match( '124' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')