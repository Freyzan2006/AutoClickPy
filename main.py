import pyautogui 
import time
import keyboard
import flet as ft
import mouse
import json

def main(win: ft.Page):
    
    def DataInfo(el:str, datatype:str):
        
        with open('data.json', 'r') as file:
            data = json.load(file)
           
            data['respanse'][datatype] = el
        
        with open('data.json', 'w') as file:
            json.dump(data, file, indent = 3)

    def TypeBtnFunc(e):
        if TypeBtn.text == "Зажимать мышь":
            TypeBtn.text = "Кликать левой"
            ClickInfo.disabled = False

            DataInfo(TypeBtn.text, 'TypeClick')

            win.update()
        elif TypeBtn.text == "Кликать левой":
            TypeBtn.text = "Кликать правой"
            ClickInfo.disabled = False

            DataInfo(TypeBtn.text, 'TypeClick')

            win.update()
        elif TypeBtn.text == "Кликать правой":
            TypeBtn.text = "Зажимать мышь"
            ClickInfo.disabled = True

            DataInfo(TypeBtn.text, 'TypeClick')

            win.update()
    
    win.title = "AutoClick"
    win.vertical_alignment = ft.MainAxisAlignment.CENTER
    TypeText = ft.Text(value = "Тип клика: ", color = "#FFFFFF", font_family = "Consolas", size = 20)
    TypeBtn = ft.ElevatedButton(text = "Кликать левой", icon = ft.icons.MOUSE_OUTLINED, icon_color = "#FFFFFF", color = "#FFFFFF", on_click = TypeBtnFunc)
    OnBtn = ft.Text(value = "start", color = "#FFFFFF", font_family = "Consolas", size = 20)
    Icon_mouse = ft.Icon(name = ft.icons.MOUSE, color = "#FFFFFF")
    AboutText = ft.Text(value = "Max кп/c",  size = 20, color = "#FFFFFF", text_align = "center")
    
    def ClickInfoChange(e):
        ClickInfoText.value = str(round(ClickInfo.value, 1)) + " кп/c"   
        ClickInfoText.update()
        DataInfo(round(ClickInfo.value, 1), 'SpeedClick')
        
    ClickInfo = ft.Slider(min=0.1, max = 5, divisions = 0.1, label="{value}sec", on_change = ClickInfoChange)
   
    with open('data.json', 'r') as file:
        data = json.load(file)
        TypeBtn.text = data['respanse']['TypeClick']
        
        if TypeBtn.text == "Зажимать мышь":
            ClickInfo.disabled = True
    
    with open('data.json', 'r') as file:
        data = json.load(file)
        ClickInfo.value = data['respanse']['SpeedClick']
        
    ClickInfoText = ft.Text(value = f"{ClickInfo.value} кп/c", font_family = "Consolas", color = "#FFFFFF", size = 20)
    AboutText2 = ft.Text(value = "Min кп/c",  size = 20, color = "#FFFFFF", text_align = "center") 

    def RuleAboutFunc(e):
        dlg.open = True
        win.update()

    RuleText = """
    Документация:
    
    ctrl+r - Старт/стоп 
        
    ctrl+left - Прибавить скорость

    ctrl+right - Убавить скорость

    ctrl+up - Сменить тип клика
    """    

    RuleAbout = ft.ElevatedButton(text = "Документация" ,on_click = RuleAboutFunc, color = "#FFFFFF")
    dlg = ft.AlertDialog(title=ft.Text(RuleText, font_family = "Consolas"))
           
    win.add (
            ft.Row (
                [
                    TypeText, TypeBtn
                ],
                alignment = ft.MainAxisAlignment.CENTER
            ),
            ft.Row (
                [
                    ClickInfoText
                ],
                alignment = ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    AboutText, ClickInfo, AboutText2
                ],
                alignment = ft.MainAxisAlignment.CENTER
            ),
        
            ft.Row (
                [
                    OnBtn, Icon_mouse
                ],
                alignment = ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    RuleAbout, dlg
                ],
                alignment = ft.MainAxisAlignment.CENTER
            )
    )
    
    def set_clicker():
        global isClicking
        if isClicking:
            OnBtn.text = 'start'
            OnBtn.color = "#FFFFFF"
            Icon_mouse.color = "#FFFFFF"
            win.update()
            isClicking = False
        else:
            OnBtn.text = 'stop'
            OnBtn.color = "blue"
            Icon_mouse.color = "blue"
            win.update()
            isClicking = True
            
    def speed_click_plus():
        if TypeBtn.text != "Зажимать мышь":
            if ClickInfo.value >= 0.1 and ClickInfo.value < 5:
                ClickInfo.value = ClickInfo.value + 0.1
                ClickInfo.value = round(ClickInfo.value, 1)
                DataInfo(round(ClickInfo.value, 1), 'SpeedClick')
                ClickInfoText.value = str(round(ClickInfo.value, 1)) + " кп/c"   
                
                ClickInfo.update()
                ClickInfoText.update()
                ClickInfoText.update()
                time.sleep(0.1)
            
    def speed_click_minus():
        if TypeBtn.text != "Зажимать мышь":
            if ClickInfo.value > 0.1:
                ClickInfo.value = ClickInfo.value - 0.1
                ClickInfo.value = round(ClickInfo.value, 1)

                DataInfo(round(ClickInfo.value, 1), 'SpeedClick')
                ClickInfoText.value = str(round(ClickInfo.value, 1)) + " кп/c"  
                ClickInfo.update()
                ClickInfoText.update()
                ClickInfoText.update()
                time.sleep(0.1)
    
    def TypeBtnFuncBtn():
        if TypeBtn.text == "Зажимать мышь":
            TypeBtn.text = "Кликать левой"
            ClickInfo.disabled = False
            DataInfo(TypeBtn.text, 'TypeClick')
            win.update()
        elif TypeBtn.text == "Кликать левой":
            TypeBtn.text = "Кликать правой"
            ClickInfo.disabled = False
            DataInfo(TypeBtn.text, 'TypeClick')
            win.update()
        elif TypeBtn.text == "Кликать правой":
            TypeBtn.text = "Зажимать мышь"
            ClickInfo.disabled = True
            DataInfo(TypeBtn.text, 'TypeClick')
            win.update()

    keyboard.add_hotkey('ctrl+r', set_clicker)
    keyboard.add_hotkey('ctrl+left', speed_click_plus)  
    keyboard.add_hotkey('ctrl+right', speed_click_minus)
    keyboard.add_hotkey('ctrl+up', TypeBtnFuncBtn)
               
    while True:
        if isClicking:
            if TypeBtn.text == "Кликать левой":
                sec = round(ClickInfo.value, 1)
                mouse.double_click(button = 'left')
                time.sleep(sec)
            elif TypeBtn.text == "Кликать правой":
                sec = round(ClickInfo.value, 1)
                mouse.double_click(button = 'right')
                time.sleep(sec)
            elif TypeBtn.text == "Зажимать мышь":
                mouse.drag(1, 1, 1, 1, duration = 0.1) 
        else: 
            time.sleep(0.1)             
                
sec = 1          
isClicking = False               
                
if __name__ == "__main__":
    ft.app(target = main)            













  
            
            
            
            
            
    
        




    
            
           
            
        
                
        

   
    
    
    
           
                

               
                
                
            
            
                
                
                
                
                
              
                
                
                
            
        
            
            

           


  

    









  

    
 
    