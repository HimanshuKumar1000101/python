tree = {
'1' : ['2','5'],
'2' : ['5', '4'],
'5' : ['3'],
'3' : [],
'4' : ['5','6'],
'6' : []
}
print(tree)
explored = set()

def bfs(explored, tree, node):
       if node not in explored:
          print (node)
          explored.add(node)
          for neighbour in tree[node]:
            bfs(explored, tree, neighbour)
print("Following is the Depth-First Search")
bfs(explored, tree, '1')