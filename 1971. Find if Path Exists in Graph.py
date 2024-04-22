class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        stack=collections.deque()
        stack.append(source)
        visited=[False]*n
        visited[source]=True
        
        
        while stack:
            curr=stack.popleft()
            if curr==destination:
                return True
            for neigh in graph[curr]:
                if not visited[neigh]:
                    visited[neigh]=True
                    stack.append(neigh)         
        return False
                
                
