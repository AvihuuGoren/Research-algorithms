def func1(a:int,b:int,c:float):
            return 5
def four_neighbor_function(node):
    (x,y) = node
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
def six_neighbor_function(node):
    (x,y,z) = node
    return [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z-1),(x,y,z+1)]

