"""
FitBuddy - End-to-end Integration Test
Verifies all routes, templates, database operations, and AI fallback responses.
"""

from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db

# Initialize database
init_db()

client = TestClient(app)

def run_tests():
    print("Testing FitBuddy Application Routes...")

    # 1. Test Home page
    res_home = client.get("/")
    assert res_home.status_code == 200, f"Expected 200, got {res_home.status_code}"
    assert "FitBuddy" in res_home.text
    print(" [1/6] GET / (Home page) passed.")

    # 2. Test Plan Generation (Web Form)
    form_data = {
        "user_id": 999,
        "name": "Sarah Connor",
        "age": 29,
        "weight": 62.5,
        "goal": "Weight Loss",
        "intensity": "High"
    }
    res_gen = client.post("/generate-workout", data=form_data)
    assert res_gen.status_code == 200, f"Expected 200, got {res_gen.status_code}"
    assert "Sarah Connor" in res_gen.text
    assert "Day 1:" in res_gen.text
    print(" [2/6] POST /generate-workout passed.")

    # 3. Test Feedback submission
    feedback_data = {
        "user_id": 999,
        "feedback": "Add 15 minutes of cardio and yoga on rest days"
    }
    res_fb = client.post("/submit-feedback", data=feedback_data)
    assert res_fb.status_code == 200, f"Expected 200, got {res_fb.status_code}"
    assert "cardio" in res_fb.text.lower()
    print(" [3/6] POST /submit-feedback passed.")

    # 4. Test Admin dashboard
    res_admin = client.get("/view-all-users")
    assert res_admin.status_code == 200, f"Expected 200, got {res_admin.status_code}"
    assert "Sarah Connor" in res_admin.text
    assert "999" in res_admin.text
    print(" [4/6] GET /view-all-users (Admin dashboard) passed.")

    # 5. Test Nutrition Tip API
    res_tip = client.get("/nutrition-tip?goal=Muscle+Gain")
    assert res_tip.status_code == 200, f"Expected 200, got {res_tip.status_code}"
    data = res_tip.json()
    assert "nutrition_tip" in data
    print(" [5/6] GET /nutrition-tip API passed.")

    # 6. Test Workout Generation API
    res_api_workout = client.post("/generate-workout/gemini", json={"goal": "Endurance", "intensity": "Medium"})
    assert res_api_workout.status_code == 200, f"Expected 200, got {res_api_workout.status_code}"
    assert "workout_plan" in res_api_workout.json()
    print(" [6/6] POST /generate-workout/gemini API passed.")

    print("\nALL 6 TEST CASES PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
