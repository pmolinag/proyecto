import unittest 

class vuelos():

    def __init__(self):
        self.corigen = {}
        self.cdestino = []
        self.vuelos = {}

    def insertaVuelo(self, origen, destino, precio):
        self.corigen.setdefault(origen, [])
        if origen not in self.corigen[origen]:
            self.corigen[origen].append(destino)
        if destino not in self.cdestino:
            self.cdestino.append(destino)
        vuelo = origen + '-' + destino
        self.vuelos[vuelo] = precio

        return vuelo + ',' + str(self.vuelos[vuelo])

    def borrarVuelo(self, vuelo):

        del self.vuelos[vuelo]

        return True

    def muestraVuelo(self, vuelo):
        print (self.vuelos[vuelo])

    def muestraCOrigen(self):
        return self.corigen

    def muestraCDestino(self):
        return self.cdestino

    def buscaDestinos(self, origen):
        return self.corigen[origen]

    def cuantosVuelos(self):
        return len(self.vuelos)

    def compruebaVuelo(self, vuelo):
        encontrado = False
        if vuelo in self.vuelos:
            encontrado = True
        return encontrado

    def compruebaDestino(self, ciudad):
        encontrado = False
        for i in self.cdestino:
            if i == ciudad:
                encontrado = True
        return encontrado

    def compruebaOrigen(self, ciudad):
            encontrado = False
            for i in self.corigen:
                if i == ciudad:
                    encontrado = True
            return encontrado

class TestVuelos(unittest.TestCase):

    def testInserta(self):
        vuelos_prueba = vuelos()
        self.assertEqual('Granada-Barcelona,50', vuelos_prueba.insertaVuelo( "Granada", "Barcelona",50), "Insertado correctamente." )

    def testBorra(self):
        vuelos_prueba = vuelos()
        vuelos_prueba.insertaVuelo( "Granada", "Barcelona", 50)
        self.assertTrue(vuelos_prueba.borrarVuelo("Granada-Barcelona"), "Borrado correctamente.")

    def testCompruebaCiudadOrigen(self):
        vuelos_prueba = vuelos()
        vuelos_prueba.insertaVuelo( "Granada", "Barcelona", 50)
        prueba = vuelos_prueba.compruebaOrigen("Granada")
        self.assertTrue(prueba, "La ciudad origen existe.")

    def testCompruebaCiudadDestino(self):
        vuelos_prueba = vuelos()
        vuelos_prueba.insertaVuelo( "Granada", "Barcelona", 50)
        prueba = vuelos_prueba.compruebaDestino("Barcelona")
        self.assertTrue(prueba, "La ciudad destino existe.")

    def testCompruebaVuelo(self):
        vuelos_prueba = vuelos()
        vuelos_prueba.insertaVuelo( "Granada", "Barcelona", 50)
        self.assertTrue(vuelos_prueba.compruebaVuelo("Granada-Barcelona"), "El vuelo existe.")

    def testCuantosVuelos(self):
        vuelos_prueba = vuelos()
        vuelos_prueba.insertaVuelo( "Granada", "Barcelona", 50)
        self.assertEqual(vuelos_prueba.cuantosVuelos(), 1, "Numero de vuelos correcto.")


if __name__ == '__main__':
    unittest.main()
