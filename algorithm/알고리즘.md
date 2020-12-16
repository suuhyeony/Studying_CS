## 알고리즘

### 1. 정렬

#### 01) 버블정렬

: 앞에서부터 두 개씩 차례대로 비교하면서 큰 값을 뒤에 놓음.

```python
def bubblesort(data):
    for index in range(len(data) - 1):
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index]
```

시간복잡도는 O(n^2) / 비효율적.



#### 02) 선택정렬

: 가장 작은 값과 첫번째 인덱스의 값을 스왑하며 정렬. (인덱스 범위는 한 개씩 줄어듦)

```python
def selection_sort(data):
    for stand in range(len(data)):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data
```

시간복잡도는 O(n^2)

최악의 경우 (23451)



#### 03) 삽입정렬

: 2번째 값부터 시작해 앞데이터와 값을 비교. 

자신이 더 작으면(스왑 후) 또 그 앞데이터와 값을 비교. 

비교할 데이터가 더 이상 없거나 자신이 더 크면 멈추고 다음 턴.

```python
def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data
```

시간복잡도는 O(n^2)

최악 (54321)



#### 04) 퀵정렬

: 기준점(pivot)을 놓고 작은 값은 왼쪽에, 큰 값은 오른쪽에 놓는 과정을 재귀적으로 반복.

최종적으로 병합.

```python
def qsort(data):
    if len(data) <= 1:
        return data
    
    left, right = list(), list()
    pivot = data[0]
    
    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    return qsort(left) + [pivot] + qsort(right)
```

```python
# list comprehension 사용
def qsort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]
    
    return qsort(left) + [pivot] + qsort(right)
```

시간복잡도는 O(n log n)

맨 처음 pivot이 가장 크거나 작으면, 모든 데이터를 비교하는 상황이 나옴 => O(n^2)



#### 05) 병합정렬 (분할정복)

: 데이터를 두 부분으로 나누고, 쪼갤 수 있을 때까지 쪼갬.

포인터를 활용해 두 부분의 데이터를 정렬하며 병합.

```python
def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    
    #case1: left/right 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1
            
    #case2: left만 남아있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
    
    #case3: right만 남아있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
        
    return merged

def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)
```

시간복잡도는 O(n log n)



- 복잡성
  - 단순 : 선택, 삽입, 버블, 쉘 (보통 O(N^2))
  - 복잡 : 퀵, 기수, 힙, 병합 (NlogN)

---



### 2. 재귀용법 (recursive call, 재귀 호출)

: 함수 안에서 동일한 함수를 호출하는 형태

(내부적으로 스택처럼 관리됨)

```python
# 일반적인 형태1
def function(입력):
    if 입력 > 일정값:				# 입력이 일정값 이상이면
        return function(입력 - 1)	  # 입력보다 작은 값
    else:
        return 일정값/입력값/특정값	  # 재귀호출 종료

# 일반적인 형태2
def function(입력):
    if 입력 <= 일정값:
        return 일정값/입력값/특정값
    function(입력보다 작은 값)
    return 결과값

# 팩토리얼 함수 구현
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num
def factiorial(num):
    if num <= 1:
        return num
    return num * factorial(num - 1)

# 리스트의 합을 리턴하는 함수
def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])

# 펠린드롬 판별 함수
def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
```

시간복잡도는 O(n-1)

파이썬에서 재귀함수의 깊이는 한 번에 1000회 이하가 되어야 함.

-> 제한 공간 늘리기

```python
import sys
sys.setrecursionlimit(1000000)
```

---



### 3. 동적 계획법(DP)과 분할정복

#### 01) 동적계획법(Dynamic Programming)

: 입력 크기가 작은 부분 문제들을 해결한 후, 그 해를 활용해 상위 문제를 해결 (상향식 접근법)

이를 위해, **Memoization**(이전에 계산한 값을 저장해 다시 계산하지 않도록 함)을 이용. ex) 피보나치 수열

부분 문제는 중복되어, 상위 문제 해결 시 재활용됨

```python
# 피보나치 수열
def fibo_dp(num):
    # memoization 기법 (재귀호출보다 빠름)
    cache = [0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1
    
    for index in range(2, num + 1):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num]
```



#### 02) 분할정복 (Divde and Conquer)

: 문제를 나눌 수 없을 때까지 잘게 쪼개서 각각을 푼 뒤, 다시 합병하여 답을 찾음

