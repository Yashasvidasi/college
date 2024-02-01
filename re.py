class graph:
    def __init__(self):
        self.list = {}
    def addnode(self, a):
        for node in self.list:
            if node  == a:
                print("already exists")
                return
        self.list.update({a:[]})
    def addedge(self, a ,b):
        for node in self.list:
            if node == a:
                if b in self.list[node]:
                    print("already exists")
                    return
                else:
                    self.list[a].append(b)
                    self.list[b].append(a)
                    
                    return
        print("not found")
        return
    def topo(self, node, visited, stack):
        visited[node] = True

        if node in self.list:
            for neighbor in self.list[node]:
                if not visited[neighbor]:
                    self.topo(neighbor, visited, stack)

        stack.append(node)

    def tp_sort(self):
        visited = {node: False for node in self.list}
        stack = []

        for node in self.list:
            if not visited[node]:
                self.topo(node, visited, stack)

        return stack[::-1]
    def cycle(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in self.list[node]:
            if not visited[neighbor]:
                if self.cycle(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    def is_cyclic(self):
        visited = {node: False for node in self.list}
        rec_stack = {node: False for node in self.list}

        for node in self.list:
            if not visited[node]:
                if self.cycle(node, visited, rec_stack):
                    return True

        return False
    def dfs_search(self, start, target, visited=None, path=None):
        if visited is None:
            visited = {node: False for node in self.list}
        if path is None:
            path = []
            
        visited[start] = True
        path.append(start)

        if start == target:
            return path

        for neighbor in self.list[start]:
            if not visited[neighbor]:
                new_path = self.dfs_search(neighbor, target, visited, path.copy())
                if new_path:
                    return new_path

        return []
                
            
        



graph = graph()
for a in range(1,21):
    graph.addnode(a)


graph.addedge(1,2)
graph.addedge(2,3)
graph.addedge(7,8)
graph.addedge(3,8)
graph.addedge(1,6)
graph.addedge(6,11)
graph.addedge(11,12)
graph.addedge(12,17)
graph.addedge(17,16)
graph.addedge(17,18)
graph.addedge(18,19)
graph.addedge(19,14)
graph.addedge(14,13)
graph.addedge(14,9)
graph.addedge(9,10)
graph.addedge(10,5)
graph.addedge(5,4)
graph.addedge(10,15)
graph.addedge(15,20)

print(graph.dfs_search(2,5))

            
