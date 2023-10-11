
def is_uppercase(inp):
    s = ''
    for i in inp:
        if i.isupper() or not i.isalpha():
            s += 'A'
        else:
            s += 'a'
    if s.isupper():
        return True
    else:
        return False
    

