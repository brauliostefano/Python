import time
import random

    def timepo_ejercucion(funcion):
        def ejercutar (*args):
            inicio = time.time()
            r = funcion (*args)
            tiempo transcurrido = (fin - inicio) * 1000
            print ("tiempo de ejecucion: {: 2f})