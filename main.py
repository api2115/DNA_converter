from zmiana import zmiana
from readData import readData,testData,check_string
from json2html import *
import webbrowser
import json
import os

def openHtml(name1, name2):
    with open(name1 + ".html", "w", encoding="utf-8") as tablehtml:
        tablehtml.write(json2html.convert(json=name2))
    url = name1+".html"
    webbrowser.open(url, new=2)

def load_data():
    if os.path.exists("./dane.txt"):
        with open('dane.txt', 'r') as file:
            data = file.read().replace('\n', '')
    else:
        data=None
    return data


def load_res():
    if os.path.exists("./res.json"):
        with open("res.json") as json_file:
            try:
                res = json.load(json_file)
            except:
                res=None
    else:
        res=None
    return res




print(""" 

                                                                                          
                      ,--.                                                                
    ,---,           ,--.'|   ,---,                                                        
  .'  .' `\     ,--,:  : |  '  .' \                                                       
,---.'     \ ,`--.'`|  ' : /  ;    '.                                                     
|   |  .`\  ||   :  :  | |:  :       \                                                    
:   : |  '  |:   |   \ | ::  |   /\   \                                                   
|   ' '  ;  :|   : '  '; ||  :  ' ;.   :                                                  
'   | ;  .  |'   ' ;.    ;|  |  ;/  \   \                                                 
|   | :  |  '|   | | \   |'  :  | \  \ ,'                                                 
'   : | /  ; '   : |  ; .'|  |  '  '--'                                                   
|   | '` ,/  |   | '`--'  |  :  :                                                         
;   :  .'    '   : |      |  | ,'                                                         
|   ,.'      ;   |.'      `--''                                ___                        
'---'        '---'                                           ,--.'|_                      
            ,---.        ,---,                      __  ,-.  |  | :,'             __  ,-. 
           '   ,'\   ,-+-. /  |     .---.         ,' ,'/ /|  :  : ' :           ,' ,'/ /| 
   ,---.  /   /   | ,--.'|'   |   /.  ./|  ,---.  '  | |' |.;__,'  /     ,---.  '  | |' | 
  /     \.   ; ,. :|   |  ,"' | .-' . ' | /     \ |  |   ,'|  |   |     /     \ |  |   ,' 
 /    / ''   | |: :|   | /  | |/___/ \: |/    /  |'  :  /  :__,'| :    /    /  |'  :  /   
.    ' / '   | .; :|   | |  | |.   \  ' .    ' / ||  | '     '  : |__ .    ' / ||  | '    
'   ; :__|   :    ||   | |  |/  \   \   '   ;   /|;  : |     |  | '.'|'   ;   /|;  : |    
'   | '.'|\   \  / |   | |--'    \   \  '   |  / ||  , ;     ;  :    ;'   |  / ||  , ;    
|   :    : `----'  |   |/         \   \ |   :    | ---'      |  ,   / |   :    | ---'     
 \   \  /          '---'           '---" \   \  /             ---`-'   \   \  /           
  `----'                                  `----'                        `----'            
""")
starter=True
result=None
while starter:
    print("1: Wczytaj dane z pliku")
    print("2: Poka?? tabele dla danych z pami??ci")
    print("3: Uruchom program")
    print("4: Tabela dla wyniku")
    print("5: Zako??cz")
    inp=input("? ")
    if inp=="1":
        data=load_data()
        if data:
            print("TO POTRWA OKO??O MINUTY")
            res = readData(data)
            openHtml("table", res)
        else:
            print("BRAKUJE PLIKU dane.txt STW??RZ GO I UZUPE??NIJ")
    if inp=="2":
        res=load_res()
        if res:
            openHtml("table", res)
        else:
            print("NIE MA DANYCH W PAMI??CI WCZYTAJ JE!!!")
    if inp=="3":
        res=load_res()
        if res:
            string = input("Podaj ci??g: ")
            while not check_string(string):
                print("PODAJ ODPOWIEDNI CI??G!!!")
                string=input("podaj ci??g: ")
            res=load_res()
            if res:
                result = zmiana(res, string)
                res2 = testData(result)
                openHtml("table2", res2)
                print("".join(result))
                with open("out.txt","w") as file:
                    file.write("".join(result))
                print("Wynik zapisano w pliku out.txt")
        else:
            print("NIE MA DANYCH W PAMI??CI WCZYTAJ JE!!!")
    if inp=="4":
        if result:
            res2 = testData(result)
            openHtml("table2", res2)
        else:
            print("NIE MA JESZCZE WYNIKU!!!")
    if inp=="5":
        starter=False






