import PySimpleGUI as sg
from pdf2docx import Converter
import box
ou="请选择文件"

def zh(pdf_file,docx_file):
    if(flag=="取消" or flag==sg.WIN_CLOSED):
        window.close()
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
l=[
    [sg.FileBrowse("打开文件"),sg.Button("转换"),sg.Button("取消")]
    ]
window=sg.Window("pdf转word",l)
while True:
    flag,fpath=window.read()
    
    if(flag=="取消"):
        window.close()
        
    if(flag=="转换"):
        fpath=fpath["打开文件"]
        dpath=fpath.split('.')[0] 
        dpath=dpath+".docx"  
        zh(fpath,dpath)
        box.box()
        break
window.close()    

        
        


    
    
