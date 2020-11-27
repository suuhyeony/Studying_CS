## Ch1. 운영체제의 개요

**-운영체제란?**

![운영체제란](https://user-images.githubusercontent.com/58247800/100134631-d9aa7d80-2ecb-11eb-8a32-7ea2f0f80759.png)

: 컴퓨터 **하드웨어 바로 위에 설치**되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 **연결**하는 소프트웨어 계층.

<br/>

**-운영체제의 목적**

: 컴퓨터 시스템의 **자원을 효율적으로 관리**. 

사용자간 형평성있게 자원을 분배하며, 주어진 자원으로 최대 성능을 내도록 한다.

- HW 자원 (프로세서/ 기억장치/ 입출력 장치 등)의 효율적 관리
- SW 자원 (프로세스/ 파일/ 메시지 등)을 관리
- 사용자 및 운영체제 자신의 보호

<br/>

: 컴퓨터 시스템을 **편리**하게 사용할 수 있는 **환경 제공**. 

실행중인 프로그램들에게 짧은 시간씩 CPU를 번갈아 할당하고, 메모리 공간도 적절히 분배해준다.

- 동시 사용자/ 프로그램들이 각각 독자적 컴퓨터에서 실행되는 듯한 느낌을 제공
- HW를 직접 다루는 복잡한 부분을 OS가 대행

<br/>

**-운영체제의 분류**

: 현재 쓰이는 운영체제의 종류를 나열하자면,

다중 작업(multi tasking) - 동시에 두 개 이상의 작업 처리

다중 사용자(multi user) - 여러 명의 컴퓨터 사용자에 의한 동시 접근을 허용

시분할(time sharing) - 여러 작업 수행 시, 일정 시간 단위로 분할해 처리 (**interactive**함)

<br/>

**-운영체제의 예**

- 유닉스(UNIX) - 보통 대형 서버 컴퓨터를 위한 OS로, 코드의 대부분이 C언어로 작성되어 있다. 최소한의 커널 구조를 가지고 있으며, 복잡한 시스템에 맞게 확장이 용이하다. (프로그램 개발에 용이) 소스코드가 공개되어 있으며, 리눅스 등 다양한 버전이 나와있다.

- MS Windows - MS사의 다중 작업용 GUI기반 OS.

<br/>

**-운영체제의 구조**

![운영체제의 구조](https://user-images.githubusercontent.com/58247800/100134777-15ddde00-2ecc-11eb-9d1a-49dee71ede68.png)

- **CPU** - 누구에게 CPU를 줄지 정하는 **CPU 스케줄링**을 담당. (짧은 시간 간격으로 줬다 뺐었다를 반복)
- **메모리** - 한정된 메모리를 어떻게 쪼개어 쓸지? (**메모리 관리**)
- **디스크** - 디스크에 파일을 어떻게 보관하며, 헤드의 움직임을 최소화하고 빨리 실행할지? (**파일 관리**)
- **입출력 장치** - 각기 다른 입출력 장치와 컴퓨터 간에 어떻게 정보를 주고 받게 할지? (**입출력 관리**)

+) 프로세스 관리 - 프로세스의 생성/삭제, 자원 할당/반환, 프로세스간 협력

+) 그 외 - 보호 시스템/ 네트워킹/ 명령어 해석기

<br/>

## Ch2. 시스템 구조와 프로그램 실행

운영체제를 본격적으로 시작하기에 앞서,

컴퓨터 시스템이 어떻게 동작하고, 프로그램들이 하드웨어 위에서 어떻게 돌아가는지 알아보자.

<br/>

**-컴퓨터 시스템 구조**

: 쉽게 말해 **컴퓨터(CPU, 메모리)**가 호스트고, **입출력 장치**(하드디스크, 키보드/마우스, 프린터, 모니터 등)와 정보를 주고 받는다. 사이에는 DMA 컨트롤러와 타이머가 있다.

