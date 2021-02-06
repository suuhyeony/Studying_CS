## JavaScript

### 1. Call Stack

: 자바스크립트가 함수 실행을 핸들하는 방법 중 하나. (한 번에 하나의 task만 처리)

자바스크립트는 스택 위에 함수를 올려 실행하고, 끝나면 스택에서 제거한다.

요청이 들어올 때마다 해당 요청을 순차적으로 call stack에 담아 처리하는 것이다. 한 번에 하나의 task만 처리하고, 이를 single thread 기반의 call stack을 가진다고 한다.

예를 들어 보면,

```javascript
function three() {				// 5. three 함수가 맨 위에 쌓임
    console.log('I love JS..');	//    실행중.. (콘솔창에 메시지가 출력됨)
}								//    함수 종료-> stack에서 제거됨
function two() {				// 4. two 함수가 그 위에 쌓임
    three();					//    실행중.. (three 함수 호출)
}								// 6. 함수 종료-> stack에서 제거됨
function one() {				// 3. one 함수가 그 위에 쌓임
    two();						// 	  실행중.. (two 함수 호출)
}								// 7. 함수 종료-> stack에서 제거됨
function zero() {				// 2. zero 함수가 stack에 쌓임
    one();						//    실행중.. (one 함수 호출)
    throw Error('error')		// 8-1. 에러발생
}								// 8-2. (에러x)함수 종료-> stack에서 제거됨
								// 9. call stack이 비워짐
zero();							// 1. zero 함수 호출
```

1~9번까지 **순서대로** 실행된다.

maximum call stack 제한이 있음.



### 2. Event Loop

: 자바스크립트 엔진은 하나의 스레드에서 동작. (stack이 하나, 한번에 하나의 작업만 할 수 있음.)

하지만, **Event Loop와 queue를 통해 비동기 작업이 가능**하다. (JS는 non-blocking 언어)

- blocking vs non-blocking

: JS는 non-blocking언어. (python은 blocking언어)

JS 가 non-blocking이기 때문에 브라우저가 다른 일을 할 때도 유저는 input창에 입력을 할 수 있다. (유저 인풋, 이벤트, fetch.. 등) 

*예외) alert 발생하면 아무 것도 할 수 없음



(그림)

- **Event loop** : 계속 반복해서 call stack과 queue 사이의 작업들을 확인하고, **call stack이 비워져 있으면**, queue에서 작업을 꺼내 call stack에 넣는다.
- queue : 비동기 작업을 위해 작업을 담아둘 곳. 
  - microtask queue -> animation frames -> task queue 순으로 진행

ex. setTimeout()이 발생했을 때, 먼저 call stack에 올리고 -> web API에 호출(콜백 전달) -> call stack 에서 setTimeout()을 pop -> web API에서 예약된 시간이 되면, task queue에 해당 작업 올림 -> (주체: event loop) call stack이 비어있으면, 해당 작업을 call stack에 올림.



### 3. Hoisting

: 끌어올리기. 변수의 정의가 그 범위에 따라 선언과 할당으로 분리되는 것.

`var`키워드로 선언된 모든 변수 선언은 호이스트된다.

- 선언 : `var x;`이 부분이 끌어올려진다!

  ​           선언문은 항시 자바스크립트 엔진 구동시 가장 최우선으로 해석되므로 호이스팅됨.

- 할당 : `x = 10;` 할당 구문은 런타임 과정에서 이루어지기 때문에 호이스팅 되지 않는다.

```javascript
function getX() {
    console.log(x);  // undefined
    var x = 10;      
    console.log(x);  // 10
}

getX();

// 작동 순서에 맞게 바꾸면
function getX() {
    var x;
    console.log(x);
    x = 10;
    console.log(x);
}

getX();

// 함수 호이스팅 (함수에 대한 선언을 호이스팅하여 global 객체에 등록시킴)
foo();
function foo() {
    console.log('hi');
}
// hi

// 함수를 변수에 할당 시 (함수 리터럴을 할당하기 때문에 호이스팅X)
foo();
function foo = function() {
    console.log('hi');
}
// Uncaught TypeError: foo is not a function
```

`let`이나 `const`는 호이스팅을 지원하지 않는 것이 아니라, 여기에 변수가 선언되기 전에는 그 변수를 실행할 수 없다는 기능을 추가한 것이다!

