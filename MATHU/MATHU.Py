with open('MATHU/MATHU.INP', 'r') as file:
    data = file.read()
    s = data.strip()
answ = ''
i = 0
logst = ''
while i < len(s):
    ch = s[i]
    i += 1
    n = ''
    while i < len(s) and s[i].isdigit():
        n += s[i]
        i += 1
    shift = int(n)
    
    if ch.islower():
        ss1 = 'a'
    else:
        ss1 = 'A'
    ss = (ord(ch)- ord(ss1) + shift) % 26
    ng = chr(ss + ord(ss1))
    answ += ng
    if i < len(s) and s[i] == '@':
        if len(answ) > len(logst):
            logst = answ
        answ = ''
        i += 1    
if len(answ) > len(logst):
    logst = answ

with open('MATHU/MATHU.OUT', 'w') as file:
    file.write(logst)

