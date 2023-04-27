import tkinter # tkinter 를 사용하겠다.
import tkinter.font # tkinter.font 를 사용하겠다.
import random

lotto_num = range(1,46) # 변수에 1에서 46 까지의 임의의 난수 발생하도록 설정 

def  buttonClick(): # 함수정의 : 버튼을 클릭할때 실행할 동작
    label = tkinter.Label(window, text=str(random.sample(lotto_num,6)))
    # 라벨 설정 : 윈도우 화면에 6개의 난수로 받은 숫자를 문자로 표현해라
    label.pack()

window=tkinter.Tk() #윈도우에 tkinter 창 설정
window.title("lotto") # lotto 제목 설정
window.geometry("400x200") # 크기설정
window.resizable(False, False) #사이즈조절 불가

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
#버튼 설정: 호버시 솔리드라인. 크기설정, 처음엔 1초 걸리고 그다음 클릭시 0.1초 
button.pack() 

window.mainloop() #동작을 반복하게 함.