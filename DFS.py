tree = {
'1' : ['2','5'],
'2' : ['3', '4'],
'5' : ['6'],
'3' : [],
'4' : ['5'],
'6' : []
}
print(tree)
explored = set()

def dfs(explored, tree, node):
       if node not in explored:
          print (node)
          explored.add(node)
          for neighbour in tree[node]:
            dfs(explored, tree, neighbour)
print("Following is the Depth-First Search")
dfs(explored, tree, '1')