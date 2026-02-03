# 🧙‍♂️ Invisible Cloak using OpenCV (with UI Panel)

A real-time **Invisible Cloak effect** using **OpenCV and Python**, inspired by Harry Potter 🪄.  
The project removes a selected cloak color from the video feed and replaces it with the captured background.

This version includes a **clean UI panel on the right side** with buttons for better user interaction.

---

## 📸 Demo Features
- Live webcam feed
- Capture background with one click
- Click to select cloak color
- Right-side UI panel for controls
- Real-time invisible cloak effect
- Cross-platform (Windows / macOS / Linux)

---

## 📁 Project Structure
Cloak_Invisibility/
│──requirement.txt
│── ui_entry_point.py # Main UI + camera handling
│── utils.py # Cloak (image processing) logic
│── README.md

▶️ How to Run
-- pip install requirement.txt
-- python ui_entry_point.py


## 🖱️ How to Use (Step-by-Step)
-Run the program
-Move away from the camera
-Click Capture BG (background is saved)
-Come back wearing a bright solid color cloth
-Click Start Cloak
-Click on the cloak color in the video
-✨ You become invisible!
-Press ESC to exit.


## 🧠 How It Works (Technical Overview)
-Capture a static background frame
-Convert video frames from BGR → HSV
-Detect the cloak color using HSV thresholding
-Create a binary mask for the cloak
-Remove the cloak region from current frame
-Replace it with the background region
-Merge and display final output in real time


## 🛠️ Known Limitations
-Works best with static backgrounds
-Sudden lighting changes may reduce accuracy
-Not suitable for multi-color cloaks (without tuning)

## 📜 License
-This project is for educational purposes.
-Feel free to modify and extend it.

