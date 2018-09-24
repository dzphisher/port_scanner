import socket
import sys
from datetime import datetime
from time import *


print(",-.----.       ,----..                   ,/   .`|                                                       ,--.         ,--.                      ")       
print("\    /  \     /   /   \  ,-.----.      ,`   .'  :          .--.--.     ,----..     ,---,              ,--.'|       ,--.'|    ,---,.,-.----.")           
print("|   :    \   /   .     : \    /  \   ;    ;     /         /  /    '.  /   /   \   '  .' \         ,--,:  : |   ,--,:  : |  ,'  .' |\    /  \ ")         
print("|   |  .\ : .   /   ;.  \;   :    \.'___,/    ,'         |  :  /`. / |   :     : /  ;    '.    ,`--.'`|  ' :,`--.'`|  ' :,---.'   |;   :    \ ")       
print(".   :  |: |.   ;   /  ` ;|   | .\ :|    :     |          ;  |  |--`  .   |  ;. /:  :       \   |   :  :  | ||   :  :  | ||   |   .'|   | .\ :   ")      
print("|   |   \ :;   |  ; \ ; |.   : |: |;    |.';  ;          |  :  ;_    .   ; /--` :  |   /\   \  :   |   \ | ::   |   \ | ::   :  |-,.   : |: |     ")    
print("|   : .   /|   :  | ; | '|   |  \ :`----'  |  |           \  \    `. ;   | ;    |  :  ' ;.   : |   : '  '; ||   : '  '; |:   |  ;/||   |  \ :       ")  
print(";   | |`-' .   |  ' ' ' :|   : .  /    '   :  ;            `----.   \|   : |    |  |  ;/  \   \'   ' ;.    ;'   ' ;.    ;|   :   .'|   : .  /         ")
print("|   | ;    '   ;  \; /  |;   | |  \    |   |  '            __ \  \  |.   | '___ '  :  | \  \ ,'|   | | \   ||   | | \   ||   |  |-,;   | |  \         ")
print(":   ' |     \   \  ',  / |   | ;\  \   '   :  |           /  /`--'  /'   ; : .'||  |  '  '--'  '   : |  ; .''   : |  ; .''   :  ;/||   | ;\  \        ")
print(":   : :      ;   :    /  :   ' | \.'   ;   |.'           '--'.     / '   | '/  :|  :  :        |   | '`--'  |   | '`--'  |   |    \:   ' | \.'        ")
print("|   | :       \   \ .'   :   : :-'     '---'               `--'---'  |   :    / |  | ,'        '   : |      '   : |      |   :   .':   : :-'          ")
print("`---'.|        `---`     |   |.'                                      \   \ .'  `--''          ;   |.'      ;   |.'      |   | ,'  |   |.'            ")
print("  `---`                  `---'                                         `---`                   '---'        '---'        `----'    `---'              ")
                                 

print("                                                       [+]CODED BY:AYMEN BENDJEDDOU[+]                                                                 ")


ip=input("Enter IP :")
t1=datetime.now()
print("Scanning start on  %s ..."% ip)
sleep(1)
try:
   
   
   host=socket.gethostbyaddr(ip)
   print(host)
except socket.herror:
   
   print("can not found host name")
try:
   
  for port in range(0,65335):
     
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.settimeout(5)
     if (s.connect_ex((ip,port))==0):
        try:
         
         
           serv = socket.getservbyport(port)
        except socket.error:
         

          serv="not-found"
     
         
         
         
   
        
     
        print(("PORT %s:OPEN  Service:%s  "%(port,serv)))
        s.close()
  t2=datetime.now()
  t3=t2-t1
  print("Scanning Completed on %s!!"%t3)
  

        
except KeyboardInterrupt:
   print("You Pressed CTRL+C =====>see You soon :) <==== ")
   sys.exit
      
   

   
   

