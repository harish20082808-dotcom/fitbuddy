# 🏋️ FitBuddy – AI Fitness Plan Generator using Gemini Models

> An AI-driven fitness and nutrition assistant built with **FastAPI**, **SQLite (SQLAlchemy ORM)**, and **Google Gemini 1.5 Pro & Flash** models. FitBuddy generates tailored 7-day workout routines, provides real-time nutrition tips, and supports continuous plan refinement through AI-powered user feedback.

---

## 🌟 Key Features

1. **AI 7-Day Workout Generation (Gemini 1.5 Pro)**:
   - Takes user profile parameters: name, age, weight, goal (e.g., muscle gain, weight loss, wellness), and intensity (low, medium, high).
   - Generates a day-by-day regimen formatted with warm-up, targeted exercises, sets/reps, and cooldowns.
2. **Contextual Nutrition Tips (Gemini Flash)**:
   - Delivers concise, actionable nutrition and recovery guidance tailored to the user's specific fitness objective.
   - Calculates macronutrient targets (calories, protein, carbohydrates, fats, hydration).
3. **Dynamic Feedback Loop (Gemini 1.5 Pro)**:
   - Allows users to request modifications (e.g., "Add more cardio", "Include yoga on rest days").
   - Intelligently revises the workout plan while preserving established progress.
4. **Admin Oversight Dashboard (`/view-all-users`)**:
   - Comprehensive admin view displaying all registered users, original AI plans, and revised plans in a structured table.
   - Allows administrators and trainers to monitor client progression and delete inactive profiles.
5. **Interactive OpenAPI / Swagger Documentation (`/docs`)**:
   - Built-in FastAPI Swagger interface to test all REST endpoints directly.

---

## 📁 Project Architecture & Directory Structure

```
Fitbuddy/
│
├── requirements.txt            # Python dependencies
├── .env                        # Local environment variables (API keys)
├── .env.example                # Example environment configuration
├── fitbuddy.db                 # Auto-generated SQLite database
├── README.md                   # Full setup and user guide
│
├── app/
│   ├── __init__.py             # Package marker
│   ├── main.py                 # FastAPI application entry point
│   ├── routes.py               # Core route handlers (Web & REST API)
│   ├── database.py             # SQLAlchemy models & CRUD operations
│   ├── schemas.py              # Pydantic schemas for data validation
│   ├── gemini_generator.py     # Gemini 1.5 Pro workout generation logic
│   ├── gemini_flash_generator.py # Gemini Flash nutrition tip generator
│   ├── updated_plan.py         # Feedback-based plan revision logic
│   └── nutrition.py            # Macronutrient & caloric calculation engine
│
├── templates/
│   ├── index.html              # Modern gym-themed input form
│   ├── result.html             # Workout plan, nutrition tip & feedback UI
│   └── all_users.html          # Admin dashboard for user oversight
│
└── static/
    ├── css/
    │   └── style.css           # Custom scrollbars & glassmorphism styles
    └── images/
        └── gym-bg.jpg          # Atmospheric dark fitness gym background
```

---

## 🚀 Step-by-Step VS Code Setup & Installation Guide

### Step 1: Open the Project in VS Code
1. Launch **Visual Studio Code**.
2. Click **File** > **Open Folder...** (or press `Ctrl + K, Ctrl + O`).
3. Select the folder:
   ```
   C:\Users\K Rajan\.gemini\antigravity\scratch\Fitbuddy
   ```

### Step 2: Open an Integrated Terminal
- Press ``Ctrl + ` `` (or select **Terminal** > **New Terminal**).

### Step 3: Create & Activate Virtual Environment
Run the following commands in your VS Code terminal:

```powershell
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment on Windows PowerShell:
.\venv\Scripts\Activate.ps1
```
*(If PowerShell restricts script execution, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then activate).*

### Step 4: Install Dependencies
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 5: Configure your Google Gemini API Key
1. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).
2. Open the `.env` file in the root of `Fitbuddy/` and add your key:
   ```env
   GOOGLE_API_KEY=AIzaSyYourActualKeyHere
   ```
> **Note:** FitBuddy includes an automatic built-in fallback generator. If no key is provided, the application will still run smoothly and display structured workout plans and nutrition tips for testing.

---

## 🏃 Running the Application

In your terminal (with the virtual environment activated), start the FastAPI server:

```powershell
python -m uvicorn app.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
Database initialized successfully.
INFO:     Application startup complete.
```

---

## 🌐 Navigating the Website

| URL | Description |
| :--- | :--- |
| **`http://127.0.0.1:8000/`** | **Home / Plan Generator**: Fill in Name, User ID, Age, Weight, Goal, and Intensity. |
| **`http://127.0.0.1:8000/view-all-users`** | **Admin Dashboard**: View all registered trainees, original plans, feedback revisions, and manage users. |
| **`http://127.0.0.1:8000/docs`** | **Interactive API Docs (Swagger)**: Test REST endpoints directly in browser. |

---

## 🧪 Testing the Complete Workflow

1. **Generate Workout Plan**:
   - Go to `http://127.0.0.1:8000/`.
   - Enter:
     - Name: `Alex Rivera`
     - User ID: `101`
     - Age: `28`
     - Weight: `75`
     - Goal: `Muscle Gain & Hypertrophy`
     - Intensity: `High`
   - Click **Generate 7-Day Plan**.
   - Review your day-by-day workout routine, Gemini Flash nutrition tip, and macronutrient targets.

2. **Test Feedback Refinement**:
   - On the results page, in the **Refine & Customize Your Routine** section, click `+ More Cardio` or type:
     ```
     Add 15 minutes of cardio at the end of each session and include yoga on Day 4.
     ```
   - Click **Regenerate & Refine Plan**.
   - Notice the updated plan with the revisions applied.

3. **Check Admin View**:
   - Click **Admin Dashboard** in the navigation bar (or visit `http://127.0.0.1:8000/view-all-users`).
   - Confirm user `#101` is listed with both their original and updated plans.
