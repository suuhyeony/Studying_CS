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

<br/>

## Ch4. 프로세스 관리

**-프로세스 생성 (Process Creation)**

: 부모 프로세스가 자식 프로세스를 **복제생성**한다. 문맥(주소공간, program counter)을 모두 복제해 생성한다. 

(효율적인 OS에서는 일단 copy하지 않고, 자식이 부모의 주소공간을 공유하다가 내용이 달라져야할 때, 그 때 일부를 copy. 즉, (내용을 바꾸는)write가 발생했을 때, copy를 하겠다 : _COW_)

- 프로세스의 트리 (계층구조) 형성 (자식을 여럿 생성, 자식이 자식을 생성..)

- 프로세스는 자원(CPU, memory)을 필요로 함 

  - **운영체제로부터 자원을 받는** 경우 (일반적)
  - 부모와 자원을 공유하는 경우

- 자원의 공유(보다는 **경쟁**) - 프로세스가 만들어지면 독립적인 프로세스가 됨

  - 부모와 자식이 모든 자원을 공유하는 모델
  - 일부만 공유하는 모델 (**copy-on-write** : _COW_)
  - 전혀 **공유하지 않는** 모델 (일반적/원칙적)

- 수행

  - 부모와 자식이 공존하며 수행되는 모델
  - 자식을 생성한 뒤, 자식이 종료될 때까지 부모가 기다리는 모델

<br/>


부모 프로세스는 어떻게 자식을 생성할까?

프로세스 생성을 OS에게 부탁해 시스템 콜을 통해 자식을 생성한다.

- 주소공간 (Address Space)

  : 자식은 부모의 공간을 복사(binary and OS data)한 뒤, 자식은 그 공간에 새 프로그램을 올린다.

- 유닉스의 예

  - 1단계 ) **fork( )** 시스템 콜이 새로운 프로세스를 생성. (OS가 대신해서 자식을 낳아주는 격) 
    - 부모를 그대로 복사(OS data except PID + binary)
    - 주소 공간 할당
  - 2단계 ) fork 다음에 이어지는 **exec( )** 시스템 콜을 통해 새로운 프로그램을 메모리에 올리고, 덮어씌움.

<br/>

**-프로세스 종료** (Process Termination)

: 프로세스의 세상에서는 자식이 부모보다 먼저 죽어야한다.

- **exit(자발적 종료)** : 프로세스가 마지막 명령을 수행한 후, OS에게 이를 알려줌.
  - 자식이 부모에게 output data를 보냄 (wait를 통해)
  - 프로세스의 각종 자원들이 OS에게 반납됨
- **abort(강제 종료)** : 부모 프로세스가 자식의 수행을 종료시킴.
  - 자식이 할당자원의 한계치를 넘어섬 (자식이 펑펑 씀)
  - 자식에게 할당된 task가 더 이상 필요하지 않음 (자식한테 시킬 일이 없음)
- **단계적 종료** : 부모가 종료되는 경우, OS는 자식이 더 이상 수행되도록 두지 않는다. (손자 죽고->자식 죽고->부모 죽음)

<br/>

프로세스의 생성부터 종료까지 관리하는 시스템 콜 종류에 대해 알아보자.

**-fork( ) 시스템 콜**

: fork( ) 시스템 콜에 의해 프로세스가 생성된다. (caller에 의해 복제된 새 주소공간 생성)

```c
// 부모 프로세스
int main()
{ int pid;
  printf('\n Hello!\n');
  pid = fork();								         // 자식 프로세스 생성됨 (context복제됨)
  if (pid == 0)		  // 자식일 때   			// 여기서부터 자식 프로세스가 실행됨
      printf('\n Hello, I am child!\n');
  else if (pid > 0) // 부모일 때
      printf('\n Hello, I am parent!\n');
}
```

자식 프로세스는 fork( ) 함수 이후부터 실행.

자식 프로세스의 결과는 Hello, I am child!

부모 프로세스의 결과는 Hello!

​										 Hello, I am parent!

<br/>

- 문제점
  - 복제본(자식)이 본인을 원본이라 주장, 부모를 복제본 취급
  - 세상 모든 프로세스가 동일한 흐름을 따름
- 해결방안 (fork의 return 값을 다르게 설정)
  - 부모 return 값을 > 0, 자식 return 값을 = 1로 설정.

<br/>

**-exec( ) 시스템 콜**

: 프로세스는 exec( ) 시스템 콜에 의해 다른 프로그램을 수행할 수 있다. 완전 **새로운 프로그램**(갓난아기)**으로 덮어 씌워짐**. 한 번 exec 하면 되돌아와 다음 함수를 실행할 수 없다. (exec 이후의 코드는 영원히 실행 불가)

<br/>

**-wait( ) 시스템 콜** (자식과 경쟁하지 않는 모델에서)

: 프로세스 A가 wait( ) 시스템 콜을 호출하면, (보통 **자식 프로세스를 만들고 wait**)

- 커널은 **child가 종료될 때까지 프로세스 A를 sleep**시킨다. (block 상태)
- childe 프로세스가 종료되면, 커널은 프로세스 A를 깨운다. (ready 상태)

![wait 시스템콜](https://user-images.githubusercontent.com/58247800/100582581-cfa1d800-332c-11eb-956d-96d4b4faec60.png)

<br/>

**-exit( ) 시스템 콜**

: 프로세스의 종료

- **자발적 종료**
  - 마지막 statement 수행 후, exit( ) 시스템 콜을 통해 종료 
  - 프로그램에 명시적으로 적어주지 않아도, main 함수가 return되는 위치에 컴파일러가 넣어줌
- **비자발적 종료** (부모/사람이)
  - 부모 프로세스가 자식 프로세스를 강제 종료시킴
  - 사람이 키보드로 kill, break 등을 친 경우
  - 부모가 종료되는 경우에는 부모 종료 전, 자식들이 먼저 종료됨

<br/>

**-프로세스 간 협력**

- 독립적 프로세스 (Independent process)

  : 프로세스는 각자의 주소 공간을 가지고 수행되므로, 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 않는다.

- 협력 프로세스 (Cooperating process)

  : 프로세스 협력 매커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미친다.

  - 프로세스간 협력 매커니즘 (**IPC : Interprocess Communication**)

    : 프로세스간 정보를 주고 받는 매커니즘

- **message passing** : **커널**을 통해 메시지 전달

  - **shared memory** : 서로 다른 프로세스 간에도 (물리적 메모리에 매핑할 때) **일부 주소 공간을 공유**하게 하는 shared 메모리 매커니즘이 있음 (신뢰할 수 있는 프로세스끼리 사용한다. 처음에는 커널이 공간을 만들어 주고, 이후에는 자기들끼리 점잖게..)

  cf) **thread 간의 협력** : thread는 사실상 하나의 프로세스이므로 프로세스간 협력으로 보기 어렵지만,

  ​									동일 프로세스를 구성하는 thread들 간에는 주소 공간을 공유하므로 협력 가능.

  <br/>

**-Interprocess Communication**

