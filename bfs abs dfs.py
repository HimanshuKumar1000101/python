def bfsdfs():
    x=int(input("enter the search 1 - BFS AND 2 - DFS"))
    if(x==1):
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
      print("Following is the Bradth -First Search")
      bfs(explored, tree, '1')

    elif(x==2):
        tree = {
            '1': ['2', '5'],
            '2': ['3', '4'],
            '5': ['6'],
            '3': [],
            '4': ['5'],
            '6': []
        }
        print(tree)
        explored = set()

        def dfs(explored, tree, node):
            if node not in explored:
                print(node)
                explored.add(node)
                for neighbour in tree[node]:
                    dfs(explored, tree, neighbour)

        print("Following is the Depth-First Search")
        dfs(explored, tree, '1')
    else:
        print("invalid")
bfsdfs()