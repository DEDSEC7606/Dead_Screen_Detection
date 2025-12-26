# Productivity & Inactivity Detection System  
A lightweight FastAPI-based tool that analyzes screenshots to detect productivity, inactivity, and dead-screen conditions.  
The system works in two modes:  

 **Analyze (Manual Upload Mode)**
- User uploads multiple screenshots.
- System compares them pair-wise.
- If 3 consecutive screenshot pairs are almost identical → **Dead Screen**.
- If activity is low but not fully frozen → **Suspicious**.
- Otherwise → **Working / Productive**.

 2) **Analyze Range (Auto Screenshot Mode)**
- System auto-saves screenshots every fixed interval (ex: 60 seconds).
- When clicking 30 min / 1 hr / 2 hr:
  - All screenshots from that time range are fetched.
  - System compares all pairs and calculates:
    - Similarity
    - Frame Difference
    - Entropy
    - Cursor Movement
  - If 70% of the pairs are identical → **Dead Screen**
  - If 40–70% identical → **Suspicious**
  - Else → **Working**

---

## Features
- FastAPI backend  
- Screenshot hashing using gradient-based dHash  
- Cosine similarity scoring  
- Entropy calculation  
- Cursor detection  
- Auto-caching for faster performance  
- Clean UI with holographic buttons  
- Time-based screenshot filtering  

---

 Project Structure

project/
│── app.py
│── utils_range.py
│── requirements.txt
│── README.md
│── how_to_use.txt
│── auto_capture.py
│── uploads/
│── auto_screens/
│── templates/
│ └── index.html
│── static/
| └──script.js
├ └──style.css
| └──bg.jpg
  └──favicon.png

---

 Installation

1) Create a virtual environment

python3 -m venv venv
source venv/bin/activate


2) Install required libraries

pip install -r requirements.txt


3) Start the FastAPI server

uvicorn app:app --reload


4) Open the UI
Go to:

http://127.0.0.1:8000


---

Enabling Auto Screenshot Capture

Run this script in a **separate terminal**:

python3 auto_capture.py


This saves screenshots into the **auto_screens/** folder automatically.

---

 Logic Summary

### Manual Upload Mode
- Compares consecutive screenshot pairs  
- Checks:
  - Similarity (dHash + cosine)
  - Frame difference
  - Entropy
  - Cursor movement  
- If 3 pairs in a row are too similar → Dead Screen

### Time Range Mode
- Collects N screenshots in the selected duration
- Calculates similarity percentages  
- Dead screen ratio threshold decides final verdict

---

##  Outputs
Each analysis returns:

```json
{
  "verdict": "Working / Productive",
  "avg_similarity": 58.3,
  "suspicion": 22.1,
  "productivity": 77.9
}

Notes

    System is optimized with caching for speed.

    Screenshots must be PNG/JPG.

    Auto screenshots should have timestamps in filename.

 Contact

Made by Ajey
FastAPI + Computer Vision Project


---


