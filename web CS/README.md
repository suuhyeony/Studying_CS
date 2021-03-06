### 1. 브라우저의 동작 원리

1. **요약**

   1. HTML 마크업을 처리하고 DOM 트리를 빌드한다. (**"무엇을"** 그릴지 결정한다.)
   2. CSS 마크업을 처리하고 CSSOM 트리를 빌드한다. (**"어떻게"** 그릴지 결정한다.)
   3. DOM 및 CSSOM 을 결합하여 렌더트리를 형성한다. (**"화면에 그려질 것만"** 결정)
   4. 렌더트리에서 레이아웃을 실행하여 각 노드의 기하학적 형태를 계산한다. (**"Box-Model"** 을 생성해 **정확한 위치**에 표시.)
   5. 개별 노드를 화면에 페인트한다.(or 래스터화)

   

   #### 브라우저의 기본 구조

   - UI - 요청한 페이지를 보여주는 창 외에 사용자가 컨트롤 할 수 있는 모든 부분
   - 브라우저 엔진 - UI와 렌더링 엔진 사이의 동작을 제어 (사용자가 UI를 클릭하면, 명령을 렌더링 엔진에게 전달해주는 역할!)
   - **렌더링 엔진** - 요청한 URI를 브라우저 엔진에게 받아서 server에게 요청한다(**통신**). server로부터 URI에 해당하는 데이터(HTML, CSS, JS)를 받아서 **파싱** 후 화면에 표시(**렌더링**). (ex. chrome webkit)
   - 통신 - 렌더링 엔진으로부터 HTTP 요청을 받아서 네트워크 처리 후 응답을 전달. (OS 단에서 실행)
   - 자바스크립트 해석기 - JS를 파싱, 실행시킴. (ex. chrome V8)
   - UI 백엔드 - 렌더 트리를 브라우저에 그리는 역할.
   - 자료 저장소 - 쿠키 등의 자료를 컴퓨터 하드디스크에 저장. (HTML5부터 웹DB에 저장 가능)

   (그림)

   #### 브라우저 렌더링 과정 (브라우저 구조 관점)

   - 1) 사용자가 주소표시줄(UI)에 URI를 입력하여 브라우저 엔진에게 전달.
   - 2-1) 브라우저 엔진은 자료 저장소에서 URI에 해당하는 자료를 찾고, 해당 자료가 쿠키로 저장되어 있다면, 그 자료를 렌더링 엔진에게 전달. (통신할 필요 X)
   - 2-2) 쿠키에 저장되어 있지 않다면, 렌더링 엔진은 URI 데이터를 통신.
   - 3) 통신 응답을 받으면
     - 렌더링 엔진이 HTML, CSS를 파싱
     - JS 해석기가 JS를 파싱
   - 4) JS해석기가 파싱 결과를 렌더링 엔진에게 전달해 HTML의 파싱 결과인 DOM트리 조작.

   - 5) 조작이 완료된 DOM node(DOM트리 구성요소)는 render object(렌더트리 구성요소)로 변함. 
   - 6) UI 백엔드에서 렌더트리의 각 노드를 가로지르며 형상을 만들어 냄.

   

   #### 렌더링 엔진 동작 과정 (렌더링 엔진 관점)

   : 렌더링 엔진은 URI를 통해 요청을 받아, 해당하는 데이터를 렌더링. chrome과 IOS는 webkit이라는 렌더링 엔진을 사용.

   - 1) DOM트리 구축을 위해, HTML/CSS/JS 파싱 : HTML 문서를 파싱한 후, 컨텐트 트리 내부에서 tag를 DOM node로 변환. CSS 파일과 함께 모든 스타일 요소를 파싱. 스타일 요소와 HTML 표시 규칙, JS의 파싱 결과물은 렌더트리를 생성한다.
   - 2) 렌더트리 구축 : HTML과 CSS를 파싱해서 만들어진 렌더트리는 색상 또는 면적 등 시각적 속성을 갖는 사각형을 포함한다. 정해진 순서대로 렌더링.
   - 3) 렌더트리 배치 : 렌더 트리 생성이 끝나면, 배치가 시작된다. 각 node가 정확한 위치에 표시되기 위해 이동.
   - 4) 렌더트리 그리기 : 각 node 배치를 완료하면, UI 백엔드에서 각 node를 가로지르며 paint 작업을 한다. 

   *1번과 2,3,4번은 병렬적으로 진행!!

   : 즉, 통신 레이어에서 데이터를 계속 받아오면서 -> 받아온 HTML/CSS/JS를 파싱(DOM트리의 자식 요소인 DOM node로 변환)하면서(1번)

     렌더트리에 node를 그린다(렌더트리의 자식요소인 render object로 변환) (2,3,4번)

   =>> 데이터를 받아오는 도중에도 계속 화면이 그려지면서 사용자 경험↑

   

   +) 

   - HTML을 파싱해 DOM트리를 구축하는 이유? -> HTML을 DOM으로 바꿔야 JS를 통해 이를 조작, 동적으로 표현할 수 있기 때문.
   - CSS를 파싱한 결과는 CSSOM(스타일 규칙)이다. (DOM node에 대한 스타일 정보를 가지고 있음)
   - DOM트리를 생성하는 동시에, 이미 생성된 DOM트리와 스타일 규칙을 Attachment한다. (DOM트리를 구성하는 하나의 DOM node는 attach라는 메서드를 가짐. attach 덕분에 DOM node가 바로바로 render object로 변환되는 것!)
   - 모든 DOM node가 전부 render object로 생성되는 것은 아니다. (ex. header, display:none)
   - `<html>`과`<body>`DOM node는 render tree root로서 render view라고 부름.
   - 나머지 DOM node들은 render object로 생성되어 이 render tree root에 추가된다.
   - 구축한 렌더트리를 배치할 때, 최상위 render object에서 시작. 화면 왼쪽 위부터 이 render object에 해당하는 DOM node를 그려나간다.
   - 렌더트리 탐색 후, 해당하는 render object의 paint 메서드를 호출해서 화면에 렌더트리를 그림.

