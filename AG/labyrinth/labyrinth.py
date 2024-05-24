from tilegamelib import Game
from tilegamelib import TiledMap
from tilegamelib.sprites import Sprite



game = Game()
game.event_loop()

MAZE = """############
#....#.....#
#.#.####.#.#
#.#.......#
#.#....#.#.#
#.#....#.#.#
#........#.#
#.####.#.#.#
#..........#
#.####.#.#.#
#..........#
############"""

class MazeGame:

    def __init__(self):
        self.game = Game()
        self.map = TiledMap(self.game)
        self.map.set_map(MAZE)
        self.map.fill_map('#', (12, 12))  # Geänderte Größe des Labyrinths


        self.sprite = Sprite(self.game, 'b.pac_right', (1, 1), speed=2)

        self.game.event_loop(figure_moves=self.move, draw_func=self.draw)

    def draw(self):
            self.map.draw()
            self.sprite.draw()
            self.sprite.move()

    def move(self, direction):
            print(direction)
            self.sprite.add_move(direction)



if __name__ == '__main__':
    maze_game = MazeGame()