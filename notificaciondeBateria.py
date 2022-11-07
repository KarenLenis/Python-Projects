#Psutil en python es una biblioteca 
# multiplataforma para recuperar información sobre 
# los procesos en ejecución y la utilización del 
# sistema (CPU, memoria, discos, redes, sensores) en Python.
from email import message
from socket import timeout
from plyer import notification #envia la notificacion
import psutil

#comando para la bateria sensor
#bateria=psutil.sen
bateria = psutil.sensors_battery()

plugged=bateria.power_plugged

if __name__=="__main__":
    if plugged:
        percent=bateria.percent
        if percent<= 80:
            notification.notify(
                title="conectado",
                message=" para mejorar la vida de su bteria cargar por encima de 80%",
                timeout=2
            )
        elif percent==100:
            notification.notify(
                title="conectado",
                message="Por favor desconectar. Bateria cargada",
                timeout=2
            )
        else:
            notification.notify(
                title="conectado",
                message="Remueva el cargador",
                timeout=2
            )
    else:
        percent=bateria.percent
        if percent <= 20:
            notification.notify(
                title="Recordatorio bateria",
                message="Bateria baja cargar",
                timeout=2
            )
        elif percent <=50:
            notification.notify(
                title="Recordatorio bateria",
                message=f"Bateria es {percent}",
                timeout=2
            )
        elif percent == 100:
            notification.notify(
                title="Recordatorio bateria",
                message="bateria full",
                timeout=2
            )
        else:
            notification.notify(
                title="Recordatorio bateria",
                message=f"bateria {percent}",
                timeout=2
            )
