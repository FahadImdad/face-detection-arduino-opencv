import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

# Initialize camera
cap = cv2.VideoCapture(0)

# Initialize face detector
detector = FaceDetector()

# Initialize serial communication with Arduino (update COM port if needed)
arduino = SerialObject('COM4')

while True:
    # Capture frame from webcam
    success, img = cap.read()

    if not success:
        print("Failed to capture image")
        continue

    # Detect faces in the frame
    img, bounding_boxes = detector.findFaces(img)

    if bounding_boxes:
        arduino.sendData([1, 0])  # Send (1,0) → Yellow LED ON, Red LED OFF
    else:
        arduino.sendData([0, 1])  # Send (0,1) → Yellow LED OFF, Red LED ON

    # Display the video feed
    cv2.imshow("Video", img)

    # Wait for 1 millisecond, exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
