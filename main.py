from ast import Continue
from classes import *
from cv2 import cv2
from playsound import playsound
import multiprocessing

tracked_objs = {} # keeps all the stuff we are tracking
labels = [] # all the labels currently in frame
LAST_SEEN_BUFFER = 5 # if not seen in 5 frames, we delete it

play_sound = False


def process_objects(frame):
    play_sound = False
    for label in labels:
        if label.id in tracked_objs.keys():
            # update coordiante
            tracked_objs[label.id].rect = label.rect
        else:
            tracked_objs[label.id] = Traffic(label.id, label.rect)
        
        tracked_objs[label.id].last_seen = 0
        obj_seen = tracked_objs[label.id].is_traffic_seen()
        obj_close = tracked_objs[label.id].is_traffic_close()
        tracked_objs[label.id].get_traffic_category()
        
        if (obj_seen):
            cv2.rectangle(frame, tracked_obj.rect, 1, (0, 255, 0)) #green
        elif (obj_close):
            cv2.rectangle(frame, tracked_obj.rect, 2, (255, 0, 0)) #red
            play_sound = True
        else:
            cv2.rectangle(frame, tracked_obj.rect, 1, (255, 255, 0)) #yellow

        cv2.putText(frame, str(label.id), tracked_obj.center, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

    # remove images outside of frame    
    for key, tracked_obj in tracked_objs.items():
        tracked_obj.last_seen += 1

        if tracked_obj.last_seen > LAST_SEEN_BUFFER:
            del tracked_objs[key]

    #process each inframe 

def play_warning_sound():
    p = multiprocessing.Process(target=playsound, args=("/sound/soundeffect.mp3",))
    if (play_sound):
        p.start()
    else:
        p.terminate()


def main():
    # fetch data from glasses (mat, x,y)

    # object tracking: list(obj(label, cv2.Rect))

    process_objects()

    play_warning_sound()
    Continue