<br>

### 2. DOM (Document Object Model)

: HTML, XML 문서에 대한 인터페이스. 프로그래밍 언어가 페이지의 콘텐츠/구조/스타일을 읽고 조작할 수 있도록 API를 제공한다. (DOM에 접근, 조작)

- 뷰 포트에 무엇을 렌더링할지 결정하기 위해 사용됨.
- 페이지의 콘텐츠/구조/스타일이 JS프로그램에 의해 수정되기 위해 사용됨.

HTML 문서의 객체 기반 표현 방식으로, 단순 텍스트로 구성된 HTML 문서의 내용과 구조가 객체 모델로 변환된다. (구조화된 노드, property, method를 갖고 있는 objects로 문서를 표현)

DOM의 개체 구조는 **노드 트리**로 표현된다. 루트 요소인 <html>은 부모줄기, 루트 요소에 내포된 태그들은 자식 나무가지, 요소 안의 컨텐츠는 잎.

- 항상 유효한 HTML 형식이다.
- JS에 의해 수정될 수 있는 동적 모델이어야 한다.
- 가상 요소를 포함하지 않는다.
- 보이지 않는 요소까지 포함한다. (`display: none`)



-예시

```html
<html>
    <head>
        <script>
          window.onload = function() {
              let title = document.createElement("h1");
              let title_text = document.createTextNode("Welcome!");
              title.appendChild(title_text);
              document.body.appendChild(title);
          }
        </script>
    </head>
    <body>
    </body>
</html>
```



참고 문서

https://wit.nts-corp.com/2019/02/14/5522

<br>

### 3. CORS (Cross-Origin Resource Sharing)

: 타 도메인 간에 자원을 공유할 수 있게 해주는 것.

이전에는 보안 상의 문제로, Origin 웹서버(동일 도메인/프로토콜/포트)에게만 Ajax 요청을 보낼 수 있지만(same origin policy), HTML5에서 다른 도메인 간 통신이 가능한 CORS라는 스펙이 추가됨.

추가 HTTP 헤더를 사용하여, 어떤 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제. (리소스가 자신의 출처 -도메인/프로토콜/포트 와 다를 때 교차 출처 HTTP 요청을 실행)

- 적용 방법

  : 요청하는 URL의 출처가 다른 경우, XMLHttpRequest 객체가 preflight, actual 요청을 자동으로 처리. 

  - 프론트) request 헤더에 CORS 관련 OPTION 메소드를 넣어줌
  - 서버) response 헤더에 해당하는 요청을 허용한다는 내용을 넣어줌

- Preflight Request

  : 실제 요청을 보내기 전, 안전한지 판단하기 위해 preflight 요청을 먼저 보냄.

  인증 헤더를 전송하여, 서버의 허용 여부를 미리 체크하는 테스트 요청.

  트래픽 증가 문제는 서버의 헤더 설정으로 캐쉬가 가능.

<br>

### 4. 크로스 브라우징

: 서로 다른 OS나 플랫폼에 대응하는 것 (어떤 환경에서도 이상없이 작동되도록). 

브라우저의 렌더링 엔진이 다른 경우, 인터넷이 이상없이 구현되도록 하는 기술. 

