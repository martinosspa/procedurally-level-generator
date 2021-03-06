import json
from pprint import pprint
from random import random, uniform, choice, randint
from math import floor
#random.seed(10)




def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def normalize(val, min_val, max_val):
	return (val - min_val)/(max_val-min_val)

class Tile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Room:
	def __init__(self, x, y, dimensions):
		self.x = x
		self.y = y
		self.dimensions = dimensions

class Level:
	def __init__(self, dimensions):
		self.width = dimensions[0]
		self.height = dimensions[1]
		self.grid = [[None for x in range(self.height)] for y in range(self.width)] 
		self.dif = 2 
		self.dif_max = 10 #max difficulty 10
		self.room_count = 0
		self.generated_rooms = []

	def get_neighbors(self,x,y):
		neighbors = 0
		neighbors = neighbors + 1 if self.grid[x+1][y] else neighbors
		neighbors = neighbors + 1 if self.grid[x-1][y] else neighbors
		neighbors = neighbors + 1 if self.grid[x][y+1] else neighbors
		neighbors = neighbors + 1 if self.grid[x][y-1] else neighbors
		return neighbors

	def generate_room(self, x, y):
		available_positions = []
		n = self.get_neighbors(x,y)
		print(f'neighbors: {n}')
		generated = False
		iterations = 0
		while not generated and iterations < 500:
			side = floor(randint(1,4))

			if side == 1:
				pass
				

			#if its stuck this breaks the loop
			iterations += 1
			

		self.generated_rooms.append((x, y))
		self.room_count += 1


	def generate(self):
		starting_limit = 10
		population_percentage = 0.6 # max 1

		room_limit = constrain(floor(uniform(starting_limit*self.dif*random(),
							   uniform(1, 2) * starting_limit * self.dif)), 
							   starting_limit, floor(self.width * self.height * population_percentage))
		print(f'max rooms: {room_limit}')

		start_x = self.width // 2
		start_y = self.height // 2
		#print(start_x, start_y)
		while self.room_count < room_limit:

			if self.generated_rooms:
				room = choice(self.generated_rooms)
				self.generate_room(room[0], room[1])
			else:
				self.generate_room(start_x, start_y)

			
			#pprint(self.grid)
			#print(self.generated_rooms)







if __name__ == "__main__":
	l1 = Level((4, 5))
	l1.generate()