![컴퓨터시스템 구조](https://user-images.githubusercontent.com/58247800/100134828-2726ea80-2ecc-11eb-80bb-a6794086ef20.png)

- **CPU** - 매순간 메모리에서 기계어(instruction)를 읽어와 실행. 한 instruction이 끝나면, interrupt line 검사. 

  입출력 장치에 직접 접근하지 않고, 메모리에만 접근. 입출력 작업을 해야할 시에는 각 장치 제어기에게 시키고 다음 일을 함. (출력 값이 있어야 다음 일을 할 수 있을 때는 다음 프로그램으로 넘어감)

  굉장히 빠른 일꾼으로, 사용자 입장에서는 **interactive**하게 응답을 받게 된다.

  - **register** - 메모리보다 더 빠르게 정보를 저장하는 작은 공간.
  - **mode bit** - 지금 CPU를 사용하고 있는 주체가 OS인지 사용자 프로그램인지를 구분해줌
  - **interrupt line** - 입출력 관련 interrupt가 발생한 경우, 발생한 interrupt를 확인

- **메모리** - CPU의 작업 공간. 

- **입출력 장치** - 정보를 입력 받고, 내보내는 장치.

  - **장치 제어기**(device controller) - 각 입출력 장치를 전담하는 **작은 CPU**. 각 장치의 어떤 부분에서 어떤 내용을 읽어올지를 담당. (입출력 장치 속도가 CPU에 비해 매우 느리기 때문에 장치 제어기가 필요)
  - **local buffer** - 장치 제어기의 작업 공간. (메모리와 같은 역할)

- **타이머** - 특정 프로그램이 CPU를 **독점하지 못하도록** 막음. (OS가 작업을 CPU에 넘겨주기 전 **timer에 시간을 걸고**, 시간이 끝나면 **timer interrupt**를 발생, OS가 주도권을 다시 가져간다. ) 

- **DMA controller** - CPU의 중재 없이 데이터를 전송하고, 작업이 완료되면 interrupt를 걸어 CPU에게 알려줌.

<br/>

예시를 들면,

CPU가 작업을 하던 중, 프로그램1이 키보드 입력정보가 필요 

-> (interrupt line을 세팅해 system call을 하고 OS가 주도권을 가짐) -> OS가 키보드 장치 제어기에게 해당 작업을 시킴 

-> 다음 프로그램2를 CPU가 진행 -> 입력값이 키보드 버퍼에 올라옴 -> 키보드 장치 제어기가 CPU에 interrupt를 걺 

-> CPU는 하던일을 멈추고, OS가 주도권을 가져가 입력값을 메모리에 copy 

-> 하던 일 프로그램2가 아직 할당시간이 끝나지 않았으므로 계속 진행됨. (프로그램1은 자기 차례를 기다림) 

<br/>

구조별로 더 자세한 설명

**-Mode bit**

: 사용자 프로그램의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기위한 **보호 장치**.

Mode bit를 통해 두 가지 모드의 operation을 지원한다.

- **1** - **사용자 모드** ) 사용자 프로그램을 수행
- **0 **- **커널모드** ) OS코드 수행

![모드비트](https://user-images.githubusercontent.com/58247800/100134877-35750680-2ecc-11eb-9a58-e5cd4532ca07.png)

interrupt가 발생하거나 예외 발생 시, HW가 mode bit를 0으로 바꿈.

사용자 프로그램에게 CPU를 넘기기 전에 mode bit를 1로 세팅.

<br/>

**-Timer**

: CPU를 특정 프로그램이 독점하는 것으로부터 보호.

정해진 시간이 흐른 뒤, OS에게 제어권이 넘어가도록 **interrupt를 발생**시킨다.

타이머는 매 클릭 tick 마다 1씩 감소 -> 타이머 값이 0이 되면 'timer interrupt' 발생.

<br/>

**-I/O Device Controller**(입출력 장치 제어기)

: 해당 I/O 장치 유형을 관리하는 일종의 **작은 CPU**.

제어 정보를 위해 control register, status register, local buffer를 가짐

I/O는 실제 device와 local buffer 사이에서 일어남 -> I/O가 끝나면 interrupt로 CPU에게 알림

<br/>

**-입출력의 수행**

: 모든 입출력 명령은 특권명령이다.

사용자 프로그램이 I/O를 하려면,

​	1) **시스템콜(System call) **발생 - 사용자 프로그램이 interrupt line을 세팅해 OS에게 I/O를 요청 -> 모드가 1에서 0으로 변경됨

​	(_**시스템콜**_ - 사용자 프로그램이 OS서비스를 받기 위해 커널함수를 호출하는 것)

