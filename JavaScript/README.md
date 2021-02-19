## JavaScript

### 0. 데이터 타입

: 자바스크립트에는 원시타입(primitive type)과 참조타입(reference type)이라는 자료형이 존재.

- 원시타입(primitive type) - number, string, boolean, null, undefined, symbol
  - 자바스크립트에서 사용할 수 있는 데이터 및 정보의 가장 단순한 형태 (객체가 아닌 것들. 값 그 자체로 저장된 것, original type)
  - 변수에 할당될 때, 메모리 상에 고정된 크기로 저장됨
  - 해당 변수가 원시 데이터 값을 보관 (값이 복사됨)
  - 비교 시, 저장된 값을 비교
- 참조타입(reference type) - 객체 (배열, 함수, 정규표현식)
  - 크기가 정해져 있지 않음
  - 변수에 할당될 때, 값이 직접 해당 변수에 저장될 수 없음 (변수에는 데이터에 대한 참조만 저장. 즉, 참조는 참조타입 데이터의 주소이지 해당 데이터의 값이 아님!)
  - 비교 시, 저장되어 있는 참조(메모리의 번지수)를 비교



#### 원시타입 종류

#### -number

: 다른 언어와는 달리(길이를 미리 정해줌), 자바스크립트에는 number type이 하나임.

#### -boolean

- false - 0, null, undefined, NaN(망한 결과값. 말이 안되는 값), ' '
- true - 다른 모든 값

#### -undefined

: 변수가 선언되었으나, 아직 할당되지 않음.  (아직 뭘 넣을지 안 정함)

```javascript
let hello;
console.log(hello === undefined)      // true
console.log(hello === null)      	  // false
```

#### -null

: 빈 값. 변수에 값이 텅텅 비어지게 할당한 것. (이 자체가 값이다!!) (아무 것도 담지 않기로 함)

```javascript
let hello;
hello = null
console.log(hello === null)           // true
```

#### -symbol

: 고유한 식별자가 필요하거나, 동시 다발적으로 일어나는 코드에서 우선순위를 주고 싶을 때 사용

`const symbol1 = Symbol('id')` 동일한 string으로 작성해도, 다른 symbol로 만들어짐



*JS는 동적타이핑 언어이다. 변수의 타입을 선언하지 않아도, 런타임 때 변수의 타입이 자동으로 파악됨. 하나의 변수에 여러 타입의 값을 넣을 수 있음. (문제 발생 => 타입스크립트 사용)

<br>

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

<br>

### 2. 변수 (var / let / const), scope

#### 변수의 생성과정

1) 선언 단계 - `let x;`

2) 초기화 단계 - undefined를 할당해주는 단계

3) 할당 단계 - `x = 10;`



#### scope

: 변수에 접근할 수 있는 범위. (한마디로 '너의 variable'이 존재하는가?)

1) 함수 스코프 : 함수 내에서 선언된 변수만 그 지역변수가 되는 것. => 유일하게 벗어날 수 없는 스코프가 함수

2) 블록 스코프 : 변수는 코드블록 내에서만 유효하며, 밖에서 접근할 수 없음.



- **var** : 선언과 초기화가 한번에 된다. **함수 스코프**이다.

  ```javascript
  // 1) 한번 선언된 변수를 다시 선언할 수 있다.
  var name = 'cardi';
  console.log(name);  // cardi
  
  var name = 'maegan';
  console.log(name);  // maegan
  
  // 2) 선언하기 전에 사용할 수 있다. (hoisting)
  console.log(name);  // undefined (선언은 호이스팅O, 할당은 호이스팅X)
  
  var name = 'cardi';  // 할당
  
  // 3) 함수 스코프이다.
  // if문에서는 외부에서 지역변수에 접근 가능
  const age = 30;
  if (age > 19) {
      var txt = '성인';
  }
  console.log(txt);  // '성인'
  
  // 함수 안의 지역 변수는 외부에서 접근 불가
  function add(num1, num2) {
      var result = num1 + num2;
  }
  
  add(2, 3);  // 5
  console.log(result); // 참조 에러
  ```

  let과 const는 TDZ(Temporal Dead Zone)의 영향을 받기 때문에 할당을 하기 전에는 변수를 사용할 수 없다.

  

