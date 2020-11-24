import matplotlib.pyplot as plt
import matplotlib.animation as animation

squares = {}

def init():
  global squares

  squares = {
  "small": {
  "x" : [3, 4, 4, 3, 3],
  "y" : [3, 3, 4, 4, 3]
  },
  "medium": {
  "x" : [2, 5, 5, 2, 2],
  "y" : [2, 2, 5, 5, 2]
  },
  "large": {
  "x" : [1, 6, 6, 1, 1],
  "y" : [1, 1, 6, 6, 1]
  }}

def animate(frame):
