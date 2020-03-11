import turtle as t

n = 5                  #오각형을 그립니다. (다른 값을 입력하면 다른 도형을 그립니다.)

t.color("purple")
t.speed(1)

t.begin_fill()         #색칠할 영역을 시작합니다.
for x in range(n):   #n 번 반복 합니다.
    t.forward(50)      #거북이가 앞으로 50만큼 이동합니다.
    t.left(360/n)      #거북이가 360/n 만큼 왼쪽으로 회전합니다.
t.end_fill()           #색ㅎ칠할 영역을 마무리합니다.