​	2) **trap**을 사용해 **interrupt vector**의 특정 위치로 이동

​	3) 제어권이 interrupt vector가 가리키는 **interrupt 서비스 루틴**으로 이동

​	4) 올바른 I/O 요청인지 확인 후, 수행

​	5) I/O 완료 시, 제어권을 시스템콜 다음 명령으로 옮김

<br/>

**-인터럽트(interrupt)**

: 인터럽트는 포괄적인 의미로, 일반적 의미는 HW가 발생시킨 인터럽트이다.

시스템콜 / 예외적으로 프로그램이 오류를 범한 경우에는 SW가 인터럽트를 발생시키게 되는데, 이를 **Trap**이라고 한다. ('Trap을 이용해 인터럽트를 건다'고 함.)

<br/>

+) **인터럽트 벡터** : **인터럽트 번호 - 주소 쌍**으로 해당 인터럽트의 처리루틴 **주소**를 갖고 있음.

**인터럽트 처리 루틴**(인터럽트 핸들러, **Interrupt Service Routine**): 해당 인터럽트를 처리하는 커널 함수로 **실제 해야할 일**이라고 생각하면 됨. 

<br/>

=> 인터럽트 당한 시점의 레지스터와 program counter를 저장한 후, CPU의 제어를 인터럽트 처리 루틴에 넘긴다.

=> 현대 OS는 interrupt 구조에 의해 구동된다. (interrupt 걸릴 때만 OS가 CPU를 가짐)

<br/>

**-동기식 입출력과 비동기식 입출력**

- **동기식 입출력**(Synchronous I/O) - I/O 요청 후, 작업이 완료된 후에야 제어가 사용자 프로그램에 넘어감. (다른 일을 수행하지 않고 기다림, 결과를 보고 다음 작업)
- **비동기식 입출력**(Asynchronous I/O) - I/O가 시작 된 후, 작업이 끝나기를 기다리지 않고, 제어가 사용자 프로그램에 즉시 넘어감. (입출력과 무관한 일로 넘어감)

<br/>

**-DMA(Direct Memory Access)**

: 입출력 장치를 메모리에 가까운 속도로 처리하기 위해 사용. CPU의 중재 없이, 장치 제어기가 장치의 buffer storage 내용을 메모리에 **block 단위**로 직접 전송.

(byte 단위가 아닌 block 단위로 인터럽트를 발생시킴)

---

<br/>

**-서로 다른 I/O 명령어**

instruction의 두 가지 종류) 

- memory에 접근하는 instruction (ex. load store)

- I/O장치에 접근하는 instruction (by I/O를 수행하는 special instruction)

이렇게 보통은 memory와 device 주소를 각각 따로 두는 것이 일반적인데,

I/O device에 memory 주소를 매겨서 memory에 접근하는 instruction을 통해 I/O에 접근할 수도 있다. (**Memory Mapped I/O**)

<br/>

**-저장장치 계층구조**

![저장장치 계층구조](https://user-images.githubusercontent.com/58247800/100134946-4a519a00-2ecc-11eb-93ed-5c1355177eda.png)

- Primary storage ) CPU가 직접 접근해서 처리 가능 (Executable, byte 단위), 휘발성 매체

​       CPU - Register - Cache Memory(중간에서 속도 완충: **Caching** - 빠른 매체로 정보를 복사해서 올림, 재사용이 목적) - Main Memory (D-RAM)

- Secondary storage ) CPU가 직접 접근해서 처리하지 못함, 비휘발성 매체

​       Magnetic Disk - Optical Disk - Magnetic Tape 

=> 상위 단계일수록 속도가 빠른 매체를 사용 (비싸고 용량 적음)

<br/>

**-프로그램의 실행** (프로그램이 컴퓨터에서 어떻게 실행되는가?)

