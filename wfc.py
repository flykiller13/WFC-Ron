""" 
rules = {
    'NORTH': ...,
    'EAST': ...,
    ...
}

possibilities = []
"""

class Bitmap:
    def __init__(self, rules: dict, template = None) -> None:
        self.rules = rules
        self.template = template

class Cell:
    def __init__(self, size_x: int ,size_y: int, pos: tuple, bitmaps: list) -> None:
        self.size: tuple = (size_x, size_y)
        self.position: tuple = pos
        self.possibilities: list[Bitmap] = bitmaps
        self.bitmap: Bitmap = None
        self.entropy: int = len(bitmaps)
        
    def update_possibilities(self, new_bitmap: Bitmap, added_from: int):
        for bitmap in self.possibilities:
            if new_bitmap not in bitmap.rules[added_from]:
                self.possibilities.remove(new_bitmap)
                
class Wave:
    def __init__(self, canvas_size: tuple, bitmap_size: tuple) -> None:
        self.wave: list[Cell] = [] # Represents a grid of cells 
        self.canvas_size = canvas_size
        self.bitmap_size = bitmap_size
        
    def init_wave(self):
        width: int = int(self.canvas_size[0]/self.bitmap_size[0])
        height: int = int(self.canvas_size[1]/self.bitmap_size[1])
        
        for i in range(height):
            for j in range(width):
                pass
        
    def get_cell(self, x, y):
        pass

def get_wave_size(canvas_size: tuple, bitmap_size: tuple):
    width: int = int(canvas_size[0]/bitmap_size[0])
    height: int = int(canvas_size[1]/bitmap_size[1])
    
    return (width, height)

def wave_function_collapse(canvas_size: tuple, bitmap_size: tuple, bitmaps: dict):
    wave_size = get_wave_size(canvas_size, bitmap_size)
    print(wave_size)
    
    wave = [[list(bitmaps.keys()) for _ in range(wave_size[1])] for _ in range(wave_size[0])]
    print(wave)
    
canvas = (10, 10)
bitmap_size = (2, 2)
bitmaps = {
    'a': ['b','c'],
    'b': ['a', 'c'],
    'c': ['a', 'b']
}
wave_function_collapse(canvas, bitmap_size, bitmaps)