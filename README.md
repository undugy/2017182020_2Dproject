# 1.게임소개
## 제목:1945
![R_Logo](https://user-images.githubusercontent.com/70964651/94256702-270a7d00-ff65-11ea-8474-fc18afc0a56b.png)
![그림1](https://user-images.githubusercontent.com/70964651/94256767-3e496a80-ff65-11ea-9c08-3664b59c1b7c.png)

- 적의 공격을 회피하여 모든 적들을 격파!
- 스테이지의 보스를 처치하여 스테이지 클리어

--------------
# 2.GameState
## 1.start_state
## 2.title_state
## 3.pause_state
## 4.main_state
---------------

# 3.GameState 항목
## 1.start_state
* 설명 : 시작 시 처음 나오는 화면
*  객체 : 게임 로고
* 이벤트 : 일정 시간이 흐르면 자동으로 title_state로전환된다.

## 2.title_state
* 설명: 캐릭터 선택창
* 객체 : 캐릭터 이미지들, 선택창 이미지
* 이벤트: space bar를 누르면 main_state로 전환된다.

## 3.pause_state
* 설명: 게임을 멈췄을때 나오는 화면
* 객체 : 메뉴화면 이미지,reasum,exit이미지
* 이벤트 : esc를 누르면 title_state로 가고 r을 누를 시 이어서 계속한다.

## 4.main_state
* 설명 : 게임 진행화면
* 객체: 게임 맵,게임 캐릭터,투사체,몬스터,스코어
* 이벤트 : p를 누를 시 pause_state로 전환된다. 
-----------------
## 다이어 그램
![다이어그램](https://user-images.githubusercontent.com/70964651/94257201-e65f3380-ff65-11ea-9924-0067ff396e44.png)

----------------
# 4.필요한 기술
### 1.다른 과목에서 배운 기술
* 투사체에 대한 충돌체크 처리

### 2.이 과목에서 배운 기술
* 다양한 객체의 랜더링
* state전환 조건 설정
* 리 팩토링 기술
* 사운드 처리

### 3.다루지 않는 것 같아서 수업에 다루어 달라고 요청 할 기술
* 여러 객체의 리스트를 관리하는 법
* 맵의 전환 방법
* 마지막 프로젝트에 추가로 필요한 모듈



