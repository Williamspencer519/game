from terrain import Terrain


class Passable(Terrain):
	def __init__(self):
		super(Passable, self).__init__()
	def check_collision(self):
		pass