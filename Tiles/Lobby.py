from Tiles.Tile import Tile
class Lobby(Tile):
	"""docstring for Teatro"""
	def __init__(self):
		self.nome = 'Lobby';
		self.largura = 2;
		self.altura = 2;
		self.num_portas = 6;
		self.e_comeco = True;
		self.path_image = 'mansion_img/lobby.jpeg';
