class PlayerState():
    def __init__(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.run = False
        self.shot = False
        self.mouse_pos = 0,0

    def __str__(self):
        a = "[\n"
        a += " UP : " + str(self.up) + "\n"
        a += " DOWN : " + str(self.down) + "\n"
        a += " RIGHT : " + str(self.right) + "\n"
        a += " LEFT : " + str(self.left) + "\n"
        a += " RUN : " + str(self.run) + "\n"
        a += " SHOT : " + str(self.shot) + "\n"
        a += " MOUSE : " + str(self.mouse_pos) + "\n"
        a += "]"
        return a