- **let** : 선언과 초기화 단계가 분리되어 실행됨. **블록 스코프**이다.

  ```javascript
  // 
  let name = 'cardi';
  console.log(name);  // cardi
  let name = 'doja';
  console.log(name);  // syntax에러
  
  //
  console.log(name);
  let name = 'cardi';  // 참조 에러
  ```

  

  호이스팅되면서 선언 단계가 발생하지만, 초기화는 실제 코드에 도달했을 때 발생하기 때문에 참조 에러가 나는 것.

- **const** : 선언 + 초기화 + 할당이 모두 같이 되어야 함.  `const hello = 'hi';`

  **블록 스코프**이다.

<br>

### 3. Event Loop

: 자바스크립트 엔진은 하나의 스레드에서 동작. (stack이 하나, 한번에 하나의 작업만 할 수 있음.)

하지만, **Event Loop와 queue를 통해 비동기 작업이 가능**하다. (JS는 non-blocking 언어)

- blocking vs non-blocking

: JS는 non-blocking언어. (python은 blocking언어)

JS 가 non-blocking이기 때문에 브라우저가 다른 일을 할 때도 유저는 input창에 입력을 할 수 있다. (유저 인풋, 이벤트, fetch.. 등) 

*예외) alert 발생하면 아무 것도 할 수 없음



(그림)

- **Event loop** : 계속 반복해서 call stack과 queue 사이의 작업들을 확인하고, **call stack이 비워져 있으면**, callback queue에서 작업을 꺼내 call stack에 넣는다.
- callback queue : 비동기 작업을 위해 작업을 담아둘 곳. 
  - microtask queue -> animation frames -> task queue 순으로 진행

ex. setTimeout()이 발생했을 때, 먼저 call stack에 올리고 -> web API에 호출(콜백 전달) -> call stack 에서 setTimeout()을 pop -> web API에서 예약된 시간이 되면, task queue에 해당 작업 올림 -> (주체: event loop) call stack이 비어있으면, 해당 작업을 call stack에 올림.

<br>

### 4. Hoisting

: 끌어올리기. (변수의 정의가 그 범위에 따라 선언과 할당으로 분리되는 것.)

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

<br>

### 5. Closure

: **함수와 그 함수가 실행될 범위의 연결**. (외부 함수에 접근할 수 있는 내부 함수 혹은 이러한 원리)

- 스코프에 따라 내부함수의 범위에서는 외부 함수 범위에 있는 변수에 접근이 가능하지만, 그 반대는 실현이 불가 (**변수를 은닉화**할 수 있다.)
- 외부함수는 외부함수의 지역변수를 사용하는 내부함수가 소멸될 때까지 소멸되지 않음. (변수 캡쳐)
- JS에서는 **함수를 리턴할 때, 클로저를 형성**하고, 이 때 **함수와 함수가 선언된 어휘적 환경의 조합(당시 관계되는 코드들)의 참조를 기억**한다.



#### 언제 사용할까?

- 어떤 데이터와 그 데이터를 조작하는 함수를 연관시켜줄 때 (이벤트 함수)
- 정보 은닉 : private 변수를 만들고, 익명 함수에서 반환된 퍼블릭 함수를 통해서만 접근 가능
- 캡슐화 : 고유의 클로저를 통한 변수의 다른 버전을 참조. (하나의 클로저에서 변수 값을 변경해도, 다른 클로저의 값에는 영향을 주지 않음)

<br>

### 6. this

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

<br>

### 7. 실행 컨텍스트

: scope, hoisting, this, function, closure 등의 동작원리를 담고 있는 자바스크립트의 핵심원리

#### 컨텍스트의 원칙

- 처음 코드를 싱행 시, **전역 컨텍스트가 생성**되고, **함수 호출 시마다 컨텍스트가 생김**
- 컨텍스트 생성 시, 컨텍스트 안에 **변수객체(arguments, variable), scope chain, this**가 생성됨
- 컨텍스트 생성 후, 함수가 실행됨. (사용되는 변수들은 변수객체 안에서 값을 찾고, 없다면 scope chain을 따라 올라가며 찾는다)
- 함수 실행이 마무리되면, 해당 컨텍스트는 사라진다. (클로저 제외) 페이지가 종료되면 전역 컨텍스트가 사라짐