![IPC](https://user-images.githubusercontent.com/58247800/100582603-d7fa1300-332c-11eb-8c27-62479baf0217.png)

<br/>

**-Message Passing**

- **message system** : 프로세스 사이에 공유변수를 일체 사용하지 않고, **커널**을 통해 통신하는 시스템.

  - **Direct Communication** : 통신하려는 프로세스의 **이름을 명시**적으로 표시

    ![direct 메시지](https://user-images.githubusercontent.com/58247800/100582619-dd575d80-332c-11eb-9bc1-3199f1b627b8.png)

  - **Indirect Communication** : **Mailbox**(또는 port)를 통해 메시지를 간접 전달 (아무나에게 보낼 수 있음)

    ![indirect 메시지](https://user-images.githubusercontent.com/58247800/100582630-dfb9b780-332c-11eb-976d-d48d22ecaab1.png)



## Ch5. CPU 스케줄링

**-CPU and I/O Bursts in Program Execution**

: CPU를 연속적으로 수행하는 단계와 I/O를 수행하는 단계가 연속적으로 나옴.

![CPU burst time](https://user-images.githubusercontent.com/58247800/100880173-c745ca80-34ef-11eb-8b12-4dbc5f0b22f0.png)

<br/>

**-CPU-burst Time의 분포**

![CPU burst time2](https://user-images.githubusercontent.com/58247800/100880190-cad95180-34ef-11eb-98b6-767da95b3148.png)

=> 여러 종류의 job(=process)이 섞여 있으므로, **'CPU 스케줄링'이 필요**하다.

- Interactive job이 오래 기다리지 않도록 적절한 응답 제공 요망 (interactive한 I/O job에게)
- CPU와 I/O장치 등 시스템 자원을 골고루 효율적으로 사용

<br/>

**-프로세스의 특성 분류**

- **I/O-bound process**

  : CPU를 잡고 계산하는 시간보다, I/O에 많은 시간이 필요한 job. 짧게 쓰는데 빈도가 많다.(many short CPU bursts) 주로 사람과 interaction하는 job.

- **CPU-bound process**

  : 계산 위주의 job. 빈도가 적지만 길게 쓴다.(few very long CPU bursts)

<br/>

**-CPU Scheduler & Dispatcher**

- CPU Scheduler (OS 안에서 수행되는 코드)

  : ready 상태의 프로세스 중에서, 이번에 CPU를 줄 프로세스를 고른다. (결정)

- Dispatcher (OS 안에서 수행되는 코드)

  : CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다. (준다)

  이 과정을 문맥교환(context switch)이라고 한다.

<br/>

**-CPU 스케줄링이 필요한 경우**

: 프로세스에게 다음의 상태 변화가 있을 때.

- 1) Running -> Blocked (ex. I/O 요청하는 시스템콜)
- 2) Running -> Ready (ex. 할당시간 만료로 timer interrupt)
- 3) Blocked -> Ready (ex. I/O 완료 후 인터럽트)
- 4) Terminate

=> 여기서 이슈! (누구에게 CPU를 줄 것인가? / CPU를 계속 쓰게할지 중간에 뺏을지?)

<br/>

**-스케줄링 방법**

- 비선점형 (**non preemptive**) - 1), 4)번과 같이 CPU를 **자진 반납**
- 선점형 (**preemptive**) - 2), 3)번과 같이 CPU를 강제로 **빼앗음** (현대적 방법)

<br/>

**-Scheduling Criteria** (스케줄링 성능척도)

: Performance Index (=performance Measure, 성능척도) (중국집 비유)

- 시스템 입장

  - **CUP utilization (이용률)**

    : CPU가 놀지 않고 **일한 시간**. CPU를 가능한 바쁘게 유지한다. (이용률을 높게)

    (주방장이 얼마나 많이 일했는가?)

  - **Throughput (처리량)**

    : 주어진 시간동안 **몇 개의 일**을 완료했는지? (처리량 많게)

    (손님이 얼마나 다녀갔는가?)

- 프로세스(고객) 입장

  - **Turnaround time (소요시간, 반환시간)**

    : 프로세스가 CPU를 쓰러 들어와서(ready), **다 쓰고 나갈 때까지** 걸리는 시간.

    (손님이 와서 다 먹기까지 시간)

  - **Waiting time (대기시간)**

    : 프로세스가 ready 큐에서 **순수하게 기다린** 시간 (기다린 시간을 모두 합친 시간)

    (손님이 기다리는 시간)

  - **Response time (응답시간)**

    : ready 큐에 들어와서 **처음으로 CPU를 얻기까지** 걸리는 시간.

    (첫 번째 요리가 나오기까지 걸리는 시간)

 <br/>

**-Scheduling Algorithms**

- FCFS (First-Come First-Served)
- SJF (Shortest-Job-First)
- SRTF (Shortest-Remaining-Time-First)
- Priority Scheduling
- RR (Round Robin)
- Multilevel Queue
- Multilevel Feedback Queue

<br/>

**-1. FCFS (First-Come First-Served)**

: 먼저 온 순서대로 처리 (**비선점형**에 포함. 사람의 세계에서.. 은행/공중 화장실) **비효율적**.

- **ex1**) 프로세스 도착순서 P1, P2, P3 (burst time은 각 24, 3, 3)

![FCFS ex1](https://user-images.githubusercontent.com/58247800/100880205-cdd44200-34ef-11eb-957b-581a1c242ab4.png)

  - waiting time = ( 0; 24; 27)

  - 평균 대기시간 = 17

가장 먼저 온 P1이 제일 오래 걸릴 경우, 응답시간과 평균대기시간이 늘어난다. (interactive하지도, 효율적이지도 않다)

<br/>

- **ex2**) 프로세스 도착순서 P2, P3, P1

![FCFS ex2](https://user-images.githubusercontent.com/58247800/100880211-d0369c00-34ef-11eb-85ed-6386f7106c55.png)

  - waiting time = (6; 0; 3)
  - 평균 대기시간 = 3

ex1 보다 훨씬 효율적. 제일 **처음에 도착한 P에 따라 대기시간이 달라진다**!

즉, 이 스케줄링에서는 **Convoy effect** (short process behind long process. 앞에 똥차가 버티고 있는..) 라는 문제점이 생긴다. (코스요리 손님 뒤에 짜장면 손님..)

<br/>

**-2. SJF (Shortest-Job-First)**

: **짧게 걸리는 프로세스 먼저** 처리. 각 프로세스의 **다음 번 CPU burst time**(예측값)을 가지고 스케줄링에 활용. (볼 일을 제일 빨리 볼 수 있는 사람부터 화장실 가기)

즉, CPU burst time이 가장 짧은 프로세스를 제일 먼저 스케줄

<br/>

- Two schemes:

  - Non-preemptive

    : 일단 CPU를 잡으면, 더 빠른 애가 오더라도 이번 CPU burst가 완료될 때까지 CPU를 선점 당하지 않음.

  - **Preemptive**

    : 현재 수행 중인 프로세스의 **남은 burst time** 보다, **더 짧은 CPU burst time**을 가지는 새로운 프로세스가 도착하면, CPU를 빼앗김. 이 방법은 **SRTF** (Shortest-Remaining-Time-First) 라고도 부른다.

<br/>

**SJF is Optimal** (평균 대기시간을 최소화함)

: 주어진 프로세스들에 대해 **minimum average waiting time**을 보장한다. (**선점형 ver.**)

- **ex**) of Non-preemptive SJF

![SJF ex1](https://user-images.githubusercontent.com/58247800/100880224-d4fb5000-34ef-11eb-934f-fa8a61b94bc9.png)

평균 대기시간 = (0 + 6 + 3 + 7) / 4 = 4

CPU를 **다 쓰고 나가는 시점**에 스케줄링 결정

<br/>

- **ex**) of Preemptive SJF

![SJF ex2](https://user-images.githubusercontent.com/58247800/100880230-d6c51380-34ef-11eb-9e91-2d81153200db.png)

평균 대기시간 = (9 + 1 + 0 + 2) / 4 = 3 (가장 짧음)

**새 프로세스가 도착하는 시점**에도 스케줄링이 결정됨!

<br/>

- 문제점

  - **starvation(기아현상)** - 내 차례가 되기 전에 자꾸 나보다 덜 걸리는 애들이 도착하면 ㅠㅠ... 난 언제쓰냐구..

  - CPU 사용시간을 미리 알 수 없다. (이번에 내가 얼마나 쓰고 나갈지 모른다.. 예측만 가능!)

<br/>

**-다음 번 CPU burst time의 예측**

: 추정만이 가능하다. (**과거의 CPU burst time을 이용해 추정**.)

- **exponential averaging** 방법 사용
  - 1) t(n) = 실제 CPU 사용 시간 (과거 자료로 이미 주어진) 
  - 2) τ(n+1) = CPU 사용을 예측한 시간 (n+1번 째)
  - α, 0 <= α <= 1
  - Define : τ * (n+1) = α * t(n) + (1-α) * τ(n) => 1), 2)를 일정 비율씩 반영한다

식을 풀면, 이런 결과가 나옴..

