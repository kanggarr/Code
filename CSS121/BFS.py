# Breadth-first search

graph = {
    'A': ['B', 'E'],
    'B': [],
    'C': ['D'],
    'D': [],
    'E': ['C']
}

visited = []
queue = []


def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbored in graph[m]:
      if neighbored not in visited:
        visited.append(neighbored)
        queue.append(neighbored)


print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')





# https://favtutor.com/blogs/depth-first-search-python