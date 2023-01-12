import sys
import datetime
import subprocess

#Tiempo 24 H
hora = 18
min = 30

seconds = hora_out = min_out = seg_out = hora_actual = min_actual = seg_actual = 0
version = 1.0
tiempoSuperado = False

out_time = lambda a, b, c: " %02d : %02d : %02d" % (a , b , c)

header = '''
    _____     ___     __  __     _____     ____   
   |_   _|   |_ _|   |  \/  |   | ____|   |  _ \  
     | |      | |    | |\/| |   |  _|     | |_) |  
     | |      | |    | |  | |   | |___    |  _ <  
     |_|     |___|   |_|  |_|   |_____|   |_| \_\ v%a
   
   Programar apagado: p -a
   Cancelar: p -c
   Ver comandos: ayuda
   Cerrar timer: salir
''' % version
comandos_msj ='''
   Temporizador: t
   Modificar temporizador: t -m
   Tiempo temporizador: t -t
   Tiempo computadora: t -c
   Programar apagado: p -a
   Programar reinicio: p -r
   Programar cerrar sesión: p -l
   Cancelar: p -c
   Cerrar timer: salir
''' 

print(header)

def dateTime():
   tiempo_actual = datetime.datetime.now().time()
   global hora_actual,min_actual,seg_actual
   hora_actual = tiempo_actual.hour
   min_actual = tiempo_actual.minute
   seg_actual = tiempo_actual.second

def timer():
   dateTime()
   global hora_out,min_out,seg_out,seconds,tiempoSuperado
   if seg_actual > 0 : seg_out = 60-seg_actual
   seconds = seg_out
   if (hora_actual + 1) == hora:
      min_out = (60-min_actual)+min
      seconds += min_out*60
   elif hora_actual < hora:
      hora_out = hora-hora_actual
      if min_actual < min :
         min_out = min-min_actual
         seconds += min_out*60
      else:
         hora_out-=1
         min_out = (60-min_actual)+min
         seconds += min_out*60
      seconds += hora_out*3600
   else:
      seg_out = 0
      seconds = 0
      tiempoSuperado = True

while True:
   comand = input("input >_: ").strip()
   if(comand == "t"):
      print(out_time(hora,min,0))
   elif(comand == "t -c"):
      dateTime()
      if tiempoSuperado:
         print(out_time(hora_actual,min_actual,seg_actual)," [TIEMPO SUPERADO]")
      else:
         print(out_time(hora_actual,min_actual,seg_actual))
   elif(comand == "t -t"):
      timer()
      if tiempoSuperado:
         print(out_time(hora_out,min_out,seg_out),"(",seconds,") [TIEMPO SUPERADO]")
      else:
         print(out_time(hora_out,min_out,seg_out),"(",seconds,")")
   elif(comand == "t -m"):
      print(" Inserte la hora en formato de 24 Horas")
      hora = int(input("input >_: ").strip())
      print(" Inserte los minutos")
      min = int(input("input >_: ").strip())
      print(" Timer actualizado:",out_time(hora,min,0))
   elif(comand == "ayuda"):
      print(comandos_msj)
   elif(comand == "p -l"):
      timer()
      subprocess.run("shutdown -l -t %d" % seconds)# Cerrar sesión
   elif(comand == "p -r"):
      timer()
      subprocess.run("shutdown -r -t %d" % seconds)# Reiniciar
   elif(comand == "p -a"):
      timer()
      subprocess.run("shutdown -s -t %d" % seconds)# Apagar
   elif(comand == "p -c"):
      subprocess.run("shutdown /a")# Cancelar
   elif(comand == "salir"):
      sys.exit()


