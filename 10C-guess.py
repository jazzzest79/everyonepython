import random

n = random.randint (1,30)					#1 ~ 30 사이에 있는 임의의 수를 뽑습니다. 

while True:									#영원히 반복합니다. 
	x = input ("맞혀 보세요!")					
	g = int (x)								#입력 받는 값을 비교할 수 있도록 정수로 바꿉니다. 
	if g == n:								#사용자가 추측한 값과 임의의 수가 같으면 정답입니다.
		print("정답!!")
		break								#정답을 맞히면 break 로 while 반복문을 빠져나갑니다. 
		
	if g < n:							
		print("너무 작아요!")
		
	if g > n:
		print("너무 커요!")