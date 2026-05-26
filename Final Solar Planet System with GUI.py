from turtle import RawTurtle, TurtleScreen, ScrolledCanvas
import math
import time
import random
from PIL import Image
import tkinter as tk
from functools import partial
import turtle
# ===============================
# 1. Planet Info
# ===============================
planet_info = {
    "Sun": {"Description": "The sun is at the center of our solar system and holds 99.9% of its mass.",
            "Surface Temp": "5,500 °C", "Distance to Earth": "149,600,000 Km",
            "Mass": "199 x 10^30 Kg (333,060 Earths)", "Diameter": "1,392,684 Km"},
    "Mercury": {"Description": "The closest planet to the Sun, covered with impact craters.",
                "Surface Temp": "-180 to 430 °C", "Distance to Sun": "57,910,000 Km",
                "Moons": "0", "Radius": "2,440 Km"},
    "Venus": {"Description": "Named after the Roman goddess of love due to its glowing appearance.",
              "Surface Temp": "460 °C", "Distance to Sun": "108,200,000 Km",
              "Moons": "0", "Radius": "6,052 Km"},
    "Earth": {"Description": "Our home planet, with liquid water and suitable conditions for life.",
              "Surface Temp": "-88 to 58 °C", "Distance to Sun": "149,600,000 Km",
              "Moons": "1", "Radius": "6,371 Km"},
    "Mars": {"Description": "Known as the red planet, with dust storms and ice caps.",
             "Surface Temp": "-125 to 20 °C", "Distance to Sun": "227,900,000 Km",
             "Moons": "2", "Radius": "3,390 Km"},
    "Jupiter": {"Description": "The largest planet, bigger than all others combined.",
                "Surface Temp": "-145 °C", "Distance to Sun": "778,500,000 Km",
                "Moons": "79", "Radius": "69,911 Km"},
    "Saturn": {"Description": "Famous for its beautiful rings made of ice and debris.",
               "Surface Temp": "-178 °C", "Distance to Sun": "1,434,000,000 Km",
               "Moons": "53", "Radius": "58,232 Km"},
    "Uranus": {"Description": "The coldest planet with a unique tilt of 98 degrees.",
               "Surface Temp": "-224 °C", "Distance to Sun": "2,871,000,000 Km",
               "Moons": "27", "Radius": "25,362 Km"},
    "Neptune": {"Description": "The farthest planet, located about 30 AU from Earth.",
                "Surface Temp": "-231 °C", "Distance to Sun": "4,498,000,000 Km",
                "Moons": "14", "Radius": "24,622 Km"}
}

# ===============================
# 2. Tkinter Window & Canvas
# ==============================

root = tk.Tk()
root.title("Solar System Demo")

# Canvas for Turtle
canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas = ScrolledCanvas(canvas_frame)
canvas.pack(fill=tk.BOTH, expand=True)

screen = TurtleScreen(canvas)
screen.bgcolor("black")
screen.tracer(0)

# ===============================
# 3. Info Panel
# ===============================
info_frame = tk.Frame(root, width=300, bg="black")
info_frame.pack(side=tk.RIGHT, fill=tk.Y)
info_frame.pack_propagate(False)

info_labels = {}
for key in ["Description", "Surface Temp", "Distance to Sun", "Distance to Earth",
            "Moons", "Mass", "Diameter", "Radius"]:
    lbl = tk.Label(info_frame, text="", fg="white", bg="black", justify="left", wraplength=280)
    lbl.pack(anchor="w", pady=2)
    info_labels[key] = lbl

def show_info(planet):
    info = planet_info.get(planet, {})
    for key, lbl in info_labels.items():
        lbl.config(text=f"{key}: {info.get(key, 'N/A')}")

# ===============================
# 4. Planet Images & Resize
# ===============================
original_images = {
    "Sun": "Sun.gif",
    "Mercury": "mercury (2).gif",
    "Venus": "venus.gif",
    "Earth": "earth.gif",
    "Mars": "mars.gif",
    "Jupiter": "jupiter.gif",
    "Saturn": "saturn.gif",
    "Uranus": "uranus.gif",
    "Neptune": "neptune.gif"
}

