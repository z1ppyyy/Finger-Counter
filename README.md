# Finger-Counter
Finger Counter using Mediapipe and OpenCV

This project is a finger counter implemented in Python, leveraging Mediapipe and OpenCV libraries. The application captures real-time video feed from a webcam, detects hand landmarks, and counts the number of fingers shown. It then overlays corresponding images and annotations onto the video feed based on the detected finger count.

# Table of contents
• [Features](https://github.com/z1ppyyy/Finger-Counter?tab=readme-ov-file#features) 

• [Requirements](https://github.com/z1ppyyy/Finger-Counter?tab=readme-ov-file#requirements)

• [Usage](https://github.com/z1ppyyy/Finger-Counter?tab=readme-ov-file#usage)

• [Result](https://github.com/z1ppyyy/Finger-Counter#result)

• [Hand Landmarks](https://github.com/z1ppyyy/Finger-Counter?tab=readme-ov-file#hand-landmarks)

• [Contributing](https://github.com/z1ppyyy/Finger-Counter?tab=readme-ov-file#contributing)

• [Help](https://github.com/z1ppyyy/Finger-Counter?tab=readme-ov-file#help)

• [License](https://github.com/z1ppyyy/Finger-Counter?tab=readme-ov-file#license)

# Features
• Real-time hand detection and finger counting.

• Displays the number of fingers detected on the screen.

• Simple and efficient implementation using Mediapipe and OpenCV.

• Easy to run and customize for various hand gesture recognition tasks.

# Requirements
To use this program you have to install follownig libraries: 
• <b>Python 3.7+</b>
• <b>OpenCV</b>
• <b>Mediapipe<b>

# Usage
1. Run the finger counter script:
   
```
python counter.py
```
2. A window will open displaying the webcam feed with the number of fingers detected.

# Result
![counter](https://github.com/z1ppyyy/Finger-Counter/assets/139076325/ea65cf33-e0f9-40d0-9db3-7bb64fb27a10)


# Hand Landmarks
![hand_landmarks](https://github.com/z1ppyyy/Finger-Counter/assets/139076325/d897b1c1-9d33-43a4-ad67-ee180a751dbc)

# Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to fork the repository and create a pull request.

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Submit a pull request to the main repository.

Please ensure that your contributions align with the project's coding style, guidelines, and licensing.

# Help
You might encounter issues with the webcam not displaying correctly or errors occurring. 
To resolve this, try adjusting the value in the following line (e.g., change it to 1):
```
cap = cv.VideoCapture(0)
```

# License
The Finger Counter is open-source software released under the MIT License.

Feel free to customize this guide page based on your specific implementation and project requirements.
