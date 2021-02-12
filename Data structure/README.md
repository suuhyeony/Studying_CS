## 자료구조

### 시간 복잡도

- 입력의 크기가 커질수록 반복문이 알고리즘 수행 시간을 지배함
- Big O 표기법: O(N)
  - 알고리즘 최악의 실행 시간을 표기
  - 아무리 최악이라도, 이 정도의 성능을 보장한다는 의미
  - 입력 n에 따라 결정되는 시간 복잡도 함수
  - O(1) < O(logN) < O(N) < O(NlogN) < O(N^2) < O(2^N) < O(N!)
- 계산 방식
  - O(1) : if문
  - O(n) : for, while문
  - O(n^2) : for문이 두 번



### 1. 배열 (Array)

: 순차적으로 연결된 공간에 데이터를 나열. 각 데이터를 인덱스에 대응하도록 구성한 자료구조. `data = [1, 2, 3]`

- **논리적 저장 순서 = 물리적 저장 순서**

- **인덱스를 통해 해당 원소에 빠른 접근 가능** (random access가능 => O(1))
- 삽입/삭제가 쉽지 않다 (해당 원소에 접근해 작업한 뒤, `shift`로 인덱스 정리까지 해야하므로 => O(n))



### 2. 링크드 리스트 (Linked List)

: 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리. (파이썬에서는 리스트 타입이 링크드 리스트의 기능을 모두 지원) 배열의 단점을 극복하고자 탄생한 자료구조.

- 각각의 원소들은 **자기 자신 다음에 어떤 원소인지만을 기억**하고 있음
- 논리적 저장 순서 != 물리적 저장 순서

- 노드) 데이터 저장 단위(데이터값, 포인터)로 구성
- **포인터**) 각 노드 안에서, 다음이나 이전 노드와의 연결 정보(주소값)를 가지고 있는 공간
- 장점
  - 데이터 **공간을 미리 할당하지 않아도 됨**
  - 다음 값만 다른 값으로 바꿔주면 삭제/삽입을 O(1)만에 해결 가능! (하지만 search 과정 때문에 결국 O(n)이 걸림)
- 단점
  - 결국 원하는 위치를 찾는 과정에 있어 **첫 번째 원소부터 다 확인해봐야 함** => O(n)
- 트리의 근간이 되는 자료구조

```python
# node 구현 (객체 활용)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
# node와 node 연결하기
node1 = Node(1)
node2 = Node(2)
node1.next = node2  #포인터 연결
head = node1   #처음 값을 알아야 다음 작업 가능

# 데이터 추가하기
def add(data):
    node = head  #시작 값 설정
    while node.next:  #다음 포인터가 없을 때까지
        node = node.next  #포인터 넘겨주기
    node.next = Node(data)  #다음 포인터 없으면, 새 데이터를 노드로 추가
    
# 정리
node1 = Node(1)
head = node1
for index in range(1, 10):
    add(index)
    
# 데이터 검색
node = head
while node.next:
    print(node.data)  #데이터 출력
    node = node.next  #포인터 옮겨주고
print(node.data)  #마지막 데이터까지 꼼꼼히 출력

# 노드를 중간에 추가하기
node3 = Node(1.5)  #중간에 추가할 노드

node = head
search = True  #플래그 (바로 앞 노드를 찾기위한)
while search:
    if node.data == 1:  #바로 앞 노드를 찾았으면 while문 빠져나옴
        search = False
    else:
        node = node.next  #포인터 옮기기
node_next = node.next  #앞 노드의 포인터를 잠시 다른 곳에 저장
node.next = node3  #앞 노드의 포인터를 새로운 노드의 주소값으로 변경
node3.next = node_next  #이전 주소값을 새 노드의 주소값으로 변경 

# 총정리
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
        
    def description(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            
# 특정노드 삭제
def delete(self, data):
    if self.head.data == data:  #삭제할 노드가 헤드라면
        temp = self.head
        self.head = self.head.next
        del temp
    else:  #삭제할 노드가 중간/마지막이라면
        node = self.head
        while node.next:
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                del temp
                return
            else:
                node = node.next
```



#### 더블 링크드 리스트

: 포인터가 양쪽에 존재. (**이전 데이터 주소 + 데이터 + 다음 데이터 주소**)

=> 맨 뒤에서부터도 데이터를 찾아갈 수 있다. (뒤에서 가까울 시 유리)

```python
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
     
    def description(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
```



### 3. Stack

: 데이터를 제한적으로 접근할 수 있는 구조. (한쪽 끝에서만 자료를 넣거나 뺄 수 있다.)

가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조 (**LIFO** 정책)

컴퓨터 내부의 **프로세스 구조의 함수 동작 방식**.

```python
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)
        
        
recursive(4)  #4 3 2 1 0 ended 
#returned 0 returned 1 returned 2 returned 3 returned 4 
```

- 장점
  - 구조가 단순해 구현이 쉽다.
  - **데이터 저장/읽기 속도가 빠르다**.
- 단점
  - 데이터 최대 갯수를 미리 정해야 한다. (파이썬의 경우 재귀함수는 1000번까지만 호출 가능)
  - **저장공간의 낭비**가 발생할 수 있음. (미리 최대 개수만큼 저장 공간을 확보해야 하므로)



```python
# 메서드 활용
data_stack = list()

data_stack.append(1) #[1]
data_stack.append(2) #[1, 2]

data_stack.pop()  #2


# 직접 구현
stack_list = list()

def push(data):
    stack_list.append(data)
    
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pop()  #9
```





### 4. Queue

: 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조 (FIFO 방식)

멀티태스킹을 위한 **프로세스 스케줄링 방식**을 구현하기 위해 사용됨.

```python
# 1) 일반적인 큐 (FIFO)
import queue

data_queue = queue.Queue()
data_queue.put("hi") #["hi"]
data_queue.put(2)  #["hi", 2]
data_queue.qsize()  #2
data_queue.get() #"hi"

# 2) LIFO queue
import queue

data_queue = queue.LifoQueue()
data_queue.put("hi")
data_queue.put(2)  #["hi", 2]
data_queue.get()  #2

# 3) Priority Queue (우선순위에 따라 데이터를 추출)
import queue

data_queue = queue.PriorityQueue()
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.get()  #(5, 1)  => 숫자가 낮아야 우선순위가 높은 것임.

# 직접 구현
queue_list = list()

def enqueue(data):
    queue_list.append(data)
    
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data
```



