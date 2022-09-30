graph = {
    'A' : ['C','D','B'],
    'B' : ['E','F','D'],
    'C' : ['F','G'],
    'D' : ['H'],
    'E' : ['H'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : []
}


start,stop = input().split()
count = 0
def find_paths(start,stop,graph,now=start,path=start):
    global count
    
    if path.count(now)>1:
        return 

    if now == stop:
        count+=1
        print("ways :",count,";",*[i for i in path])
        return 
    
    for i in graph[now]:
        find_paths(start,stop,graph,i,path+i)
    

find_paths(start,stop,graph)