from datos_personales import DatosPersonales
from gustos import Gustos


        
class TodosDatos(DatosPersonales, Gustos):
    def __init__(self, ):
        super().__init__()
        self.datos_personales()
    # def datos_generales(self):
    #     print(self.datos_personales('john', '12345678A', 'sf', 'esp'))
    #     print(self.gustos_musicales('sh', 'lz', 'hr'))
    def todos_los_datos(self):
        return self.tus_datos and self.tus_datos
            
        
        
todo = TodosDatos('john', '12345678A', 'san ful', 'esp')
todo.gustos_musicales('stairway to heaven', 'led zeppelin', 'hardrock')