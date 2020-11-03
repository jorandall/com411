# Import module
import os

# Define current working directory folder retrieve
def cwd():
  path = os.getcwd()
  print(f"Current Working Folder Path: {path}")
  print("This folder contains the following:")
  for file in os.listdir(path):
    print(file)

# Define run function
def run():
  print("Processing...")
  cwd()

run()