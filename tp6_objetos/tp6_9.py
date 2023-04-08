# 9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4,
# e impórtela al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse
# que la importación funcionó.

import Tp6_4

RestauranteImportado=Tp6_4.Restaurante("El Culto del Pancho","Panchos")

RestauranteImportado.abrir_restaurante()
RestauranteImportado.describir_restaurante()