![식](https://user-images.githubusercontent.com/58247800/100880252-da589a80-34ef-11eb-8148-1968a320fa24.png)

α와 (1-α)가 둘 다 1 이하이므로 후속 term은 선행 term보다 더 적은 가중치 값을 가진다.

즉, 더 이전의 실제 실행 시간을 적게 반영하는 것이다.

<br/>

**-3. Priority Scheduling**

: 우선순위가 높은 프로세스부터 스케줄링. (추상적 개념) 각 프로세스마다 우선순위 번호가 할당되어 있다. highest priority(=smallest integer)를 가진 프로세스에게 CPU할당.

선점형/비선점형 두 가지 ver. 있음.

*SJF는 일종의 Priority scheduling이다.

Priority = 다음 CPU burst time을 예측한 것

<br/>

- 문제점

  **Starvation(기아현상)** : 특정 프로세스가 지나치게 차별받는다. 낮은 우선순위의 프로세스는 영원히 실행될 수 없음.

- 해결책

  **Aging(노화)** : 아무리 우선순위가 낮아도, **오래 기다리게 되면 우선순위가 올라가도록** 해준다.

  ​						(경로우대..)

<br/>  

**-4. RR (Round Robin)**

: 각 프로세스는 **동일한 크기의 할당시간**(**time quantum** - 일반적으로 10~100 miliseconds)을 가짐. (선점형)

할당시간이 지나면 프로세스는 선점당하고, ready 큐의 맨 뒤에 가서 다시 줄 섬. (**현대 컴퓨터 방식**)

(5분 동안만 사용할 수 있는 홍대 화장실... 5분 뒤 문열림ㅋㅋ)

- 장점

  - 누구나 CPU를 조금이라도 맛볼 수 있어 **응답시간이 빨라진다**.

  - **기다리는 시간이 본인의 작업 처리시간과 비례한다.**

  n개의 프로세스가 ready큐에 있고, 할당시간이 q time unit인 경우, 각 프로세스는 최대 q time unit 단위로 CUP시간의 1/n을 얻는다.

  => **어떤 프로세스도 (n-1)q time unit 이상 기다리지 않는다**.

  - 예측 시간을 계산할 필요가 없다.

- performance (극단적 상황)

  - q large -> FCFS
  - q small -> context switch 오버헤드가 커짐

  => **적당한 할당 시간이 필요**하다.

- **ex**) of RR (with Time Quantum = 20)

![RR](https://user-images.githubusercontent.com/58247800/100880260-dcbaf480-34ef-11eb-842d-da52a2250169.png)

  일반적으로 SJF 보다 average turnaround time / waiting time이 길지만, **response time은 더 짧다**. 보통 짧은 작업 긴 작업이 섞여있기 때문에 RR이 효과가 있다.

  (극단적일 경우- 모든 프로세스의 사용시간 같을 시, 굳이 난도질할 필요 없이 q time을 길게 잡는다.)

<br/>

**-5. Multilevel Queue**

: 그동안 한 줄 서기를 했는데, 여러 줄로 CPU를 기다리는 줄을 세운다. 줄마다 우선 순위가 다르고, 위로 갈수록 우선순위가 높다. (성골, 진골, 6두품, 노비...) 태어난 신분에 따라 영원히 그 줄로 살아야 함. (차별적)

![multilevel큐](https://user-images.githubusercontent.com/58247800/100880280-e2183f00-34ef-11eb-9b89-d00ea4d80f47.png)

- **Ready Queue를 여러 개로 분할**

  - **foreground** (interactive한 job)
  - **background**(batch - no human interaction)

- 각 큐는 **독립적인 스케줄링 알고리즘**을 가진다.

  - foreground - RR (응답시간을 짧게 하기 때문에)
  - background -FCFS (응답시간을 짧게 할 필요가 없어서)

- 큐에 대한 스케줄링이 필요하다.

  - **Fixed priority scheduling**

    : foreground에서 모두 스케줄링하고, background거 스케줄링 -> starvation 발생

  - **Time slice**

    : 각 큐에 **CPU Time을 적절한 비율로 할당** (starvation 방지)

    (ex. 80% 는 foreground걸 RR방식으로, 20%는 background걸 FCFS방식으로) 

<br/>    

**-6. Multilevel Feedback Queue**

프로세스가 다른 큐로 이동(승격/떨어짐) 가능.

보통 처음 들어오는 프로세스에게 제일 우선순위 높은 큐(할당시간은 적음)를 준다.

그 안에 끝나지 못하면, 아래 큐로 강등되고, 기다렸다가 위쪽 큐가 비었을 때 다시 진행된다.

미리 예측할 필요가 없으며, **진행시간이 짧은 프로세스가 (RR보다)우대**받는다! 

<br/>

에이징을 이와 같은 방식으로 구현할 수 있다.

- 고려사항
  - 프로세스를 어느 줄에 넣을지?
  - 기아현상 방지
  - 몇개 큐?
  - 떨어지고 올라가는 기준
- Multilevel-feedback queue scheduler를 정의하는 파라미터
  - queue의 수
  - 각 queue의 scheduling algorithm
  - Process를 상위 queue로 보내는 기준
  - Process를 하위 queue로 내쫓는 기준
  - Process가 CPU 서비스를 받으려할 때, 들어갈 queue를 정하는 기준

- ex) of Multilevel feedback queue

![multilevel feedback 큐](https://user-images.githubusercontent.com/58247800/100880290-e47a9900-34ef-11eb-896c-1cc839897b4e.png)

  - Three queues

    - Q0 ) time quantum 8 miliseconds
    - Q1 ) time quantum 16 miliseconds
    - Q2 ) FCFS

  - Scheduling

    : new job이 queue Q0 으로 들어감.

    - CPU를 잡아서 할당시간 8ms 동안 수행됨
    - 8ms 동안 끝내지 못하면, queue Q1으로 내려감
    - Q1에 줄서서 기다렸다가, CPU를 잡아서 16ms 동안 수행됨
    - 16ms에 끝내지 못할 경우, queue Q2로 쫓겨남

<br/>

**-Multiple-Processor Scheduling**

: CPU가 여러 개인 경우 (스케줄링이 더 복잡하다)

- Homogeneous Processor인 경우 (한 줄 서기)

  : 큐에 한 줄로 세워서 각 프로세서가 알아서 꺼내가게 할 수 있다. 반드시 특정 프로세서에서 수행되어야 하는 프로세스 존재 시, 문제가 더 복잡해진다.

- Load sharing

  : 일부 프로세서에 job이 몰리지 않도록 부하를 적절히 공유하는 매커니즘 필요. 

  별개의 큐를 두는 방법 vs 공동 큐를 사용하는 방법

- Symmetric Multiprocessing(SMP)

  : 각 CPU가 알아서 스케줄링 결정 (모든 CPU가 대등)

- Asymmetric Multiprocessing

  : 하나의 CPU가 시스템 데이터의 접근과 공유를 책임지고, 나머지 CPU는 거기에 따름.

<br/>

**-Real-Time Scheduling**

: real-time job을 미리 배치해서, 데드라인을 보장하는게 중요하다.

- Hard real-time systems

  : hard real-time task는 정해진 시간 안에 **반드시** 끝내도록 스케줄링 해야함.

- Soft real-time systems

  : soft real-time task는 다른 일반 프로세스에 비해 높은 priority를 갖도록 해야함.

<br/>

**-Thread Scheduling**

- Local Scheduling

  : user level thread의 경우, 사용자 수준의 thread library에 의해 어떤 thread를 스케줄할지 결정 (사용자 프로세스가 직접)

- Global Scheduling

  : kernel level thread의 경우, 일반 프로세스와 마찬가지로 커널의 단기 스케줄러가 어떤 thread를 스케줄할지 결정

<br/>

**-Algorithm Evaluation** (어떤 알고리즘이 좋은지 평가방법)

- **Queueing models** (이론적)