즉, 어느 한쪽에 최적화되어 치우치지 않도록 공통요소를 사용해 웹페이지를 제작하는 방법.

- 웹표준 검사하기 (Can i use? / CSS-Validator)
- feature detection
- reset.css 사용하기 (default 값 초기화)
- prefix 적기

<br>

### 5. SSR(Server Side Rendering) vs CSR(Client Side Rendering)

- SPA (Single Page web Application)

  : 최초 한번 페이지 전체(정적 리소스)를 로딩한 이후부터는 데이터만 변경해 사용할 수 있는 웹 애플리케이션. 전체적인 트래픽을 감소할 수 있고, 새로고침이 발생하지 않아 사용자 경험 향상.

- SSR : 요청할 때마다 새로고침이 발생해, 서버로부터 리소스를 전달받아 해석/렌더링. 데이터가 많을수록 성능문제 발생.

  - 장점) 초기로딩 성능 개선. SEO 최적화.
  - 단점) 매번 서버에 request 요청을 통해 해결. DOM 조작 시, 요청/탐색 비용 발생 (성능 악화)

- CSR : 서버는 단지 JSON 파일만 보내주는 역할을 하고, html을 그리는 역할은 클라이언트 측에서 자바스크립트가 수행.

  - 장점) 초기 구동 이후, 빠른 인터랙션.
  - 단점) 초기 구동 속도가 느림. 검색엔진 최적화 문제(HTML 에서만 콘텐츠를 수집). 보안문제(사용자 정보를 쿠키 외에 저장할 공간이 마땅치 않음)

<br>

### 6. 쿠키/세션/캐시

#### 쿠키

 : 상태 정보를 유지하는 기술 중 하나로,특정 웹사이트를 방문했을 때 만들어지는 정보를 담는 파일을 지칭한다. (만료 기한이 있는 키-값 저장소)

클라이언트-서버 간의 지속적인 데이터 교환을 위해 만들어졌으며, 쿠키에 사용자 정보를 담아 서버로 보내고, 서버는 쿠키를 읽어서 사용자 식별을 한다.



#### -쿠키를 사용하는 이유?

- HTTP 프로토콜의 특징이자 약점을 보완하기 위해 사용된다.
  - Stateless (상태 정보를 유지하지 않음)
  - Connectionless (요청에 맞는 응답을 받은 후, 연결을 끊음)
- HTTP 요청의 주체가 누구인지 알아야 한다.

   => *즉, HTTP 요청의 주체가 누구인지 식별하고, 사용자별 정보를 담기 위해 사용된다.*



정리하자면, 아래와 같은 목적으로 쿠키를 사용한다. 

1. **세션관리**) 로그인, 유저 닉네임, 접속 시간, 장바구니 등 서버가 알아야할 정보들을 저장한다.
2. **개인화**) 유저마다 다르게 적절한 페이지를 보여줄 수 있다.
3. **트래킹**) 유저의 행동과 패턴을 분석, 기록한다.



#### -종류

> **Persistent cookie와 Session cookie 두 종류로 쿠키를 나눠볼 수 있다.**

