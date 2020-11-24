import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Define animation function
def animate(frame):
  global ax
  ax.set_xlim(0, 10) # Set the size for y-axis
  ax.set_ylim(0, 10) # Set the size for x-axis

  ax.plot(frame, frame, "ro") # What we are actually animating

def run():
  global fig 

  simple_animation = animation.FuncAnimation(
    fig, # Delcare what we are animating
    animate, # Function call to animate
    frames = 10, # How many frames our animation will have
    interval = 1000, # Time delay between animation in milliseconds
    repeat = False # Stop animation from repeating
    )

  plt.show()

run()