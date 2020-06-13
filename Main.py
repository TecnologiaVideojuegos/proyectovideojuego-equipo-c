import arcade
import Jugador
import os
import HUD
import random
import Habitaciones

# --- Constantes ---

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900


class PhantomGear(arcade.Window):
    """ Ventana principal del juego """

    def __init__(self):
        """ Constructor """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Phantom Gear")
        # Sprite lists
        self.player_list = None
        self.bullet_list = None
        self.lista_balas_laser = None
        self.lista_balas_gas = None
        # Habitaciones
        self.current_room = 0
        self.rooms = None
        self.cambiado = False
        self.cambiado_piso = False
        # Set up the player
        self.jugador = None
        self.physics_engine = None
        self.physics_engine_enemigos = None
        self.velocidad_jugador = 4
        self.vida_jugador = 10
        self.carga_fantasmal_jugador = 100
        # Atributos para el disparo del jugador
        self.velocidad_disparo = 10
        # Atributos enemigos
        self.velocidad_enemigos = 1.2
        self.velocidad_disparo_enemigos = 5
        # Atributos para el manejo del comienzo del juego
        self.empezado = False
        self.mirando_controles = False
        # Pausar el juego
        self.pausado = False
        # Musica de fondo
        self.musica_lab = arcade.load_sound("Sonidos" + os.path.sep + "Piso Final.wav")
        self.musica_ruinas = arcade.load_sound("Sonidos" + os.path.sep + "piso2.wav")
        self.musica_prision_activa = False
        self.musica_ruinas_activa = False
        self.musica_lab_activa = False
        # Otros sonidos
        self.sonido_cambio_piso = arcade.load_sound("Sonidos"+os.path.sep+"cambio de lvl(provisional).wav")
        # Atributos para manejar el mostrar mensajes dependiendo del buff y administrar los buffs en sí
        self.contador_quitar_mensaje = 0
        self.buffs_activos = []
        self.recogido_buff1 = False  # para mostrar el mensaje correspondiente
        self.recogido_buff2 = False
        self.recogido_buff3 = False
        self.recogido_buff4 = False
        self.recogido_buff5 = False

        self.frame_count = 0

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.lista_balas_laser = arcade.SpriteList()
        self.lista_balas_gas = arcade.SpriteList()
        # Create the player
        self.jugador = Jugador.Jugador()  # OJO!
        self.jugador.center_x = 350
        self.jugador.center_y = 350
        self.player_list.append(self.jugador)
        self.buffs_activos = [False, False, False, False,
                              False]  # True en la posicion 0: buff1 activo; True en la posicion 1: buff2 activo, etc
        # Los ponemos en el setup tambien para cuando hagamos el reinicio se inicien correctamente:
        self.recogido_buff1 = False
        self.recogido_buff2 = False
        self.recogido_buff3 = False
        self.recogido_buff4 = False
        self.recogido_buff5 = False
        self.velocidad_jugador = 4
        self.vida_jugador = 10
        self.carga_fantasmal_jugador = 100
        self.contador_quitar_mensaje = 600  # 10s

        # Musica reset
        self.musica_prision_activa = False
        self.musica_ruinas_activa = False
        self.musica_lab_activa = False

        # Rooms
        self.cambiado = False
        self.rooms = Habitaciones.setup_habs()  # lista de todas las habitaciones
        self.current_room = 0  # habitacion inicial (cambiar a 0)/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

        # Fisicas para la habitacion en la que estemos
        self.physics_engine = arcade.PhysicsEngineSimple(self.jugador, self.rooms[self.current_room].wall_list)
        for enemigos in self.rooms[self.current_room].enemigos_list:
            self.physics_engine_enemigos = arcade.PhysicsEngineSimple(enemigos, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        arcade.start_render()
        if self.empezado:
            if self.pausado:
                HUD.dibujar_hud_pausado(self.buffs_activos)
            elif self.jugador.muerto:
                HUD.dibujar_hud_gameover()
            else:
                # Draw the background texture
                arcade.draw_lrwh_rectangle_textured(0, 0,
                                                    SCREEN_WIDTH, SCREEN_HEIGHT,
                                                    self.rooms[self.current_room].background)
                HUD.dibujar_hud(self.vida_jugador, self.carga_fantasmal_jugador)
                if self.jugador.estado_fantasmal:
                    HUD.dibujar_contador_de_muerte(self.jugador.contador_de_muerte)
                self.rooms[self.current_room].wall_list.draw()
                self.player_list.draw()
                self.bullet_list.draw()
                self.lista_balas_laser.draw()
                self.lista_balas_gas.draw()
                # Mostramos mensajes relacionados con los buffs que vayamos cogiendo
                if self.recogido_buff1:
                    HUD.mostrar_mensaje_buff(1)
                    if self.contador_quitar_mensaje == 0:
                        self.recogido_buff1 = False
                        self.contador_quitar_mensaje = 600
                    else:
                        self.contador_quitar_mensaje -= 1
                elif self.recogido_buff2:
                    HUD.mostrar_mensaje_buff(2)
                    if self.contador_quitar_mensaje == 0:
                        self.recogido_buff2 = False
                        self.contador_quitar_mensaje = 600
                    else:
                        self.contador_quitar_mensaje -= 1
                elif self.recogido_buff3:
                    HUD.mostrar_mensaje_buff(3)
                    if self.contador_quitar_mensaje == 0:
                        self.recogido_buff3 = False
                        self.contador_quitar_mensaje = 600
                    else:
                        self.contador_quitar_mensaje -= 1
                elif self.recogido_buff4:
                    HUD.mostrar_mensaje_buff(4)
                    if self.contador_quitar_mensaje == 0:
                        self.recogido_buff4 = False
                        self.contador_quitar_mensaje = 600
                    else:
                        self.contador_quitar_mensaje -= 1
                elif self.recogido_buff5:
                    HUD.mostrar_mensaje_buff(5)
                    if self.contador_quitar_mensaje == 0:
                        self.recogido_buff5 = False
                        self.contador_quitar_mensaje = 600
                    else:
                        self.contador_quitar_mensaje -= 1

                self.rooms[self.current_room].recargas_list.draw()
                if self.rooms[self.current_room].buffs_list is not None:
                    self.rooms[self.current_room].buffs_list.draw()
                HUD.dibujar_partes_artefacto(self.buffs_activos)
                self.rooms[self.current_room].enemigos_list.draw()
                self.rooms[self.current_room].balas_list.draw()

        else:
            if self.mirando_controles:
                HUD.dibujar_controles()
            else:
                HUD.dibujar_pantalla_de_inicio()

    def on_update(self, delta_time: float = 1 / 60):
        if not self.pausado or self.jugador.muerto:
            # Actualizar todos los sprites
            self.physics_engine.update()
            if len(self.rooms[self.current_room].enemigos_list) > 0:
                self.physics_engine_enemigos.update()
            self.jugador.update_animation()
            self.bullet_list.update()
            self.lista_balas_laser.update()
            self.lista_balas_gas.update()

            # Si estamos en modo fantasmal y matamos a todos los enemigos de la sala
            # --> reset de modo fantasmal (quitar buffs y demás)
            if len(self.rooms[self.current_room].enemigos_list) == 0 and self.jugador.estado_fantasmal:
                self.vida_jugador = 10
                self.jugador.desactivar_modo_fantasmal()
                # Quitamos los buffs
                if self.buffs_activos[1]:  # si tenemos el buff de velocidad activo
                    self.velocidad_jugador /= 1.5
            # Si estamos en modo fantasamal y nos quedamos sin tiempo
            # --> game over
            if self.jugador.contador_de_muerte <= 0 and self.jugador.estado_fantasmal:
                # menor o igual que cero porque si ponemos igual a 0 puede que los updates no estén sincronizados
                # y nunca entremos a este if
                self.jugador.morir()
                return
            # Activar modo fantsamal (si podemos)
            if self.vida_jugador == 0 and not self.jugador.estado_fantasmal:
                if self.carga_fantasmal_jugador >= 100:  # Aplicamos buffs modo fant.
                    self.jugador.activar_modo_fantasmal()
                    self.carga_fantasmal_jugador -= 100
                    # Buffs
                    if self.buffs_activos[1]:  # si tenemos el buff de velocidad activo
                        self.velocidad_jugador *= 1.5
                else:  # morimos
                    self.jugador.morir()
                    return

            # Mirar en que habitación estamos y si necesitamos cambiar a otra
            if len(self.rooms[self.current_room].enemigos_list) == 0:
                self.current_room, self.jugador.center_x, self.jugador.center_y, self.cambiado, self.cambiado_piso = \
                    Habitaciones.check_cambio_habitacion(self.current_room, self.jugador.center_x,
                                                         self.jugador.center_y)
                if self.cambiado:
                    self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                                     self.rooms[self.current_room].wall_list)
                    for enemigos in self.rooms[self.current_room].enemigos_list:
                        self.physics_engine_enemigos = arcade.PhysicsEngineSimple(enemigos, self.rooms[
                            self.current_room].wall_list)
                    self.bullet_list = arcade.SpriteList()
                    if self.cambiado_piso:
                        self.sonido_cambio_piso.play()
                    self.lista_balas_laser = arcade.SpriteList()
                    self.lista_balas_gas = arcade.SpriteList()
            else:
                # Límites para que el jugador no salga de la habitación mientras haya enemigos
                if self.jugador.center_x < 125:
                    self.jugador.center_x = 135
                elif self.jugador.center_x > 775:
                    self.jugador.center_x = 765
                elif self.jugador.center_y > 775:
                    self.jugador.center_y = 765
                elif self.jugador.center_y < 125:
                    self.jugador.center_y = 135

            # Limites para cuando el jugador cambia de piso o va a la sala del boss
            if self.current_room == 7 or self.current_room == 22 or self.current_room == 68:
                if self.jugador.center_y < 125:
                    self.jugador.center_y = 135

            # Actualizar balas jugador
            # Loop through each bullet
            for bala in self.bullet_list:
                # Mirar si ha chocado con una pared
                hit_list = arcade.check_for_collision_with_list(bala, self.rooms[self.current_room].wall_list)
                # Si choca contra una pared, eliminar la bala
                if len(hit_list) > 0:
                    bala.remove_from_sprite_lists()
                # Mirar si choca contra un enemigo
                hit_list2 = arcade.check_for_collision_with_list(bala, self.rooms[self.current_room].enemigos_list)
                if len(hit_list2) > 0:
                    # Vamos a identificar el enemigo que ha sido golpeado:
                    for enemigo in self.rooms[self.current_room].enemigos_list:
                        if enemigo in hit_list2:
                            if self.buffs_activos[4]:
                                enemigo.recibir_damage(2)
                            else:
                                enemigo.recibir_damage(1)
                            # Muerte de enemigos
                            if enemigo.vida <= 0:
                                # (por si les hacemos más daño de la vida que tienen y se queda con vida negativa)
                                # Dropeos
                                n = random.randint(0, 10)
                                if n == 10:  # 10 % de drop
                                    # Dropeo exitoso:
                                    recarga = arcade.Sprite("sprites_master" + os.path.sep + "alma.png")
                                    recarga.center_x = enemigo.center_x
                                    recarga.center_y = enemigo.center_y
                                    self.rooms[self.current_room].recargas_list.append(recarga)

                                # Eliminamos al enemigo sin vida
                                enemigo.remove_from_sprite_lists()

                    bala.remove_from_sprite_lists()
            for laser in self.lista_balas_laser:
                hit_list = arcade.check_for_collision_with_list(laser, self.rooms[self.current_room].wall_list)
                if len(hit_list) > 0:
                    laser.remove_from_sprite_lists()
                hit_list2 = arcade.check_for_collision_with_list(laser,self.player_list)
                if len(hit_list2) > 0:
                    laser.remove_from_sprite_lists()
                    self.vida_jugador -=2

            for gas in self.lista_balas_gas:
                hit_list = arcade.check_for_collision_with_list(gas, self.rooms[self.current_room].wall_list)
                if len(hit_list) > 0:
                    gas.remove_from_sprite_lists()
                hit_list2 = arcade.check_for_collision_with_list(gas, self.player_list)
                if len(hit_list2) > 0:
                    gas.remove_from_sprite_lists()
                    self.vida_jugador -=2

            hit_list_enemigos = arcade.check_for_collision_with_list(self.jugador,
                                                                     self.rooms[self.current_room].enemigos_list)

            if len(hit_list_enemigos) > 0:

                    self.vida_jugador -= 0.25

            for enemigos in self.rooms[self.current_room].enemigos_list:
                enemigos.update_animation()
                enemigos.follow_sprite(self.jugador, self.velocidad_enemigos)
                enemigos.atacar(enemigos, self.velocidad_disparo_enemigos, self.jugador, self.lista_balas_laser, self.lista_balas_gas)



            # Mirar si hemos cogido alguna recarga
            hit_list3 = arcade.check_for_collision_with_list(self.jugador, self.rooms[self.current_room].recargas_list)
            for recarga in hit_list3:
                recarga.remove_from_sprite_lists()
                self.carga_fantasmal_jugador += 100

            # Mirar si hemos recogido algun buff y aplicarlo
            if self.rooms[self.current_room].buffs_list is not None:
                hit_list4 = arcade.check_for_collision_with_list(self.jugador, self.rooms[self.current_room].buffs_list)
                for buff in self.rooms[self.current_room].buffs_list:
                    if buff in hit_list4:
                        buff.remove_from_sprite_lists()
                        if self.current_room == 0:  # hemos cogido el buff de habilitar modo fantasmal
                            self.recogido_buff1 = True
                            self.buffs_activos[0] = True
                        if self.current_room == 6:  # hemos cogido el buff de x2 vel en modo fant.
                            self.recogido_buff2 = True
                            self.buffs_activos[1] = True
                        if self.current_room == 14:  # hemos cogido el buff de triple disparo en modo fantasmal
                            self.recogido_buff3 = True
                            self.buffs_activos[2] = True
                        if self.current_room == 20:  # hemos cogido el buff de velocidad por 1.2
                            self.recogido_buff4 = True
                            self.buffs_activos[3] = True
                            self.velocidad_jugador *= 1.2  # aplicamos el buff permanente durante toda la partida
                        if self.current_room == 67:  # hemos cogido el buff de daño doble
                            self.recogido_buff5 = True
                            self.buffs_activos[4] = True
            # Actualizar la música de fondo
            if self.current_room <= 6 and not self.musica_prision_activa:
                self.musica_prision_activa = True
            elif 7 <= self.current_room <= 21 and not self.musica_ruinas_activa:
                arcade.play_sound(self.musica_ruinas)
                self.musica_ruinas_activa = True
            elif 22 <= self.current_room <= 67 and not self.musica_lab_activa:
                arcade.play_sound(self.musica_lab)
                self.musica_lab_activa = True

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # Comienzo del juego
        if not self.empezado:
            if key == arcade.key.ENTER:
                self.empezado = True
            elif key == arcade.key.C:
                self.mirando_controles = True
            elif key == arcade.key.BACKSPACE:
                self.mirando_controles = False
            return  # no necesitamos comprbar más controles
        if self.jugador.muerto:
            # Reiniciar el juego desde el principio:
            if key == arcade.key.R:  # Potencialmente puede dar problemas más adelante!!! REVISAR /\/\/\/\/\/\/\/\/\/\
                self.setup()
                self.jugador.muerto = False
                self.jugador.estado_fantasmal = False  # por si morimos en modo fontasmal
        # Pausar el juego
        if key == arcade.key.P and not self.pausado:
            self.pausado = True
        elif key == arcade.key.P and self.pausado:
            self.pausado = False
        # Movimiento
        if key == arcade.key.UP or key == arcade.key.W:
            self.jugador.change_y = self.velocidad_jugador
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.jugador.change_y = -self.velocidad_jugador
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.jugador.change_x = -self.velocidad_jugador
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.jugador.change_x = self.velocidad_jugador
        # Disparo
        if key == arcade.key.Q:
            if self.jugador.estado_fantasmal and self.buffs_activos[2]:  # disparo triple en modo fantasmal
                # Creamos las 3 balas
                bala = self.jugador.disparar(self.jugador, self.velocidad_disparo)
                self.bullet_list.append(bala)
                bala = self.jugador.disparar(self.jugador, self.velocidad_disparo, True)
                self.bullet_list.append(bala)
                bala = self.jugador.disparar(self.jugador, self.velocidad_disparo, False, True)
                self.bullet_list.append(bala)
            else:
                bala = self.jugador.disparar(self.jugador, self.velocidad_disparo)
                self.bullet_list.append(bala)
        # Bloquear direccion a la que mira el personaje (hay que mantener)
        if key == arcade.key.SPACE:
            self.jugador.bloquear_direccion()
        # Hacerse daño a sí mismo (PROVISIONAL, PARA PRUEBAS)/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
        if key == arcade.key.Z:
            self.vida_jugador -= 5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.jugador.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.jugador.change_x = 0
        # Desbloquear direccion a la que mira el personaje
        if key == arcade.key.SPACE:
            self.jugador.desbloquear_direccion()


def main():
    ventana = PhantomGear()
    ventana.setup()
    arcade.run()


if __name__ == "__main__":
    main()
