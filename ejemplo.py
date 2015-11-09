#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# andando04_alternative.py
# Movimiento animado personalizado usando grilla
#-----------------------------------------------------------------------
import pilasengine

pilas = pilasengine.iniciar()

VELOCIDAD = 4

# Definimos las teclas que moverán al personaje
teclas = {pilas.simbolos.a:'izquierda', pilas.simbolos.s:'derecha'}
# Creamos un control personalizado con esas teclas
mandos = pilas.control.Control(teclas)

# Definimos la clase de nuestro actor
class Hombre(pilasengine.actores.Actor):
    '''Un actor que se mueve con las teclas a y s y con animación'''
    
    def iniciar(self):
        self.imagen = pilas.imagenes.cargar_grilla("andando.png",6)
        self.definir_cuadro(0)
        # Hacemos que el actor se mueva con el comportamiento personalizado
        self.hacer("Caminando")

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)

class Caminando(pilasengine.comportamientos.Comportamiento):
    '''Actor en posicion normal hasta que el usuario pulse alguna tecla'''
    def iniciar(self, receptor):
        self.receptor = receptor

        self.cuadros = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
        self.paso = 0

    def actualizar(self):
        if mandos.izquierda:
            if not self.receptor.espejado:
                self.receptor.espejado = True
            self.receptor.x -= VELOCIDAD
            self.avanzar_animacion()
        elif mandos.derecha:
            if self.receptor.espejado:
                self.receptor.espejado = False
            self.receptor.x += VELOCIDAD
            self.avanzar_animacion()

    def avanzar_animacion(self):
        self.paso += 1
        if self.paso>=len(self.cuadros):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.paso])

pilas.comportamientos.vincular(Caminando)
pilas.actores.vincular(Hombre)

chuck = pilas.actores.Hombre()
pilas.ejecutar()