|       항목       |                 Persistent cookie (지속쿠키)                 |      Session cookie (세션쿠키 :*세션으로 줄여 부른다*)       |
| :--------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  **저장 위치**   | 방문자의 정보를 브라우저에 저장하여, 클라이언트가 인증 정보를 책임지게 된다. | 웹 서버가 세션ID 파일을 만들어 서버에 저장하며, 서버가 인증을 책임지게 된다. **세션ID) 클라이언트가 요청을 보내면, 해당 서버가 클라이언트에게 부여하는 유일한 ID* |
|  **저장 기간**   |      지정된 만료일까지 저장된다. (쿠키 저장 시에 지정)       |    **브라우저 종료 시 삭제된다.** (만료일자 지정은 가능)     |
| **라이프사이클** | **브라우저를 종료해도 사용자의 하드 드라이브에 저장된다**.<br />직접 삭제하는 것이 가능하다. | **일시적으로 브라우저를 끄거나, 로그아웃, 일정 시간 지나면 삭제된다.**<br />서버에서 만료일자를 정해 삭제할 수 있다. |
|     **보안**     | 클라이언트 측에 저장되므로 임의로 고치거나 지울 수 있고, 가로채기도 쉬워 보안 문제가 발생한다. | 지속쿠키에서 발생할 수 있는 취약점을 대응할 수 있다. (ex. 헤더 값 활용) |
|     **용량**     | 클라이언트당 최대 300개<br />도메인당 최대 20개<br />쿠키당 4KB |         서버가 허용하는 한, 갯수와 용량 제한이 없다.         |
|  **속도/성능**   |    파일에서 읽어오기 때문에 세션보다 요청 속도가 빠르다.     | 서버에 정보가 있으므로 일반 쿠키보다는 속도가 느릴 수 있으나, 비슷한 수준이다.<br />사용자가 많아질수록 서버 과부하가 발생해 성능이 저하된다. |
|  **동작 방식**   | 1. 클라이언트가 페이지를 요청서버에서 쿠키를 생성<br />2. HTTP 헤더에 쿠키를 포함시켜 응답<br />3. 브라우저가 종료되어도 만료기간이 있다면, 클라이언트에서 보관<br />4. 동일 요청일 경우 HTTP 헤더에 쿠키를 함께 발송<br />5. 서버에서 쿠키를 읽고 상태정보를 변경할 필요가 있으면, 쿠키 업데이트 후 변경된 쿠키를 HTTP헤더에 포함시켜 응답 | 1. 클라이언트가 서버에 접속 시 세션ID를 발급받음<br />2. 클라이언트는 세션ID를 쿠키 형태로 저장해 갖고있음<br />3. 클라이언트는 서버 요청 시, 이 쿠키의 세션ID를 서버에 전달<br />4. 서버는 세션ID를 전달받아 세션에 있는 클라이언트의 정보를 가져옴 |
|     **활용**     | 사용자의 편의를 위하되, 보안 이슈가 없을만한 설정에 쓰인다. <br />- 최근 방문 사이트<br />- 로그인 시, ID 자동완성<br />- 팝업 하루동안 안보기<br />- 비로그인 시 장바구니 담기<br /> | 외부에 노출되어서는 안되는 정보를 저장한다. <br />- 세션ID로 사용자를 구별해 요구에 맞는 서비스 제공<br />- 사용자 정보로그인 유지 |

 => 세션을 과하게 사용하면 속도가 느려질 수 있으므로, (외부에 노출되면 안되는 정보를 저장하는 용도로) 최소화로 사용하고,

쿠키에는 사용자의 편의를 위하되, 보안에 문제되지 않는 정보를 저장하자!



- **캐시** : 가져오는데 비용이 드는 데이터를 한 번 가져온 뒤에는 임시로 저장해두는 임시장소. (저장공간이 작고 비용이 비싼 대신, 빠른 성능을 제공) 반복적으로 데이터를 불러오는 경우에, 지속적으로 DBMS 혹은 서버에 요청하는 것이 아니라 Memory에 데이터를 저장하였다가 불러다 쓰는 것. 
  - 어떤 데이터를 대상으로 사용될까?
    - 접근하는 시간이 오래 걸리는 데이터 (서버의 균일한 API 데이터)
    - 반복적으로 동일한 결과를 리턴하는 데이터 (이미지/썸네일) 
  - 사용자가 여러 번 방문할 법한 사이트에서는 한 번 받아온 데이터를 사용자의 컴퓨터 혹은 중간 역할을 하는 웹 캐시 서버(프록시 서버의 한 형태)에 저장해둠.

*웹 개발자는 어떤 정보를 쿠키에 담을지, 세션에 담을지 적절한 판단을 내릴 수 있어야 한다.

<br>

### 7. Redux

: 상태관리 라이브러리로(Global State Container), 공유된 state를 저장하는 방법을 제공한다.

- 컴포넌트들의 상태 관련 로직들을 다른 파일들로 분리시켜 더욱 효율적으로 관리할 수 있다. 
- 컴포넌트끼리 상태를 공유할 때, 여러 컴포넌트를 거치지 않아도 된다.
- 미들웨어 기능을 통해, 비동기 작업, 로깅 등의 확장적인 작업을 쉽게할 수 있다.



#### 리덕스가 필요한 이유

- 컴포넌트는 **local state**를 갖고있고, 앱은 **global state**를 갖고있기 때문.

  그런데, 앱은 많은 컴포넌트를 기반으로 지어졌는데, 동시에 global state를 갖고있다.

  - local state 예) '좋아요' 기능 : 눌렀을 때 빨간색 / 안눌렀을 때 회색.

  - global state 예) '로그인' 기능 : user가 로그인을 했는지 / 안했는지에 따라 앱이 다르게 보임. 

즉, global state에서는 모든 컴포넌트가 영향을 받는다.

- 때때로 state는 하위 컴포넌트들에게 공유되어야 하는데, (user의 로그인 여부를 모든 컴포넌트들이 알기를 원함. 즉, 좋아요 / 댓글 기능은 user 정보가 필요)

  이 때, **flying props** 문제(중간 컴포넌트에서 필요하지 않은 정보를 prop으로 전달받고 있는)가 발생함.

