#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro:
# @Capítulo: 9 - Albaricoques, cerezas y clustering
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   SCIKIT-LEARN : 0.21.0
#   MATPLOTLIB : 3.0.3
#   JOBLIB : 0.13.2
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------



#---- IMPORTAR MÓDULOS --
import random
import pandas as pnd

from datos_cerezas import datos_cerezas
from datos_albaricoques import datos_albaricoques

class Datos(datos_cerezas, datos_albaricoques):

    def __init__(self):
        super().__init__(self)

    def generar_frutas():
        cerezas=datos_cerezas.generar_cerezas()
        albaricoques=datos_albaricoques.generar_albaricoques()
        #Constitución de las observaciones
        frutas = cerezas+albaricoques
        #Mezcla de las observaciones
        random.shuffle(frutas)

        #Guardado de las observaciones en un archivo
        frutas_df = pnd.DataFrame(frutas)
        frutas_df.to_csv("datas/frutas.csv", index=False,header=False)

        return frutas_df

