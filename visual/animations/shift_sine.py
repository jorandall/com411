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

  # Calculate the y value with sin function, and dividing pi by 180
  y = np.sin((x + frame) * (np.pi / 180))

  ax.plot(x, y)

def run():
  global fig # Declare fig as the global variable

  sine_animation = animation.FuncAnimation(
    fig, # Delcare what we are animating
    animate, # Function call to animate
    frames = 720, # How many frames our animation will have
    interval = 100, # Time delay between animation in miliseconds
    )
  
  plt.show()

run()



