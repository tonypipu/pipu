import pywhatkit
import time

try:
    
   
    for i in range(5):
        pywhatkit.sendwhatmsg("+51 AQUI VA EL NUMERO",  
                        "TE AMO MUCHO",
                        16,10)
       
        print('Mensaje se ha enviado #'+str(i+1)+'enviado')
       
       
  
except:
  print("Ocurrio Un Error")
  



    
