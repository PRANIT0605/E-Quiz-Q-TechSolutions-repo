from flask import Flask, render_template, request, redirect, session, url_for
import os
import time

app = Flask(__name__)
app.secret_key = 'quiz_secret_key'

USER_DATA_FILE = 'users_data.txt'
QUESTIONS_FILE = 'questions.txt'

# Admin credentials
ADMIN_EMAIL = "admin@quiz.com"
ADMIN_PASSWORD = "admin123"

# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if email already exists
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            users = [line.strip().split(',')[0] for line in f]
            if email in users:
                return "Email already registered! Please log in."

        # Save new user and auto-login
        with open(USER_DATA_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{email},{password}\n")
        session['user'] = email
        return redirect(url_for('user'))

    return render_template('register.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('admin'))

        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                saved_email, saved_password = line.strip().split(',')
                if email == saved_email and password == saved_password:
                    session['user'] = email
                    return redirect(url_for('user'))

        return render_template('invalid.html')  # Invalid login

    return render_template('login.html')


# User Dashboard
@app.route('/user')
def user():
    if 'user' in session:
        return render_template('user.html')
    return redirect(url_for('login'))


# Admin Page
@app.route('/admin')
def admin():
    if 'admin' in session:
        return render_template('admin.html')
    return redirect(url_for('login'))


# Add Questions (Admin Only)
@app.route('/add_question', methods=['POST'])
def add_question():
    if 'admin' not in session:
        return redirect(url_for('login'))

    quiz_type = request.form['quiz_type']
    question = request.form['question']
    option1 = request.form['option1']
    option2 = request.form['option2']
    option3 = request.form['option3']
    option4 = request.form['option4']
    answer = request.form['answer']

    # Save question to file
    with open(QUESTIONS_FILE, 'a', encoding='utf-8') as file:
        file.write(f"{quiz_type}|{question}|{option1}|{option2}|{option3}|{option4}|{answer}\n")

    return redirect(url_for('admin'))


# Modify User Credentials (Admin Only)
@app.route('/modify_user', methods=['POST'])
def modify_user():
    if 'admin' not in session:
        return redirect(url_for('login'))

    email = request.form['email']
    new_password = request.form['new_password']
    updated_data = []

    # Update user credentials
    with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            saved_email, saved_password = line.strip().split(',')
            if saved_email == email:
                updated_data.append(f"{email},{new_password}\n")
            else:
                updated_data.append(line)

    with open(USER_DATA_FILE, 'w', encoding='utf-8') as file:
        file.writelines(updated_data)

    return redirect(url_for('admin'))


# Delete User Profile (Admin Only)
@app.route('/delete_user', methods=['POST'])
def delete_user():
    if 'admin' not in session:
        return redirect(url_for('login'))

    email = request.form['email']
    updated_data = []

    # Remove user from file
    with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.startswith(email):
                updated_data.append(line)

    with open(USER_DATA_FILE, 'w', encoding='utf-8') as file:
        file.writelines(updated_data)

    return redirect(url_for('admin'))


# Start Quiz
@app.route('/quiz/<quiz_type>', methods=['GET', 'POST'])
def quiz(quiz_type):
    if 'user' not in session:
        return redirect(url_for('login'))

    questions = []
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('|')
            if parts[0] == quiz_type:
                questions.append({
                    'question': parts[1],
                    'options': parts[2:6],
                    'answer': parts[6]
                })

    start_time = time.time()  # Start timer

    if request.method == 'POST':
        elapsed_time = time.time() - start_time
        if elapsed_time > 600:  # 10 minutes = 600 seconds
            return render_template('result.html', score=0, total=len(questions), timeout=True)

        score = 0
        for i, q in enumerate(questions):
            user_ans = request.form.get(f'q{i}', '').strip().lower()
            correct_ans = q['answer'].strip().lower()
            if user_ans == correct_ans:
                score += 1

        # Get user's answers for all questions
        user_answers = []
        for i in range(len(questions)):
            user_answers.append(request.form.get(f'q{i}'))
        
        return render_template('result.html',
                            score=score,
                            total=len(questions),
                            questions=questions,
                            user_answers=user_answers,
                            timeout=False)

    return render_template('quiz.html', questions=questions, quiz_type=quiz_type, start_time=start_time)


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