planet_scale = {
    "Sun": 0.18, "Mercury": 0.07, "Venus": 0.10, "Earth": 0.10,
    "Mars": 0.09, "Jupiter": 0.11, "Saturn": 0.16, "Uranus": 0.14, "Neptune": 0.14
}

resized_images = {}

def resize_image(input_path, output_path, scale):
    img = Image.open(input_path)
    w, h = img.size
    new_size = (int(w * scale), int(h * scale))
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    img.save(output_path)

for planet, file in original_images.items():
    resized_file = f"resized_{file}"
    resize_image(file, resized_file, planet_scale[planet])
    resized_images[planet] = resized_file
    screen.register_shape(resized_file)

# ===============================
# 5. Distances, Speeds, Angles
# ===============================
distances = {
    "Mercury": 80, "Venus": 120, "Earth": 160, "Mars": 200,
    "Jupiter": 280, "Saturn": 350, "Uranus": 420, "Neptune": 490
}

elip = 0.7
Bdist = {planet: dist * elip for planet, dist in distances.items()}

speeds = {
    "Mercury": 1.8, "Venus": 1.4, "Earth": 1.0, "Mars": 0.8,
    "Jupiter": 0.4, "Saturn": 0.3, "Uranus": 0.2, "Neptune": 0.1
}

angles = {planet: 0 for planet in speeds}

#Draw stars

def stars(count):
    star = RawTurtle(screen)
    star.hideturtle()
    star.color("white")
    star.penup()
    star.speed(0)
    for i in range(count):
        Xstar= random.randint(-600,600)
        Ystar= random.randint(-300,300)
        star.goto(Xstar,Ystar)
        rand=random.uniform(1,4)   #randint integer
        if rand<=1:
            star.color('red')
        elif rand<2:
            star.color('yellow')
        elif rand<3 :
            star.color("blue")
        else :
            star.color("white")
        star.dot(rand)    
stars(200)

# ===============================
# 6. Draw Orbits
# ===============================
def draw_orbit(dist, bdist):
    orbit = RawTurtle(screen)
    orbit.hideturtle()
    orbit.color("gray")
    orbit.penup()
    for i in range(361):
        x = dist * math.cos(math.radians(i))
        y = bdist * math.sin(math.radians(i))
        orbit.goto(x, y)
        orbit.pendown()

for planet in distances:
    draw_orbit(distances[planet], Bdist[planet])

# ===============================
# 7. Planets
# ===============================
planet_turtles = {}

# Sun
sun = RawTurtle(screen)
sun.shape(resized_images["Sun"])
sun.penup()
sun.goto(0,0)
sun_label = RawTurtle(screen)
sun_label.penup()
sun_label.hideturtle()
sun_label.color("orange")
sun_label.goto(40,30)
sun_label.write("Sun", font=("Arial",10,"normal"))
planet_turtles["Sun"] = sun

# Planets
for planet in distances:
    t = RawTurtle(screen)
    t.shape(resized_images[planet])
    t.penup()
    planet_turtles[planet] = t

# ===============================
# 8. Labels
# ===============================
def create_label(color):
    label = RawTurtle(screen)
    label.hideturtle()
    label.color(color)
    label.penup()
    return label

labels = {planet: create_label("white")
          for planet in distances.keys()}

# ===============================
# 9. Click Handler
# ===============================
def click_handler(x, y):
    for planet, t in planet_turtles.items():
        px, py = t.position()
        if math.hypot(x - px, y - py) < 20:
            show_info(planet)
            break

screen.onclick(click_handler)

global run,number
number=0
run=True
def start():
    global run,number
    number==1
    run=True
    animate()
def stop():
    global run
    run=False
extra=0
def plus_speed():
    global extra
    extra=extra+1
    label.config(text=str(extra))
def minus_speed():
    global extra
    extra=extra-1
    label.config(text=str(extra))
def default_speed():
    global extra
    extra=0
    label.config(text=str(extra))

row= tk.Frame(root)
row.pack(pady=10,anchor="w")

row2= tk.Frame(root)
row2.pack(pady=10,anchor="w")

row3= tk.Frame(root)
row3.pack(pady=10,anchor="w")

