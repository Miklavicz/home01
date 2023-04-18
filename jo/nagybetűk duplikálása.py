def dupl(original: str)->str:
    mh='aeiou'
    ret=''
    for c in original:
        ret+=c
        if c.lower() in mh:
            ret+=c
    return ret
print(dupl("sargpowpoqdkslakfre"))
