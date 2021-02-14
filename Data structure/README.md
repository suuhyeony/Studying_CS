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





### 5. Hash Table

: key에 value를 저장하는 데이터 구조. key값의 연산에 의해 직접 접근이 가능한 데이터 구조.

- key를 통해 바로 데이터를 받아올 수 있어 검색 속도가 획기적으로 빨라짐.
- 보통 배열로 미리 hash table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법 = 공간을 늘림으로써 해시테이블 충돌을 막아 탐색 시간 빠르게 함)
- 파이썬의 Dictionary 타입.



-용어)

- Hash - 임의 값을 고정 길이로 변환하는 것.
- 해싱 함수 - key에 대해 산술 연산을 이용해 데이터 위치를 찾는 함수
- 해쉬 값 / 해쉬 주소 - 해싱 함수의 결과 값
- 슬롯 - 한 개의 데이터를 저장할 수 있는 공간



```python
# hash table 만들기
hash_table = [0 for _ in range(10)]

# hash function 만들기 (division방법)
def hash_func(key):
    return key % 5

# 저장
data1 = 'A'
data1 = 'D'
data3 = 'T'
# 아스키 코드를 key값으로 활용
print(ord(data1), ord(data2), ord(data3)) # 65 68 84
print(ord(data1), hash_func(ord(data1))) # 65 0

# hash table에 값 저장하는 함수
def storage_data(data, value):
    key = ord(data[0])  # data를 가지고 key값을 만듦
    hash_address = hash_func(key)  # key값을 가지고 해싱함수를 통해 주소를 알아냄
    hash_table[hash_address] = value  # 해시 테이블에서 해당 주소를 찾아 값을 저장

storage_data('Suhyeon', 20)

# 데이터를 읽어오기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

get_data('Suheyon')  # 20
```



- 장점
  - 데이터 저장/읽기 속도가 빠르다.
  - 해쉬는 키에 대한 중복 확인이 쉽다.
- 단점
  - 일반적으로 저장 공간이 좀 더 많이 필요하다.
  - **여러 키에 해당하는 주소가 동일할 경우, 충돌을 해결하기 위한 별도 자료구조가 필요**.
- 주요 용도
  - 검색이 많이 필요한 경우
  - 저장, 삭제, 읽기가 빈번한 경우
  - 캐쉬 구현 시 (중복 확인이 쉽기 때문)

```python
# 파이썬에서 사용
hash_table = [0 for _ in range(8)]

def get_key(data):
    return hash(data)

def hash_func(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_func(get_key(data))
    hash_table[hash_address] = value
    
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]
```



#### 해쉬 충돌(hash collision) 해결 알고리즘

1. **Chaining 기법 (Open hashing 기법)** : 해쉬 테이블 저장공간 외의 공간 활용. 충돌이 일어나면, 링크드 리스트 자료구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결.

2. **Linear Probing 기법 (Close hashing 기법)** : 해쉬 테이블 저장공간 안에서 빈 공간을 찾아 충돌 문제를 해결. 충돌이 일어나면, 해당 hash address의 다음 address부터 탐색하며, 맨 처음 나오는 빈공간에 저장. (저장 공간 활용도를 높이기 위함)

```python
# 1) chaining 기법 (기존 코드에 추가)
def save_data(data, value):
    index_key = get_key(data)  # 중복 데이터를 구별하기 위해 정보를 하나 더 추가
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:  # 데이터가 이미 있다면,
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key: # key값 중복 시
                hash_table[hash_address][index][1] = value # value를 덮어 씌움
                return
        hash_table[hash_address].append([index_key, value]) # key값 다르면 뒤에 추가
    else: # 데이터가 없으면
        hash_table[hash_address] = [index_key, value] # 테이블의 주소에 그냥 저장

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
    
    
# 2) Linear Probing 기법
def save_data(data, value):
    index_key = get_key(data)  # 중복 데이터를 구별하기 위해 정보를 하나 더 추가
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:  # 데이터가 이미 있다면,
        for index in range(hash_address, len(hash_table)):  # 검색 시작
            if hash_table[index] == 0:  # 데이터가 없으면,
                hash_table[index] = [index_key, value]  # 데이터 추가
                return
            elif hash_table[index][0] == index_key:  # key값이 같으면
                hash_table[index][1] = value  # 데이터 덮어씌움
                return
    else: # 데이터가 없으면
        hash_table[hash_address] = [index_key, value] # 테이블의 주소에 그냥 저장

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:  # 저장된 적이 없다면,
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None
```



3. 빈번한 충돌 개선하기

​      => hash table의 저장공간을 확대!



- 시간 복잡도
  - 일반적인 경우(충돌X) => O(1)
  - 최악의 경우(모두 충돌) => O(n)