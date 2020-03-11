def sum_func (n):
	s = 0							#합을 구하기 위한 변수 s (시작 값을 0으로 지정함)
	for x in range (1, n+1):		#range(1,n+1)로 1, 2, ..., n 까지 반복합니다. (n+1 은 제외)
		s = s + x					#지금까지 계산된 s 값에 x 를 더해서 다시 s 에 저장합니다. 
	return s						#계산된 s 값을 결과값으로 돌려줍니다. 

print (sum_func(10))
print (sum_func(100))

	