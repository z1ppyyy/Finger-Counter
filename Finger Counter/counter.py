import cv2 as cv
import mediapipe as mp
import math

# Turn on the camera
cap = cv.VideoCapture(0)

# Reading the finger count images
finger0 = cv.imread('Images/0.jpeg')
finger0_h,finger0_w,_ = finger0.shape

finger1 = cv.imread('Images/1.jpeg')
finger1_h,finger1_w,_ = finger1.shape

finger2 = cv.imread('Images/2.jpeg')
finger2_h,finger2_w,_ = finger2.shape

finger3 = cv.imread('Images/3.jpeg')
finger3_h,finger3_w,_ = finger3.shape

finger4 = cv.imread('Images/4.jpeg')
finger4_h,finger4_w,_ = finger4.shape

finger5 = cv.imread('Images/5.jpeg')
finger5_h,finger5_w,_ = finger5.shape

# Initialize Mediapipe Hands model
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# Drawing utils for hand landmarks
mpDraw = mp.solutions.drawing_utils
drawSpec1 = mpDraw.DrawingSpec(color=(0,255,0), thickness=3, circle_radius=3)
drawSpec2 = mpDraw.DrawingSpec(color=(255,0,0), thickness=3, circle_radius=3)


while True:
    success, img = cap.read() # Read a frame from the camera
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB) # Convert the image to RGB
    results = hands.process(imgRGB) # Process the image to detect hands
    
    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS,drawSpec1, drawSpec2)
            
            finger = []
            # Extract landmark coordinates
            for id,lm in enumerate(handLms.landmark):
                ih, iw, ic = img.shape
                x,y = int(lm.x * ih), int(lm.y * iw)
                finger.append([x,y])

            if finger:
                # Assign coordinates to each finger landmark
                pinky_finger = finger[4]
                ring_finger = finger[8]
                middle_finger = finger[12]
                index_finger = finger[16]
                thumb_finger = finger[20]
                bottom_hand = finger[0]
                ring_mcp = finger[13]
                thumb_mcp = finger[5]

                x1,y1 = pinky_finger
                x2,y2 = ring_finger
                x3,y3 = middle_finger
                x4,y4 = index_finger
                x5,y5 = thumb_finger
                x6, y6 = bottom_hand
                x7,y7 = ring_mcp
                x8,y8 = thumb_mcp

                # Calculate distances between landmarks
                lenght_index_pinky = math.sqrt((x4-x1) **2 + (y4-y1) **2)
                lenght_middle_pinky = math.sqrt((x3-x1) **2 + (y3-y1) **2)
                lenght_index_ring = math.sqrt((x4-x2) **2 + (y4-y2) **2)
                lenght_thumb_pinky = math.sqrt((x5-x1) **2 + (y5-y1) **2)
                lenght_index_middle = math.sqrt((x4-x3) **2 + (y4-y3) **2)
                lenght_thumb_index = math.sqrt((x5-x4) **2 + (y5-y4) **2)
                lenght_bottom_hand_index = math.sqrt((x6-x4) **2 + (y6-y4) **2)
                lenght_thumb_ring = math.sqrt((x5-x2) **2 + (y5-y2) **2)
                lenght_thumb_middle = math.sqrt((x5-x3) **2 + (y5-y3) **2)
                lenght_ring_mcp_pinky = math.sqrt((x7-x1) **2 + (y7-y1) **2)
                lenght_thumb_mcp_thumb = math.sqrt((x8-x5) **2 + (y8-y5) **2)
                lenght_bottom_hand_middle = math.sqrt((x6-x5) **2 + (y6-y5) **2)


                # Coordinates for the overlay images
                x = 0
                y = 0

                # Determine the number of raised fingers based on calculated lengths
                if lenght_middle_pinky > 260 and lenght_ring_mcp_pinky > 110 and lenght_bottom_hand_index > 500:
                    cv.rectangle(img, (0,550), (300,300), (128,128,128), -1)
                    cv.putText(img, '5', (115,490), cv.FONT_HERSHEY_DUPLEX, 4, (255,255,255), 3,cv.LINE_AA) 
                    img[ y:y+finger5_h, x:x+finger5_w] = finger5   

                elif lenght_ring_mcp_pinky < 115 and lenght_bottom_hand_index > 400 and lenght_bottom_hand_middle > 400:
                    cv.rectangle(img, (0,550), (300,300), (128,128,128), -1)
                    cv.putText(img, '4', (115,490), cv.FONT_HERSHEY_DUPLEX, 4, (255,255,255), 3,cv.LINE_AA)      
                    img[ y:y+finger4_h, x:x+finger4_w] = finger4

                elif lenght_thumb_pinky < 200 and lenght_thumb_index > 240:
                    cv.rectangle(img, (0,550), (300,300), (128,128,128), -1)
                    cv.putText(img, '3', (115,490), cv.FONT_HERSHEY_DUPLEX, 4, (255,255,255), 3,cv.LINE_AA)     
                    img[ y:y+finger3_h, x:x+finger3_w] = finger3

                elif lenght_index_middle > 150 and lenght_thumb_pinky < 300:
                    cv.rectangle(img, (0,550), (300,300), (128,128,128), -1)
                    cv.putText(img, '2', (115,490), cv.FONT_HERSHEY_DUPLEX, 4, (255,255,255), 3,cv.LINE_AA) 
                    img[y:y+finger2_h, x:x+finger2_w ] = finger2

                elif lenght_index_pinky < 200 and lenght_index_middle < 120 and lenght_index_ring > 250:
                    cv.rectangle(img, (0,550), (300,300), (128,128,128), -1)
                    cv.putText(img, '1', (115,490), cv.FONT_HERSHEY_DUPLEX, 4, (255,255,255), 3,cv.LINE_AA) 
                    img[y:y+finger1_h, x:x+finger1_w ] = finger1
                
                elif lenght_bottom_hand_index < 500 and lenght_thumb_ring < 220:
                    cv.rectangle(img, (0,550), (300,300), (128,128,128), -1)
                    cv.putText(img, '0', (115,490), cv.FONT_HERSHEY_DUPLEX, 4, (255,255,255), 3,cv.LINE_AA) 
                    img[y:y+finger0_h, x:x+finger0_w ] = finger0


    # Display the image
    cv.imshow('Finger Counter', img)
    # Exit the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv.destroyAllWindows()