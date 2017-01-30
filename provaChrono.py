#!/usr/bin/python

import sys
import os

import chronogram


#-------------------------#
#          MAIN           #
#-------------------------#
def main (argv):

    
    mCores = 1
    hyper = 10000
    
    chronogram.chronoInit(mCores, hyper, "chrono")


#Pone una linea por cada core con su nombre: C0, C1, C2, .....    
    for i in range(mCores):
        chronogram.chronoAddLine(i, "C"+str(i))

#ejemplo de lo que pondre en cada core: cada uno de los tiempos en los se ejecuta una tarea 
# conendra el nombre de la tarea el instante de inicio y instante de terminacion

# coore
    listaEjecuciones = (("T1", 0, 4), ("T2", 4, 10), ("T3", 10, 18), ("T1", 20, 24), ("T2", 30, 36), ("T1", 40, 44), ("T4", 60, 72), ("T1", 72, 76), ("T2", 80, 86), ("T1", 86, 90), ("T3", 90, 98), ("T1", 100, 104), ("T2", 104, 110), ("T3", 110, 118), ("T1", 120, 124), ("T2", 124, 130), ("T1", 140, 144), ("T2", 150, 156), ("T1", 160, 164), ("T4", 164, 176), ("T1", 180, 184), ("T3", 184, 192), ("T2", 192, 198), ("T1", 200, 204), ("T2", 210, 216), ("T1", 220, 224), ("T4", 224, 236), ("T3", 240, 248), ("T1", 250, 254), ("T2", 254, 260), ("T1", 260, 264), ("T2", 270, 276), ("T1", 280, 284), ("T3", 284, 292))

    for le in listaEjecuciones:
        (tsk, start, end) = le
        chronogram.chronoAddExec(0, start, end, tsk)

#core 0
#     listaEjecuciones = (("T1", 0, 10), ("T2", 10, 20), ("T1", 20, 30), ("T2", 100, 105), ("T1", 160, 200))
    
#     for le in listaEjecuciones:
#         (tsk, start, end) = le
#         chronogram.chronoAddExec(0, start, end, tsk)
            
# #core 1

#     listaEjecuciones = (("T3", 0, 50), ("T4", 60, 80), ("T5", 110, 190), ("T3", 200, 205), ("T5", 250, 290))
    
#     for le in listaEjecuciones:
#         (tsk, start, end) = le
#         chronogram.chronoAddExec(1, start, end, tsk)

# #core 2
#     listaEjecuciones = (("T6", 0, 10), ("T7", 10, 20), ("T6", 40, 70), ("T7", 100, 155), ("T6", 160, 240))
    
#     for le in listaEjecuciones:
#         (tsk, start, end) = le
#         chronogram.chronoAddExec(2, start, end, tsk)
            
# #core 3

#     listaEjecuciones = (("T9", 0, 50), ("T8", 60, 80), ("T9", 110, 180), ("T8", 200, 205), ("T10", 250, 290))
    
#     for le in listaEjecuciones:
#         (tsk, start, end) = le
#         chronogram.chronoAddExec(3, start, end, tsk)


#cierra el chronograma y escribe el fichero con el grafico
    chronogram.chronoClose()
        
main (sys.argv)