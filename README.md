목표 및 목적

1. 문제 분석
   
   * 최종 목적 :  단축키 실행 프로그램인 shortcut Launcher를 완성
        상위 목적 : GUI에 버튼을 구현한다.
            하위 목적 : 창의 이름을 Turbo Launcher로 바꾼다.
                        800x200의 창을 구현한다.
                        버튼을 2행 4열의 그리드 버튼으로 구현한다.

        상위 목적 : GUI에 버튼을 눌렀을 때, 응용프르그램을 실행시킨다.
            하위 목적 : 버튼에 UI 이미지를 넣는다.
                        버튼을 눌렀을 때 메모장, 계산기, 폴더 C:\열기, 구글열기 기능을 넣는다.


2. 개발 사양
하드웨어
* CPU : Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz, 2.71 GHz, 4core
  RAM : 8.00GB
  SSD : 128GB
  GPU : Intel(R) HD Graphics 620 (내장그래픽)

소프트웨어
OS : [Microsoft Windows 10 Home 버전 2004(OS 빌드 19041)]
개발 스택 : [Tkinter]
개발 프로그램 : Sublime Text 3
개발 언어 : [Python v3.8]

코드 룰

# 변수명
my_age = 13


#클래스명
class PersonImformation:
    def __init__(self):
        @property
        self.my_weight = 41
        
    def reveal_your_weight(self):
        print(self.my_weight)


if __name__ == "__main__":
    my_age = PersonImformation(43)
    my_age.reveal_your_weight()


# 개발 스택을 Tkinter로 한 이유
Tkinter와 PyQt5을 비교해봤는데 PyQt5보다 Tkinter가 간단하고 배우기 쉬울 것 같아서 선택했습니다.
