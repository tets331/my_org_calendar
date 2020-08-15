from PIL import Image
from PIL import ImageDraw
import datetime

class myCalendar:
    def __init__(self, x, y, start_time=6):
        self.img = Image.new("RGB", (x, y), "#ffffff")
        self.draw = ImageDraw.Draw(self.img)
        self.start_time = start_time

    def save_img(self, fn):
        self.img.save(fn)

    def vertical_line(self, start_pos, length, fill, width=0):
        self.draw.line((start_pos, (start_pos[0], start_pos[1]+length)), fill, width)

    def horizontal_line(self, start_pos, length, fill, width=0):
        self.draw.line((start_pos, (start_pos[0]+length, start_pos[1])), fill, width)

    def grid(self):
        color = (220,220,220) #gray
        self.start_x = self.img.size[0]/10
        self.start_y = self.img.size[1]/10
        vert_num = 7
        hori_num = 16
        self.grid_w = (self.img.size[0]-self.start_x*2)/vert_num
        self.grid_h = (self.img.size[1]-self.start_y*2)/hori_num

        for i in range(vert_num+1):
            self.vertical_line((self.start_x+self.grid_w*i, self.start_y), self.img.size[1]*0.8, color)

        for i in range(hori_num+1):
            self.horizontal_line((self.start_x, self.start_y+self.grid_h*i), self.img.size[0]*0.8, color)

    def rectangle(self, start_pos, length, width, fill = "#bbddff", rx=10, ry=10):
        self.draw.rectangle((start_pos, (start_pos[0]+width,start_pos[1]+length)), fill)

    def task(self, start_time, end_time):
        col = self.day2col(start_time)
        start = start_time.hour + start_time.minute/60.0
        end = end_time.hour + end_time.minute/60.0
        length = (end - start) * self.grid_h
        start_pos = (self.start_x + col * self.grid_w + 5, self.start_y + (start - self.start_time) * self.grid_h + 5)

        self.rectangle(start_pos, length - 10, self.grid_w - 10)

    def day2col(self, date):
        map = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}
        # TODO: make the logic can change the start day of the week.
        return map[date.strftime('%a')]

    def time2row(self, date):
        t = date.hour + date.minute/60

if __name__ == "__main__":
    my_cal = myCalendar(3200,1800)
    my_cal.grid()

    sd = datetime.datetime(2020,8,14,15,30)
    ed = datetime.datetime(2020,8,14,16,15)
    my_cal.task(sd, ed)

    sd = datetime.datetime(2020,8,14,16,15)
    ed = datetime.datetime(2020,8,14,18,45)
    my_cal.task(sd, ed)
    my_cal.save_img("testimg.jpg")