상위의 답을 구하기 위해 아래로 내려감 (하향식 접근법)

- Divide ) 문제를 하나 또는 둘 이상으로 나눈다.
- Conquer ) 나눠진 문제가 충분히 작고 해결 가능하다면 해결. 그렇지 않다면 다시 나눈다. 

**재귀함수**로 구현. 

문제를 잘게 쪼갤 때, 부분 문제는 서로 중복되지 않음 -> Memoization 사용 안함

ex) 병합정렬 참고

---

### 4. 탐색

#### 01) 이진 탐색

: 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법.

데이터가 정렬되어 있다면, 순차 탐색보다 빠름.

- Dived ) 리스트를 두 개의 서브 리스트로 나눈다.

- Conquer ) 검색할 숫자 > 중간값이면, 뒷 부분의 서브 리스트에서 검색.

  ​                   검색할 숫자 < 중간값이면, 앞 부분의 서브 리스트에서 검색.

```python
def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False
    
    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)
```

시간복잡도는 O(logn)



#### 02) 순차 탐색

: 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾음.

```python
from random import

rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1,100))
    
def sequencial(data_list, search_data):
    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index
    return -1
```

- 시간복잡도) 최악의 경우 리스트 길이가 n일 때, O(n)



### 5. 그래프 탐색

---

#### -그래프

: 실제 세계의 현상이나 사물을 정점/노드와 간선으로 표현한 것.

- 노드 (Node) - 위치를 말함. 정점(vertex)라고도 함.
- 간선 (Edge) - 위치 간의 관계를 표시한 선 (노드를 연결한 선). link/branch



**종류)**

**무방향 / 방향 그래프**

**가중치 그래프** / 네트워크 (간선에 비용/가중치가 할당된 그래프)

연결 / 비연결 그래프

사이클, 비순환 그래프

완전 그래프 (그래프의 모든 노드가 서로 연결되어 있는 그래프)



**그래프와 트리의 차이**

: 트리는 그래프에 속한 특별한 종류

- 방향성이 있는 비순환 그래프 (방향 그래프만 존재, 사이클 존재X)
- 루트 노드 존재
- 부모 자식 관계 존재

```python
# 딕셔너리로 그래프 구현
from collections import defaultdict

graph = defaultdict(list)
for _ in range(len(edge)):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 리스트로 구현
graph = [[] for _ in range(len(node) + 1)]
for _ in range(len(edge)):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
```





#### 01) 너비 우선 탐색 (BFS - Breadth First Search)

: 한 단계씩 내려가면서, 해당 노드와 같은 레벨의 노드들(형제노드)부터 먼저 순회.

자료구조 큐를 사용.

```python
def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    
    need_visit.append(start_node)
    
    while need_visit:
        cur_node = need_visit.pop(0)
        if cur_node not in visited:
            visited.append(cur_node)
            need_visit.extend(graph[cur_node])
    return visited
```

시간복잡도는 O(V + E)



#### 02) 깊이 우선 탐색(DFS - Depth First Search)

: 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 순회.

스택(need_visit)과 큐(visited)를 활용함.

```python
def dfs(graph, start_node):
    need_visit, visited = list(), list()
    
    need_visit.append(start_node)
    
    while need_visit:
        cur_node = need_visit.pop()
        if cur_node not in visited:
            visited.append(cur_node)
            need_visit.extend(graph[cur_node])
    return visited
```

시간복잡도는 O(V + E)



#### 03) 최단 경로

: 두 노드를 잇는 가장 짧은 경로를 찾는 것. 가중치 그래프에서 간선의 가중치 합이 최소가 되도록 하는 경로를 찾아야 함.

**종류)**

-  단일 출발 및 단일 도착 (1-1)
- 단일 출발 최단 경로 문제 (특정 노드와 그 나머지 노드들 간 최단 거리)

- 전체 쌍 최단 경로 (u, v)



#### -다익스트라 알고리즘

: 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신. (BFS와 유사)



우선순위 큐(MinHeap)를 활용, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨. -> 거리가 긴 경로는 나중에 계산할 필요 없이 민힙 이용.



- 첫 정점을 기준으로 배열을 선언해, 첫 정점에서 각 정점까지의 거리를 저장.

  -초기에 첫 정점의 거리는 0, 나머지는 무한대 inf로 저장함

  -우선순위 큐에 (첫 정점, 거리 0) 만 먼저 넣음