rowL=tk.Frame(root)
rowL.pack(pady=10, anchor="w")

rowL1=tk.Frame(root)
rowL1.pack(pady=10, anchor="w")

rowL2=tk.Frame(root)
rowL2.pack(pady=10, anchor="w")

rowL3=tk.Frame(root)
rowL3.pack(pady=10, anchor="w")

button = tk.Button(row, text="run", command=start)
button.pack(side="left",padx=5)

button2 = tk.Button(row, text="stop", command=stop)
button2.pack(side="left",padx=5)

button3 = tk.Button(row2, text="minus", command=minus_speed)
button3.pack(side="left",padx=5)

label = tk.Label(row2, text=str(extra), font=("Arial", 20))
label.pack(side="left",padx=5)

button4 = tk.Button(row2, text="plus", command=plus_speed)
button4.pack(side="left",padx=5)

button5=tk.Button(row3, text="default", command=default_speed)
button5.pack(side="left",padx=5)

# ===============================
# 10. Animation Loop
# ===============================

planet_visible = {planet: True
                     for planet in distances}
def visible(planetName):
    if planet_visible[planetName]:
        planet_turtles[planetName].hideturtle()
        labels[planetName].clear()
        planet_visible[planetName] = False
    else:
        planet_turtles[planetName].showturtle()
        labels[planetName].write(planetName, font=("Arial", 10, "normal"))
        planet_visible[planetName] = True
i=0
for name in distances:
    i+=1
    if i<3:
        buttonL = tk.Button(rowL, text=name, command=partial(visible, name))
        buttonL.pack(side="left", padx=2)
    elif i<6:
        buttonL = tk.Button(rowL1, text=name, command=partial(visible, name))
        buttonL.pack(side="left", padx=2)
    elif i<9:
        buttonL = tk.Button(rowL2, text=name, command=partial(visible, name))
        buttonL.pack(side="left", padx=2)
        

def hideSun():
    if sun.isvisible():
        sun.hideturtle()
        sun_label.clear()
    else:
        sun.showturtle()
        sun_label.goto(40,30)
        sun_label.color("orange")
        sun_label.write("Sun", font=("Arial",10,"normal"))
button6=tk.Button(rowL, text="Sun", command=hideSun)
button6.pack(side="left",padx=5)

moon = RawTurtle(screen)
moon.shape("circle")   
moon.color("white")
moon.shapesize(0.3, 0.3)  
moon.penup()
global moonBool
moonBool=True

moonDist = 25 
moonAngle = 0       
moonSpeed = 5

moonLabel=RawTurtle(screen)
moonLabel.hideturtle()
moonLabel.color("white")
moonLabel.penup()

def MoonHide():
    if moon.isvisible():
        global moonBool
        moon.hideturtle()
        moonLabel.clear()
        moonBool=False
    else:
        moonBool=True
        moon.showturtle()

buttonMoon = tk.Button(rowL3, text="Moon", command=MoonHide)
buttonMoon.pack(side="left",padx=5)

def animate():
    global boolean,name,moonAngle,moonBool #add only moonAngle cause vea change value everytime
    if run==True:
        for planet in distances:
            angles[planet] += speeds[planet] + extra
            x = distances[planet] * math.cos(math.radians(angles[planet]))
            y = Bdist[planet] * math.sin(math.radians(angles[planet]))
            planet_turtles[planet].goto(x, y)
            labels[planet].clear()
            
            if planet_visible[planet]:
                labels[planet].goto(x + 10, y - 5)
                labels[planet].write(planet, font=("Arial", 8, "normal"))
            if planet == "Earth":
                moonAngle += moonSpeed
                moonx = x + moonDist * math.cos(math.radians(moonAngle))
                moony = y + moonDist * math.sin(math.radians(moonAngle))
                moon.goto(moonx, moony)
                moonLabel.clear()
                if moonBool==True:
                    moonLabel.write("Moon", font=("Arial",7,"normal"))
                    moonLabel.goto(moonx+10,moony+5)
                else:
                    moonLabel.clear()
        screen.update()
        root.after(10, animate)
if number!=1:
    animate()
root.mainloop()
