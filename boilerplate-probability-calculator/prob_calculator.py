import copy
import random

class Hat:
  def __init__(self, **kwargs):
    #create contents list with str items
    self.contents=[]
    for k,v in kwargs.items():
      self.contents += v*[k]
 
  def draw (self,num):
    #if num of drawn balls exceeds available quantity, return all the balls
    if (num > len(self.contents)):
      return self.contents
    #select random num of balls
    drawn=random.sample(self.contents,num)
    #remove selected balls from hat
    for ball in drawn:
      self.contents.remove(ball)
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success=0
  for _ in range(num_experiments):
      copyhat = copy.deepcopy(hat)
      copydr = copyhat.draw(num_balls_drawn)
      copyexp=copy.deepcopy(expected_balls)
      #check if expected balls match the drawn ones
      for col in copydr:
          if(col in copyexp):
              copyexp[col]-=1
      if(all(_ <= 0 for _ in copyexp.values())):
          success+=1
  
  prob = success / num_experiments
  return prob
