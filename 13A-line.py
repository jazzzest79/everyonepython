import turtle as t

t.bgcolor("black")						# 배경색을 검은색을 지정합니다. 
t.speed(0)								# 거북이 속도를 가장 빠르게 (0) 지정합니다. 

for x in range(200):					# for 반복 블록을 200번 실행합니다. 
	if x % 3 == 0:						# 번갈아가면서 선의 색깔을 바꿉니다. 
		t.color("red")
	
	if x % 3 == 1:
		t.color("yellow")
		
	if x % 3 == 2:
		t.color("blue")

	t.forward(x*2)						# x*2 만큼 앞으로 이동합니다. (반복하면서 선이 점점 길어짐)
	t.left (119) 						# 거북이를 119도 왼쪽으로 회전합니다. 	