![알고리즘 평가척도](https://user-images.githubusercontent.com/58247800/100880320-ea707a00-34ef-11eb-88a1-4b28481b6858.png)

  : 확률 분포로 주어지는 **arrival rate**(도착률)와 **service rate**(처리율) 등을 통해 각종 performance index 값을 계산

- **Implementation** (구현) & **Measurement** (성능 측정)

  : 실제 시스템에 알고리즘을 구현하여 실제작업(workload)에 대해 성능을 측정 비교

- **Simulation** (모의 실험)

  : 알고리즘을 모의 프로그램으로 작성 후, **trace**(input data)를 입력으로 하여 결과 비교


<br />


## Ch6. 프로세스 동기화

**-Process Synchronization** (=Concurrency Control, 병행 제어)

: 하나의 자원을 한 순간에 하나의 프로세스만이 이용하도록 제어하는 것.

**공유 데이터의 동시 접근**은 **데이터의 불일치 문제**를 발생시킬 수 있다.

일관성 유지를 위해서는 **협력 프로세스 간의 실행 순서를 정해주는** 매커니즘(동기화)이 필요.

<br />

**-데이터의 접근**

: 컴퓨터 시스템 안에서 데이터에 어떻게 접근할까?

![데이터의 접근](https://user-images.githubusercontent.com/58247800/101870685-74da6d00-3bc5-11eb-9f9b-fc85a8c79244.PNG)

데이터가 저장되어 있는 위치로부터 데이터를 읽어와서 연산한 뒤, 연산한 결과를 이전에 저장되어있던 그 위치에 다시 저장.

데이터를 읽기만 하면 문제가 없는데, **데이터를 수정하게 되면 누가 먼저 읽어 갔는지가 중요**하게 됨.

<br />

**-Race Condition (경쟁상태)**

: 여러 프로세스들이 **동시에 공유 데이터를 접근**하는 상황.

데이터의 최종 연산 결과는 **마지막에 그 데이터를 다룬 프로세스에 따라 달라짐**.

![경쟁상태](https://user-images.githubusercontent.com/58247800/101870700-7f950200-3bc5-11eb-907c-500c2a982830.PNG)

S-box(Memory Address space)를 공유하는 E-box(CPU Process)가 여럿있는 경우 Race condition의 가능성이 있다.

한 군데에서 데이터를 가져와 1 증가시키는 도중에, 다른 한 곳에서 또 데이터를 가져가 1 감소시키면, (count--) 의 결과만 반영됨.

<br />

그렇다면, 언제 race condition이 발생할까?

- Multiprocessor system

- 공유 메모리를 접근하는 루틴들 간 

  (ex. 커널모드 수행 중, 인터럽트로 커널모드 다른 루틴 수행 시)

=> race condition을 막기 위해서는 **동시접근(concurrent process)은 동기화되어야** 함.

<br />

**-OS에서 race condition이 언제 발생할까?**

- 1. kernel 수행 중 인터럽트 발생 시
- 2. Process가 system call을 하여 kernel mode로 수행 중인데 context switch 발생 시
- 3. Multiprocessor에서 shared memory 내의 kernel data

<br />

위의 세 가지 경우를 자세히 알아보자.

**-OS에서의 race condition (1)**

: kernel 수행 중 인터럽트 발생 시 (interrupt handler vs kernel)

![os에서의 경쟁상태1](https://user-images.githubusercontent.com/58247800/101870737-90de0e80-3bc5-11eb-882b-32cedec26886.PNG)

커널 모드 running (1.)중, 인터럽트가 발생해 인터럽트 처리루틴이 수행됨.

(양쪽 다 커널 코드이므로 kernel address space공유)

결과적으로 count--계산 결과는 반영되지 않음. (count++부분을 저장했다가 interrupt를 처리한 거라서)

<br />

- 어떻게 share할 수 있을까? 

  중요한 계산 중에는 interrupt 들어와도 처리하지 않고, 다 끝나고 처리.

<br />

**-OS에서의 race condition (2)**

: Process가 system call을 하여 kernel mode로 수행 중인데 context switch 발생 시

(**커널에서 코드 수행 중인데 CPU를 preempt 당한다면?**)

<br />

![os에서의 경쟁상태2-1](https://user-images.githubusercontent.com/58247800/101870743-93d8ff00-3bc5-11eb-88bb-3d460ddc86b1.PNG)

- 두 프로세스의 주소공간 간에는 data sharing이 없다.
- 그러나 system call하는 동안에는 커널 주소공간의 data를 access하게 됨(share)
- 이 작업 중간에 CPU를 preempt 해가면 race condition 발생

<br />

**-if you preempt CPU while in kernel mode**

![os에서의 경쟁상태2-2](https://user-images.githubusercontent.com/58247800/101870750-963b5900-3bc5-11eb-9110-32ee7a4e2714.PNG)

(1) 프로세스 A가 실행 중이다가 system call

(2) 커널 모드에서 count++ 수행하다가, 할당시간 만료로 CPU를 뺏김

(3) 프로세스 B가 커널 모드에서 count++ 수행 중, 시간 만료로 CPU 뺏김

(4) 프로세스 A가 CPU를 되돌려 받아, 아까 작업하던 count++ 진행

결과적으로 프로세스B의 count++는 반영되지 않음! (문맥이 프로세스A걸 저장하고 있기 때문에)

<br />

- 해결책)

  : **커널 모드에서 수행 중일 때는 할당 시간이 끝나도, CPU를 preempt하지 않음**.

  커널 모드에서 사용자 모드로 돌아갈 때 preempt.

<br />

**-OS에서의 race condition (3)**

: Multiprocessor에서 shared memory 내의 kernel data (작업 주체인 CPU가 여럿)

![os에서의 경쟁상태3](https://user-images.githubusercontent.com/58247800/101870755-99364980-3bc5-11eb-9744-57ad833bf4ea.PNG)

어떤 CPU가 마지막으로 count를 store했느냐에 따라 결과가 달라짐.

multiprocessor의 경우, interrupt enable / disable로 해결되지 않음.

- 방법1) 한 번에 하나의 CPU만이 커널에 들어갈 수 있도록 하고, 하나의 커널을 lock으로 막고, 커널을 빠져나올 때 unlock. (**커널 전체를 lock**하기 때문에 비효율적)
- 방법2) 커널 내부에 있는 **각 공유 데이터**에 접근할 때마다 그 데이터에 대한 lock/unlock

<br />

**-The Critical-Section 문제**

: n개의 프로세스가 공유 데이터를 동시에 사용하길 원하는 경우, 각 프로세스의 code segment에는 공유 데이터를 접근하는 코드인 '**critical-section**'(임계구역)이 존재.

<br />

- 과제

  : 하나의 프로세스가 critical-section에 있을 때, 다른 모든 프로세스는 critical-section에 들어갈 수 없어야 함.

![critical-section](https://user-images.githubusercontent.com/58247800/101870717-89b70080-3bc5-11eb-8604-7eeccc33d0c6.PNG)

<br />

**-Initial Attempts to Solve Problem**

- 두 개의 프로세스가 있다고 가정 (P0, P1)

- 프로세스들의 일반적인 구조

  ```c
  do {
  	entry section		// 공유 데이터에 접근하기 이전에 lock을 건다
  	critical section	// 공유 데이터를 접근하는 코드
  	exit section		// 끝나면 unlock(다른 프로세스가 critical-section에 들어갈 수 있게)
  	remainder section
  } while(1);
  ```

- 프로세스들은 수행의 동기화를 위해 몇몇 변수를 공유할 수 있다. (synchronization variable)

<br />

**-프로그램적 해결법의 충족 조건**

: Critical-section을 해결하기 위해서 만족해야 하는 조건은

- **Mutual Exclusion** (상호배제)

  : 프로세스가 critical section 부분을 수행 중이면, 다른 모든 프로세스들은 그들의 critical section에 들어가면 안 됨. (배타적으로 접근해야 함)

- **Progress** (진행)

  : 아무도 critical section에 있지 않은 상태에서 critical section에 들어가고자 하는 프로세스가 있으면, critical section에 들어가게 해줘야 함.

- **Bounded Waiting** (유한대기)

  : 프로세스가 critical section에 들어가려고 요청한 후부터, 그 요청이 허용될 때까지 다른 프로세스들이 critical section에 들어가는 횟수에 한계가 있어야 함. (프로세스가 3개일 때, 2개만 왔다갔다하고, 1개가 왕따 당할 때)

가정) 모든 프로세스의 수행 속도는 > 0, 프로세스들 간의 상대적 수행 속도는 가정X.

<br />

**-Algorithm 1**

- synchronization variable (프로세스 P0 입장에서)

  ```c
  // int turn;
  // initially turn = 0;
  ```

  프로세스 P(i)는 **turn이 i(자기 차례)**일 때, 자신의 critical section에 들어갈 수 있다.

- Process P0 

  ```c
  do {
  	while(turn != 0);	// 내 turn이 아니면 while문 돌며 대기
  	critical section	// turn이 0일 때 수행
  	turn = 1;			// 다 끝나면 turn을 바꿔줌
  	remainder section
  } while(1);
  ```

- Process P1

  ```c
  do {
      while(turn != 1)
      critical section
      turn = 0
      remainder section
  } while(1);
  ```

=> mutual exclusion은 만족, 하지만 progress는 만족하지 못한다.

즉, **과잉양보 현상**이 발생한다.

<br />

*과잉양보

: 반드시 한 번씩 교대로 들어가야만 함 (swap-turn). 그가 turn 값을 내 값으로 바꿔 줘야만 내가 들어갈 수 있음. 특정 프로세스가 더 빈번히 critical section에 들어가야 한다면?

<br />

**-Algorithm 2**

- synchronization variables

  - **boolean flag[2]**; (flag : CS에 들어갈 의견 표시)

    초기에 **flag[모두] = false**;   (아무도 CS에 없다)

  - Pi 가 CS에 들어가고 싶을 때 (**flag[i] == true**)

  <br />

- Process Pi

```c
do {
    flag[i] == true;	// 나 들어가려고 해
    while (flag[j]);	// 다른 사람 있으면 기다릴게
    critical section	// 다른 사람 없을 때 수행..
    flag[i] = false;	// 나 이제 나왔어. 깃발 내릴게
    remainder section
} while(1);
```

=> mutual exclusion은 만족하지만 progress 요구를 충족하지 못한다. 한 명이 깃발을 들고 CPU를 뺏긴 뒤, 다른 한 명이 깃발 들 경우, 둘 다 2행까지 수행 후, 끊임없이 양보 ㅋㅋ

<br />

**-Algorithm 3**

- 알고리즘 1과 2를 합침
- Process P(i)

```c
do {
    flag[i] = true;		// 나 들어가고 싶어..
    turn = j;			// 상대방의 차례로 세팅
    while (flag[j] && turn == j); // 상대방이 깃발도 들면 난 기다릴게..
    critical section
    flag[i] = false;	// 나 나왔어! 깃발 내릴게
    remainder section
} while(1);
```

=> 3가지 조건을 모두 충족한다. 하지만 **Busy Waiting(=spin lock)** 발생. (상대가 turn을 바꿔주지 않는 이상, 계속 CPU와 메모리를 쓰면서 wait. 비효율적)

<br />

**-Synchronization Hardware**

원래는 데이터를 읽고 쓰는 것을 하나의 instruction으로 할 수 없어서 생긴 문제인데, 이게 하나의 instruction으로 해결되면 간단히 lock걸고 해제할 수 있다.

즉, 하드웨어적으로 하나의 (Test & modify를 atomic하게 수행할 수 있도록 지원하는) instruction만 주어지면 critical section문제는 쉽게 해결된다!

**Test_and_set(a)** 이라는 고유 instruction이 제공된다.

![test-and-set](https://user-images.githubusercontent.com/58247800/101871075-3f824f00-3bc6-11eb-8ea5-89a4821b9ef3.PNG)

a라는 데이터를 읽어와서 값을 1로 바꿔준다. (즉, 읽고 쓰기를 동시에!)

<br />

- Mutual Exclusion with Test & Set

  - Sychronization variable: boolean lock = false;

<br />

```c
// Process P(i)

do {
    while (Test_and_Set(lock)); // lock 걸려있는지 체크하고, 아무도 없으면 내가 들어가기 전 lock을 건다 (true로)
    critical section
    lock = false;
    remainder section	
}		
```

<br />

**-Semaphores**

: lock/unlock 기능, **공유 자원을 획득하게 해줌**.

- 앞의 방식들을 **추상화**시킴

- **Semaphore S** (변수- **자원의 개수**)

  - integer variable (정수값)
  - 아래의 두 가지 atomic 연산에 의해서만 접근 가능
    - **P(S) , V(S)**

  ```c
  // P(S) (공유 데이터 semaphore S를 획득하는 과정)
  while (S<=0) do no-op; // 자원이 없다면 wait
  S--;		// 음수일 때는 busy-wait 문제 발생
  
  // V(S) (다 쓰고 반납하는 과정)
  S++;
  ```

<br />

**-Critical Section of n Process**

(semaphore가 지원 된다면, 프로그래머는 P&V 연산만 넣으면 된다.)

- synchronization variable

  ​	semaphore mutex; (초기값 1 : 1개가 CS에 들어갈 수 있다)

- Process P(i)

  ```c
  do {
      P(mutex);
      critical section
      V(mutex);
      remainder section
  } while(1);
  ```

=> busy-wait는 여전히 존재, 효율적이지 않다.

Block & Wack up 방식의 구현 (= sleep lock)으로 해결 가능. 

자원이 없을 때, block 됐다가, 자원 생기면 깨어남.

<br />

**-Block / Wackup Implementation**

- semaphore를 다음과 같이 정의

  ```c
  typedef struct
  {
      int value;		// semaphore
      struct process *L;  // 자원을 얻기 위해 기다리는 큐
  } semaphore;
  ```

- block과 wakeup을 다음과 같이 가정

  - block : 커널은 block을 호출한 프로세스를 suspend시킴. 이 프로세스의 PCB를 semaphore에 대한 wait 큐에 넣음.
  - wakeup(P) : block된 프로세스 P를 wakeup 시킴. 이 프로세스의 PCB를 ready큐로 옮김.

![semaphore_block wakeup](https://user-images.githubusercontent.com/58247800/101870781-a94e2900-3bc5-11eb-9ff3-a4d2e959120b.PNG)

  semaphore를 기다리면서, 잠들어 있는 PCB를 연결.

<br />

**- Implementation : block/wakeup version of P() & V()**

: semaphore 연산에 block/wakeup 작업이 들어가야 함.

- P(S)

  ```c
  S.value--;			// 들어갈 준비
  if (S.value < 0)	// 음수면 못 들어가고 block상태
  {
      add this process to S.L;
      block();
  }
  ```

  <br />

- V(S)

  ```c
  S.value++;			// 자원을 내놓았는데도
  if (S.value <= 0)	// 자원이 0 이하라는 것은 잠들어있는 놈들이 존재
  {
      remove a process P from S.L;
      wakeup(P);
  }
  ```

  => 여기서 음수라는 것은 누군가 자원을 쓰기 위해 기다리고 있다는 의미.

  <br />

**-which is better?**

: semaphore를 구현하는 방식에 있어서

- Busy-wait v.s. Block/wakeup (보통은 Block/wakeup이 효율적!)
- Block/wakeup overhead v.s. Critical section 길이
  - 상태를 바꿔줄 때도 오버헤드가 생김
    - critical section 길이가 길면, Block/wakeup이 적당
    - critical section 길이가 매우 짧으면, 이 때의 오버헤드가  busy-wait 오버헤드보다 더 커질 수 있음.

<br />

**-Two types of Semaphores**

- Counting semaphore

  - 도메인이 0 이상인 임의의 정수값
  - 주로 resource counting에 사용

- Binary semaphore (=mutex)

  - 0 또는 1 값만 가질 수 있는 semaphore
  - 주로 mutual exclusion (lock/unlock)에 사용

<br />

**-Deadlock and Starvation**

: semaphore를 쓸 때, 문제점이 있다.

- **Deadlock**

  : 둘 이상의 프로세스가 **서로 상대방에 의해 충족될 수 있는 event**를 무한히 기다리는 현상

- ex of deadlock) S와 Q가 1로 초기화된 semaphore라 하자.

![deadlock](https://user-images.githubusercontent.com/58247800/101870790-ad7a4680-3bc5-11eb-894b-916300062d26.PNG)

  => P0과 P1는 S와 Q를 동시에 가질 수 없다.

  자원 갖는 순서를 (S->Q)로 지정하면 해결 가능.

- **Starvation (indefinite blocking)**

  : 프로세스가 suspend된 이유에 해당하는 semaphore 큐에서 빠져나갈 수 없는 현상.

<br />

### Classical Problems of Synchronization

: process 동기화에 관한 고전적인 세 가지 문제에 대해 알아보자.

**-1) Bounded-Buffer Problem**

: 공유 버퍼의 크기가 유한한 환경에서 생기는 문제

- **생산자-소비자 문제**
  - 두 개의 생산자 혹은 소비자가 **동시에 데이터 접근 시**
  - 소비자/생산자 없이 생산자/소비자만 드글드글(**자원 부족**)

아래와 같이 공유버퍼에 두 종류의 프로세스가 있다.

![bounded-buffer-problem](https://user-images.githubusercontent.com/58247800/101870799-b0753700-3bc5-11eb-8e64-9cb36ee34dad.PNG)

- **Producer** (buffer에 데이터 넣기)
  - Empty buffer(자원)가 있나? (없으면 기다림)
  - **공유 데이터에 lock을 건다**
  - Empty buffer에 데이터 입력 및 buffer 조작
  - Lock을 푼다
  - Full buffer 하나 증가 (pointer)
- **Consumer** (buffer에서 데이터 꺼내기)
  - Full buffer(자원)가 있나? (없으면 기다림)
  - **공유 데이터에 lock을 건다**
  - Full buffer에서 데이터를 꺼내고 buffer 조작
  - Lock을 푼다
  - Empty buffer 하나 증가 (pointer)

<br />

- Shared data : buffer 자체 및 buffer 조작변수 (empty/full buffer의 시작위치)

- Synchronization variables (**이런 semaphore변수들이 필요**)

  - mutual exclusion -> binary semaphore 필요 (공유된 데이터의 상호배제를 위한 lock용)
  - resource count -> integer semaphore 필요 (남은 자원의 수 표시하기 위해)

  => semaphore full = 0(full buffer의 개수), empty = n(empty buffer의 개수), mutex = 1(lock을 걸기 위한 변수);

```c
// - Producer
do {
    produce an item in x
        ...
    P(empty);             // 빈 퍼버가 있는지 확인
    P(mutex);			  // 있다면, lock을 건다
    	...
    add x to buffer
        ...
    V(mutex);			  // lock을 푼다
    V(full); 			  // full buffer의 개수 1 증가
}

// - Consumer
do {
    P(full);			  // full 버퍼가 있는지 확인
    P(mutex);			  // 있다면, lock을 건다
    	...
    remove an item from buffer to y
        ...
    V(mutex);			  // lock을 푼다
    V(empty);			  // empty buffer의 개수 1 증가
    	...
    consume the item in y
}
```

둘이 상반되는 과정.

<br />

**-2) Readers-Writers Problem**

: reader와 writer 두 개의 프로세스가 DB를 공유하는 환경.

- 문제
  - 한 프로세스가 **DB(공유자원)**에 write 중일 때, 다른 프로세스가 접근하면 안 됨.
  - **read는 동시에 여럿이 해도 됨**. (=> 모든 상황에 lock걸면 비효율)

- Solution

  - Writer가 DB에 아직 접근 허가를 못받은 상태에서는 모든 대기 중인 Reader들을 다 DB에 접근하게 해줌
  - **Reader들을 다 DB에 접근하게 해줌**
  - Writer는 대기 중인 Reader가 하나도 없을 때, DB 접근이 허용됨
  - 일단 **writer가 DB에 접근 중이면 Reader들은 접근이 금지됨**
  - Writer가 DB에서 빠져 나가야만 Reader의 접근이 허용됨

- Shared data : DB 자체

  ​						int **readCount** = 0;   (현재 DB에 접근 중인 Reader의 수)

- Synchronization variables

  - **mutex = 1**

    공유변수 read count를 접근하는 코드(critical section)의 상호배제 보장을 위해 사용 (reader간 reader count의 lock용도)

  - **db = 1**

    Reader와 Writer가 공유 DB 자체를 올바르게 접근하게 하는 역할 (DB에 대한 lock용도)

```c
// - Writer
P(db);					// writer가 들어가면 lock을 건다
...
writing DB is performed
...
V(db);					// lock을 풀어줌

// - Reader
P(mutex);				// readcount를 증가시키기 위한 lock 걸기
readcount++;			// readcount 1 증가
if (readcount == 1) P(db); // 내가 처음 들어온 reader라면 DB lock 걸기
V(mutex);				// readcount에 대한 lock 풀기
...
reading DB is performed
...
P(mutex);				// readcount를 감소시키기 위한 lock 걸기
readecount--;
if (readcount == 0) V(db); // 내가 마지막 reader라면 DB lock 풀기
V(mutex);				// readcount에 대한 lock 풀기
```

<br />

- **starvation** 발생 가능

  reader 뭉탱이들이 겁~나 많은 상황에서, 마지막 reader가 빠져 나가기 전에 reader 또 오고... writer는 언제 DB에 접근하냥..ㅜ

  => 개선) 어느 정도의 reader가 빠져 나가면 writer에게 차례 줌 (신호등 생기면 언젠가는 건널 수 있다!)

<br />

**-3) Dining-philosophers Problem** (식사하는 철학자 문제)

: 5명의 철학자는 생각하거나 / 밥을 먹는 두 가지 행위를 할 수 있다. 인접한 철학자끼리는 젓가락을 공유하고,  왼쪽과 오른쪽 젓가락 두 개를 획득해야 밥을 먹을 수 있다.

- Synchronization variables

  : semaphore chopsticks[5];  (초기값은 모두 1: 혼자서만 젓가락을 잡을 수 있음)

![철학자](https://user-images.githubusercontent.com/58247800/101871065-3a250480-3bc6-11eb-9068-59c7b0ccf115.PNG)

- Philosopher i

```c
do {
    P(chopstick[i]);			// 왼쪽 젓가락을 잡는 행위
    P(chopstick[(i+1) % 5]);	// 오른쪽 젓가락을 잡는 행위
    ...
    eat();						// 밥 먹는 중..
    ...
    V(chopstick[i])				// 왼쪽 젓가락 놓기
    V(chopstick[(i+1) % 5])		// 오른쪽 젓가락 놓기
    ...
    think();
}
```

- 문제점

  : **deadlock 가능성** (모든 철학자가 동시에 배가 고파져 왼쪽 젓가락을 집은 경우)

- 해결방안

  -  4명의 철학자만이 테이블에 동시에 앉도록 함.
  - 젓가락을 두 개 모두 집을 수 있을 때에만 젓가락을 집을 수 있게 한다.
  - 비대칭(짝수/홀수) 철학자는 왼쪽/오른쪽 젓가락부터 집도록(같은 젓가락!)

- 변수

  : enum { thinking, hungry, eating } state[5]; (상태표현)

  semaphore self[5] = 0; (젓가락 두 개 확보 가능해 밥먹을 권리 부여)

  semaphore mutex = 1; (상태를 동시에 바꾸지 못하도록 lock걸기)

```c
// Philosopher i
do {
    pickup(i);
    eat();
    putdown(i);
    think();
}

void pickup(int i) {
	P(mutex);			// 상태 바꾸기 전 lock 걸기
    state[i] = hungry;	// hungry로 상태 변경
    test(i);			// 젓가락 둘 다 집을 수 있는지 테스트
    V(mutex); 			// lock 풀고
    P(self[i]);			// 밥 먹을 수 있는 권리 해제(1->0)
}

void test(int i) {
    if (state[(i+4)%5] != eating && state[i] == hungry && state[(i+1)%5] != eating) {// 양쪽 철학자가 먹고있지 않고 내가 배고플 때
        state[i] = eating; // eating으로 상태 변경
        V(self[i]);		   // 밥 먹을 수 있는 권리 부여(0->1)
    }
}

void putdown(int i) {
    P(mutex);
    state[i] = thinking;
    test((i+4)%5);		// 혹시 나 땜에 못먹었는지 양쪽 철학자 테스트
    test((i+1)%5);
    V(mutex);
}
```

- **semaphore의 문제점**

: 코딩하기 힘들다, 정확성의 입증이 어렵다, 자발적 협력이 필요, 한 번의 실수가 모든 시스템에 치명적.

ex) V,P연산을 실수로 바꿔 쓰면 상호배제 깨짐. 실수로 같은 연산 쓰면 Deadlock.

<br />

**-Monitor**

: 동시 수행 중인 프로세스 사이에서 abstract data type의 안전 공유를 보장하기 위한 high-level synchronization construct (semaphore에 비해 프로그래머의 부담을 줄여주고, **moitor가 알아서 해줌**)

```c
monitor monitor-name
{	shared variable declarations
    procedure body P1(...){
    	...
	}
 	procedure body P2(...){
        ...
    }
 	{
     	initialization code
 	}
}
```

**monitor라고 정의된 내부의 프로시저를 통해서만 공유 데이터에 접근 가능**.

<br />

![monitor](https://user-images.githubusercontent.com/58247800/101870806-b539eb00-3bc5-11eb-8610-02d4d23033f1.PNG)

- monitor내부에 A, B프로세스(각각 공유 데이터를 접근하는 코드)를 가지고 있다.

- **모니터 내에서는 한 번에 하나의 프로세스만이 활동 가능** (operations)

  => 프로그래머가 동기화 제약 조건을 명시적으로 코딩할 필요가 없음(**lock을 걸 필요X**)

  만약, 실행 도중에 CPU를 빼앗겨도, monitor내부에 active한 상태로 남아있게 된다. 따라서, 다른 프로세스가 monitor내의 코드를 실행하지 못하고 밖의 큐에 줄 서서 있게 됨. monitor 내부에 active한 자원 수가 0이 될 때, 밖에서 기다리던 프로세스가 들어옴.

- 프로세스가 모니터 안에서 기다릴 수 있게 **condition variable**(자원 여분 여부/ **어떤 조건을 충족시키지 못해 잠들거나 깨울 때**)사용. 

  (condition x, y;) 자원이 있으면 바로 접근, 없으면 기다리게 함. (**condition variable은 값을 가지는 변수가 아님!**)

- condition variable은 **wait**와 **signal**연산에 의해서만 접근 가능.

  - **x. wait();** - 자원 x를 원하는 줄에 기다리는..

    => x. wait()을 invoke한 프로세스는 다른 프로세스가 x.signal()을 invoke하기 전까지 suspend된다.

  - **x. signal();** - 자원 x를 기다리는 프로세스가 있으면 빠져나올 수 있도록.

    => x.signal()은 정확하게 하나의 suspend된 프로세스를 resume 한다. suspend된 프로세스가 없으면 아무 일도 일어나지 않음.

<br />

- 1) monitor bounded-bufffer

```c
monitor내부에 monitor bounded_buffer {
    int buffer[N];			
    // 공유 버퍼가 모니터 안에 정의(굳이 lock을 걸지 않아도 produce나 consume 중 하나만 실행됨)
    condition full, empty;
    // 값을 가지지 않고, 자신의 큐에 프로세스를 매달아 sleep시키거나, 큐에서 프로세스를 깨우는 역할만 함
    
    void produce(int x) {
        empty.wait();	// 빈 버퍼가 없으면 줄서서 기다림
        add x to an empty buffer
        full.signal();  // 다 채운 후, 기다리는 프로세스를 깨워줌
    }
    
    void consume(int *x) {
        full.wait();	// 찬 버퍼가 없으면 줄서서 기다림
        remove an item from buffer and store it to *x
        empty.signal();	// 비운 후, 기다리는 프로세스를 깨워줌
    }
}
```

<br />

- 2) Dining Philosophers (monitor ver.)

```c
Each Philosopher: {
    pickup(i);		// enter monitor
    eat();
    putdown(i);		// enter monitor
    think();
}

monitor dining_philosopher {
    enum {thinking, hungry, eating} state[5];
    condition self[5];
    void pickup(int i) {
        state[i] = hungry;
        test(i);
        if (state[i] != eating)
            self[i].wait();		 // wait here
    }
    
    void putdown(int i) {
        state[i] = thinking;
        test((i+4)%5);		
        test((i+1)%5);
    }
    
    void test(int i) {
        if ((state[(i+4)%5] != eating) && (state[i] == hungry) && (state[(i+1)%5] != eating)) {
            state[i] = eating;
            self[i].signal();	// wake up P(i)
        }
    }
    void init() {
        for(int i = 0; i < 5; i++)
            state[i] = thinking;
    }
}
```



## Ch7. Deadlock

**-Deadlock (교착상태)**

: 일련의 프로세스들이 **서로가 가진 자원을 기다리며 block된 상태**

각자 자원을 가지고 있으면서, 상대방의 자원을 더 요청하는.. 더 이상 진행이 되지 않는 상황. (어느 누구도 양보하지 않으면 진행이 안됨.)



**-Resource** (자원)

- 하드웨어, 소프트웨어 등을 포함하는 개념 (ex. I/O device, CPU cycle, memory space, semaphore 등)
- 프로세스가 자원을 사용하는 절차 (4단계)
  - Request(요청), Allocate(획득), Use(사용), Realease(반납)

**-Deadlock Example**

1) 하드웨어 - I/O device의 경우, 시스템에 2개의 tape drive가 있다.

프로세스 p(1)과 p(2) 각각이 하나의 tape drive를 보유한 채, 다른 하나를 기다리고 있다.

2) 소프트웨어 - binary semaphore A and B