<br>

### 8. Promise

#### -callback

: 나중에 실행되는 코드! (비동기적)

```javascript
// event
btn.addEventListener('click', () => {
    console.log('btn');
});

// timer
console.log('시작');
setTimeout(() => {
    console.log('hello');
}, 0);
console.log('끝');

// 시작 -> 끝 -> hello (setTimeout은 JS내에서 연산되는 것이 아니라, web API단에서 실행되기 때문. 0초 뒤 실행되는 것이 아니라, 0초 뒤에 task큐로 보내는 것!)
```

=> 비동기 함수간의 의존성을 처리할 때 콜백을 사용하면, 유지보수하기 힘들다.



#### -promise

: 비동기를 간편하게 처리할 수 있도록 도와주는 object로, 콜백 중첩을 해결하기 위해 등장한 패턴. 

"리턴값을 지금 사용하든 아니든, 이건 비동기 함수로 약속!"

정해진 장시간의 기능을 수행하고 나서 정상적으로 기능이 수행되어졌다면, 성공 메시지와 함께 결과값을 전달해줌. 에러 발생 시 에러 전달.

- state : 수행 중인지, 완료되어 성공/실패 상태

  - pending - promise가 만들어져서, 우리가 지정한 operation이 수행 중일 때
  - fullfilled
  - rejected

- producer : 정보 제공자 (promise object)

  - promise는 class라서 new로 object 생성가능

  - executor라는 콜백함수 안에 두 개의 콜백함수(resolve, reject) 전달

    promise가 생성되는 순간 콜백함수인 executor가 실행됨 (불필요한 network 작업 주의)

    - resolve - 기능을 정상적을 수행해서 최종 값을 전달
    - reject - 문제가 생기면 처리할 내용

  ```javascript
  const promise = new Promise((resolve, reject) => {
      // doing some heavy work (network, read files)
      console.log('doing smth...');
      setTimeout(() => {
          resolve('suhyeon');		// 성공 시
          reject(new Error('no network'));	// 에러 시
      }, 2000);
  });
  ```

- consumer : 정보 소비자

  - then - promise가 정상적으로 수행되어 최종적으로 resolve의 값이 value로 들어옴

    ​			(then은 값/promise를 바로 받아옴)

  - catch - 에러 시 수행할 내용

  - finally - 성공/실패와 상관없이 마지막으로 실행됨

  ```javascript
  promise
  .then(value => {
      console.log(value); 		// suhyeon
  });
  .catch(error => {
      console.log(error);
  });
  .finally(() => {
      console.log('finally');		// 무조건 수행됨
  });
  ```

- Promise chaining

  ```javascript
  const fetchNumber = new Promise((resolve, reject) => {
      setTimeout(() => resolve(1), 1000);
  });
  fetchNumber
  .then(num => num * 2)
  .then(num => num * 3)
  .then(num => {
      return new Promise((resolve, reject) => {
          setTimeout(() => resolve(num - 1), 1000);
      });
  })
  .then(num => console.log(num));
  ```

- Error Handling

  ```javascript
  const getHen = () =>
  	new Promise((resolve, reject) => {
          setTimeout(() => resolve('암탉'), 1000);
      });
  const getEgg = hen =>
  	new Promise((resolve, reject) => {
          //setTimeout(() => resolve(`${hen} => 달걀`), 1000);
          setTimeout(() => reject(new Error(`${hen} => 달걀`)), 1000);
      });
  const cook = egg =>
  	new Promise((resolve, reject) => {
          setTimeout(() => resolve(`${egg} => 후라이`), 1000);
      });
  
  getHen()
  .then(getEgg)
  .catch(error => {
      return '빵';			// 빵 => 후라이  // 위에서 발생하는 에러를 바로 잡기
  })
  .then(cook)
  .then(console.log);		// 암탉 => 달걀 => 후라이
  .catch(console.log);
  ```

  

#### 장점

