#!/usr/bin/env python

"""
@author Joshua Calzadillas
@version 1.0.0

@description

Menu Designer

This is a menu designer class that allows the user to make a menu
and load it with commands based on an array of inputs.
"""

import yaml
from os import system

# Changes input to raw_input
if hasattr(__builtins__, 'raw_input'):
      input=raw_input

# Yaml Loader Class
class YAMLLoader:
    def __init__(self, file):
        self.file = open(file, "r")
    
    def load_config(self):
        try:
            return yaml.safe_load(self.file)
        except yaml.YAMLError as exc:
            print(exc)

# Menu CLass
class Menu:
    def __init__(self, header, commands):
        self.header = header
        self.commands = commands
    
    # print menu
    def printMenu(self):
        print("%30s Menu %30s" % (30 * "-", 30 * "-"))
        for i in range(1, (len(self.header) - (len(self.header) - len(self.commands)))+1):
            print("%20s%d. %s" % (" ", i, self.header[i-1]))
        print(67 * "-")
    
    # user input
    def userInput(self):
        choice = input("\nPlease write a number (1-%d): " % int((len(self.header) - (len(self.header) - len(self.commands)))))
        if unicode(str(choice), "utf-8").isnumeric():
            if int(choice) in range(1, (len(self.header) - (len(self.header) - len(self.commands)))+1):
                self.execute(self.commands[int(choice)-1])
        return choice
    
    # execute the system
    def execute(self, command):
      if command in self.commands:
        print("Running Command: %s" % command)
        if (command != "exit"):
          system(command)
    
    # Start the menu loop
    def start(self):
        quit_loop = True
        self.printMenu()
        choice = str(self.userInput())
        if choice == str(len(self.commands)):
          quit_loop = False

        # while loop setup
        while (quit_loop):
            print("\n\n")
            self.printMenu()
            choice = str(self.userInput())
            if choice == str(len(self.commands)):
              quit_loop = False
        print("\n\nThank You!")


# Load YAML Config
y = YAMLLoader("test.yml")
config = y.load_config()
headers = []
commands = []

# Menu Items
if len(config["Menu-Items"]) > 0:
  for i in range(0,len(config["Menu-Items"])):
    headers.append(config["Menu-Items"][i]["header"])
    commands.append(config["Menu-Items"][i]["command"])
  
  # Autoadd clear
  headers.append("Clear")
  commands.append("clear")

  # Autoload Quit
  headers.append("Quit")
  commands.append("exit")

  # Setup the menu
  m = Menu(headers, commands)
  m.start()