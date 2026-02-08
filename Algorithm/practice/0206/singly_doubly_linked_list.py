# 링크드 리스트 개념 설명
# 싱글리 링크드리스트의 삽입, 삭제, 출력, 탐색을 구현해보세요
# 더블리 링크드리스트의 삽입, 삭제, 출력, 탐색을 구현해보세요

"""
링크드 리스트 (Linked List)
- 노드들이 연결된 자료구조
- 삽입/삭제가 빠름 O(1)
- 탐색이 느림 O(n) (순차 접근만 가능)

종류:
1. 싱글리 링크드 리스트: 다음 노드만 가리킴 (→)
2. 더블리 링크드 리스트: 이전/다음 노드 모두 가리킴 (⇄)"""


#  싱글리 링크드 리스트
# 노드 클래스
class Node:
    def __init__(self, data):
        self.data = data  # 데이터 저장 (ex: 기차 칸, 10, 20, 30)
        self.next = None  # 다음 노드를 가리키는 포인터 (처음은 None으로 시작한다.)


# 싱글리 링크드 리스트 클래스
class SinglyLinkedList:

    def __init__(self):
        self.head = None  # 리스트의 시작점 , 리스트의 시작점은 head이다.

    # 메서드 구현 시작
    # 삽입 (맨 앞에 추가)
    # 사용할 메서드 삽입, 삭제,탐색, 출력
    # insert(front,back), deldete, search , display
    def insert_front(self, data):
        # 삽입 (맨 앞)
        new_node = Node(data)  # 새 노드 생성
        new_node.next = self.head  # 새 노드가 기존 head를 가리킴
        self.head = new_node  # head를 새 노드로 변경

    # 삽입 (맨 뒤)
    def insert_back(self, data):
        new_node = Node(data)

        if self.head is None:  # 리스트가 비어있으면
            self.head = new_node
            return

        # 마지막 노드 찾기
        current = self.head  # 헤드 (첫 노드) 부터 시작
        while current.next:  # next가 None이 아닐 때까지
            current = current.next  # 다음노드로 이동

        current.next = new_node  # 마지막 노드가 새 노드를 가리킴

    # 삭제 (값을 가진 노드를 삭제)
    def delete(self, data):
        if self.head is None:  # 빈 리스트
            return

        # 첫 번째 노드의 데이터가 삭제하려는 값과 같다면
        if self.head.data == data:  # 헤드를 다음 노드로 옮긴다.(제외 시킨다.)
            self.head = self.head.next
            return  # 함수 종료

        # 중간이나 끝 노드 삭제
        current = self.head  # 헤드 부터 시작해서
        while current.next:  # 다음 노드가 있을 때까지
            if current.next.data == data:  # 다음 노드가 삭제 대상이라면
                #  중간에 있는 [10],[15] 노드 삭제
                # (ex. [5 , 10, 15 ,20] > [5, 20])
                current.next = current.next.next  # 연결 건너뛰기
                return  # 함수가 종료 되고
            current = current.next  # 다음노드로 이동

    # 탐색 : 특정 값을 가진 노드 찾기
    def search(self, data):

        current = self.head  # 헤드부터 시작해서
        position = 0  # 찾으려는 위치 초기화

        while current:  # 노드가 있을때 까지 반복 수행
            if current.data == data:  # 찾았다면
                return position  # 위치 반환
            current = current.next  # 다음 노드로 이동
            position += 1  # 위치를 증가 시키고

        return -1  # 찾지 못한다면 -1 을 반환 시킨다.

    # 출력 : 리스트의 모든 노드 출력
    def display(self):
        if self.head is None:  # 리스트 가 비어있다면
            print("리스트가 비어있습니다.")  # 출력
            return

        current = self.head  # 헤드부터 시작
        result = []  # 결과를 담을 리스트
        while current:  # 노드가 있을 때 까지 반복수행
            result.append(str(current.data))  # 데이터를 문자 열로 추가
            current = current.next  # 다음노드를 이동하면서
        print(" → ".join(result))  # 화살표로 연결하며 출력한다.


# ==================== 더블리 링크드 리스트 ====================


