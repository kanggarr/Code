# Depth-first search 

graph = {
    'A': ['B', 'E'],
    'B': [],
    'C': ['D'],
    'D': [],
    'E': ['C']
}


visited = set() 


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbored in graph[node]:
            dfs(visited, graph, neighbored)

print("Following is the Depth-First Search")
dfs(visited, graph, 'A')





# https://favtutor.com/blogs/Depth-first-search-python