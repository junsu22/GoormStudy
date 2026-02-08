# 다익스트라 알고리즘과 벨만포드알고리즘에 대해 이해하고 구현하세요
import heapq

# queue 사용
# 빠름
# dijikstra 시작 정점부터 정점까지의 최단 경로를 찾는 알고리즘
# 주로 음의 가중치를 가진 간선없는 그래프에 잘 작동함.
# 탐욕적 방법 기반으로 최소 비용을 찾아냄 .


def dijkstra(graph, start):
    # 모든 정점 까지의 거를 무한대로 초기화
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0  # 시작의 정점은 0
    priority_queue = [(0, start)]  # (거리, 정점) 우선순위 큐에 삽입

    while priority_queue:  # 큐가 빌 때까지
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # 이미 처리된 정점이면
        if current_distance > distances[current_vertex]:
            continue  # 스킵
        # 현재 정점의 인접 정점들을 확인
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 더 짧은 경로를 발견하면 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 실행예시
if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }

    result = dijkstra(graph, "A")
    print("A 로 부터의 최단거리: ", result)


# A 로 부터의 최단거리:  {'A': 0, 'B': 1, 'C': 3, 'D': 4}


# Bellman-Ford
# diijiksta와 반대로 음의 가중치 가능.
# 음의 사이클 감지
# 느림


def bellman_ford(graph, start):
    """
    graph: 형태
    start: 시작 정점
    """
    # 모든 정점까지의 거리를 무한대로 초기화
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0  # 시작 정점은 0

    # (정점 개수 - 1)번 반복하며 모든 간선 확인
    for _ in range(len(graph) - 1):
        for vertex in graph:  # 모든 정점에 대해
            for neighbor, weight in graph[vertex]:  # 인접 정점들 확인
                # 거리갱신 : 현재 정점을 거쳐가는 것이 더 짧으면 갱신
                if distances[vertex] + weight < distances[neighbor]:
                    # 현재 정점까지 최단거리 + 가중치 < 기존인접 정점까지 거리
                    distances[neighbor] = distances[vertex] + weight

    # 음의 사이클 감지
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            # 아직도 더 짧은 경로가 있다면 = 음의 사이클 존재
            if distances[vertex] + weight < distances[neighbor]:
                print("음의 사이클이 감지 됨")
                return None

    return distances


# 실행 예시
if __name__ == "__main__":
    # 음의 가중치가 있는 그래프
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", -2), ("D", 5)],  # 음의 가중치
        "C": [("D", 1)],
        "D": [],
    }

    result = bellman_ford(graph, "A")
    print("A로부터의 최단거리:", result)


# 실행 결과:
# A로부터의 최단거리: {'A': 0, 'B': 1, 'C': -1, 'D': 0}
