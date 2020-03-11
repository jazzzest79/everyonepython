import random

a = random.randint (1, 30)			#a 에 1 ~ 30 사이의 임의의 수를 저장합니다. 
b = random.randint (1, 30)			#b 에 1 ~ 30 사이의 임의의 수를 저장합니다. 

print (a, "+", b, "=") 				#문제를 출력합니다. 
x = input ()						#답을 입력 받아 x 에 저장합니다 (문자열로 자동 저장됩니다.)
c = int (x)							#비교를 위해 문자열을 정수로 바꿉니다. 

if a+b == c:
	print ("천재!")
	
else:
	print ("바보!")

