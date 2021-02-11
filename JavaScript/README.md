## JavaScript

### 0. 데이터 타입

: 자바스크립트에는 원시타입(primitive type)과 참조타입(reference type)이라는 자료형이 존재.

- 원시타입(primitive type) - number, string, boolean, null, undefined, symbol
  - 자바스크립트에서 사용할 수 있는 데이터 및 정보의 가장 단순한 형태 (객체가 아닌 것들. 값 그 자체로 저장된 것)
  - 변수에 할당될 때, 메모리 상에 고정된 크기로 저장됨
  - 해당 변수가 원시 데이터 값을 보관 (값이 복사됨)
  - 비교 시, 저장된 값을 비교
- 참조타입(reference type) - 객체 (배열, 함수, 정규표현식)
  - 크기가 정해져 있지 않음
  - 변수에 할당될 때, 값이 직접 해당 변수에 저장될 수 없음 (변수에는 데이터에 대한 참조만 저장. 즉, 참조는 참조타입 데이터의 주소이지 해당 데이터의 값이 아님!)
  - 비교 시, 저장되어 있는 참조(메모리의 번지수)를 비교

#### number

: 다른 언어와는 달리(길이를 미리 정해줌), 자바스크립트에는 number가 하나임

#### boolean

- false - 0, null, undefined, NaN, ' '
- true - 다른 모든 값

#### null

: 빈 값. 변수에 값이 텅텅 비어지게 할당한 것. `let nothing = null`

#### undefined

: 변수가 선언되었으나, 아직 할당되지 않음.

#### symbol

: 고유한 식별자가 필요하거나, 동시 다발적으로 일어나는 코드에서 우선순위를 주고 싶을 때 사용

`const symbol1 = Symbol('id')` 동일한 string으로 작성해도, 다른 symbol로 만들어짐



*JS는 동적타이핑 언어이다. 변수의 타입을 선언하지 않아도, 런타임 때 변수의 타입이 자동으로 파악됨. 하나의 변수에 여러 타입의 값을 넣을 수 있음. (문제 발생 => 타입스크립트 사용)



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



### 2. 변수 (var / let / const), scope

#### 변수의 생성과정

1) 선언 단계 - `let x;`

2) 초기화 단계 - undefined를 할당해주는 단계

3) 할당 단계 - `x = 10;`



#### scope

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





### 3. Event Loop

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



### 4. Hoisting

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



### 5. Closure

: **함수와 그 함수가 실행될 범위의 연결**. (외부 함수에 접근할 수 있는 내부 함수 혹은 이러한 원리)

- 스코프에 따라 내부함수의 범위에서는 외부 함수 범위에 있는 변수에 접근이 가능하지만, 그 반대는 실현이 불가 (**변수를 은닉화**할 수 있다.)
- 외부함수는 외부함수의 지역변수를 사용하는 내부함수가 소멸될 때까지 소멸되지 않음. (변수 캡쳐)
- JS에서는 **함수를 리턴할 때, 클로저를 형성**하고, 이 때 **함수와 함수가 선언된 어휘적 환경의 조합(당시 관계되는 코드들)의 참조를 기억**한다.



#### 언제 사용할까?

- 어떤 데이터와 그 데이터를 조작하는 함수를 연관시켜줄 때 (이벤트 함수)
- 정보 은닉 : private 변수를 만들고, 익명 함수에서 반환된 퍼블릭 함수를 통해서만 접근 가능
- 캡슐화 : 고유의 클로저를 통한 변수의 다른 버전을 참조. (하나의 클로저에서 변수 값을 변경해도, 다른 클로저의 값에는 영향을 주지 않음)



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





### 7. 실행 컨텍스트

#### 컨텍스트의 원칙

- 처음 코드를 싱행 시, **전역 컨텍스트가 생성**되고, **함수 호출 시마다 컨텍스트가 생김**
- 컨텍스트 생성 시, 컨텍스트 안에 **변수객체(arguments, variable), scope chain, this**가 생성됨
- 컨텍스트 생성 후, 함수가 실행됨. (사용되는 변수들은 변수객체 안에서 값을 찾고, 없다면 scope chain을 따라 올라가며 찾는다)
- 함수 실행이 마무리되면, 해당 컨텍스트는 사라진다. (클로저 제외) 페이지가 종료되면 전역 컨텍스트가 사라짐

