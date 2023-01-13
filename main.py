import sys
import datetime
import subprocess

#Tiempo 24 H
hora = 18
min = 30

version = 1.1
out_time = lambda a, b, c: " %02d : %02d : %02d" % (a , b , c)

header = '''
    _____     ___     __  __     _____     ____   
   |_   _|   |_ _|   |  \/  |   | ____|   |  _ \  
     | |      | |    | |\/| |   |  _|     | |_) |  
     | |      | |    | |  | |   | |___    |  _ <  
     |_|     |___|   |_|  |_|   |_____|   |_| \_\ v%a
   by @pacsoda

   Programar apagado: p -a
   Cancelar: p -c
   Ver comandos: ayuda
   Cerrar timer: salir
''' % version
comandos_msj ='''
   Temporizador: t
   Modificar temporizador: t -m
   Duracion temporizador: t -t
   Tiempo computadora: t -c
   Programar apagado: p -a
   Programar reinicio: p -r
   Programar cerrar sesión: p -l
   Cancelar: p -c
   Cerrar timer: salir
''' 

print(header)

def dateTime():
   global dt_actual
   dt_actual = datetime.datetime.now()

def timer():
   dateTime()
   global duracion,seconds,tiempoSuperado
   dt_timer = datetime.datetime(dt_actual.year,dt_actual.month,dt_actual.day,hora,min,00)#yr, mo, day, hr, min, sec
   duracion = dt_timer - dt_actual
   if duracion.days == -1: 
      tiempoSuperado = True 
      duracion = "00:00:00"
      seconds = 0
   else:
      tiempoSuperado = False
      seconds = duracion.total_seconds()

while True:
   comand = input("input >_: ").strip()
   if(comand == "t"):
      print(out_time(hora,min,0))
   elif(comand == "t -c"):
      dateTime()
      print(dt_actual.time())
   elif(comand == "t -t"):
      timer()
      if tiempoSuperado:
         print(duracion,"(",seconds,") [TIEMPO SUPERADO]")
      else:
         print(duracion,"(",seconds,")")
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