- 따라서, 공유되는 state를 어딘가에 저장해야 한다.



=> **Redux = State Container**

flying props가 발생하지 않을 정도로 간단한 프로젝트라면 리덕스가 필요없다.

리덕스는 쉬운 앱 만들기를 헷갈리게 할 순 있지만, 복잡한 앱을 쉽게 만들게 한다.



#### 리덕스 원리

리덕스를 갖는 것은 **state의 DB**를 갖는 것과 비슷하다. 

컴포넌트의 state를 저장한 박스 (**Redux Store**)를 만든다.

그러면 부모 컨테이너에서 물려받는 것이 아니라, 컴포넌트들이 필요한 정보만 쏙쏙 가져올 수 있다. 

즉, 서로에게 props를 줄 필요가 없고, 리덕스 state database에서 가져오면 된다.  (flying props 문제 해결!)



#### 장점

- 상태의 중앙화 : store라는 이름의 전역 js변수를 통해 상태를 한 곳에서 관리.
- 읽기 전용 상태 : 상태를 변경하기 위해서는 상태의 일부를 바꾸는게 아니라, 상태 전체를 갈아치워야 함.
- 부수효과 없는 리듀서 : 액션만으로도 상태 변화를 완벽히 예측 가능.
- 리액트와의 유사성 : state, setState와 같은 유사 성질을 가지고 있음.



단점은 리덕스 설계 철학에서 요구하는 대로 코딩 방식을 바꾸어야 하므로, 오히려 코드가 복잡해지거나 코딩하기 어려워질 수 있음.



#### 주의사항

- 모든 state는 object로 저장된다. (JS object로 이루어진 store)

- object의 data를 수정하는 방법 : 

  action을 reducer로 보내면(**dispatch**), **reducer**가 대신 object를 변경해준다. 

  ex. 만약 action이 00라면, **를 할거야. (switch 문법을 사용함)

  (state들이 복잡하고 커질 수 있기 때문에, 해당 object를 수정하는 것에 매우 엄격)

<br>

### 8. AJAX (Asynchronous Javascript And Xml)

: **JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고받는 기술**이다.

 JavaScript의 라이브러리중 하나로, 브라우저가 가지고있는 XMLHttpRequest 객체를 이용해, 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법. 



#### 사용배경

: 기본적으로 HTTP 프로토콜은 클라이언트쪽에서 Request를 보내고 서버쪽에서 Response를 받으면 이어졌던 연결이 끊기게 되어있다. 그래서 화면의 내용을 갱신하기 위해서는 다시 request를 하고 response를 하며 페이지 전체를 갱신하게 된다. => 자원낭비와 시간낭비

AJAX는 HTML 페이지 전체가 아닌 일부분만 갱신할 수 있도록 XMLHttpRequest객체를 통해 서버에 request한다. 이 경우, **JSON이나 XML형태로 필요한 데이터만 받아 갱신하기 때문에 그만큼의 자원과 시간을 아낄 수 있다.**



- 장점
  - 웹페이지의 속도향상
  - 서버의 처리가 완료될 때까지 기다리지 않고 처리가 가능하다.
  - 서버에서 Data만 전송하면 되므로 전체적인 코딩의 양이 줄어든다.
- 단점
  - 히스토리 관리가 되지 않는다.
  - 페이지 이동없는 통신으로 인한 보안상의 문제가 있다.
  - 연속으로 데이터를 요청하면 서버 부하가 증가할 수 있다.
  - XMLHttpRequest를 통해 통신하는 경우, 사용자에게 아무런 진행 정보가 주어지지 않는다. (요청이 완료되지 않았는데 사용자가 페이지를 떠나거나 오작동할 우려가 발생하게 된다.)



#### 진행과정

1. XMLHttpRequest Object를 만든다.
   - request를 보낼 준비를 브라우저에게 시키는 과정
   - 이것을 위해서 필요한 method를 갖춘 object가 필요함
2. callback 함수를 만든다.
   - 서버에서 response가 왔을 때 실행시키는 함수
   - HTML 페이지를 업데이트 함
3. Open a request
   - 서버에서 response가 왔을 때 실행시키는 함수
   - HTML 페이지를 업데이트 함
4. send the request

<br>

### 9. FE 보안관련 이슈

사용자 데이터를 안전하게 보호해야할 책임은 Front-end와 Back-end 둘 다 가지고 있다. response 헤더를 잘 구성하고, 올바른 개발방법을 준수하면 된다.