![프로그램의 실행1](https://user-images.githubusercontent.com/58247800/100134970-550c2f00-2ecc-11eb-8cf3-1ddb0d72b0d4.png)

보통 프로그램은 파일 시스템(비휘발성 디스크)내에 실행파일 형태로 저장되어 있다. 이 실행파일을 실행시키면 **메모리**에 올라가 **프로세스**가 된다. (정확하게는 **가상 메모리**를 거쳐 물리적 메모리로 올려 실행시킴, 논리적 메모리 주소가 물리적 메모리 주소로 변환됨)

![프로그램의 실행](https://user-images.githubusercontent.com/58247800/100134984-58071f80-2ecc-11eb-9a6b-cf6536b9e2c7.png)

1) 프로그램을 실행하면 그 프로그램의 **독자적인 메모리 주소공간**(code, data, stack 영역을 가진)이 생김.

- **code** - 기계어 코드를 담고 있음
- **data** - 변수 / 자료구조를 담고 있음
- **stack** - 데이터를 쌓거나 빼가는 용도

2) 당장 필요한 것만 물리적 메모리에 올린다. 그렇지 않은 부분은 디스크의 Swap area(메인 메모리의 연장공간, 전원 나가면 종료)에 내려놓는다.

부팅하면 커널영역은 메모리에 항상 상주해있지만, 사용자 프로그램 주소공간은 프로그램 종료 시 사라진다.

<br/>

**-커널 주소 공간의 내용**

![커널 주소공간](https://user-images.githubusercontent.com/58247800/100134999-5dfd0080-2ecc-11eb-8222-8c82218146cb.png)

- **code** (커널 코드) 

  - 시스템콜, 인터럽트 처리 코드
  - 자원 관리를 위한 코드
  - 편리한 서비스 제공을 위한 코드

- **data** (운영체제가 사용하는 자료구조들)

  - CPU, memory, disk와 같은 HW를 관리하기 위해 각각의 자료구조를 갖고 있음.
  - 프로세스들을 관리하기 위해 각 프로세스마다 자료구조(**PCB**)를 갖고 있음.

- **stack** (함수 호출 시 사용)

  : 사용자 프로그램마다 커널스택을 따로 갖고 있음.

<br/>

**-사용자 프로그램이 사용하는 함수**

- **사용자 정의 함수**

  : 자신의 프로그램에서 정의한 함수 (내가 직접 작성한 함수를 불러와 씀)

- **라이브러리 함수**

  : 자신의 프로그램에서 정의하지 않고 가져다 쓴 함수

=> 사용자 정의 함수와 라이브러리 함수 둘 다 자신의 프로그램 실행파일에 포함되어 있음. (사용자 프로세스의 code영역 내에서 점프하며 실행)

- **커널 함수**

  : 운영체제 프로그램의 함수. 내가 갖고있지 않고, 커널 함수를 호출해(virtual memory 내에서 점프할 수 없으므로, interrupt line을 세팅하고 **시스템 콜**) 씀.

<br/>

**-프로그램의 실행** (프로그램 A 관점에서)

![프로그램A의 관점 실행](https://user-images.githubusercontent.com/58247800/100135008-60f7f100-2ecc-11eb-8050-e4a95be52ce9.png)

<br/>

## Ch3. 프로세스

**-프로세스의 개념**

: 프로세스는 **실행 중인 프로그램**이라는 뜻이다. 프로그램이 메인 메모리에 올라와 실행되고 있다면, (CPU가 이를 다룰 수 있는 상태) 프로세스라고 한다.

<br/>

**-프로세스의 문맥**(context)

: 현재 어디서, 어떤 instruction을 수행했고, 어떤 상태인지를 나타내는 **프로세스의 모든 실행정보**.

CPU가 여러 프로세스를 왔다갔다(**동적상태**)하므로 이러한 문맥(어디까지 했으며, 어디서부터 다시 시작할지..)이 중요하다.

![프로세스 문맥 요소](https://user-images.githubusercontent.com/58247800/100429958-7beb8080-30d9-11eb-9ad1-101d7c5f36e1.png)

프로세스의 문맥을 나타내는 세 가지 요소를 알아보자.

- CPU 수행상태를 나타내는 **하드웨어 문맥** (현재 어떤 instruction을 수행하는지 보여준다)

  : program counter가 어딜 가리키는지? / 각종 register에 어떤 내용이 담겼는지?

- **프로세스의 주소공간** (memory 방면)

  : code, data, stack

- 프로세스 관련 **커널 자료구조** (커널상태 규명)

  : PCB, Kernel stack

<br/>

- **프로세스의 상태**(Process State)

: 프로세스는 상태가 변경되며 수행된다.

- **Running** - CPU를 **잡고** instruction을 수행 중인 상태

- **Ready** - CPU를 **기다리는** 상태 (다른 조건은 모두 만족한 뒤)

- **Blocked** (wait, sleep) - CPU를 주어도 당장은 instruction을 **수행할 수 없는** 상태. 

  프로세스 자신이 요청한 이벤트(ex. I/O)가 만족되지 않아 이를 기다리는 중. (ex. 디스크에서 파일을 읽어와야 하는 경우)

<br/>  

-중기 스케줄러로 인해 생긴 상태

- **Suspended** (stopped) - **외부적인 이유**로 프로세스의 수행이 강제로 정지된 상태. 프로세스는 통째로 디스크에 **swap out**되고, 메모리를 잃어버림. (ex. 사용자가 프로그램을 일시정지함 : break-key / 시스템이 여러 이유로 프로세스를 일시정지함)

***Blocked와 Suspended의 차이**

: Blocked는 자신이 요청한 event가 **완료되면 Ready**. 

Suspended는 **외부에서 resume** 해주어야 다시 active.

<br/>

+)

+ New - 프로세스가 생성 중인 상태
+ Terminated - 수행이 끝난 상태 (종료 전 정리...)

<br/>

**-프로세스 상태도1**

먼저, _상태변화_에 초점을 맞춘 프로세스 상태도를 살펴보자. 

![프로세스 상태도1](https://user-images.githubusercontent.com/58247800/100430122-ab9a8880-30d9-11eb-9954-84bc521bae7b.png)

1) 처음에 프로세스가 생성 중인 상태(**New**) 

2) 프로세스가 생성되면(memory를 가지고) **ready** 상태 

3) 본인 차례가 돼서 CPU를 얻으면 **running** 

