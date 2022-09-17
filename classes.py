from cv2 import cv2

TRAFFIC_WIDTH_LIMIT = 100
CENTER_TRAFFIC_WIDTH_LIMIT = 50
CENTER_OFFSET = 50

class Label:
    def __init__(self,id, type, rect):
        self.id = id
        self.rect = rect

class Traffic:
    def __init__(self, id, rect, is_seen=False, is_close=False, last_seen=0):
        self.id = id
        self.rect = rect
        self.is_seen = is_seen
        self.is_close = is_close
        self.last_seen = last_seen
        self.center = (self.rect.x + self.rect.width/2, self.rect.y - self.rect.height/2)

    def is_traffic_seen(self, eye_track_coor):
        # traffic that's seen can't be unseen
        if self.is_seen or self.rect.contains(eye_track_coor):
            self.is_seen = True
        return self.is_seen
    
    def is_traffic_close(self):
        # if it's super close then it's close
        # 100 is arbritary
        if self.rect.width > TRAFFIC_WIDTH_LIMIT: 
            self.is_close = True
        
        # or if it's somewhat close but it's near the center
        elif ((self.rect.width > CENTER_TRAFFIC_WIDTH_LIMIT) and (pow(self.center[0]),2 + pow(self.center[1]),2 < CENTER_OFFSET)):
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



