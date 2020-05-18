from Maps.Map import Map
from Tiles.Teatro import Teatro
from Tiles.Lobby import Lobby
class Map01(Map):
	"""docstring for Map01"""
	def __init__(self):
		self.tiles = [Teatro(), Lobby()]
		self.max_tiles = 4		
		# super(Map01, self).__init__(lista_de_tiles, max_tiles)
