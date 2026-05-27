# 기본 제공 GUI => tkinter
import tkinter as tk


mywind = tk.Tk() # main 윈도우 객체 생성
mywind.geometry("600x600+500+200") # 윈도우 사이즈 조절 및 출력 위치 조절

# 제어 변수
numcnt = tk.IntVar() # 내부 프로그램 메모리 값과 GUI 표시 데이터의 연동 변수 역할
numcnt.set(0) # 제어변수에 값 설정.

# 함수 추가
def IncreaseFunction():
    numcnt.set(numcnt.get() + 1)
    print("increase")

def DecreaseFunction():
    numcnt.set(numcnt.get() - 1)
    print("decrease")

# label
lb1 = tk.Label(text="numbering", textvariable=numcnt)
lb1.pack()

# 버튼 자식 윈도우 생성
b1 = tk.Button(
    text="increase", 
    padx=20, 
    pady=20, 
    font=20, 
    background='blue',
    command=IncreaseFunction,
    repeatdelay=500,
    repeatinterval=50)
b1.pack()

b2 = tk.Button(
    text="decrease", 
    padx=20,
    pady=20, 
    font=20, 
    background='pink',
    command=DecreaseFunction,
    repeatdelay=500,
    repeatinterval=50)
b2.pack(padx=10,pady=10)


#자식 윈도우를 부모 윈도우에 배치(grid, pack, place)

mywind.mainloop() # window 객체를 화면에 갱신해서 출력