4-1) 자진해서 반납할 경우 -> (I/O같은 오래걸리는 작업할 때) **blocked** 후 결과값을 얻어서 다시 **ready** 

4-2) 할당시간 만료로 CPU 뺏긴 경우 -> 다시 줄을 선다. (**ready**) 

5) 본인의 역할을 다하면 상태종료 (**terminated**)

<br/>

**-프로세스 상태도2**

이번엔 컴퓨터 _시스템 입장_에서의 프로세스 상태도를 살펴보자. (마치 여러 놀이기구를 운영하는 것과 비슷..)

![프로세스 상태도2](https://user-images.githubusercontent.com/58247800/100430144-b6551d80-30d9-11eb-9c26-a18c04d2b896.png)

- CPU에는 하나의 프로세스만 running 하고 있고, 시간이 다 되어 CPU를 뺏기면 **Ready queue**에 줄을 세움. 그 다음 프로세스가 CPU를 얻고... 

- I/O 입출력이 필요하면 blocked 상태가 되어 Disk **I/O queue**에 줄을 선다. 디스크는 장치 컨트롤러의 지휘 하에 요청이 들어온 내용을 순서에 맞게 처리한다. 작업이 다 끝나면 장치 컨트롤러가 CPU에게 작업이 끝났다는 인터럽트를 걸고, CPU는 하던 일을 잠시 멈추고 **OS 커널**이 주도권을 가져가게 됨. 

커널은 1) 프로세스의 메모리 영역에 해당하는 데이터(I/O작업의 결과)를 넘겨줌 

​			 2) 프로세스의 **상태를 blocked에서 ready로** 바꿔줌 (다시 CPU를 얻을 수 있도록)

*사실 커널이 자신의 데이터 영역에 자료구조로 queue를 만들어 놓고, 상태를 바꿔가며 운영하는 것.

<br/>

**-프로세스 상태도3**

![프로세스 상태도3](https://user-images.githubusercontent.com/58247800/100430152-b81ee100-30d9-11eb-9bf9-522f5fecd73c.png)

마지막으로, _사용자 프로그램_의 관점에서 프로세스 상태도를 살펴보자.

running 상태를 두 가지로 나눠서 표현 (user mode / monitor mode) 했다.

유의할 점) 'OS가 running 하고 있다'라고는 표현하지 않고, '**프로세스가 커널모드에서 running** 하고있다'라고 함.

suspended 상태에서는 메모리를 잃어버렸으므로, CPU작업을 수행할 수가 없는 inactive 상태가 된다.

<br/>

**-PCB (Process Control Block)**

: 운영체제가 각 프로세스를 관리하기 위해 **프로세스당** 유지하는 정보

