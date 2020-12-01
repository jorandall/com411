import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

data = []

def init():
  global squares

  data.append({"x": [3, 3, 4, 4, 3], "y": [3, 4, 4, 3, 3]})
  data.append({"x": [2, 2, 5, 5, 2], "y": [2, 5, 5, 2, 2]})
  data.append({"x": [1, 1, 6, 6, 1], "y": [1, 6, 6, 1, 1]})

def animate(frame):
  global data, ax
  index = frame % 3
  ax.cla()
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)
  ax.plot(data[index]["x"], data[index]["y"])


def run():
  global fig # Declare fig as the global variable

  squares_animation = animation.FuncAnimation(
    fig, # Delcare what we are animating
    animate, # Function call to animate
    frames = 3, # How many frames our animation will have
    interval = 1000, # Time delay between animation in milliseconds
    init_func=init
    )
  
  plt.show()

run()
