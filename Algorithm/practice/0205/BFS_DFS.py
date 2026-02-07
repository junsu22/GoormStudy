from collections import deque

# 그래프 정의 (먼저!)
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


# BFS
def bfs(graph, start):
    visited = set()  # 방문한 노드를 저장할 집합
    queue = deque([start])  # 시작 노드를 큐에 삽입

    while queue:  # 큐가 비어있지 않는 동안
        vertex = queue.popleft()  # 큐에서 노드를 하나 꺼냄
        if vertex not in visited:  # 방문하지 않은 노드라면
            visited.add(vertex)  # 방문 처리
            print(vertex, end=" ")
            # 방문하지 않은 인접 노드를 모두 큐에 삽입
            queue.extend([i for i in graph[vertex] if i not in visited])


# DFS
visited = {key: False for key in graph.keys()}
#  그래프의 모든 노드를 False 로 초기화 한다.


# 재귀함수 사용
def dfs_recursive(graph, visited, node):
    if not visited[node]:  # 만일 방문을 하지 않았다면
        print(node, end=" ")  # 출력
        visited[node] = True  # 방문 처리
        for neighbour in graph[node]:  # 현재의 모든 인접한 노드들을 순회.
            dfs_recursive(graph, visited, neighbour)
            # 인접노드 에 대해 재귀호출


# 실행 ( 두 알고리즘 을 비교)
print("BFS 방문 순서: ")
bfs(graph, "A")  # A 부터 시작하는 BFS 함수 호출
print("\n")  # 개행처리

# DFS 실행 예시
print("DFS 방문 순서: ")
dfs_recursive(graph, visited, "A")  # A 부터 시작하는 DFS 함수 호출

# BFS 방문 순서:
# A B C D E F

# DFS 방문 순서:
# A B D E F C


# 스택을 사용하는 방법
def dfs_stack(graph, start):
    visited = set()  # 방문한 노드를 저장할 집합
    stack = [start]  # 시작 노드를 스택에 추가

    while stack:  # 스택이 비어있지 않는 동안 반복
        node = stack.pop()  # 스택에서 하나의 노드를 꺼냄
        if node not in visited:
            print(node, end=" ")
            visited.add(node)  # 방문한 노드에 추가
            # 현재 노드에 인접하고 아직 방문하지 않은 모든 노드를 스택에 추가.
            # 여기서는 인접 노드를 거꾸로 스택에 추가하여,
            # 그래프의 순서대로 탐색되도록 합니다
            stack.extend([x for x in graph[node] if x not in visited])


print("DFS 방문 순서 (스택 사용):")
dfs_stack(graph, "A")

# BFS 방문 순서:
# A B C D E F

# DFS 방문 순서:
# A B D E F C DFS 방문 순서 (스택 사용):
# A C F E B D
