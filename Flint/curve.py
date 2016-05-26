class curve:
    def __init__(self,NAME,LEFT,RIGHT,COLOR,TRACK_NUM,TYPE):
        self.name = NAME
        self.left_scale = LEFT
        self.right_scale = RIGHT
        self.color = COLOR
        self.track_num = TRACK_NUM
        self.type = TYPE                # log / linear / fill_right / fill_left
        self.fill_color = ''
