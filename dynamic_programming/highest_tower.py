'''
Given N boxes with dimensions Wi, Di, Hi, calculate the highest possible stack of boxes height.
Boxes can be placed on top of each other only if top box is strictly smaller in all dimensions.
'''

class Box:
    def __init__(self, w, d, h):
        self.w = w
        self.d = d
        self.h = h


def highest_tower(boxes: list[Box]) -> int:
    dp = [0 for _ in range(len(boxes)+1)]
    towers_boxes = [[] for _ in boxes]
    
    for n in range(1, len(dp)):
        # update possible towers
        processed_towers = {}
        for i in range(len(boxes)):
            # no towers yet
            if not len(towers_boxes[i]):
                towers_boxes[i].append(i)
                continue

            for ti, tower in enumerate(towers_boxes):
                if not processed_towers.get(ti, False) and not i in tower:
                    insert_idx = -1
                    for j in range(len(tower)):
                        box_below = boxes[tower[j]]
                        box_above = boxes[tower[j+1]] if j+1<len(tower) else None

                        lt_below = box_below.h > boxes[i].h and \
                            box_below.w > boxes[i].w and \
                            box_below.d > boxes[i].d

                        gt_above = True
                        if box_above:
                            gt_above = box_above.h < boxes[i].h and \
                            box_above.w < boxes[i].w and \
                            box_above.d < boxes[i].d

                        if lt_below and gt_above:
                            insert_idx = j+1

                    if insert_idx > 0:
                        tower.insert(insert_idx, i)
                        processed_towers[ti] = True
                        
                                            
        highest_tower = 0
        for t in towers_boxes:
            height = 0 
            for b in t:
                height += boxes[b].h
            highest_tower = max(highest_tower, height)

        dp[n] = max(dp[n-1], highest_tower)

        '''
        print(dp)
        for t in towers_boxes:
            print(t)
        print()
        '''

    return dp[-1]


def calc_height(boxes: list[Box], bottom_index: int, height_map: list[int]) -> int:
    if bottom_index < len(height_map) and  height_map[bottom_index] > 0:
        return height_map[bottom_index]

    bottom_box = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index + 1, len(boxes)):
        box = boxes[i]
        if bottom_box.h > box.h and \
           bottom_box.w > box.w and \
           bottom_box.d > box.d:
            height = calc_height(boxes, i, height_map)
            max_height = max(max_height, height)

    max_height += bottom_box.h
    height_map[bottom_index] = max_height
    return max_height


def highest_tower_2(boxes: list[Box]) -> int:
    # sort boxes in descending order of height
    boxes = sorted(boxes, key=lambda b: b.h, reverse=True)
    max_h = 0
    height_map = [0 for _ in range(len(boxes))]
    
    for i in range(len(boxes)):
        # calc height of stack of boxes with i at the bottom
        h = calc_height(boxes, i, height_map)
        max_h = max(max_h, h)
    
    return max_h


if __name__ == '__main__':
    boxes = [Box(1, 1, 3), Box(1, 1, 0.5), Box(3, 3, 2), Box(2, 2, 1), Box(5, 5, 1), Box(6, 6, 1.5), Box(7, 7, 2)]
    print(highest_tower(boxes))
    print(highest_tower_2(boxes))
