def title_to_number(title: str) -> int:
    return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,columnTitle))
    
