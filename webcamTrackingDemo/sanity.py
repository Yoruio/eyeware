# import the opencv library
import cv2
import imutils

# Initializing the HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Reading the Image

cap = cv2.VideoCapture(0)




while(True):
    ret, image = cap.read()
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    # Resizing the Image
    # image = imutils.resize(image,width=min(400, image.shape[1]))

    # Detecting all the regions in the image that has a pedestrians inside it
    (regions, _) = hog.detectMultiScale(image,winStride=(4, 4),padding=(4, 4),scale=1.05)

    # Drawing the regions in the Image
    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y),(x + w, y + h),(0, 0, 255), 2)


    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('capture.jpg', image)
        break

cap.release()
cv2.destroyAllWindows()

