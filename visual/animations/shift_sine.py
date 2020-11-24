import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
  ax.cla()
  # Set the limits for x and y
  ax.set_xlim(0, 2*np.pi)
  ax.set_ylim(-1, 1)

  x = np.arange(0, 2*np.pi, 0.01)
  y = np.sin(x * frame/50)

  ax.plot(x, y)

def run():
  global fig # Declare fig as the global variable

  shifting_sine_animation = animation.FuncAnimation(
    fig, # Delcare what we are animating
    animate, # Function call to animate
    frames = 100, # How many frames our animation will have
    interval = 100, # Time delay between animation in miliseconds
    )
  
  plt.show()

run()



