#EyeWare

## Inspiration
In 2019, close to 400 people in Canada died due to distracted drivers. They also cause an estimated $102.3 million worth of damages. While some modern cars have pedestrian collision avoidance systems, most drivers on the road lack the technology to audibly cue the driver if they may be distracted. We want to improve driver attentiveness and safety in high pedestrian areas such as crosswalks, parking lots, and residential areas. Our solution is more economical and easier to implement than installing a full suite of sensors and software onto an existing car, which makes it perfect for users who want peace of mind for themselves and their loved ones.


## What it does
EyeWare combines the eye-tracking capabilities of the AdHawk MindLink with the onboard camera to provide pedestrian tracking and driver attentiveness feedback through audio cues.

## How we built it
Using the onboard camera of the AdHawk MindLink, we pass video to the openCV machine learning algorithm to classify and detect people (pedestrians) based on their perceived distance from the user and assign them unique IDs. Simultaneously, we use the AdHawk Python API to track the user's gaze and cross-reference the detected pedestrians to ensure that the user has seen the pedestrian.

## Challenges we ran into
The biggest challenge was integrating the complex and cross-domain systems in little time. Over the last 36 hours, we learned and developed applications on mindFlex glasses, utilized object detection with YOLO (You only look once) machine learning algorithm and SORT object tracking algorithms. 

## Accomplishments that we're proud of
Getting the Adhawk mindlink to work with OpenCV was groundbreaking and enabled machine learning applications to run directly using mindlink’s stream. Furthermore, we got two major technologies working during this hackathon, both eye tracking and machine learning. The process was extremely complex and arduous and we are proud that we are able to accomplish it at the end.

## What we learned
In this hackathon, we had the privilege of working with AdHawk team on bring the flexmind eye tracking glasses to life. We learned so much about eye tracking APIs and the technologies as a whole. We also worked extensively with object detection algorithms like YOLO, OpenCV for image processing, and SORT algorithm for object tracking for temporal consistency


## What's next for Eyeware
Our platform is highly portable can be easily retrofitted to existing vehicles and be used by drivers around the world. We are excited to partner with OEMs and make this feature more widely available to people. Furthermore, we were limited by the mobile compute power at the hackathon, so removing that limit will also enable us to use more powerful object detection and tracking algorithms like deepSort.
