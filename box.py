import PySimpleGUI as sg
import os
import sys
def box():
    layout = [[(sg.Text('完成', size=[40, 1])),sg.Ok()]]
 
    window = sg.Window('完成', layout, default_element_size=(30, 2))
 
    s,n=window.read()
    if(s=="Ok" or s==sg.WIN_CLOSED):
        window.close()
        return 0
    while True:
        if(n,s!="None"):
            s,n=window.read()
            print(s,n)
        else:
            break
        if(s=="Ok" or s==sg.WIN_CLOSED):
            break
    window.close()   
    
        

    