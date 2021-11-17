'''
Design a musical juke box.


what actions can a juke box perform:

- play a song requires a coin
- get a list of available songs
- select a vinyl disc (move it to the top)
- rewind the vinyl disc to the beginning
- flip a vinyl disc to the other side
- change volume
'''

from collections import deque, namedtuple
from enum import Enum

Song = namedtuple('Song', 'artist album songname')

class VinylDisc:
    def __init__(self, artist: str, album: str, songs_side_a: list[Song],
        songs_side_b: list[Song]
    ):
        self.artist = artist
        self.album = album
        self.songs_side_a = songs_side_a
        self.songs_side_b = songs_side_b
        self.face_up = True


class Coin(Enum):
    FiveCent = 5
    TenCent = 10
    Quarter = 25
    FiftyCent = 50


class JukeBox:
    def __init__(self, vinyls: list[VinylDisc], play_coin: Coin = Coin.Quarter):
        self.vinyls = vinyls
        self.play_coin = play_coin
        self.volume = 5
        self.max_volume = 10

    def play(self, song: Song, coin: Coin) -> None:
        '''
        * Checks if coin quantity is enough to start playing
        * Finds a vinyl with the given song, and moves to the top of the queue
        * Flips the vinyl if the given song is on the other side
        * Rewinds the vinyl to the beginning of the song
        * Starts playing
        '''
        if not self.__validate_coin(coin):
            return

        self.__select_vinyl(song)
        self.__flip_vinyl_if_needed(song)
        self.__rewind_vinyl(song)
        self.__play()

    def volume_up(self) -> None:
            pass

    def volume_down(self) -> None:
        pass

    def get_songs(self) -> list[str]:
        pass

    def __validate_coin(self, coin: Coin) -> bool:
        '''Validates if a given coin is enough quantity to start playing music.'''
        pass

    def __select_vinyl(self, song: Song) -> None:
        '''Finds a vinyl by song, and moves it to the top.'''
        pass

    def __flip_vinyl_if_needed(self, song: Song) -> None:
        '''Checks if selected vinyl is on the side where the given song is written.'''
        pass

    def __rewind_vinyl(self, song: Song) -> None:
        '''Rewinds the selected vinyl to the beginning of the given song.'''
        pass

    def __play(self) -> None:
        '''Starts playing the vinyl at the top of the queue.'''
        pass