- 우선순위 큐에서 노드를 꺼냄 (우선순위 큐에 꺼낼 노드가 없을 때까지 반복)

  -처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
  
  -첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 (첫 정점에서 각 정점까지의) 거리를 비교.
  
  -배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트
  
  -배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.
  
  ​	-> 결과적으로 BFS와 유사하게, 첫 정점에 인접한 노드들을 순차적 방문
  
  ​	-> 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다 더 긴 거리를 가진 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음.



```python
# 그래프 만들기
mygraph = {
    'A':{'B':8, 'C':1, 'D':2},
    'B':{},
    'C':{'B':5, 'D':2},
    'D':{'E':3, 'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

# 알고리즘 구현
import heapq

def dijkstra(graph, start):
    distances = {node:float('inf')for node in graph}
    queue = []
    
    distances[start] = 0
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        cur_distance, cur_node = heapq.heappop(queue)
        
        if distances[cur_node] < cur_distance:
            continue
            
        for adj, weight in graph[cur_node].items():
            distance = cur_distance + weight
            
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(queue, [distance, adj])
    return distances

dijkstra(mygraph, 'A')
```

**시간복잡도**

​	과정1) 각 노드마다 인접한 간선들을 모두 검사 => O(E)

​	과정2) 우선순위 큐에 노드/거리 정보를 넣고 pop하는 과정 

​				=> 추가 시간은 O(E),  우선순위 큐를 유지하는 시간은 O(logE).

​					 즉, O(ElogE)

​	총 O(E) + O(ElogE) = **O(ElogE)** 





### 6. 탐욕 (Greedy)

---

: 최적의 해에 가까운 값을 구하기 위해 사용.

여러 경우 중 하나를 결정해야 할 때마다, 매순간 최적이라고 생각되는 경우를 선택해, 최종 값을 구함.

```python
# 동전문제
coin_list = [500, 100, 50, 1]

def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_coin_count, details

# 부분 배낭 문제 (w, v)
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()
    
    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details 
```

한계) 항상 최적의 해를 구하는 것은 아님(근사치 추정)



### 7. 백트래킹 (backtracking)

---

: 제약 조건 만족 문제에서 해를 찾기 위한 전략

해를 찾기 위해, 후보군에 제약 조건을 점진적으로 체크하다가, 해당 후보군이 제약 조건을 만족할 수 없다고 판단되는 즉시, backtrack(다시는 이 후보군을 체크하지 않을 것을 표기)하고, 바로 다른 후보군으로 넘어가며, 결국 최적의 해를 찾는 방법.



실제 구현 시, 고려할 수 있는 모든 경우의 수(후보군)를 **상태 공간 트리**(문제해결 과정의 중간 상태를 각각의 노드로 나타낸 트리)를 통해 해결

- 각 후보군을 DFS 방식으로 확인
- 상태공간 트리를 탐색하면서, 제약이 맞지 않으면 해의 후보가 될만한 곳으로 바로 넘어가서 탐색
  - promising : 해당 루트가 조건에 맞는지를 검사하는 기법
  - pruning(가지치기) : 조건에 맞지 않으면 포기하고 다른 루트로 바로 돌아서서, 탐색 의 시간을 절약하는 기법

즉, 백트래킹은 트리 구조를 기반으로 DFS로 깊이 탐색을 진행하면서, 각 루트에 대해 조건에 부합하는지 체크(Promising), 만약 해당 트리(나무)에서 조건에 맞지 않는 노드는 더 이상 DFS로 깊이 탐색을 진행하지 않고, 가지를 쳐버림(Pruning) 



```python
# N Queen 문제 (N X N 크기의 체스판에 N개의 퀸을 서로 공격할 수 없도록 배치)
def is_available(candidate, cur_col):
    cur_row = len(candidate)
    for queen_row in range(cur_row):
        if candidate[queen_row] == cur_col or abs(cadidate[queen_row] - cur_col) == cur_row - queen_row:
            return False
    return True

def DFS(N, cur_row, cur_candidate, final_result):
    if cur_row == N:
        final_result.append(cur_candidate[:])
        return
    
    for candidate_col in range(N):
    	if is_available(cur_candidate, candidate_col):
            cur_candidate.append(candidate_col)
            DFS(N, cur_row + 1, cur_candidate, final_result)
            cur_candidate.pop()
            
def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result
```





