def hist(s):
    if s=="": return {}
    d=hist(s[1:])
    if s[0] in d: d[s[0]]+=1
    else: d[s[0]]=1
    return d
print(hist("abracadabra"))