p(0)이 A를 획득하고 CPU 뺏김, p(1)이 B를 가진 상황에서 A를 가지려하는데, A는 p(0)이 갖고 있음.. CPU가 어느 쪽에 가더라도 진행이 안 됨.



**-Deadlock 발생의 4가지 조건**

: deadlock은 왜 발생하는가?

- **Mutual exclusion (상호배제)** : 매 순간 하나의 프로세스만이 자원을 사용할 수 있음.
- **No preemption (비선점)** : 프로세스는 자원을 스스로 내어놓을 뿐, 강제로 빼앗기지 않음.
- **Hold and wait (보유대기)** : 자원을 가진 프로세스가 다른 자원을 기다릴 때, 보유 자원을 놓지 않고 계속 가지고 있음.
- **circular wait (순환대기)** : 자원을 기다리는 프로세스간에 사이클이 형성되어야 함. p(0)은 p(1)이 가진 자원을 기다림. p(1)은 p(2)가 가진 자원을 기다림. p(n)은 p(0)이 가진 자원을 기다림.



**- Resource-Allocation Graph (자원할당 그래프)**

: deadlock이 발생했는지 알아보기 위해 사용.

![자원할당 그래프](https://user-images.githubusercontent.com/58247800/103292570-70b9a680-4a31-11eb-88b1-4e8ff0a49150.PNG)

- vertex

: 동그라미는 프로세스, 네모는 자원. 네모 안의 점은 자원의 수.

- edge

: 자원 -> 프로세스 (이 프로세스가 해당 자원을 가지고 있다.)

프로세스 -> 자원 (이 프로세스가 해당 자원을 요청. 아직 획득하진 못함)

![자원할당 그래프](https://user-images.githubusercontent.com/58247800/103292570-70b9a680-4a31-11eb-88b1-4e8ff0a49150.PNG)
![자원할당 그래프2](https://user-images.githubusercontent.com/58247800/103292586-7b743b80-4a31-11eb-9c03-d495d66cb2a6.PNG)

- 그래프에 cycle이 없으면 deadlock이 아니다
- 그래프에 cycle이 있으면
  - 자원당 instance(개수)가 하나 밖에 없으면, deadlock
  - 자원당 instance가 여러개면, deadlock일 수도 아닐 수도

두 그림 모두 cycle이 존재, 

왼쪽은 R(2) 자원을 p(1),p(2)가 갖고 있으면서, p(3)가 요청하는 상황이기에 deadlock.

오른쪽은 p(4)가 R(2)를 반납하거나, p(2)가 R(1)을 반납할 수 있기에 deadlock 아님.



**-Deadlock의 처리 방법**

- 미연에 방지하는 방법

  - 1) Deadlock Prevention : 자원 할당 시, Deadlock의 4가지 필요 조건 중 어느 하나가 만족되지 않도록 하는 것. 

  - 2) Deadlock Avoidance : 자원 요청에 대한 부가적인 정보를 이용해서, deadlock의 가능성이 없는 경우에만 자원을 할당.

    시스템 state가 원래 state로 돌아올 수 있는 경우에만 자원 할당.

- deadlock이 생기게 놔둠

  - 3) Deadlock Detection and recovery : deadlock 발생은 허용하되, 그에 대한 detection 루틴을 두어 deadlock 발견 시 recover

  - 4) **Deadlock Ignorance** (현대 OS 에서 채택: deadlock이 자주 발생하지 않기 때문에, 미연에 방지하는데 드는 overhead가 더 크다.)

    : deadlock을 시스템이 책임지지 않음. UNIX를 포함한 대부분의 OS가 채택.