- 비동기 작업들을 컨트롤하기 수월해진다. 
  - 비동기 메서드에서 마치 동기 메서드처럼 값을 반환!
  - 비동기 작업을 객체로 다룸으로써 좀 더 유연한 비동기 처리가 가능하다.
- 예외처리에 대한 구조가 존재하므로 오류 처리 등에 대해 보다 가시적으로 관리할 수 있다.



#### 동작과정 요약

- Promise 객체가 생성되는 직후부터 resolve나 reject가 호출되기 전까지 => pending
- 비동기 작업을 마친 뒤, 결과물을 약속대로 잘 줄 수 있다면 => resolve 함수 호출
- 실패했다면 => reject 함수 호출
- 호출 시, Promise 객체가 리턴됨
- 비동기 작업이 정상적으로 완료되었을 때 `.then`을 호출 (첫번째 파라미터에는 성공시 호출할 함수를, 두번째 파라미터에는 실패시 호출할 함수 선언) 또는 `.catch`로 에러작업 설정

<br>

### 9. async / await

: promise 기반의 비동기 코드 작성법으로, promise를 좀 더 간결/간편하고, 동기적으로 실행되는 것처럼 보이게 해준다.

(기존에 존재하는 것 위에 살짝 덧붙인 syntactic sugar.)

무조건 async await으로 대체해야 하는 것은 아니다.

"promise이기만 하면, 우리는 기다릴 수 있어"

- function 키워드 앞에 `async`를 붙여준다. (async를 함수 앞에 쓰면, 코드 블럭이 자동으로 promise로 바뀌게 된다!!)
-  function 내부의 promise를 반환하는 비동기 처리 함수 앞에 `await`를 붙여주면 된다. 
- `await`는 promise의 값이 사용 가능할 때까지 메소드의 실행을 일시중지 시킨다.
- (모든 async함수는 promise를 리턴하고, 모든 await함수는 일반적으로 promise가 된다)



#### 장점

- promise보다 비동기 코드의 겉모습을 더 깔끔하게 한다!
- 동기와 비동기 에러 모두를 `try/catch`를 통해 처리할 수 있게 한다

```javascript
// promise로 접근
function getUser() {
    return getUsers()
        .then(users => {
          return users.name;
    })
        .catch(error => {
          return {name: 'default user'};
    });
}

// async await으로 접근
async function getUser() {
    try {
        let users = await getUsers();
        return users.name;
    } catch (error) {
        return {name: 'default user'};
    }
}

// all : promise 배열들을 전달하면, 모든 promise들이 병렬적으로 수행되는 것을 모아줌. (배열 형태로 promise를 전달!)
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function getApple() {
    await delay(3000);			// delay가 끝날 때까지 기다려준다.
    return '사과';
}

async function getBanan() {
    await delay(3000);			// delay가 끝날 때까지 기다려준다.
    return '바나나';
}

function pickAllFruits() {
    return Promise.all([getApple(), getBanan()])
    .then(fruits => fruits.join(' + '));
}
pickAllFruits().then(console.log);

// race (가장 먼저 실행된 promise 값만 출력)
function pickOnlyOne() {
    return Promise.race([getApple(), getBanan()]);
}
pickOnlyOne().then(console.log);		// 바나나 만 출력
```

<br>

### 10. ES6에 추가된 스펙

0. const / let (var는 이제 사용하지 않음)

1. 리터럴 문법
2. 객체 비구조화 할당
3. 객체 프로퍼티 초기화 단축 : 객체 프로퍼티 이름이 로컬 변수 이름과 같으면 생략 가능.
4. for... of... : `for(let name of ppl)`
5. 스프레드 문법
6. Rest parameter
7. Arrow function
8. Trailing Commas : 데이터가 늘어날 경우를 대비해, 객체 마지막 값 뒤에 `,`를 붙일 수 있다.
9. Default Params 세팅 : `(name = defaultValue)` 
10. includes 메서드
11. map, set

<br>

### 11. Arrow Function

- 이름이 없다.

  ```javascript
  // 일반 함수
  function hi () {
  
  }
  
  // 화살표 함수 
  () => {
  
  }
  ```

  

