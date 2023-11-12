import mouse
import keyboard

def mouse_pressed():
    print('Mouse pressed')

def keyboard_down(evt):
    print('Keyboard down {}'.format(evt.name)) #입력된 키를 출력합니다.

def mouse_control(evt):
    mouse.move(100,100,duration=2) #x=100, y=100의 좌표로 2의 속도로 이동합니다.
    mouse.click(button='right') #현재 위치에서 마우스 우클릭 합니다.

mouse.on_click(mouse_pressed) #마우스 왼쪽 버튼을 누르면 mouse_pressed 함수를 호출합니다.
keyboard.on_press(keyboard_down) #키보드 버튼을 누르면 keyboard_down 함수를 호출합니다.
keyboard.on_press_key('x', mouse_control) #키보드 x키를 누르면 mouse_control 함수를 호출합니다.
keyboard.wait('esc') #esc 키를 누를때 까지 대기합니다.