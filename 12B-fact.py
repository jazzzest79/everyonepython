def factorial (n):
	fact = 1						#곱을 구하기 위한 변수 fact (시작 값을 1로 지정)
	for x in range (1, n+1):		#range (1,n+1) 로 1, 2, ..., n 까지 반복합니다. (n+1 은 제외)
		fact = fact * x				#지금까지 계산된 값에 x 를 곱해 fact 에 다시 저장합니다. 
	return fact						#계산된 fact 값을 돌려 줍니다. 

print (factorial(5))
print (factorial(10))