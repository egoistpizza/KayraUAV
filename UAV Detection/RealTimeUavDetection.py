"""
* Bu kod OpenCV modülü kullanılarak YOLO bazlı gerçek zamanlı UAV tespiti yapılmasını sağlamaktadır.
* Kullanımı, YoloTrain.py üzerinden eğitim sonucu sağlanan değerlerin katkısıyla gerçekleşmektedir.
! Kod henüz testlere tabi tutulmamıştır.
TODO: Testler hazırlanacak.
"""

import cv2
import numpy as np

def detect_drones(model, classes, colors, webcam=0):
    # Initialize webcam
    cap = cv2.VideoCapture(webcam)
    # Set video frame width and height
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        # Get current frame from webcam
        ret, frame = cap.read()

        if ret:
            # Pass frame through model
            output = model(frame)

            # Iterate through detections
            for detection in output:
                x, y, w, h, conf, cls_conf, cls_pred = detection

                # Get bounding box coordinates
                x1, y1, x2, y2 = x - w / 2, y - h / 2, x + w / 2, y + h / 2

                # Get class index
                class_index = int(cls_pred)

                # Get class name
                class_name = classes[class_index]

                # Get color for this class
                color = colors[class_index]

                # Draw bounding box
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)

                # Draw label
                cv2.putText(frame, class_name, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Show output frame
            cv2.imshow("Drone Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release webcam
    cap.release()
    cv2.destroyAllWindows()

# Define classes and colors
classes = ["drone"]
colors = [(0, 0, 255)]

# Load trained model
model = torch.load("trained_weights.pth")

# Start drone detection
detect_drones(model, classes, colors)
