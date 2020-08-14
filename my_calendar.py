from PIL import Image
from PIL import ImageDraw

class myCalendar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = Image.new("RGB", (x, y), "#ffffff")
        self.draw = ImageDraw.Draw(self.img)
    
    def save_img(self, fn):
        self.img.save(fn)
        
    def vertical_line(self, start_pos, length, fill, width=0):
        self.draw.line((start_pos, (start_pos[0], start_pos[1]+length)), fill, width)

    def horizontal_line(self, start_pos, length, fill, width=0):
        self.draw.line((start_pos, (start_pos[0]+length, start_pos[1])), fill, width)

if __name__ == "__main__":
    my_cal = myCalendar(500,500)
    my_cal.vertical_line((100,100), 300, (230,230,230), 1)
    my_cal.horizontal_line((100,100), 300, (230,230,230), 1)
    my_cal.save_img("testimg.jpg")