# 클래스 생성
class DoubleNode:
    def __init__(self, data):
        self.data = data  # 데이터 저장
        self.prev = None  # 이전 노드를 가리키는 포인터
        self.next = None  # 다음 노드를 가리키는 포인터


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 시작점

    # 삽입 (맨 앞에 추가)
    def insert_front(self, data):
        new_node = DoubleNode(data)  # 새 노드 생성

        if self.head is None:  # 리스트가 비어있다면
            self.head = new_node  # 새 노드를 head로 설정
            return

        new_node.next = self.head  # 새 노드가 head를 가리킴
        self.head.prev = new_node  # 기존 head가 새 노드를 가리킴
        self.head = new_node  # head 를 새 노드로 변경

    # 삽입 (맨 뒤에 추가)
    def insert_back(self, data):
        new_node = DoubleNode(data)  # 새 노드를 head로 설정

        if self.head is None:  # 빈 리스트
            self.head = new_node  # 새 노드를 head 로 생성
            return

        # 마지막 노드 찾기
        current = self.head  # 헤드부터 시작
        while current.next:  # next 가 None이 아닐 때 까지
            current = current.next  # 다음 노드로 이동

        current.next = new_node  # 마지막 노드가 새 노드를 가리킴
        new_node.prev = current  # 새 노드가 이전 노드를 가리킴

    # 삭제 (특정 값을 가진 노드를 값으로 삭제)
    def delete(self, data):
        if self.head is None:  # 빈 리스트
            return

        current = self.head  # 헤드부터 시작

        # 첫 번째 노드가 삭제 대상
        if current.data == data:  # 첫번째 노드의 데이터가 삭제하려는 값과 같다면
            self.head = current.next  # head를 다음 노드로 변경
            if self.head:  # 다음노드가 있으면(head != None)
                self.head.prev = None  # 새 head 의 prev를 None 으로 설정
            return  # 함수종료

        # 중간이나 끝 노드 삭제
        while current:  # 노드가 있을때까지
            # 삭제 대상을 찾고, 이전 노드가 있다면
            if current.data == data:  # 삭제 대상을 찾았으면
                if current.prev:  # 이전 노드가 있으면
                    current.prev.next = current.next  # 이전 노드가 다음 노드를 가리킴
                if current.next:  # 다음 노드가 있으면
                    current.next.prev = current.prev  # 다음노드가 이전 노드를 가리킴
                return  # 함수종료
            current = current.next  # 다음 노드로 이동

    # 탐색 : 특정 값을 가진 노드 찾기
    def search(self, data):
        current = self.head  # 헤드부터 시작
        position = 0  # 위치값 초기화

        while current:  # 노드가 있을때 까지 반복수행
            if current.data == data:  # 찾았다면
                return position  # 위치를 반환
            current = current.next  # 다음노드로 이동
            position += 1  #  위치를 증가시키고

        return -1  # 찾지못했다면, -1을 반환

    # 출력 (정방향) , 리스트의 모든 노드 출력 (앞에서 뒤로)
    def display(self):
        if self.head is None:  # 리스트가 비어있다면
            print("리스트가 비어있습니다.")  # 출력
            return

        current = self.head  # 헤드 부터 시작
        result = []  # 결과 를 담을 리스트
        while current:  # 노드가 있을 때까지 반복수행
            result.append(str(current.data))  # 데이터를 문자열(str)으로 추가(append)
            current = current.next  # 다음 노드로 이동

        print(" ⇄ ".join(result))  # 양방향 화살표로 연결하며 출력

    # 출력 (역방향) , 리스트의 모든 노드 출력 (뒤에서 앞으로)
    def display_reverse(self):
        if self.head is None:  # 리스트가 비어있다면
            print("리스트가 비어있습니다.")  # 출력
            return

        # 마지막 노드로 이동
        current = self.head  # 헤드부터 시작
        while current.next:  # next가 None이 아닐 때까지 (마지막 노드까지) 반복
            current = current.next  # 다음노드 로 이동

        # 역방향 출력
        result = []  # 결과를 담을 리스트
        while current:  # 노드가 있을 때 까지 반복 수행
            result.append(str(current.data))  # 데이터를 문자열로 추가
            current = current.prev  # 역방향 : 이전 노드로 이동 역방향에서는 여기가 핵심

        print(" ⇄ ".join(result))  # 양방향 화살표로 연결하며 출력


#  실행 예시

if __name__ == "__main__":
    print("=" * 50)
    print("싱글리 링크드 리스트")
    print("=" * 50)
    sll = SinglyLinkedList()  # 싱글리 리스트 생성

    # 삽입
    sll.insert_back(10)
    sll.insert_back(20)
    sll.insert_back(30)
    sll.insert_front(5)

    print("리스트 출력:")
    sll.display()  # 5 → 10 → 20 → 30

    # 탐색
    print(f"\n20의 위치: {sll.search(20)}")  # 2
    print(f"100의 위치: {sll.search(100)}")  # -1

    # 삭제
    sll.delete(20)
    print("\n20 삭제 후:")
    sll.display()  # 5 → 10 → 30

    # ========여기서 부터 더블리==========
    print("\n" + "=" * 50)
    print("더블리 링크드 리스트")
    print("=" * 50)

    dll = DoublyLinkedList()

    # 삽입
    dll.insert_back(10)
    dll.insert_back(20)
    dll.insert_back(30)
    dll.insert_front(5)

    print("리스트 출력 (정방향):")
    dll.display()  # 5 ⇄ 10 ⇄ 20 ⇄ 30

    print("\n리스트 출력 (역방향):")
    dll.display_reverse()  # 30 ⇄ 20 ⇄ 10 ⇄ 5

    # 탐색
    print(f"\n20의 위치: {dll.search(20)}")  # 2

    # 삭제
    dll.delete(20)
    print("\n20 삭제 후:")
    dll.display()  # 5 ⇄ 10 ⇄ 30


"""
==================================================
싱글리 링크드 리스트
==================================================
리스트 출력:
5 → 10 → 20 → 30

20의 위치: 2
100의 위치: -1

20 삭제 후:
5 → 10 → 30

==================================================
더블리 링크드 리스트
==================================================
리스트 출력 (정방향):
5 ⇄ 10 ⇄ 20 ⇄ 30

리스트 출력 (역방향):
30 ⇄ 20 ⇄ 10 ⇄ 5

20의 위치: 2

20 삭제 후:
5 ⇄ 10 ⇄ 30



"""
