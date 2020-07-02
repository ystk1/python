import sys

f = open('set_ip.bat')
lines = f.readlines()
print(lines[1])
print(f.readlines())
# ['line 1\n', 'line 2\n', 'line 3']
f.close()
