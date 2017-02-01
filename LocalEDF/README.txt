Planificador multicore para tiempo Real con política EDF (Earliest Deadline First)

----- Descripción -----

El sistema ejecuta la planificación de una serie de tareas especificadas por el usuario. Las tareas van asociadas a particiones a las que se asigna la prioridad según el criterio EDF.

El planificador es local, lo que quiere decir que las tareas no podrán migrar de core durante el tiempo de ejecución, por eso se les asigna un core al inicio de la planificación. Las particiones se ubican en los cores disponibles según la política de ubicación deseada (Best Fit, Next Fit, First Fit o Worst Fit).

También se ha de especificar la utilización global, que corresponde con la utilización máxima que puede planificarse en un determinado core.
Los resultados se muestran por terminal y se realiza una representación gráfica en un fichero .svg (chrono.svg) que se crea en el mismo directorio.

Adicionalmente, se han implementado dos modos de ejecución diferentes del mismo planificador: por ticks de reloj o basado en eventos.

----- Ejemplo de uso -----

La inicialización del sistema se lleva a cabo en el fichero "provaGSRMsched.py". Se han de especificar los siguientes parámetros:
 - Utilización global
 - Número de cores
 - Número de particiones
 - Política de ubicación
 - Modo de ejecución
 - Parámetros de las tareas

 Esta inicialización se ha de especificar entre las líneas 27 y 34 del citado fichero. Un ejemplo sería:

    globalUtil = 0.8        # Max utilization = 1
    mCores = 2              # Cores in the system
    nPartCriticas = 4       # nPartitions = nTasks
    allocationPolicy = "FF" # Policy to allocate tasks in cores ("FF", "NF", "BF", "WF")
    sched = LSEDFe          # Scheduling mode by ticks (LSEDFt) or based on events (LSEDFe)

    params = ((20,4,0.2), (30, 6, 0.2), (50, 8, 0.16), (60, 12, 0.5))

* La utilización global ha de tener un máximo de 1
* El número de cores no está limitado
* El número de particiones ha de ser menor o igual que el número tareas definidas en la variable "params"
* La política de ubicación puede variar entre FF, NF, BF y WF
* El modo de ejecución puede referirse a LSEDFt para el modo por ticks o LSEDFe para el modo por eventos
* Cada tarea debe estar definida por (periodo, tiempo de cómputo o WCET, utilización)

----- Ejecución -----

Para ejecutar el planificador y obtener los resultados, ejecutar en el terminal:

$ python provaLSEDFsched.py

Puesto que el planificador es local, la planificación se ejecutará secuencialmente para cada uno de los cores.



