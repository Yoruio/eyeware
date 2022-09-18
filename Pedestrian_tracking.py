from BoundingBox import BoundingBox
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
class CentroidTracker():
    def __init__(self, maxDisappeared=25):
        # Init object Id autoincrement
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()

        self.maxDisappeared = maxDisappeared

    def register(self, centroid, bounding_boxes, rect):
        print(f"registering: {str(rect)}")
        # use auto-increment ID, to create new object
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] = 0
        bounding_boxes[self.nextObjectID] = BoundingBox(rect, 1)
        self.nextObjectID += 1
        

    def deregister(self, objectID, bounding_boxes):
        # delete object from objects, dissapeared, and bounding box dirs
        del self.objects[objectID]
        del self.disappeared[objectID]
        del bounding_boxes[objectID]
    
    # rects: from ML
    # bounding_boxes is dictionary of id -> BoundingBox
    def update(self, rects, bounding_boxes):
		# check to see if the list of input bounding box rectangles
		# is empty
        if len(rects) == 0:

            # Dissapear appropriate objects
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID, bounding_boxes)
            return self.objects

        inputCentroids = np.zeros((len(rects), 2), dtype="int")
		# loop over the bounding box rectangles
        for (i,rect) in enumerate(rects):
			# use the bounding box coordinates to derive the centroid
            inputCentroids[i] = rect[2]
		# No additional logic needed if nothing to compare to
        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i], bounding_boxes, rects[i][1])
        else:
            # grab the set of object IDs and corresponding centroids
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())
            # map all centroid distances
            D = dist.cdist(np.array(objectCentroids), inputCentroids)

            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]
            usedRows = set()
            usedCols = set()

            # loop over the combination of the (row, column) index
            # tuples
            for (row, col) in zip(rows, cols):
                # ignore rows that have been seen
                if row in usedRows or col in usedCols:
                    continue
                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                # only change bounding boxes if all coordinates are valid
                if (rects[col][1][0] > 0 and rects[col][1][1] > 0 and rects[col][1][2] > 0 and rects[col][1][3] > 0):
                    bounding_boxes[objectID].rect = rects[col][1]
                self.disappeared[objectID] = 0
                usedRows.add(row)
                usedCols.add(col)

            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)

            if D.shape[0] >= D.shape[1]:
                # loop over the unused row indexes
                for row in unusedRows:
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1
                    # deregistr old objects that are not present in curren frame
                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID, bounding_boxes)
            else:
                # Register new objects that werent present in previous frames
                for col in unusedCols:
                    self.register(inputCentroids[col], bounding_boxes, rects[col][1])
        # return the set of trackable objects
        return self.objects