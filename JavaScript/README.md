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

- : 끌어올리기. (변수의 정의가 그 범위에 따라 선언과 할당으로 분리되는 것.)

  스코프 내부 어디서든 변수 선언은 최상위에 선언된 것처럼 행동!

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



### 4. Closure

: **함수와 그 함수가 실행될 범위의 연결**. (외부 함수에 접근할 수 있는 내부 함수 혹은 이러한 원리)

- 스코프에 따라 내부함수의 범위에서는 외부 함수 범위에 있는 변수에 접근이 가능하지만, 그 반대는 실현이 불가 (**변수를 은닉화**할 수 있다.)
- 외부함수는 외부함수의 지역변수를 사용하는 내부함수가 소멸될 때까지 소멸되지 않음. (변수 캡쳐)
- JS에서는 **함수를 리턴할 때, 클로저를 형성**하고, 이 때 **함수와 함수가 선언된 어휘적 환경의 조합(당시 관계되는 코드들)의 참조를 기억**한다.



#### 언제 사용할까?

- 어떤 데이터와 그 데이터를 조작하는 함수를 연관시켜줄 때 (이벤트 함수)
- 정보 은닉 : private 변수를 만들고, 익명 함수에서 반환된 퍼블릭 함수를 통해서만 접근 가능
- 캡슐화 : 고유의 클로저를 통한 변수의 다른 버전을 참조. (하나의 클로저에서 변수 값을 변경해도, 다른 클로저의 값에는 영향을 주지 않음)



### 5. this

: JS에서 모든 함수는 실행될 때마다 함수 내부에 `this`라는 객체가 추가된다. `arguments`라는 유사 배열 객체와 함께 함수 내부로 암묵적으로 전달되는 것. 따라서 'this'의 값은 **함수를 호출한 방법에 의해 결정**된다. 즉, 어떻게 함수를 호출했느냐에 따라 'this'의 값이 바뀐다.

```javascript
const name = 'window';

function log() {
    console.log(this.name); // this는 대부분 객체이다.
}

const obj = {
    name: 'dotgae',
    logName: log
};

log();  // window
obj.logName();  // dotgae
```



#### this를 실행하는 4가지 방법

```javascript
// 1. Regular function call (일반함수 실행)
// 1-1) 일반모드일 때, this는 window 객체
const age = 100;
function foo() {
    const age = 99;
    bar();  // 일반함수 실행 방법!
}

function bar() {
    console.log(this.age);  // 'this' === global object (window 객체)
}

foo();  // 100


// 1-2) strict 모드일 때, this는 undefined
'use strict';
const name = 'dotgae';
function foo() {
    console.log(this.name);  // 'this' === undefined
}

foo();  // undefined


// 2. Dot Notation (객체의 메서드를 호출할 때)
function foo() {
    console.log(this.age);
}
const age = 100;
const dotgae = {
    age: 20,
    foo: foo
};
const jun = {
    age: 30,
    foo: foo
};

dotgae.foo();  // 20 ('this' === .앞의 객체를 가리킴)
jun.foo();  // 30


// 3. call, bind, apply 사용 (상황에 의존하지 않고 this를 JS코드로 주입/설정 가능)
// 3-1) call, apply (인수가 하나일 때)
const age = 100;
function foo() {
    console.log(this.age);
}
const dotgae = {
    age: 20
};
const jun = {
    age: 30
};

foo();  // 100
foo.call(jun);  // 30  (foo 함수를 실행할 때 인자로 jun을 넘겨주어 'this' === jun)
foo.apply(dotgae);  // 20 (위와 같다)

// 3-2) call, apply (인수가 두 개 이상일 때)
const age = 100;
function foo(a, b, c, d) {
    console.log(this.age);
    console.log(arguments);
}
const dotgae = {
    age: 20
};

foo.call(dotgae, 'cute', 'smart', 'dev', 'intp')
// 첫번째 인수인 dotgae를 인자로 넘겨주어 'this' === dotgae  // 20
// 나머지 인수들은 foo 함수의 인자로 차례대로 넘어간다.  // [뒤에 것들 다] 출력
foo.apply(dotgae, ['cute', 'smart', 'dev', 'intp'])
// apply는 인수를 두 개만 설정 가능!! 기능은 call과 같음
// 20, ['cute', 'smart', 'dev', 'intp']

// 3-3) bind
const age = 100;
function foo() {
    console.log(this.age);
};
const dotgae = {
    age: 20
};
const bar = foo.bind(dotgae);  // 'this'값을 dotgae로 bind 시켜놓고, 함수를 리턴
bar();  // 20


// 4. 'new' keyword (생성자 함수를 통해 객체를 생성할 때)
// 4-1)
function foo() {
    // 2) this = {};
    this.name = 'dotgae';
    // 3) {name: 'dotgae'}
    // 4) return this; // 자동으로 this 객체를 리턴해줌
}

const dev = new foo();  // 1) 'this'에는 빈 객체가 할당되어 새 함수를 리턴함!
console.log(dev);  // {name: 'dotgae'}

// 4-2)
function Person(name, age) {
    this.name = name;
    this.age = age;
}
const dotgae = new Person('dotgae PARK', 20);
const jun = new Person('junho', 30);

console.log(dotgae);  // 'dotgae PARK', 20
console.log(jun);  // 'junho', 30
```

#### bind

: 함수를 어떻게 호출했느냐와 상관없이 this값을 설정할 수 있는 메서드.

- this는 원본 함수를 가진 새로운 함수를 생성한다.
- 함수를 **선언**할 때, this와 파라미터를 지정해줄 수 있다. `function(val1, val2) {}.bind(this, 1, 2)`

*apply, call은 함수를 **호출**할 때, this와 파라미터를 지정.