import arcade
import os
import Enemigos

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900


class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # Todas las listas de las habitaciones
        self.wall_list = None
        self.background = None
        self.enemigos_list = None
        self.balas_list = None
        self.recargas_list = None
        self.buffs_list = None


def setup_room_p1():
    """Crea y devuelve la habitacion prision 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()
    room.buffs_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y OBJETOS")
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION6.png")

    # Buffs
    buff = arcade.Sprite("sprites_master" + os.path.sep + "PARTE1.png")
    buff.center_x = 750
    buff.center_y = 450
    room.buffs_list.append(buff)

    esqueleto1 = Enemigos.Skeleton()
    esqueleto1.center_y = 300
    esqueleto1.center_x = 700
    room.enemigos_list.append(esqueleto1)

    # Definir muros
    room.wall_list = obstaculos
    return room


def setup_room_p2():
    """Crea y devuelve la habitacion prision 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION2.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION2.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p3():
    """Crea y devuelve la habitacion prision 3"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p4():
    """Crea y devuelve la habitacion prision 4"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION4.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p5():
    """Crea y devuelve la habitacion prision 5"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION8.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION8.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p6():
    """Crea y devuelve la habitacion prision 6"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION7.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION7.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_p7():
    """Crea y devuelve la habitacion prision 7
    Cambio de piso a las ruinas"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()
    room.buffs_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION1.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION1.png")

    # Buffs
    buff = arcade.Sprite("sprites_master" + os.path.sep + "PARTE3.png")
    buff.center_x = 450
    buff.center_y = 250
    room.buffs_list.append(buff)

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r1():
    """Crea y devuelve la habitacion ruinas 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS11.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r2():
    """Crea y devuelve la habitacion ruinas 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS1.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS1.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r3():
    """Crea y devuelve la habitacion ruinas 3"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r4():
    """Crea y devuelve la habitacion ruinas 4"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS15.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS15.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r5():
    """Crea y devuelve la habitacion ruinas 5"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS1.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS1.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r6():
    """Crea y devuelve la habitacion ruinas 6"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS12.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r7():
    """Crea y devuelve la habitacion ruinas 7"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS2.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS2.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r8():
    """Crea y devuelve la habitacion ruinas 8
    Cambio de piso al laboratorio"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()
    room.buffs_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS13.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS13.png")

    # Buffs
    buff = arcade.Sprite("sprites_master" + os.path.sep + "PARTE2.png")
    buff.center_x = 450
    buff.center_y = 250
    room.buffs_list.append(buff)

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r9():
    """Crea y devuelve la habitacion ruinas 9"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS14.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r10():
    """Crea y devuelve la habitacion ruinas 10"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS4.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r11():
    """Crea y devuelve la habitacion ruinas 11"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS2.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS2.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r12():
    """Crea y devuelve la habitacion ruinas 12"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r13():
    """Crea y devuelve la habitacion ruinas 13"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r14():
    """Crea y devuelve la habitacion ruinas 14"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()
    room.buffs_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS14.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS14.png")

    # Buffs
    buff = arcade.Sprite("sprites_master" + os.path.sep + "MOVIMIENTOPOWERUP.png")
    buff.center_x = 450
    buff.center_y = 250
    room.buffs_list.append(buff)

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_r15():
    """Crea y devuelve la habitacion ruinas 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS4.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l1():
    """Crea y devuelve la habitacion laboratorio 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB10M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB10.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l2():
    """Crea y devuelve la habitacion laboratorio 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l3():
    """Crea y devuelve la habitacion laboratorio 3"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l4():
    """Crea y devuelve la habitacion laboratorio 4"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB14M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l5():
    """Crea y devuelve la habitacion laboratorio 5"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l6():
    """Crea y devuelve la habitacion laboratorio 6"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l7():
    """Crea y devuelve la habitacion laboratorio 7"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l8():
    """Crea y devuelve la habitacion laboratorio 8"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l9():
    """Crea y devuelve la habitacion laboratorio 9"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l10():
    """Crea y devuelve la habitacion laboratorio 10"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l11():
    """Crea y devuelve la habitacion laboratorio 11"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l12():
    """Crea y devuelve la habitacion laboratorio 12"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB12M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l13():
    """Crea y devuelve la habitacion laboratorio 13"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB9.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l14():
    """Crea y devuelve la habitacion laboratorio 14"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l15():
    """Crea y devuelve la habitacion laboratorio 15"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l16():
    """Crea y devuelve la habitacion laboratorio 16"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB10M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB10.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l17():
    """Crea y devuelve la habitacion laboratorio 17"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB13.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB13.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l18():
    """Crea y devuelve la habitacion laboratorio 18"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l19():
    """Crea y devuelve la habitacion laboratorio 19"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB12M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l20():
    """Crea y devuelve la habitacion laboratorio 20"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l21():
    """Crea y devuelve la habitacion laboratorio 21"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l22():
    """Crea y devuelve la habitacion laboratorio 22"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l23():
    """Crea y devuelve la habitacion laboratorio 23"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB9M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB9.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l24():
    """Crea y devuelve la habitacion laboratorio 24"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l25():
    """Crea y devuelve la habitacion laboratorio 25"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l26():
    """Crea y devuelve la habitacion laboratorio 26"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB7M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB7.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l27():
    """Crea y devuelve la habitacion laboratorio 27"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB14M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l28():
    """Crea y devuelve la habitacion laboratorio 28"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l29():
    """Crea y devuelve la habitacion laboratorio 29"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB15M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB15.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l30():
    """Crea y devuelve la habitacion laboratorio 30"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l31():
    """Crea y devuelve la habitacion laboratorio 31"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l32():
    """Crea y devuelve la habitacion laboratorio 32"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB7M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB7.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l33():
    """Crea y devuelve la habitacion laboratorio 33"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB3.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB3.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l34():
    """Crea y devuelve la habitacion laboratorio 34"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l35():
    """Crea y devuelve la habitacion laboratorio 35"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB14M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB14.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l36():
    """Crea y devuelve la habitacion laboratorio 36"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l37():
    """"Crea y devuelve la habitacion laboratorio 37"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB13.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB13.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l38():
    """Crea y devuelve la habitacion laboratorio 38"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l39():
    """Crea y devuelve la habitacion laboratorio 39"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l40():
    """Crea y devuelve la habitacion laboratorio 40"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l41():
    """Crea y devuelve la habitacion laboratorio 41"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB6.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB6.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l42():
    """Crea y devuelve la habitacion laboratorio 42"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB12M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB12.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l43():
    """Crea y devuelve la habitacion laboratorio 43"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l44():
    """Crea y devuelve la habitacion laboratorio 44"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB5M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB5.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l45():
    """Crea y devuelve la habitacion laboratorio 45"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB11M.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB11.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_l46():
    """Crea y devuelve la habitacion laboratorio 46"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()
    room.buffs_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LAB4.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB4.png")

    # Buffs
    buff = arcade.Sprite("sprites_master" + os.path.sep + "BALASPOWERUP.png")
    buff.center_x = 700
    buff.center_y = 700
    room.buffs_list.append(buff)

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_room_lboss():
    """Crea y devuelve la habitacion laboratorio donde está el boss"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()
    room.recargas_list = arcade.SpriteList()

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "LABSALAFINAL.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "OBJETOS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "LAB1.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


def setup_habs():
    # Prision: (0-6)
    rooms = []
    room = setup_room_p1()
    rooms.append(room)
    room = setup_room_p2()
    rooms.append(room)
    room = setup_room_p3()
    rooms.append(room)
    room = setup_room_p4()
    rooms.append(room)
    room = setup_room_p5()
    rooms.append(room)
    room = setup_room_p6()
    rooms.append(room)
    room = setup_room_p7()
    rooms.append(room)
    # Ruinas: (7-21)
    room = setup_room_r1()
    rooms.append(room)
    room = setup_room_r2()
    rooms.append(room)
    room = setup_room_r3()
    rooms.append(room)
    room = setup_room_r4()
    rooms.append(room)
    room = setup_room_r5()
    rooms.append(room)
    room = setup_room_r6()
    rooms.append(room)
    room = setup_room_r7()
    rooms.append(room)
    room = setup_room_r8()
    rooms.append(room)
    room = setup_room_r9()
    rooms.append(room)
    room = setup_room_r10()
    rooms.append(room)
    room = setup_room_r11()
    rooms.append(room)
    room = setup_room_r12()
    rooms.append(room)
    room = setup_room_r13()
    rooms.append(room)
    room = setup_room_r14()
    rooms.append(room)
    room = setup_room_r15()
    rooms.append(room)
    # Laboratorio (22-boss final)
    room = setup_room_l1()  # 22
    rooms.append(room)
    room = setup_room_l2()  # 23
    rooms.append(room)
    room = setup_room_l3()
    rooms.append(room)
    room = setup_room_l4()
    rooms.append(room)
    room = setup_room_l5()
    rooms.append(room)
    room = setup_room_l6()
    rooms.append(room)
    room = setup_room_l7()
    rooms.append(room)
    room = setup_room_l8()
    rooms.append(room)
    room = setup_room_l9()  # 30
    rooms.append(room)
    room = setup_room_l10()  # 31
    rooms.append(room)
    room = setup_room_l11()
    rooms.append(room)
    room = setup_room_l12()
    rooms.append(room)
    room = setup_room_l13()
    rooms.append(room)
    room = setup_room_l14()
    rooms.append(room)
    room = setup_room_l15()
    rooms.append(room)
    room = setup_room_l16()
    rooms.append(room)
    room = setup_room_l17()
    rooms.append(room)
    room = setup_room_l18()  # 39
    rooms.append(room)
    room = setup_room_l19()  # 40
    rooms.append(room)
    room = setup_room_l20()  # 41
    rooms.append(room)
    room = setup_room_l21()  # 42
    rooms.append(room)
    room = setup_room_l22()
    rooms.append(room)
    room = setup_room_l23()
    rooms.append(room)
    room = setup_room_l24()
    rooms.append(room)
    room = setup_room_l25()
    rooms.append(room)
    room = setup_room_l26()
    rooms.append(room)
    room = setup_room_l27()
    rooms.append(room)
    room = setup_room_l28()  # 49
    rooms.append(room)
    room = setup_room_l29()  # 50
    rooms.append(room)
    room = setup_room_l30()  # 51
    rooms.append(room)
    room = setup_room_l31()  # 52
    rooms.append(room)
    room = setup_room_l32()  # 53
    rooms.append(room)
    room = setup_room_l33()
    rooms.append(room)
    room = setup_room_l34()
    rooms.append(room)
    room = setup_room_l35()
    rooms.append(room)
    room = setup_room_l36()
    rooms.append(room)
    room = setup_room_l37()
    rooms.append(room)
    room = setup_room_l38()
    rooms.append(room)
    room = setup_room_l39()
    rooms.append(room)
    room = setup_room_l40()
    rooms.append(room)
    room = setup_room_l41()
    rooms.append(room)
    room = setup_room_l42()
    rooms.append(room)
    room = setup_room_l43()
    rooms.append(room)
    room = setup_room_l44()
    rooms.append(room)
    room = setup_room_l45()
    rooms.append(room)
    room = setup_room_l46()
    rooms.append(room)
    room = setup_room_lboss()
    rooms.append(room)
    return rooms


def check_cambio_habitacion(current_room, jugador_x, jugador_y):
    # Prision: (0-6)
    cambiado = True
    if jugador_x > SCREEN_WIDTH - 90 and current_room == 0:  # 0-->1
        current_room = 1
        jugador_x = 100

    elif jugador_x < 90 and current_room == 1:  # 1-->0
        current_room = 0
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 1:  # 1-->2
        current_room = 2
        jugador_x = 100

    elif jugador_x < 90 and current_room == 2:  # 2-->1
        current_room = 1
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 2:  # 2-->3
        current_room = 3
        jugador_y = 100

    elif jugador_y < 90 and current_room == 3:  # 3-->2
        current_room = 2
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y < 90 and current_room == 2:  # 2-->4
        current_room = 4
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 4:  # 4-->2
        current_room = 2
        jugador_y = 100

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 4:  # 4-->5
        current_room = 5
        jugador_x = 100

    elif jugador_x < 90 and current_room == 5:  # 5-->4
        current_room = 4
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_y < 90 and current_room == 4:  # 4-->6
        current_room = 6
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 6:  # 6-->4
        current_room = 4
        jugador_y = 100

    elif jugador_y < 90 and current_room == 6:  # 6-->Ruinas 7(r1)
        current_room = 7
        jugador_y = 200  # emepzamos por la parte de abajo la primera sala de ruinas


    # Ruinas: (7-21)
    # Ruta principal:
    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 7:  # 7(r1)-->8(r2)
        current_room = 8
        jugador_y = 100

    elif jugador_y < 90 and current_room == 8:  # 8(r2)-->7(r1)
        current_room = 7
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 8:  # 8(r2)-->9(r3)
        current_room = 9
        jugador_y = 100

    elif jugador_y < 90 and current_room == 9:  # 9(r3)-->8(r2)
        current_room = 8
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 9:  # 9(r3)-->10(r4)
        current_room = 10
        jugador_x = 100

    elif jugador_x < 90 and current_room == 10:  # 10(r4)-->9(r3)
        current_room = 9
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 10:  # 10(r4)-->11(r5)
        current_room = 11
        jugador_y = 100

    elif jugador_y < 90 and current_room == 11:  # 11(r5)-->10(r4)
        current_room = 10
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 11:  # 11(r5)-->12(r6)
        current_room = 12
        jugador_y = 100

    elif jugador_y < 90 and current_room == 12:  # 12(r6)-->11(r5)
        current_room = 11
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 12:  # 12(r6)-->13(r7)
        current_room = 13
        jugador_x = 100

    elif jugador_x < 90 and current_room == 13:  # 13(r7)-->12(r6)
        current_room = 12
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 13:  # 13(r7)-->14(r8)
        current_room = 14
        jugador_x = 100

    elif jugador_x < 90 and current_room == 14:  # 14(r8)-->13(r7)
        current_room = 13
        jugador_x = SCREEN_WIDTH - 110

    # Desvío R3
    elif jugador_x < 90 and current_room == 9:  # 9(r3)-->15(r9)
        current_room = 15
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 15:  # 15(r9)-->9(r3)
        current_room = 9
        jugador_x = 100

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 15:  # 15(r9)-->16(r10)
        current_room = 16
        jugador_y = 100

    elif jugador_y < 90 and current_room == 16:  # 16(r10)-->15(r9)
        current_room = 15
        jugador_y = SCREEN_HEIGHT - 110

    # Desvío R1
    elif jugador_x < 90 and current_room == 7:  # 7(r1)-->17(r11)
        current_room = 17
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 17:  # 17(r11)-->7(r1)
        current_room = 7
        jugador_x = 100

    elif jugador_x < 90 and current_room == 17:  # 17(r11)-->18(r12)
        current_room = 18
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 18:  # 18(r12)-->17(r11)
        current_room = 17
        jugador_x = 100

    elif jugador_y < 90 and current_room == 18:  # 18(r12)-->19(r13)
        current_room = 19
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 19:  # 19(r13)-->18(r12)
        current_room = 18
        jugador_y = 100

    elif jugador_x < 90 and current_room == 18:  # 18(r12)-->20(r14)
        current_room = 20
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 20:  # 20(r14)-->18(r12)
        current_room = 18
        jugador_x = 100

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 20:  # 20(r14)-->21(r15)
        current_room = 21
        jugador_y = 100

    elif jugador_y < 90 and current_room == 21:  # 21(r15)-->20(r14)
        current_room = 20
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y < 90 and current_room == 14:  # 14(r8)-->22(l1)
        current_room = 22
        jugador_y = 300


    # Laboratorio:

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 22:  # 22(l1)-->23(l2)
        current_room = 23
        jugador_y = 100

    elif jugador_y < 90 and current_room == 23:  # 23(l2)-->22(l1)
        current_room = 22
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 23:  # 23(l2)-->24(l3)
        current_room = 24
        jugador_y = 100

    elif jugador_y < 90 and current_room == 24:  # 24(l3)-->23(l2)
        current_room = 23
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 24:  # 24(l3)-->25(l4)
        current_room = 25
        jugador_y = 100

    elif jugador_y < 90 and current_room == 25:  # 25(l4)-->24(l3)
        current_room = 24
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 25:  # 25(l4)-->26(l5)
        current_room = 26
        jugador_x = 100

    elif jugador_x < 90 and current_room == 26:  # 26(l5)-->25(l4)
        current_room = 25
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 26:  # 26(l5)-->27(l6)
        current_room = 27
        jugador_x = 100

    elif jugador_x < 90 and current_room == 27:  # 27(l6)-->26(l5)
        current_room = 26
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 27:  # 27(l6)-->28(l7)
        current_room = 28
        jugador_x = 100

    elif jugador_x < 90 and current_room == 28:  # 28(l7)-->27(l6)
        current_room = 27
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 28:  # 28(l7)-->29(l8)
        current_room = 29
        jugador_x = 100

    elif jugador_x < 90 and current_room == 29:  # 29(l8)-->28(l7)
        current_room = 28
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 29:  # 29(l8)-->30(l9)
        current_room = 30
        jugador_x = 100

    elif jugador_x < 90 and current_room == 30:  # 30(l9)-->29(l8)
        current_room = 29
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_y < 90 and current_room == 28:  # 28(l7)-->31(l10)
        current_room = 31
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 31:  # 31(l10)-->28(l7)
        current_room = 28
        jugador_y = 100

    elif jugador_y < 90 and current_room == 31:  # 31(l10)-->32(l11)
        current_room = 32
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 32:  # 32(l11)-->31(l10)
        current_room = 31
        jugador_y = 100

    elif jugador_y < 90 and current_room == 32:  # 32(l11)-->33(l12)
        current_room = 33
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 33:  # 33(l12)-->32(l11)
        current_room = 32
        jugador_y = 100

    elif jugador_x < 90 and current_room == 33:  # 33(l12)-->34(l13)
        current_room = 34
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 34:  # 34(l13)-->33(l12)
        current_room = 33
        jugador_x = 100

    elif jugador_x < 90 and current_room == 34:  # 34(l13)-->35(l14)
        current_room = 35
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 35:  # 35(l14)-->34(l13)
        current_room = 34
        jugador_x = 100

    elif jugador_x < 90 and current_room == 35:  # 35(l14)-->22(l1)
        current_room = 22
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 22:  # 22(l1)-->35(l14)
        current_room = 35
        jugador_x = 100

    elif jugador_y < 90 and current_room == 34:  # 34(l13)-->36(l15)
        current_room = 36
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 36:  # 36(l15)-->34(l13)
        current_room = 34
        jugador_y = 100

    elif jugador_y < 90 and current_room == 36:  # 36(l15)-->37(l16)
        current_room = 37
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 37:  # 37(l16)-->36(l15)
        current_room = 36
        jugador_y = 100

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 37:  # 37(l16)-->38(l17)
        current_room = 38
        jugador_x = 100

    elif jugador_x < 90 and current_room == 38:  # 38(l17)-->37(l16)
        current_room = 37
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_y < 90 and current_room == 38:  # 38(l17)-->39(l18)
        current_room = 39
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 39:  # 39(l18)-->38(l17)
        current_room = 38
        jugador_y = 100

    elif jugador_y < 90 and current_room == 39:  # 39(l18)-->40(l19)
        current_room = 40
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 40:  # 40(l19)-->39(l18)
        current_room = 39
        jugador_y = 100

    elif jugador_x < 90 and current_room == 40:  # 40(l19)-->41(l20)
        current_room = 41
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 41:  # 41(l20)-->40(l19)
        current_room = 40
        jugador_x = 100

    elif jugador_x < 90 and current_room == 41:  # 41(l20)-->42(l21)
        current_room = 42
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 42:  # 42(l21)-->41(l20)
        current_room = 41
        jugador_x = 100

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 42:  # 42(l21)-->43(l22)
        current_room = 43
        jugador_y = 100

    elif jugador_y < 90 and current_room == 43:  # 43(l22)-->42(l21)
        current_room = 42
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 43:  # 43(l22)-->44(l23)
        current_room = 44
        jugador_y = 100

    elif jugador_y < 90 and current_room == 44:  # 44(l23)-->43(l22)
        current_room = 43
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_x < 90 and current_room == 44:  # 44(l23)-->45(l24)
        current_room = 45
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 45:  # 45(l24)-->44(l23)
        current_room = 44
        jugador_x = 100

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 44:  # 44(l23)-->37(l16)
        current_room = 37
        jugador_x = 100

    elif jugador_x < 90 and current_room == 37:  # 37(l16)-->44(l23)
        current_room = 44
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x < 90 and current_room == 45:  # 45(l24)-->46(l25)
        current_room = 46
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 46:  # 46(l25)-->45(l24)
        current_room = 45
        jugador_x = 100

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 46:  # 46(l25)-->47(l26)
        current_room = 47
        jugador_y = 100

    elif jugador_y < 90 and current_room == 47:  # 47(l26)-->46(l25)
        current_room = 46
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 47:  # 47(l26)-->48(l27)
        current_room = 48
        jugador_y = 100

    elif jugador_y < 90 and current_room == 48:  # 48(l27)-->47(l26)
        current_room = 47
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 48:  # 48(l27)-->22(l1)
        current_room = 22
        jugador_x = 100

    elif jugador_x < 90 and current_room == 22:  # 22(l1)-->48(l27)
        current_room = 48
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x < 90 and current_room == 47:  # 47(l26)-->49(l28)
        current_room = 49
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 49:  # 49(l28)-->47(l26)
        current_room = 47
        jugador_x = 100

    elif jugador_x < 90 and current_room == 49:  # 49(l28)-->50(l29)
        current_room = 50
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 50:  # 50(l29)-->49(l28)
        current_room = 49
        jugador_x = 100

    elif jugador_x < 90 and current_room == 50:  # 50(l29)-->51(l30)
        current_room = 51
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 51:  # 51(l30)-->50(l29)
        current_room = 50
        jugador_x = 100

    elif jugador_x < 90 and current_room == 51:  # 51(l30)-->52(l31)
        current_room = 52
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 52:  # 52(l31)-->51(l30)
        current_room = 51
        jugador_x = 100

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 52:  # 52(l31)-->53(l32)
        current_room = 53
        jugador_y = 100

    elif jugador_y < 90 and current_room == 53:  # 53(l32)-->52(l31)
        current_room = 52
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_x < 90 and current_room == 53:  # 53(l32)-->54(l33)
        current_room = 54
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 54:  # 54(l33)-->53(l32)
        current_room = 53
        jugador_x = 100

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 53:  # 53(l32)-->55(l34)
        current_room = 55
        jugador_y = 100

    elif jugador_y < 90 and current_room == 55:  # 55(l34)-->53(l32)
        current_room = 53
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 55:  # 55(l34)-->56(l35)
        current_room = 56
        jugador_y = 100

    elif jugador_y < 90 and current_room == 56:  # 56(l35)-->55(l34)
        current_room = 55
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 56:  # 56(l35)-->57(l36)
        current_room = 57
        jugador_x = 100

    elif jugador_x < 90 and current_room == 57:  # 57(l36)-->56(l35)
        current_room = 56
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 57:  # 57(l36)-->58(l37)
        current_room = 58
        jugador_x = 100

    elif jugador_x < 90 and current_room == 58:  # 58(l37)-->57(l36)
        current_room = 57
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_y < 90 and current_room == 58:  # 58(l37)-->59(l38)
        current_room = 59
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 59:  # 59(l38)-->58(l37)
        current_room = 58
        jugador_y = 100

    elif jugador_y < 90 and current_room == 59:  # 59(l38)-->60(l39)
        current_room = 60
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 60:  # 60(l39)-->59(l38)
        current_room = 59
        jugador_y = 100

    elif jugador_y < 90 and current_room == 60:  # 60(l39)-->50(l29)
        current_room = 50
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 50:  # 50(l29)-->60(l39)
        current_room = 60
        jugador_y = 100

    elif jugador_y < 90 and current_room == 50:  # 50(l29)-->61(l40)
        current_room = 61
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 61:  # 61(l40)-->50(l29)
        current_room = 50
        jugador_y = 100

    elif jugador_y < 90 and current_room == 61:  # 61(l40)-->62(l41)
        current_room = 62
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 62:  # 62(l41)-->61(l40)
        current_room = 61
        jugador_y = 100

    elif jugador_y < 90 and current_room == 62:  # 62(l41)-->63(l42)
        current_room = 63
        jugador_y = SCREEN_HEIGHT - 110

    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 63:  # 63(l42)-->62(l41)
        current_room = 62
        jugador_y = 100

    elif jugador_x < 90 and current_room == 63:  # 63(l42)-->64(l43)
        current_room = 64
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 64:  # 64(l43)-->63(l42)
        current_room = 63
        jugador_x = 100

    elif jugador_x < 90 and current_room == 64:  # 64(l43)-->65(l44)
        current_room = 65
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 65:  # 65(l44)-->64(l43)
        current_room = 64
        jugador_x = 100

    elif jugador_x < 90 and current_room == 65:  # 65(l44)-->66(l45)
        current_room = 66
        jugador_x = SCREEN_WIDTH - 110

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 66:  # 66(l45)-->65(l44)
        current_room = 65
        jugador_x = 100

    elif jugador_x > SCREEN_WIDTH - 90 and current_room == 30:  # 30(l9)-->67(l46)
        current_room = 67
        jugador_x = 100

    elif jugador_x < 90 and current_room == 67:  # 67(46)-->30(l9)
        current_room = 30
        jugador_x = SCREEN_WIDTH - 110

    # Pasar a la sala del boss final (no se puede volver)
    elif jugador_y > SCREEN_HEIGHT - 90 and current_room == 66:  # 66(l45)-->68(boss)
        current_room = 68
        jugador_y = 100
    else:
        cambiado = False

    return current_room, jugador_x, jugador_y, cambiado
