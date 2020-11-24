import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
  ax.cla()
  # Set the limits for x and y
  ax.set_xlim(0, 720)
  ax.set_ylim(-1, 1)

  # X value range from 0 to 720
  x = np.arange(0, 720)

  # Convert x into shifting radians
  x_in_radians = (x + frame) * (np.pi / 180)

  # Calculate the y value with sin function
  y = np.sin(x_in_radians)

  ax.plot(x, y)

def run():
  global fig # Declare fig as the global variable

  shifting_sine_animation = animation.FuncAnimation(
    fig, # Delcare what we are animating
    animate, # Function call to animate
    frames = 720, # How many frames our animation will have
    interval = 100, # Time delay between animation in miliseconds
    )
  
  plt.show()

run()