- XSS(Cross-Site Scripting) : 웹사이트 관리자가 아닌 이가 웹 페이지에 악성 스크립트를 삽입하는 것. 
- 클릭 재킹 : 실제와 똑같이 생긴 가짜 사이트에서 공격자가 원하는 클릭을 유도.



#### 보안 대책

: 클라우드 호스팅 제공 업체가 어떤 response 헤더를 사용하는지, 이에 대한 작동하는 방식을 배우고 적절하게 구성하면 된다.

- 강력한 컨텐츠 보안정책(CSP) 사용 : XSS(Cross-Site Scripting: 웹사이트 관리자가 아닌 이가 웹 페이지에 악성 스크립트를 삽입) 및 클릭 재킹(실제와 똑같이 생긴 가짜 사이트에서 공격자가 원하는 클릭을 유도)을 포함해 특정 유형의 코드 삽입 공격을 탐지하고 막아줌.
  - XSS 보호모드 사용 : 사용자 입력에서 악성 코드가 입력되는 것을 감지하고, 브라우저가 response를 차단.
  - 클릭재킹 공격을 방지하기 위해 iframe Embed 막기 : 헤더에 X-Frame-option을 주기
- 브라우저 기능 및 API에 대한 액세스 제한하기
- referrer 값 노출시키지 않기 : 웹 사이트에서 마지막 위치의 URL을 referrer 헤더로 받는데, 민감한 데이터가 포함될 수도 있기 때문에 노출하면 안된다.
- 유저로부터 입력값을 받을 곳에 innerHTML 사용하지 말기 : XSS 공격의 위험이 있으므로, textContent를 쓰는 것이 바람직.
- UI 프레임워크 사용하기 : React, Vue, Angular와 같은 UI 프레임워크들은 이미 좋은 보안 시스템이 내장되어 있음. XSS에 민감한 DOM API를 사용할 일을 많이 줄여줌.
- 디펜던시들을 최신상태로 유지 : 디펜던시가 믿을만한 건지 체크, 수정.
- third-party 사용 고려하기 : third-party가 손상되면 웹사이트도 손상됨. 

<br>

### 10. 웹 성능과 관련된 Issue

1. 네트워크 요청에 빠르게 응답할 것 (CDN 사용하기, 동시 커넥션 수를 최소화 하기)
2. 최소한의 크기로 자원을 내려 받을 것 (gzip 압축 사용하기, HTML App cache 활용하기)
3. 효율적인 마크업 구조를 가질 것 (중복 코드 최소화, third-party 스크립트 삽입X)
4. 미디어 사용을 개선할 것 (이미지 sprite 사용하기, 비디오 미리보기 이미지)
5. 빠른 자바스크립트를 작성할 것 (코드 최소화, DOM 접근 최소화하기)
6. 어플리케이션이 어떻게 동작되는지 알고 있을 것 (Timer 사용에 유의..)

<br>

### 11. CSS 방법론

: CSS를 보다 효율적으로 작성하는 여러가지 아이디어들.

- 공통 지향 목표
  - 쉬운 유지보수 / 코드의 재사용 / 확장 가능 / 직관적 네이밍
  - CSS 선택자로 id와 tag를 사용하지 말 것을 권장. (id는 재사용이 불가능한 요소이고, tag는 의존성이 강하므로)



#### 1. SMACSS (Scalable and Modular Architecture for CSS)

: 스타일을 다섯 가지 유형으로 분류(범주화)하고, 각 유형에 맞는 선택자와 작명법을 제시.

- 기초(Base)
  - element 스타일의 default 값을 지정해주는 것이다. 선택자로는 요소 선택자를 사용한다.
- 레이아웃(Layout)
  - 구성하고자 하는 페이지를 컴포넌트를 나누고 어떻게 위치해야 하는지를 결정한다. `id`는 CSS 에서 클래스와 성능 차이가 없는데, CSS 에서 사용하게 되면 재사용성이 떨어지기 때문에 클래스를 주로 사용한다.
- 모듈(Module)
  - 레이아웃 요소 안에 들어가는 더 작은 부분들에 대한 스타일을 정의한다. 클래스 선택자를 사용하며 요소 선택자는 가급적 피한다. 클래스 이름은 적용되는 스타일의 내용을 담는다.
- 상태(States)
  - 다른 스타일에 덧붙이거나 덮어씌워서 상태를 나타낸다. 그렇기 때문에 자바스크립트에 의존하는 스타일이 된다. `is-` prefix 를 붙여 상태를 제어하는 스타일임을 나타낸다. 특정 모듈에 한정된 상태는 모듈 이름도 이름에 포함시킨다.