- `arguments`가 없다.

  ```javascript
  // #일반 함수에는 배열처럼 접근할 수 있는 arguments라는 속성이 존재
  const myFun = function() {
      console.log(arguments);
  }
  
  myFun(1, 2, 3, 4);  // Arguments(4) [1, 2, 3, 4]
  
  // #화살표 함수에는 arguments가 없음.
  const myFun = () => {
      console.log(arguments);
  }
  
  myFun(1, 2, 3, 4);  // 에러
  
  // #해결하기 (일반 함수로 감싸주기)
  function outter() {
      const myFun = () => {
      console.log(arguments);
   }
   myFun();
  }
  
  outter(1, 2, 3, 4);  // Arguments(4) [1, 2, 3, 4]
  // myFun에는 arguments가 없기 때문에, 화살표 함수가 정의된 outter함수가 실행될 때의 스코프를 참조하게 된다.
  
  // #전개 연산자
  const myFun = (...args) => {
      console.log(args);
  }
  
  myFun(1, 2, 3);  // (3) [1, 2, 3] 실제 배열!
  ```

  

- `this`가 없다.

  ```javascript
  // #일반 함수
  const myObj = {
      count: 3,
      setCounter: function() {
          console.log(this.count);
          btn.addEventListener('click', function() {
              console.log(this);
          });
      }
  };
  
  myObj.setCounter();  // 3
  // btn 클릭 시 => <button id="btn">버튼</button>
  
  btn.addEventListener('click', (function() {
      console.log(this);
  }).bind(this));
  // btn 클릭 시 => {count: 0, setCounter: f}
  
  // #화살표 함수
  btn.addEventListener('click', () => {
      console.log(this);
  });
  // btn 클릭 시 => this가 자신 쪽에 없기 때문에 그 밖에서 찾는다. {count: 0, setCounter: f}
  
  btn.addEventListener('click', () => {
      console.log(this.count++);
  });
  // btn 클릭 시 => this가 자신 쪽에 없기 때문에 그 밖에서 찾는다. 1
  
  // #생성자 함수를 쓸 수 없음 (프로토타입 존재X)
  const MyClass = () => {
      
  }
  
  new MyClass();  // 에러
  ```


<br>

### 12. JS Engine 

: 자바스크립트 코드를 해석하고 실행시켜주는 프로그램 혹은 인터프리터. (JS 엔진은 인터프리터로 구현될 수도, JIT 컴파일러로도 구현될 수도 있다.) **가능한 짧은 시간 내에 가장 최적화된 코드를 생성하는 것**이 목표이다. 

 JS 엔진은 크게 Heap 이라는 메모리를 관리하는 영역과, 실행할 태스크를 관리하는 Stack 영역으로 구분된다.

자바스크립트 엔진은 ECMAscript라고도 불리며, (특정 버전의 ECMAscript를 구현하기 때문에) ECMAscript가 발전하는 만큼 엔진도 발전한다. 웹 브라우저마다 사용하는 엔진이 다른데, 크롬에서는 구글의 V8 엔진을 사용한다.

 V8은 웹 브라우저 내부에서 자바스크립트 수행 속도의 개선을 목표로 처음 고안되었다. 속도 향상을 위해 V8은 인터프리터를 사용하는 대신, 자바스크립트 코드를 더 효율적인 머신 코드로 번역한다. **JIT(저스트인타임)** 컴파일러를 구현함으로써, 코드 실행 시에 자바스크립트 코드를 **머신 코드로 컴파일**하는데, 이는 스파이더몽키나 리노와 같은 현대적인 다른 자바스크립트 엔진에서도 마찬가지이다. 주된 차이는 V8은 바이트코드와 같은 중간 코드를 생산하지 않는다는 점이다.

<br>

### 13. AMP(Accelerated Mobile Pages)

: 모바일 가속화 페이지. 모바일 환경에서 빠른 속도로 페이지를 렌더링하여 제공한다.

페이지 속도 개선, 사용자 만족도 향상



+**Wireshark** : 네트워크 패킷을 캡쳐하고 분석하는 오픈소스 도구. 해킹뿐만 아니라 보안 취약점 분석, 보안 컨설팅 등 여러 분야에서 폭넓게 사용된다.