다음의 구성요소를 가짐 (구조체로 유지)

![PCB 구조](https://user-images.githubusercontent.com/58247800/100430197-ca991a80-30d9-11eb-9b3c-e5c0e7dfca86.png)

- 1) OS가 관리상 사용하는 정보
  - Process state(프로세스가 어떤 상태인지), Process ID
  - Scheduling information, priority
- 2) CPU 수행 관련 HW 값 (문맥 관련)
  - Program counter, registers
- 3) 메모리 관련
  - code, data, stack의 위치정보
- 4) 파일 관련
  - Open file descriptors...

<br/>

**-문맥 교환 (Context Swith)**

: 한 프로세스에서 **다른 프로세스**로 CPU를 넘겨주는 과정.

*CPU가 다른 프로세스에게 넘어갈 때 OS는?

: CPU를 내어주는 프로세스의 상태를 그 프로세스의 **PCB(in 커널 주소공간)에 저장**. (여기까지 했다잉)

CPU를 새롭게 얻는 프로세스의 상태를 **PCB에서 읽어와** HW에 복원. (어디까지 했더라? 어디서부터 해야하지?)

<br/>

*system call / interrupt 발생 시, 반드시 문맥교환이 일어나는 것은 아니다. (ex. 프로그램A -> OS 커널 -> 프로그램A)

이 경우에도 약간의 정보가 PCB에 저장되지만, 문맥교환이 일어나는 경우보다 부담이 적다.

<br/>

**-프로세스를 스케줄링하기 위한 큐**

**Job queue** ) 현재 시스템 내에 있는 모든 프로세스의 집합

- **Ready queue** - 현재 메모리 내에 있으면서, **CPU를 잡아 실행되기를 기다리는** 프로세스의 집합
- **Device queue** - **I/O device의 처리를 기다리는** 프로세스의 집합

=> 프로세스들은 각 큐들을 오가며 수행된다.