**- 1) Deadlock Prevention**

- Mutual Exclusion : 막을 수 없음. 공유해서는 안되는 자원의 경우, 반드시 성립해야 함.
- Hold and Wait : 프로세스가 자원을 요청할 때는 다른 어떤 자원도 가지고 있지 않아야 한다.
  - 방법 1) 프로세스 시작 시, 모든 필요한 자원을 할당받게 하는 방법. (중간에 추가로 필요한 자원이 없을 것. 비효율적..)
  - 방법 2) 자원이 필요할 경우, 보유 자원을 모두 놓고 다시 요청. (자진 반납)
- No Preemption
  - 프로세스가 어떤 자원을 기다려야 하는 경우, 이미 보유한 자원이 선점됨
  - 모든 필요한 자원을 얻을 수 있을 때, 그 프로세스는 다시 시작됨
  - state를 쉽게 save하고, restore할 수 있는 자원에서 주로 사용(CPU, 메모리)
- Circular Wait
  - 자원들이 꼬리에 꼬리를 물 때 사용 (cycle이 생기지 않도록)
  - 모든 자원 유형에 할당 순서를 정하여, 정해진 순서대로만 자원 할당
  - 예를 들어, 순서가 3인 자원R(i)를 보유 중인 프로세스가 순서가 1인 자원 R(j)를 할당받기 위해서는, 우선 R(i)를 release해야 함!

