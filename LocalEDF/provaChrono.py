#!/usr/bin/python

import sys
import os

import chronogram


#-------------------------#
#          MAIN           #
#-------------------------#
def main (argv):

    
    mCores = 3
    hyper = 1000
    
    chronogram.chronoInit(mCores, hyper, "chrono")


#Pone una linea por cada core con su nombre: C0, C1, C2, .....    
    for i in range(mCores):
        chronogram.chronoAddLine(i, "C"+str(i))

#ejemplo de lo que pondre en cada core: cada uno de los tiempos en los se ejecuta una tarea 
# conendra el nombre de la tarea el instante de inicio y instante de terminacion


#core 0
    #listaEjecuciones = (("T1", 0, 10), ("T2", 10, 20), ("T1", 20, 30), ("T2", 100, 105), ("T1", 160, 200))
    #listaEjecuciones = (("T1", 0, 4), ("T2", 4, 10), ("T3", 10, 18), ("T1", 20, 24), ("T2", 30, 36), ("T1", 40, 44), ("T4", 60, 72), ("T1", 72, 76), ("T2", 80, 86), ("T1", 86, 90), ("T3", 90, 98), ("T1", 100, 104), ("T2", 104, 110), ("T3", 110, 118), ("T1", 120, 124), ("T2", 124, 130), ("T1", 140, 144), ("T2", 150, 156), ("T1", 160, 164), ("T4", 164, 176), ("T1", 180, 184), ("T3", 184, 192), ("T2", 192, 198), ("T1", 200, 204), ("T2", 210, 216), ("T1", 220, 224), ("T4", 224, 236), ("T3", 240, 248), ("T1", 250, 254), ("T2", 254, 260), ("T1", 260, 264), ("T2", 270, 276), ("T1", 280, 284), ("T3", 284, 292))
    #listaEjecuciones = (("T1", 0, 4), ("T2", 4, 10), ("T3", 10, 18), ("T4", 18, 20), ("T1", 20, 24), ("T4", 24, 30), ("T2", 30, 36), ("T4", 36, 40), ("T1", 40, 44), ("T3", 50, 58), ("T1", 60, 64), ("T2", 64, 70), ("T4", 70, 80), ("T1", 80, 84), ("T4", 84, 86), ("T2", 90, 96), ("T1", 100, 104), ("T3", 104, 112), ("T1", 120, 124), ("T2", 124, 130), ("T4", 130, 140), ("T1", 140, 144), ("T4", 144, 146), ("T2", 150, 156), ("T3", 156, 160), ("T1", 160, 164), ("T3", 164, 168), ("T1", 180, 184), ("T2", 184, 190), ("T4", 190, 200), ("T1", 200, 204), ("T4", 204, 206), ("T3", 206, 210), ("T2", 210, 216), ("T3", 216, 220), ("T1", 220, 224), ("T1", 240, 244), ("T2", 244, 250), ("T3", 250, 258), ("T4", 258, 260), ("T1", 260, 264), ("T4", 264, 270), ("T2", 270, 276), ("T4", 276, 280), ("T1", 280, 284))
    #listaEjecuciones = (("T1", 0, 4), ("T3", 4, 12), ("T1", 20, 24), ("T1", 40, 44))
#    listaEjecuciones = (("T1", 0, 4), ("T2", 4, 10), ("T3", 10, 18), ("T1", 20, 24), ("T2", 30, 36), ("T1", 40, 44), ("T3", 50, 58), ("T1", 60, 64), ("T2", 64, 70), ("T1", 80, 84), ("T2", 90, 96), ("T1", 100, 104), ("T3", 104, 112), ("T1", 120, 124), ("T2", 124, 130), ("T1", 140, 144))
    #listaEjecuciones = (("T1", 0, 4), ("T2", 4, 10), ("T3", 10, 18), ("T1", 20, 24), ("T2", 30, 36), ("T1", 40, 44), ("T3", 50, 58), ("T1", 60, 64), ("T2", 64, 70), ("T1", 80, 84), ("T2", 90, 96), ("T1", 100, 104), ("T3", 104, 112), ("T1", 120, 124), ("T2", 124, 130), ("T1", 140, 144))
    #listaEjecuciones = (("T1", 0, 4), ("T3", 4, 12), ("T1", 20, 24), ("T1", 40, 44))
    listaEjecuciones = (("T5", 0, 2), ("T1", 2, 6), ("T5", 10, 12), ("T2", 12, 18), ("T5", 20, 22), ("T1", 22, 26), ("T5", 30, 32), ("T3", 32, 40), ("T5", 40, 42), ("T1", 42, 46), ("T2", 50, 56), ("T5", 56, 58), ("T5", 60, 62), ("T1", 62, 66), ("T5", 70, 72), ("T2", 72, 78), ("T5", 80, 82), ("T1", 82, 86), ("T3", 90, 98), ("T5", 98, 100), ("T5", 100, 102), ("T1", 102, 106), ("T2", 110, 116), ("T5", 116, 118), ("T5", 120, 122), ("T1", 122, 126), ("T5", 130, 132), ("T2", 132, 138), ("T3", 140, 148), ("T5", 148, 150))
    for le in listaEjecuciones:
        (tsk, start, end) = le
        chronogram.chronoAddExec(0, start, end, tsk)
            
# #core 1

#     listaEjecuciones = (("T3", 0, 50), ("T4", 60, 80), ("T5", 110, 190), ("T3", 200, 205), ("T5", 250, 290))
    #listaEjecuciones = (("T2", 0, 6), ("T4", 6, 18), ("T2", 30, 36))
    #listaEjecuciones = (("T2", 0, 6), ("T4", 6, 18), ("T2", 30, 36))
    listaEjecuciones = (("T6", 0, 5), ("T4", 5, 17))

    
    for le in listaEjecuciones:
        (tsk, start, end) = le
        chronogram.chronoAddExec(1, start, end, tsk)

# #core 2
    #listaEjecuciones = (("T6", 0, 10), ("T7", 10, 20), ("T6", 40, 70), ("T7", 100, 155), ("T6", 160, 240))
    listaEjecuciones = (("T8", 0, 3), ("T7", 3, 7))
    for le in listaEjecuciones:
        (tsk, start, end) = le
        chronogram.chronoAddExec(2, start, end, tsk)
            
# #core 3

#     listaEjecuciones = (("T9", 0, 50), ("T8", 60, 80), ("T9", 110, 180), ("T8", 200, 205), ("T10", 250, 290))
    
#     for le in listaEjecuciones:
#         (tsk, start, end) = le
#         chronogram.chronoAddExec(3, start, end, tsk)


#cierra el chronograma y escribe el fichero con el grafico
    chronogram.chronoClose()
        
main (sys.argv)