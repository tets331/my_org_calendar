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

    def grid(self):
        color = (220,220,220) #gray
        start_x = self.x/10
        start_y = self.y/10
        vert_num = 7
        hori_num = 16
        w = (self.x-start_x*2)/vert_num
        h = (self.y-start_y*2)/hori_num

        for i in range(vert_num+1):
            self.vertical_line((start_x+w*i, start_y), self.y*0.8, color)

        for i in range(hori_num+1):
            self.horizontal_line((start_x, start_y+h*i), self.x*0.8, color)

if __name__ == "__main__":
    my_cal = myCalendar(3200,1800)
    my_cal.grid()
    my_cal.save_img("testimg.jpg")