- 테마(Theme)
  - 테마는 프로젝트에서 잘 사용되지 않는 카테고리이다. 사용자의 설정에 따라서 css 를 변경할 수 있는 css 를 설정할 때 사용하게 되며 접두어로는 `theme-`를 붙여 표시한다.



#### 2. OOCSS(Object Oriented CSS)

: 객체지향 CSS 방법론으로 2가지 기본원칙을 갖고 있다.

- 원칙 1. 구조와 모양을 분리한다.
  - 반복적인 시각적 기능을 별도의 스킨으로 정의하여 다양한 객체와 혼합해 중복코드를 없앤다.
- 원칙 2. 컨테이너와 컨텐츠를 분리한다.
  - 스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않는다. 사물의 모양은 어디에 위치하든지 동일하게 보여야 한다.



#### 3. BEM(Block Element Modifier)

: 웹 페이지를 각각의 컴포넌트의 조합으로 바라보고 접근한 방법론이자 규칙이다. SMACSS보다 범위가 좁은 반면, 강제성이 강함. 

- 재사용성을 높이기 위해,
  - id를 사용하는 것을 막는다. 
  - 요소 셀렉터를 통해서 직접 스타일을 적용하는 것도 불허. 
  - 자손 선택자 사용불허. 

- Naming Convention
  - 소문자와 숫자만을 이용해 작명하고 여러 단어의 조합은 하이픈(`-`)과 언더바(`_`)를 사용하여 연결한다.
- BEM 의 B 는 “Block”이다.
  - 블록(block)이란 재사용 할 수 있는 독립적인 페이지 구성 요소를 말하며, HTML 에서 블록은 class 로 표시된다. 블록은 주변 환경에 영향을 받지 않아야 하며, 여백이나 위치를 설정하면 안된다.
- BEM 의 E 는 “Element”이다.
  - 블록 안에서 특정 기능을 담당하는 부분으로 block_element 형태로 사용한다. 요소는 중첩해서 작성될 수 있다.
- BEM 의 M 는 “Modifier”이다.
  - 블록이나 요소의 모양, 상태를 정의한다. `block_element-modifier`, `block—modifier` 형태로 사용한다. 수식어에는 불리언 타입과 키-값 타입이 있다.

<br>

### 12. normalize vs reset

: 브라우저마다 기본적으로 제공하는 element 의 style을 통일시키기 위해 사용하는 css.

#### reset.css

: 기본적으로 제공되는 브라우저 스타일 전부를 **제거**하기 위해 사용된다. `reset.css`가 적용되면 `<H1>~<H6>`, `<p>`, `<strong>`, `<em>` 등 과 같은 표준 요소는 완전히 똑같이 보이며 브라우저가 제공하는 기본적인 styling 이 전혀 없다.

#### normalize.css

: 모든 것을 "해제"하기보다는 유용한 기본값을 보존하는 것. 브라우저 간 일관된 스타일링을 목표로, `<H1>~<H6>`과 같은 요소는 브라우저간에 일관된 방식으로 굵게 표시됩니다. 추가적인 디자인에 필요한 style 만 CSS 로 작성해주면 된다.

normalize.css 는 reset.css 보다 넓은 범위를 가지고 있으며 HTML5 요소의 표시 설정, 양식 요소의 글꼴 상속 부족, pre-font 크기 렌더링 수정, IE9 의 SVG 오버플로 및 iOS 의 버튼 스타일링 버그 등에 대한 이슈를 해결해준다.

<br>

### 13. Webpack vs Babel

#### Webpack

: 의존성을 분석해 모듈을 번들(여러 개를 하나로 묶어주는)시켜주는 역할을 한다. 수많은 라이브러리들을 빌드라는 과정을 통해 하나의 파일로 만들어 주는 것이다.



#### Babel

: 코드 변환기. 최신 자바스크립트 문법을 구형 브라우저에서도 돌아갈 수 있게 코드를 변환시켜준다.  



<br>



### 14. MPA vs SPA

- **MPA**(Multi Page Application) - 전통적인 웹 애플리케이션 개발 방식. 

  - 웹 브라우저에서 특정 페이지에 대한 요청을 서버에 보내면, HTML 문서로 응답을 해준다. 이 때, 전체 페이지가 다시 불러와져 화면이 깜빡이게 되는 것이다. (좋지 않은 UX)
  - 프론트-백이 결합되어 있어, 비즈니스가 복잡해지면 관리하기 어려워진다.
  - SEO 친화적이다.

  

