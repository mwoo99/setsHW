def intersect(a,b):
    return [i for i in a if i in b]
def union(a,b): 
    return a + diff(b,a)
def diff(a, b):
    return [i for i in a if i not in b]
def symmetricdiff(a,b):
    return diff(union(a,b),intersect(a,b))
def prod(a,b):   
    return [(i, j) for i in a for j in b]
