import funciones
import os
from time import time

cantidad_de_discos=0
while(True):
    pasos=0
    cantidad_de_discos=funciones.menu()  
    os.system('cls')
    funciones.colocar_discos(cantidad_de_discos),funciones.mostrartorres(pasos)
    
    time1=time()
    while(not funciones.ganar(cantidad_de_discos)):
        torre1 = int(input('ingrese su movimiento '+str(pasos+1)+' '))
        if torre1>5: break
        elif torre1==5: cantidad_de_discos=funciones.menu(); break
        elif torre1 == 4: funciones.Inicializar_torres(cantidad_de_discos); break
        else:
            torre2 = int(input('ingrese su movimiento '+str(pasos+1)+' '))

            if(torre2 == 4): funciones.Inicializar_torres(cantidad_de_discos); break
            if(torre2 == 5): cantidad_de_discos=funciones.menu(); break
            if(torre2 == 6): break

            funciones.mover_torre(torre1,torre2)
            os.system('cls'); pasos+=1 ; funciones.mostrartorres(pasos)

    time2=time()
    os.system('cls')
    funciones.mostrartorres(pasos),funciones.mensaje(time1,time2)
    k=input()
    if(k=='3'): break