=> 문제점 : utilization(자원 이용률) 저하, throughput(전체 시스템 성능) 감소, starvation 문제



**- 2) Deadlock Avoidance**

: 자원 요청에 대한 부가정보를 이용해서, 자원 할당이 deadlock으로부터 안전한지를 동적으로 조사, 안전한 경우에만 할당. (deadlock이 발생할 수 있는 요청은 거부.)

가장 단순하고 일반적인 모델은 프로세스들이 필요로 하는 각 자원별 최대 사용량을 미리 선언하도록 하는 방법.

- **safe state** : 시스템 내의 프로세스들에 대한 **safe sequence**가 존재하는 상태
- **safe sequence **
  - 프로세스의 sequence <P(1),P(2), ... , P(n)>이 safe하려면 P(i) (1 <= i <= n)의 자원요청이 **"가용자원 + 모든 P(j) (j < i)의 보유자원"**에 의해 충족되어야 함.
  - 조건을 만족하면 다음 방법으로 모든 프로세스의 수행을 보장
    - P(i)의 자원요청이 즉시 충족될 수 없으면, 모든 P(j) (j < i)가 종료될 때까지 기다린다
    - P(i-1)이 종료되면 P(i)의 자원요청을 만족시켜 수행한다



- 시스템이 safe state에 있으면 => no deadlock
- 시스템이 unsafe state에 있으면 => possibility of deadlock

