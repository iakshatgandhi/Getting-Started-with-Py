from enum import Enum, auto

class state(Enum):
   PLAYING = 0
   PAUSED = 1
   GAME_OVER = 2
   
# enum are used when  we need the state or value of the variable to constant 
#within  in the program
# but the values matter in case they don't then we can use auto

'''
class state(Enum):
   PLAYING = auto()
   PAUSED = auto()
   GAME_OVER = auto()
'''
# if the values does n't matter what they are but only thing is the had to be unique
# auto does the job
print(state.PLAYING)
print(state["GAME_OVER"])
print(state(1))
print(state.GAME_OVER.value)

print(list(state))
print(len(state))