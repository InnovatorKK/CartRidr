from ursina import *
from ursina.shaders import lit_with_shadows_shader 
import threading
app = Ursina()

gauge = 300
speed = time.time()
direction = ""
start = 0
current_time = 0
spaced = False
cube = Entity(model="cube", collider="mesh", scale=(500, 1, 500), posistion=(0, 0, 0), texture="grass.jpg")
player = Entity(model="car_low.obj", scale=(0.5, 0.5, 0.5), position=(0, 1, 0),shader=lit_with_shadows_shader)
c = Entity(model="cube", scale=(1, 1, 1))
tesla = Entity(model="car_low.obj", scale=(.1, .1, .1), position=(0, 10, 0), shader=lit_with_shadows_shader)

camera.fov = 100
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))


def Gauge():
    global gauge
    gauge -= 1
    
def update():
    global speed, gauge, direction, start, current_time, spaced
    t = threading.Timer(1, Gauge)
    current_time = time.time()
    rotation = player.rotation_y * pi / 180
    camera_rotation = player.rotation_y
    camera.fov = 110
    if held_keys['d']:
        direction="left"
        #if player.rotation_y >= 60:
        #    pass
        #else:
        camera_rotation = player.rotation_y + 10
        player.rotation_y  += 3
        camera.fov = 120
        
    if held_keys['a']:
        direction="right"
        #if player.rotation_y <= -60:
        #    pass
        #else:
        camera_rotation = player.rotation_y - 10
        player.rotation_y  -= 3
        camera.fov = 120
    if held_keys['w']:
        player.z += cos(rotation) * speed
        player.x += sin(rotation) * speed
    if held_keys['s']:
        player.z -= cos(rotation) * speed
        player.x -= sin(rotation) * speed
    
    if held_keys['shift']:
        if direction=="right":
            speed = 0.5
            player.x += 1
            #sdfsdfhsk
        if direction =="left":
            speed = 0.5
            player.x -= 1
    if held_keys['space'] and gauge >= 0:
        invoke(Gauge, delay=0.1)
        speed = 3
    else:
        speed = 1
        spaced = False
    
    if spaced:
        if gauge <= 0:
            ...
        else:
            invoke(Gauge, delay=0.1)
            
    
    
    '''      
    if 0.2 > current_time - start > 0.1:
            gauge -= 1
            start = current_time - 0.01
    '''
    
    print(gauge, spaced)

    tesla.rotation_y += 1
    camera.position = (player.x - 35*sin(rotation), 30, player.z-35 - 35*cos(rotation) +35)
    camera.rotation = (40, camera_rotation, 0)
    
    
    #c.position = (player.x - sin(rotation), 20, player.z-25 - cos(rotation))
    #c.rotation = (40, player.rotation_y, 0)

def input(key):
    global gauge, start
    if key == "space": 
        start = current_time
        
Sky()

app.run()