![safeunsafe](https://user-images.githubusercontent.com/58247800/103292599-83cc7680-4a31-11eb-93d8-ed22c5471270.PNG)

- deadlock avoidance 
  - 시스템이 unsafe state에 들어가지 않는 것을 보장
  - 2가지 경우의 avoidance 알고리즘
    - 1) 자원당 instance가 한 개일 때 => resource allocation graph 알고리즘 사용
    - 2) 자원당 instacne가 여러 개일 때 => banker's 알고리즘 사용



- **1) 자원당 instance가 한 개일 때** => **resource allocation graph 알고리즘** 사용

![instance한개일때](https://user-images.githubusercontent.com/58247800/103292611-8929c100-4a31-11eb-97de-37d2b53a78e5.PNG)

  - claim edge (p(i) -> R(j))
    - 프로세스 p(i)가 자원 R(j)를 미래에 요청할 수 있음 (점선)
    - 프로세스가 해당 자원 요청 시, request edge(실선)로 바뀜
    - R(j)가 release되면, assignment edge는 다시 claim edge로 바뀜
  - requese edge의 assignment edge 변경 시 (점선 포함) cycle이 생기지 않는 경우에만 요청 자원을 할당.
  - cycle 생성 여부 조사시, 프로세스의 수가 n일 때, O(n^2) 시간이 걸림.

  

- **2) 자원당 instace가 여러 개일 때** => **Banker's 알고리즘** 사용

  **example of Banker's Algorithm**

  : **Need(각 프로세스의 자원 요청)를 받아들일지 아닐지를 결정!!** 항상 최악의 상황을 가정하며, 굉장히 보수적임. **프로세스들이 본인의 최대 요청을 할 것이라 가정하고, 가용 자원(Available)에서 줄 수 있는지를 본다.** 가용자원으로 충족되면 처리되고, 추가 요청이 가용자원으로 충족되지 않을 시에는 처리되지 않음.

![Bankers알고리즘](https://user-images.githubusercontent.com/58247800/103292629-92b32900-4a31-11eb-81cf-5fe9bfb236e5.PNG)

  - 각 프로세스는 최대로 사용하는 자원의 수를 미리 알 수 있음(Max), 하지만 어느 시점에 필요할지는 알 수 없다.
  - 평생에 요청할 수 있는 최대 자원의 수는 Need (Max - Allocation)
  - sequence <P(1)-P(3)-P(4)-P(2)-P(0)>가 존재하므로 시스템은 safe state.
  - deadlock이 생기지 않지만, 자원이 있는데도 주지 않으므로 비효율적.

  

![p1 request](https://user-images.githubusercontent.com/58247800/103292773-d443d400-4a31-11eb-99a1-43a297fbe1e5.PNG)



**- 3) Deadlock Detection and Recovery**

- deadlock detection
  - resource type당 single instance인 경우
    - 자원할당 그래프에서의 cycle이 곧 deadlock을 의미
  - resource type당 multiple instance인 경우
    - banker's 알고리즘과 유사한 방법 활용



- wait-for graph 알고리즘

![waitforgraph](https://user-images.githubusercontent.com/58247800/103292827-f6d5ed00-4a31-11eb-9b6f-a12aeedad058.PNG)

  - resource type당 single instance인 경우
  - wait-for graph
    - 자원할당 그래프의 변형
    - 프로세스만으로 node 구성
    - P(j)가 가지고 있는 자원을 P(k)가 기다리는 경우 P(k) -> P(j)
  - 알고리즘
    - wait-for graph에 사이클이 존재하는지를 주기적으로 조사
    - cycle을 찾는데 걸리는 시간 : O(n^2) 

- resource type당 multiple instance인 경우

  : 보수적이지 않고, 낙관적으로 생각함 (자원을 반납할거라 생각)

![낙관적일때](https://user-images.githubusercontent.com/58247800/103292841-fe959180-4a31-11eb-8468-c9a3a4fb1c5f.PNG)

=> No deadlock : sequence <P(0)-P(2)-P(3)-P(1)-P(4)> will work!

먼저 가용자원(Available)으로 커버할 수 있는지 본다.

다음으로 요청자원이 없는 프로세스를 보고, 내어놓을 수 있는 자원을 살펴본다.

그 자원을 가용자원으로 합쳐놓고, 요청자원을 만족하는 프로세스를 진행시킨다.

문제 없이 끝까지 갈 수 있다면, No deadlock!!



만약, deadlock이 발견되면 recovery를 해야한다.

- **Recovery**
  - **Process termination** : deadlock에 연루된 프로세스들을 사살
    - 1) 연루된 모든 프로세스들을 사살
    - 2) 하나씩 죽이면서 deadlock이 해결되는지 살펴봄 (deadlock이 없어질 때까지 반복)
  - Resource Preemption : deadlock에 연루된 프로세스들로부터 자원을 뺏음
    - 비용을 최소화할 victim 선정 (자원을 빼앗을 희생양 선정)
    - safe state로 rollback하여 프로세스를 재시작
    - starvation 문제 (p1한테서 a자원을 뺏었는데 다른 p가 a자원을 요청하기도 전에 p1이 a자원을 또 요청..)
      - 동일한 프로세스가 계속해서 victim으로 선정되는 경우
      - cost factor에 rollback 횟수도 같이 고려 (꼭 비용만 최소화하는게 아니라~)

**- 4) Deadlock Ignorance**

: deadlock이 일어나지 않는다고 생각하고, 아무런 조치도 취하지 않음

- deadlock이 매우 드물게 발생하므로, deadlock에 대한 조치 자체가 더 큰 오버헤드일 수 있다.
- 만약 시스템에 deadlock이 발생한 경우, 시스템이 비정상적으로 작동하는 것을 사람이 느낀 후, 직접 프로세스를 kill하는 등의 방법으로 대처
- UNIX, Windows 등 대부분의 범용 OS가 채택
