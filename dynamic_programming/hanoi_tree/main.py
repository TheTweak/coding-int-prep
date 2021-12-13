import sys
import threading
from time import sleep
from collections import deque

import dearpygui.dearpygui as dpg

WIDTH = 800
HEIGHT = 600
DISC_H = 10
DISC_W = 10
DELAY_BETWEEN_FRAMES_SEC = 0.2


class Tower:
    def __init__(self, pmin, pmax):
        self.pmin = pmin
        self.pmax = pmax


class Disc:
    def __init__(self, width):
        self.width = width

    def __str__(self) -> str:
        return 'disc w=' + str(self.width)


class HanoiTowers:
    def __draw_towers(self):
        self.towers = []
        for i in range(3):
            tower_width = self.max_disc_w            
            offset = i*(tower_width+10)
            pmin = (0+offset, HEIGHT-6*5)
            pmax = (tower_width+offset, HEIGHT-5*5)
            self.towers.append(Tower(pmin, pmax))
    
        for t in self.towers:
            dpg.draw_rectangle(t.pmin, t.pmax, fill=(0, 255, 0, 255))

    def __draw_discs(self):
        for ti, td in enumerate(self.discs):
            for di, d in enumerate(td):
                offset_y = di * (DISC_H + 5)
                offset_x = ti * (self.max_disc_w + 10)
                pmin = (offset_x, HEIGHT - 5 * DISC_H - offset_y)
                pmax = (offset_x + d.width, HEIGHT - 4 * DISC_H - offset_y)
                dpg.draw_rectangle(pmin, pmax, fill=(255, 255, 255, 255))            
    
    def __init__(self, n=3):
        dpg.create_context()

        self.max_disc_w = n*DISC_W
        self.n = n
        self.move_queue = deque()

        self.discs = [[], [], []]
        for i in range(self.n):
            disc_w = self.max_disc_w-i*DISC_W 
            self.discs[0].append(Disc(disc_w)) 

    def start(self):                        
        dpg.create_viewport(title='Hanoi Towers', width=WIDTH, height=HEIGHT)
        dpg.setup_dearpygui()
        dpg.show_viewport()

        while dpg.is_dearpygui_running():
            with dpg.window(label="Hanoi Towers", width=WIDTH, height=HEIGHT):
                self.__draw_towers()
                self.__draw_discs()
            if len(self.move_queue):
                a, b = self.move_queue.popleft()
                self.__move(a, b)
            dpg.render_dearpygui_frame()
            sleep(DELAY_BETWEEN_FRAMES_SEC)      

        dpg.destroy_context()

    def __move(self, a, b):
        src_disc = None
        if len(self.discs[a]):
            src_disc = self.discs[a][-1]

        if not src_disc:
            print(f'no disc available to move from {a}')
            return
            
        dest_disc = None
        if len(self.discs[b]):
            dest_disc = self.discs[b][-1]

        print(f'{src_disc} [{a}] -> {dest_disc} [{b}]', end=' ')
        if dest_disc and src_disc and dest_disc.width < src_disc.width:
            print(f'WARN: can not move: disc on tower {a} is > than disc on {b}')
            return
        print()

        self.discs[b].append(src_disc)
        self.discs[a].pop()

    def move(self, a, b):
        self.move_queue.append((a, b))


class Solution:
    def __init__(self, ht: HanoiTowers):
        self.ht = ht

    def __move(self, n, src, dst, tmp) -> None:    
        '''
        Move n top discs from src tower to dst, using tmp
        as a buffer.
        '''
        if n == 0:
            return

        self.__move(n-1, src, tmp, dst)
        self.ht.move(src, dst)
        self.__move(n-1, tmp, dst, src)
        
    def solve(self) -> None:
        self.__move(self.ht.n, 0, 2, 1)

    
if __name__ == "__main__":
    n = int(sys.argv[1])
    ht = HanoiTowers(n=n)
    htt = threading.Thread(target=ht.start)
    htt.start()
    Solution(ht).solve()
