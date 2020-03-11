import turtle as t

def turn_right():								#오른쪽으로 이동하는 함수
	t.setheading(0)								#t.seth(0) 으로 입력해도 됩니다. 
	t.forward(10)								#t.fd(10) 으로 입력해도 됩니다. 

def turn_up():									#위로 이동하는 함수
	t.setheading(90)
	t.forward(10)								

def turn_left():								#왼쪽으로 이동하는 함수
	t.setheading(180)
	t.forward(10)
	
def turn_down():								#아래로 이동하는 함수
	t.setheading(270)
	t.forward(10)
	
def blank():									#화면을 지우는 함수
	t.clear()

t.title ("TURTLE")								#거북이 그래픽 창의 이름을 지정합니다. 
t.shape ("turtle")								#거북이 모양을 사용합니다. 
t.speed(0)										#거북이 속도를 가장 빠르게 지정합니다. 
t.onkeypress(turn_right,"Right")			    #오른쪽 화살표키를 누르면 turn_right 함수를 실행합니다. 
t.onkeypress(turn_up,"Up")					    #위 화살표키를 누르면 turn_up 함수를 실행합니다.
t.onkeypress(turn_left,"Left")					#왼쪽 화살표키를 누르면 turn_left 함수를 실행합니다.
t.onkeypress(turn_down,"Down")					#아래 화살표키를 누르면 turn_down 함수를 실행합니다. 
t.onkeypress(blank,"Escape")					#ESC 키를 누르면 blank 함수를 실행합니다. 
t.listen()										#거북이 그래픽 창이 키보드 입력을 받습니다.
t.mainloop()									#t.mainloop 함수는 사용자가 거북이 그래픽 창을 종료
                                                #할 때 까지 프로그램을 실행하면서 마우스나 키보드 입력을
                                                #처리하도록 하는 함수입니다. 

 
#궁금증
#1. 화살표 키로 움직이면 연속 입력이 되는데, 알파벳으로 하면 연속 입력이 안 되는 이유가 뭘까?
