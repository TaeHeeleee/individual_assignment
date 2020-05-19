from tkinter import*
from tkinter improt messagebox

##전역 변수 선언 부분##
window = None
canvas = None
XSIZE, YSIZE = 9999, 9999
inImage=[]filename = ''

## 함수 선언 부분 ##
global filename

filename = ""

global inImage, XSIZE, YSIZE
fp = open(filename, 'rb')

def func_open():
    print("사진 파일을 입력하세요")
    filename = askopenfilename(parent = window, filetypes=(("GIF파일","*.gif"), ("모든파일","*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_match():
    print("사진에 존재하는 음식이 맞는지 확인해주세요")
    print("존재하지 않은 음식은 선택해주세요")
    ~   ~   ~   ~   ~

def func_calorie():
    print("칼로리를 확인해드립니다")
    print("너무 충격 먹지 마세요^^")
    ~   ~   ~   ~   ~

def func_nutrient():
    print("영양소를를 확인해드립니다")
    print("골고루 드세요^^")
    ~   ~   ~   ~   ~

def fuc_want_calorie():
    print("원하는 칼로리 기준을 알려주세요")

def func_want_nutirent():
    print("원하는 영양소를 알려주세요")
    print("영양소에는 ~~~ 있습니다")
    nutrient1 = Radiobutton(window, text = "탄수화물", variable = var, value = 1)

def func_recommend():
    print("칼로리와 영양소 기준에 맞는 적절한 음식을 추천합니다")
    ~   ~   ~   ~

window = Tk()
maiMenu = Menu(window)
window.config(menu = mainMenu)
window.title("음식")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

## 실행 및 종료 코드 ##
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "실행 및 종료", menu = fileMenu)
fileMenu.add_command(label = "실행", command = )
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = quit)

## 사진 칼로리 알려주기 코드 ##
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "칼로리 읽어들이기", menu = fileMenu)
fileMenu.add_command(label = "사진 파일 불러오기", command = func_open)
fileMenu.add_command(label = "음식 매칭", command = func_match)
fileMenu.add_command(label = "칼로리 알려주기", command = fuc_calorie)

## 사진 영양소 알려주기 코드 ##
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "영양소 읽어들이기", menu = fileMenu)
fileMenu.add_command(label = "사진 파일 불러오기", command = func_open)
fileMenu.add_command(label = "음식 매칭", command = func_match)
fileMenu.add_command(label = "영양소 알려주기", command = fuc_nutrient)

## 영양소와 칼로리 기준으로 음식 정보 알려주기 코드 ##
fileMenu = Menu(mainMenu)
mainMenu.add_casecade(label = "음식 추천", menu = fileMenu)
fileMenu.add_command(label = "원하는 칼로리 설정", command = func_want_calorie)
fileMenu.add_command(label = "원하는 영양소 설정", command = func_want_nutirent)
fileMenu.add_command(label = "음식 추천", command = func_recommend)

