## 목적  
스터디원 진행현황 확인하기


## 아이디어

|    | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> [요세푸스 문제](https://www.acmicpc.net/problem/1158) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> [카드 구매하기](https://www.acmicpc.net/problem/11052) |  <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>  [사과나무](https://www.acmicpc.net/problem/20002)  |  <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>  [문제집](https://www.acmicpc.net/problem/1766) |  
|:---------:|:---------:|:---------:|:---------:|:---------:|  
|112224| 😠 | 😠  |😿| 😄 |

아직 안품 : 😠  
AC : 😄  
WA : 😿  
위와 같은 형식으로 한 눈에 스터디원의 진행 상황을 파악하고 싶다.  
(일일히 확인하기에는 너무 번거롭다.)

## 구현  
필요한 정보를 나열하면 문제정보(tier), (유저이름, 문제번호) -> 해당 문제에 대한 진행상황이 될 것이다.  
* 먼저 문제의 tier 정보가 필요하기 때문에 [solved.ac의 api](https://solvedac.github.io/unofficial-documentation/#/%EA%B8%B0%ED%83%80/get_search_suggestion)를 이용한다.  
* 유저 이름과 문제 번호는 참여자에 대한 파일과 n주차 문제에 대한 파일로 직접 저장해두고, 파일에서 읽어오는 것으로 해결한다.  
* 이후 ```https://www.acmicpc.net/status?problem_id=&user_id=``` 에 요청을 보내고 해당 페이지를 파싱 .md 문법에 맞게 파일 작성  

자동화 관련  
* github의 action을 이용하여 자동화할 예정
* cron 주기는 30분 ~ 3시간 정도로 하여 서버의 과부하를 막을 것.
* 새로운 주의 문제 파일이 올라오거나, 일주일이 지나면 진행현황의 수정이 아닌 새로운 주의 문제에 대해 작성한다.


## 진행상황
1. 현재 풀이 결과를 받아오는 것은 성공
2. 채점 현황에 tier 정보(img)를 받아와서 사용하려 하였지만 실패, 본래 계획대로 api 호출 이용 예정 
