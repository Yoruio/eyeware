from cv2 import cv2

TRAFFIC_WIDTH_LIMIT = 100
CENTER_TRAFFIC_WIDTH_LIMIT = 50
CENTER_OFFSET = 50

class Label:
    def __init__(self,name, type, rect):
        self.name = name
        self.rect = rect

class Traffic:
    def __init__(self, name, rect, is_seen, is_close, last_seen=0):
        self.name = name
        self.rect = rect
        self.is_seen = is_seen
        self.is_close = is_close
        self.last_seen = last_seen
        self.center = (self.rect.x + self.rect.width/2, self.rect.y - self.rect.height/2)

    def is_trafic_seen(self, eye_track_coor):
        # traffic that's seen can't be unseen
        if self.is_seen or self.rect.contains(cv2.Point):
            self.is_seen = True
        return self.is_seen
    
    def is_traffic_close(self):
        # if it's super close then it's close
        # 100 is arbritary
        if self.rect.width > TRAFFIC_WIDTH_LIMIT: 
            self.is_close = True
        
        # or if it's somewhat close but it's near the center
        elif self.rect.width > CENTER_TRAFFIC_WIDTH_LIMIT and abs(self.center[0]) + abs(self.center[1]) < CENTER_OFFSET:
            self.is_close = True
        
        else:
            self.is_close = False
        return self.is_close
        
    def get_traffic_category(self):
        if self.is_seen():
            self.category = 'g'
        elif self.is_traffic_close():
            self.category = 'r'
        else:
            self.category = 'y'