- **SPA**(Single Page Application) - 단일 HTML 파일로 화면을 구성하고, 변경되는 부분만 리렌더링하는 효율적인 웹 애플리케이션 개발 방식.

  - 새로고침이 되지 않고 변경되는 부분만 리렌더링되어, 사용자에게 좋은 경험을 제공할 수 있다.
  - 초기 렌더링 속도가 느리다.
  - SEO에 취약하다.



<br>



### 15. 웹 사이트 vs 웹 애플리케이션

- **웹 사이트** - 웹 페이지들의 순수한 모음. (ex. 과거의 블로그, 뉴스 페이지)

- **웹 애플리케이션** - 유저와 대화하는 식(ex. 댓글달기, 좋아요)으로 인터넷을 이용하는 컴퓨터 프로그램. 유저의 요구에 따른 애플리케이션이 동작해야 한다. (ex. Facebook)

=> 현재는 과거의 웹사이트에도 검색/댓글 기능 등의 애플리케이션들이 포함되었기 때문에, 사실상 둘의 경계가 무너졌다고 볼 수 있다.



<br>



### 16. MVC vs Flux

- **MVC 패턴**

  : 사용자에게 보여지는 View와 데이터 및 비즈니스 로직(Model, Controller)을 분리하여 상호간 독자적으로 개발/수정/테스트가 가능하도록 하는 패턴. **controller가 view-model 작업을 제어하고, view-model 단은 지속적으로 동기화되어, 양방향 데이터 흐름을 이루게 된다**.

  **양방향 데이터 흐름** 아키텍쳐에서는 애플리케이션이 복잡해지면 view-model간 동기화가 어려워져 예측 불가능한 버그(ex. Facebook 알림 서비스)가 발생할 수도 있다. 

  => (이 부분 관련하여 멘토님께 여쭈어 보았으나, 그동안 복잡한 사항/문제는 발생한 적이 없다고 하셨다. 다른 커뮤니티도 확인해보니, flux패턴은 페이스북이 처한 문제의 상황에 맞게 프레임워크화하려는 시도라는 의견이 있었다.)

  - 한 controller가 여러 model&view에 연결되어 있을 수 있다.
  - 연쇄적 이벤트 작용(view가 model을 업데이트할 때, 다른 model에서도 또 다른 view를 업데이트하는..) 발생, 중첩된 업데이트를 일으키기 쉽다.

- **Flux 패턴**

  : React / Angular2에 적용가능한 패턴으로, 확장성과 가독성 두 가지 측면에서 MVC 패턴을 대체하고자 만들어졌다. 

  **단방향 데이터 흐름**을 이루고 있기 때문에, 데이터 변화를 예측하기 훨씬 쉽다.

  애플리케이션의 사이즈가 커져 여러 model&view단을 가지고 있더라도, 새 기능이 다른 컴포넌트들에 어떤 영향을 미칠지 고민하지 않아도 된다. 

  <img src="https://blog.kakaocdn.net/dn/lmfPW/btqBQnTPgIs/Z1jmHHdNcOTNiu93kQ9gMk/img.png" alt="Flux" style="zoom:67%;" />




<br>



### 17. 상태관리

- **상태(state)란?**

  > 상태라기보다는 화면을 구성하는 **데이터**라고 생각하면된다. (혹은 객체가 가지고 있는 데이터)

- **상태관리란?**

  > - 데이터(상태)에 맞춰 적절하게 UI를 설계하고 구현하는 것.
  > - 여러 컴포넌트 간의 데이터 전달과 이벤트 통신을 한 곳에서 관리하는 패턴. 
  >
  > 예를들어, instagram의 게시물 상태(한 장인지/여러 장인지)에 따라 UI가 다르게 반응한다.
  >
  > 리액트에서는 Redux / Mobx, 뷰는 Vuex라는 상태관리 라이브러리를 사용한다.

  컴포넌트 기반 프레임워크에서는 작은 단위의 여러 컴포넌트로 화면을 구성하기 때문에,

  컴포넌트 간의 통신이나 데이터 전달을 좀더 유기적으로 관리할 필요성이 있다. 

  - **컴포넌트 간의 상태 공유 여부**로 **지역적 상태인지, 전역적 상태인지를 적절히 구분해 설계**해야 한다.
  - 일관적인 형태를 유지해 **무결성의 원칙**을 지켜야한다. (ex. 팔로워의 실시간 증가를 모든 화면에 반영해야한다.)
  - 상태를 **어디에, 어떻게 저장**하고 사용할것인지도 중요하다. (redux, vuex, 쿠키, localStorage, 웹소켓)
  - 상태와 상태의 조합에 따른 경우의 수가 많으므로, 우선순위를 설정해 UI에 반영해야 한다.

