from terrain import Terrain


class Solid(Terrain):
	def __init__(self):
		super(Solid, self).__init__()

	def check_collision(self):
		pass