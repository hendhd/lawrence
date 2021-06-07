#! /usr/bin/ python
# -*- coding=utf-8 -*- 

# A demo program to show how classes in python work


class cat:

# A method of the class cat. Note that the function needs the self
# refering as an argument so it can access the attributes. 

  def pur(self):
    print ("{name} is purring".format(name=self.name) )
    return

  def dies(self):
    self.lifes -= 1

    if self.lifes<=0:
      print ("{name} seems to be a ghost".format(name=self.name) )
    else:
      print ("{name} died but still has {lifes} cat lifes left".format(name=self.name, lifes=self.lifes) )

# When the class is instanced, these are the attributs that will be
# created. 

  def __init__(self, name, furcolor, lifes=9):
    self.furcolor = furcolor
    self.name = name
    self.lifes = lifes


# The function main() is not part of the class! 
def main():
  florence=cat("Florence", "grey")
  florence.pur()


# If the script is run, the function main() will
# be executed. 

if __name__=="__main__":
  main()



