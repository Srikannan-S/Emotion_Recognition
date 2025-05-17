😊 Real-Time Facial Emotion Recognition using OpenCV

This project uses the `facial_emotion_recognition` library with OpenCV to detect and classify human emotions in real-time through a webcam.

🔥 Features

1. Real-time emotion recognition from webcam feed  
2. Detects emotions like Happy, Sad, Angry, Neutral, etc.  
3. Uses deep learning under the hood (via facial_emotion_recognition)  
4. Displays the emotion label on the video frame  
5. Runs on CPU by default  

🚀 Technologies Used

1. Python – Programming language  
2. OpenCV – For accessing and displaying webcam feed  
3. facial_emotion_recognition – Emotion classification library  

⚙️ Installation & Usage

1. Clone the repository:
   ```bash 
   git clone https://github.com/yourusername/facial-emotion-recognition.git  
   cd facial-emotion-recognition
   ```

2. Install required packages:
   ``bash
   pip install facial_emotion_recognition opencv-python  
   ```
   
3. Run the script:  
   ```bash
   python app.py
   ```

🛠️ How It Works

- Captures video from the system’s webcam  
- Passes each frame to `facial_emotion_recognition`  
- The model processes and predicts the emotion  
- The predicted emotion label is drawn directly on the video  
- Continues until you press the `Esc` key  

📂 Project Structure
```bash
📂facial-emotion-recognition  
├── app.py         # Main Python script  
└── README.md      # Project documentation
``` 
