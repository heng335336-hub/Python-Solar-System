from turtle import Screen, Turtle
import math
import time
import random
from PIL import Image

# =====================================
# 1. Resize Planet Images
# =====================================
def resize_image(input_path, output_path, scale):
    """Resize planet images to make them smaller or larger."""
    img = Image.open(input_path)
    w, h = img.size
    new_size = (int(w * scale), int(h * scale))
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    img.save(output_path)

# =====================================
# 2. Setup Screen
# =====================================
screen = Screen()
screen.title("Solar System Demo")
screen.setup(width=1200, height=700)  # Perfect for 14-inch screen
screen.bgcolor("black")
screen.tracer(0)  # Smooth animation by manual screen update

# =====================================
# 3. Planet Images
# =====================================
original_images = {
    "Sun": "Sun.gif",
    "Mercury": "mercury (2).gif",
    "Venus": "venus.gif",
    "Earth": "earth.gif",
    "Mars": "mars.gif",
    "Jupiter": "jupiter.gif",
    "Saturn": "saturn.gif",
    "Uranus": "uranuss.gif",
    "Neptune": "neptune.gif"
}

# Planet scale - balanced for visibility and realism
planet_scale = {
    "Sun": 0.18,
    "Mercury": 0.07,
    "Venus": 0.10,
    "Earth": 0.10,
    "Mars": 0.09,
    "Jupiter": 0.11,
    "Saturn": 0.16,
    "Uranus": 0.09,
    "Neptune": 0.14
}

# Resize and register images
resized_images = {}
for planet, file in original_images.items():
    resized_file = f"resized_{file}"
    resize_image(file, resized_file, planet_scale[planet])
    resized_images[planet] = resized_file
    screen.addshape(resized_file)

# =====================================
# 4. Stars Background
# =====================================
def draw_stars(count=150):
    star = Turtle()
    star.hideturtle()
    star.penup()
    star.speed(0)
    for _ in range(count):
        x = random.randint(-580, 580)
        y = random.randint(-330, 330)
        star.goto(x, y)
        color = random.choice(["white", "yellow", "blue"])
        star.color(color)
        star.dot(random.uniform(1, 3))

draw_stars(200)

# =====================================
# 5. Orbit Distances
# =====================================
# Scaled down to fit nicely on a 14-inch screen
distances = {
    "Mercury": 80,
    "Venus": 120,
    "Earth": 160,
    "Mars": 200,
    "Jupiter": 280,
    "Saturn": 350,
    "Uranus": 420,
    "Neptune": 490
}

# Elliptical orbits
elip = 0.7
Bdist = {planet: dist * elip for planet, dist in distances.items()}

# =====================================
# 6. Orbit Speeds
# =====================================
# Higher speed = faster orbit
speeds = {
    "Mercury": 1.8,
    "Venus": 1.4,
    "Earth": 1.0,
    "Mars": 0.8,
    "Jupiter": 0.4,
    "Saturn": 0.3,
    "Uranus": 0.2,
    "Neptune": 0.1
}

angles = {planet: 0 for planet in speeds}  # Starting angles

# =====================================
# 7. Draw Orbit Paths
# =====================================
def draw_orbit(dist, bdist):
    orbit = Turtle()
    orbit.hideturtle()
    orbit.color("gray")
    orbit.penup()
    orbit.goto(dist, 0)
    orbit.pendown()
    for i in range(361):
        x = dist * math.cos(math.radians(i))
        y = bdist * math.sin(math.radians(i))
        orbit.goto(x, y)

for planet in distances:
    draw_orbit(distances[planet], Bdist[planet])

# =====================================
# 8. Create Planet Turtles
# =====================================
planet_turtles = {}

# Sun
sun = Turtle()
sun.shape(resized_images["Sun"])
sun.penup()
sun.goto(0, 0)
planet_turtles["Sun"] = sun

# Planets
for planet in distances.keys():
    t = Turtle()
    t.shape(resized_images[planet])
    t.penup()
    planet_turtles[planet] = t

# =====================================
# 9. Labels
# =====================================
def create_label(color):
    label = Turtle()
    label.hideturtle()
    label.color(color)
    label.penup()
    return label

labels = {planet: create_label("white") for planet in distances.keys()}

# =====================================
# 10. Animation Loop
# =====================================
running = True

def stop_program():
    global running
    running = False
    screen.bye()

screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", stop_program)

while running:
    for planet in distances.keys():
        # Update angle
        angles[planet] += speeds[planet]

        # Calculate new position
        x = distances[planet] * math.cos(math.radians(angles[planet]))
        y = Bdist[planet] * math.sin(math.radians(angles[planet]))

        # Move planet
        planet_turtles[planet].goto(x, y)

        # Label
        labels[planet].clear()
        labels[planet].goto(x + 10, y - 5)
        labels[planet].write(planet, font=("Arial", 8, "normal"))

    screen.update()
    time.sleep(0.01)

try:
    screen.mainloop()
except:
    pass