![큐](https://user-images.githubusercontent.com/58247800/100430228-d684dc80-30d9-11eb-9ff4-793ddb575399.png)

자료구조 형태로 보면,

큐에 줄 서있다는 것은 **PCB를 줄세워** 놓았다는 것. (pointer를 이용해)

프로세스들이 다양한 큐에 줄 서서 서비스를 받기를 기다리고, OS가 관리함.

<br/>

![스케줄링 받는](https://user-images.githubusercontent.com/58247800/100430240-da186380-30d9-11eb-8389-9ae2ccc3f89a.png)

하나의 프로세스가 스케줄링 되는 모습을 표현

<br/>

**-스케줄러 (Scheduler)**

- **Long-term scheduler** (장기 스케줄러, job scheduler)

  : 프로세스에 **memory 및 각종 자원을 주는 문제**를 다룬다.

  즉, 시작 프로세스 중 어떤 것들을 ready queue로 보낼지(memory를 줄지) 결정한다. (New -> ready로 admitted)

  이런 방식으로 **degree of Multiprogramming**을 제어 (메모리에 올라가 있는 프로그램의 수를 _처음부터_ 조절 - 프로그램이 메모리에 너무 많아도 적어도 성능 안 좋음)

  보통 우리가 사용하는 time sharing system에는 장기 스케줄러가 없다. (프로그램 실행 시키면 무조건 메모리를 주어 ready로) **중기 스케줄러가 메모리 성능 제어를 대신**함.

<br/>

- **Short-term scheduler** (단기 스케줄러, CPU scheduler)

  : 프로세스에 **CPU를 주는 문제**를 다룬다.

  즉, 어떤 프로세스를 다음번에 running 시킬지 결정한다.

  따라서 충분히 빨라야 한다. (millisecond 단위)

<br/>

- **Medium-term scheduler** (중기 스케줄러, Swapper)

  : 프로세스에게서 **memory를 '뺏는'** 문제를 다룬다.

  _일단 프로그램을 메모리에 다 올려놓고_ **여유공간 마련을 위해 프로세스를 통째로 (메모리에서 디스크로) 쫓아낸다. ** -> (악역이지만, 장기 스케줄러보다 훨씬 더 효과적)

  이런 방식으로 degree of Multiprogramming을 제어

<br/>

**-Thread** (= lightweight process)

: 프로세스를 여러 개 두지 않고, 프로세스 내부에 CPU 수행단위만 여러 개 두고 있는 것. 

즉, 프로세스를 하나만 띄우고, 프로그램 카운터(현재 어느 부분을 수행하고 있는지 가리킴)만 여러 개를 두는 것. 

<br/>

- heavyweight process - 하나의 thread를 가지고 있는 task

![heavyweight 프로세스](https://user-images.githubusercontent.com/58247800/100430276-e7355280-30d9-11eb-89df-8e109745fc6e.png)

프로세스마다 왼쪽의 주소공간이 생긴다. 그리고 프로세스 하나를 관리하기 위해 OS 내부에서 프로세스 정보가 담긴 PCB를 관리한다.

그런데 만약, **동일한 일을 하는 프로세스가 여러 개** 있다면, 프로세스 주소공간이 여러 개가 만들어짐. (**메모리가 낭비됨**)

<br/>

- lightweight process - 여러 개의 thread를 가지고 있는 task

![thread](https://user-images.githubusercontent.com/58247800/100430285-eac8d980-30d9-11eb-88d2-315bf553cfb0.png)

=>  **주소공간을 하나만** 띄워놓고, 각 프로세스마다 **다른 부분의 코드를 수행**할 수 있게 해주면 된다.

CPU 수행 단위가 여러개 있으니, stack도 별도로 두어야 한다.

프로세스 여러 개를 두는 것보다 효율적이다. 프로세스 하나에서 공유할 수 있는 것들(메모리 주소, 프로세스 상태, 각종 자원)은 최대한 공유하고, CPU 수행과 관련 있는 것들(프로그램 카운터, register, stack)만 독립적으로 가진다.

<br/>

- Thread의 구성 (CPU 수행과 관련있는 것들을 독립적으로 가짐)

  - Program counter
  - register set
  - stack space

- Thread가 동료 thread와 공유하는 부분 (= task) 

  (프로세스 1개에 여러개의 threads와 task 1개)

  - code section
  - data section
  - OS resources

프로세스가 하나이기 때문에 PCB도 하나만 생성됨. 그러나 PCB 안에 CPU 수행과 관련된  정보를 각 thread마다 별도의 copy를 가지게 된다. (program counter, registers)

<br/>

- 장점

  - 다중 thread로 구성된 task 구조에서는, 

    하나의 서버 thread가 blocked(waiting)상태인 동안에도, 

    동일한 task 내의 다른 thread가 실행(running)되어 빠른 처리가 가능하다. (빠른 응답성 제공) 

    (ex. 웹페이지 읽어올 때, img thread가 실행되는 동안 txt thread가 완료)

  - 동일한 일을 수행하는 다중 thread가 협력하여 높은 처리율(throughput)과 성능향상(자원절약)을 얻을 수 있다.

  - thread를 사용하면 병렬성을 높일 수 있다. (ex. CPU가 많은 컴퓨터에서만)

<br/>

- 장점요약

  - **응답성**(Responsiveness) : 일종의 **비동기식 작업**과 같이, 만약 한 thread(img)가 blocked 상태여도, 다른 thread(txt)가 continue. (ex. multi-threaded web)

  - **자원의 공유**(Resource sharing) : n개의 thread가 binary code, data, 프로세스 자원 공유.

  - **경제성**(Econonmy) : thread에서 **creating & CPU switching**(문맥교환) 하는 것이 프로세스에서 하는 것보다 빠름. 

    즉, 프로세스 생성보다 thread 생성(숟가락만 얹는..)이 30배 더 빠르다. 또한, CPU 문맥교환보다는 프로세스 내에서 thread간 이동이 5배 더 빠르다.

  - Utilization of MP architectures : 다른 CPU 위에서 각각의 thread들이 병렬적으로 실행된다. (다중 CPU 환경에서)

<br/>

**-Thread 수행**

- **Kernel Threads** (supported by Kernel)

  : 커널이 thread가 많다는 것을 OS가 알고 있다. 

  ex. windows 95/98/NT, Solaris, Digital UNIX, March

- **User Threads** (supported by library)

  : OS는 thread가 많다는 것을 모르고, user program이 라이브러리의 지원을 받아 스스로 thread를 관리한다.

  ex. POSIX Pthreads, March C-threads, Solaris threads

- real-time threads
