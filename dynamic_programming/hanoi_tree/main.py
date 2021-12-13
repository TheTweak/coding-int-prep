import sys
import dearpygui.dearpygui as dpg

WIDTH = 800
HEIGHT = 600
DISC_H = 10
DISC_W = 20

class HanoiTowers:
    def __init__(self, n=3):
        dpg.create_context()

        max_disc_w = n*DISC_W
                
        with dpg.window(label="Hanoi Towers", width=WIDTH, height=HEIGHT):
            # Draw towers
            for i in range(3):
                tower_width = max_disc_w
                offset = i*(tower_width+10)
                dpg.draw_rectangle((0+offset, HEIGHT-6*5), \
                    (tower_width+offset, HEIGHT-5*5), \
                    fill=(0, 255, 0, 255))
            # Draw disks
            for i in range(n):
                offset = i*(DISC_H+5)
                disc_w = max_disc_w-i*DISC_W 
                dpg.draw_rectangle((0, HEIGHT-5*DISC_H-offset), \
                    (disc_w, HEIGHT-4*DISC_H-offset), \
                    fill=(255, 255, 255, 255))
        
        dpg.create_viewport(title='Custom Title', width=WIDTH, height=HEIGHT)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    
if __name__ == "__main__":
    ht = HanoiTowers(n=int(sys.argv[1]))
