def find(s,sub):
    l=len(sub)
    for i,j in enumerate(s):
        if s[i:i+l]==sub:
            return i
def rfind(s,sub):
    l=len(sub)
    for i,j in enumerate(s):
        if s[i:i+l]==sub:
            ans=i
    return ans
def count(s,sub):
    l=len(sub)
    c=0
    for i,j in enumerate(s):
        if s[i:i+l]==sub:
            c+=1
    return c
def first(s):
    return s.split()[0]
