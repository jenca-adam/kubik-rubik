def switch(k,tr):
    a=chr(k)
    if k == 259:
        return "x'"
    if k== 258:
        return "x"
    if k == 260:
        return "y'"
    if k == 261:
        return "y"
    if a in "xyz":
        return a
    if a in tr:
        if a.isupper():
            return a.lower()
        return a.upper()
    return ""
