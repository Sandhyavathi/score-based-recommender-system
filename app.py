from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('study_plan_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def index():
    return render_template('quiz.html')

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.json
    score = data['score']
    return jsonify({'score': score}), 200

def get_study_plan(score):
    input_data = [f"Student scored {score}%"]
    input_tfidf = vectorizer.transform(input_data)
    study_plan_text = model.predict(input_tfidf)[0]

    # Split the study plan into structured sections
    sections = study_plan_text.split("Goal: ")
    title = sections[0].strip()
    
    goal_and_weeks = sections[1].split("Week ")
    goal = goal_and_weeks[0].strip()
    
    weeks = []
    for week_info in goal_and_weeks[1:]:
        week_parts = week_info.split("Resources:")
        week_title = "Week " + week_parts[0].strip()
        resources = [res.strip() for res in week_parts[1].split("-") if res.strip()]
        
        weeks.append({
            "title": week_title,
            "resources": resources
        })

    return {
        "title": title,
        "goal": goal,
        "weeks": weeks
    }

@app.route('/show-study-plan')
def show_study_plan():
    score = request.args.get('score', default=0, type=int)
    study_plan = get_study_plan(score)
    return render_template('study-plan.html', score=score, study_plan=study_plan)

if __name__ == '__main__':
    app.run(debug=True)

