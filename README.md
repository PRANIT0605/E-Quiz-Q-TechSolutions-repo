Documentation for the project to explain its purpose and objectives:
INTRODUCTION:
The E-Quiz Web Application is a Python-based online quiz platform designed to provide users with an interactive and user-friendly environment to take quizzes across multiple categories. Developed using the Flask framework, HTML/CSS for the frontend, and text files for simple data storage, this application supports features like user registration, login authentication, category-wise quiz selection, automatic scoring, and result generation.
This platform aims to enhance learning and self-assessment through various quiz categories such as Technical, Entertainment, and Astronomy, while also providing an admin panel to monitor and manage users' data. It serves as a lightweight and efficient tool for both educational and entertainment purposes.

________________________________________

SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
1. Planning:
The project aims to develop an online quiz system accessible via a web interface. The from predefined text files. Flask serves as the backend framework, ensuring lightweight performance, while HTML and application includes user roles (user/admin), allows registration/login, and presents questions CSS ensure a clean UI. The project avoids complex databases and instead relies on local .txt files, making it easy to maintain and portable.
2. Defining Requirements:
•	Operating System: Windows/Linux/macOS
•	Programming Language: Python 3.7+
•	Framework: Flask
•	Frontend: HTML, CSS
•	Storage: Text files (questions.txt, users_data.txt)
•	Dependencies:
o	Flask
o	Jinja2
Installation can be done using pip install -r requirements.txt (or manually install Flask via pip install flask).
________________________________________
3. Designing:
System Architecture:
The application follows a 2-tier architecture:
•	Frontend: HTML templates rendered using Jinja2
•	Backend: Python (Flask) handling routes, logic, and file I/O
UI Design:
The user interface includes:
•	Home Page (index.html)
•	User Registration & Login (register.html, login.html)
•	Quiz Pages (quiz.html, technical_quiz.html, etc.)
•	Result Page (result.html)
•	Admin Dashboard (admin.html)

________________________________________
4. Building (Implementation):
Core files:
•	controller.py: Main application file handling routes and user logic.
•	utils.py: Helper functions for question retrieval, scoring, and validation.
•	questions.txt: Stores all questions categorized by quiz types.
•	users_data.txt: Stores registered user information.
Key Functionalities:
•	User Registration & Login
•	Quiz Category Selection
•	Question Parsing from .txt files
•	Scoring Mechanism
•	Admin Panel for User Overview
________________________________________
5. Testing:
•	Unit Testing: Individual functions for login, scoring, question parsing were tested.
•	Integration Testing: Verified the flow from registration to quiz submission and result display.
•	UI Testing: Manual testing on different browsers to check responsiveness and navigation.
•	Tools: Manual testing and simulated inputs for validation.

________________________________________
6. Deployment:
The application runs locally via Flask and can be deployed using WSGI servers like Gunicorn or hosted on platforms like Render, Heroku, or Replit.
Run using:
bash
python controller.py
________________________________________
CONCLUSION:
The E-Quiz Web Application successfully delivers an engaging, minimal, and functional solution for conducting online quizzes. With its simple file-based architecture, it is ideal for small-scale educational institutions or self-learning platforms. The project showcases the effective use of Python and Flask for backend logic and HTML/CSS for an interactive frontend.
________________________________________
PROCEDURE AND METHODS USED:
Procedure:
•	Designed HTML templates for user interaction.
•	Created Flask routes for handling quiz logic and user sessions.
•	Stored questions and users in text files for simplicity.
•	Implemented scoring and result display.
Methods Used:
•	Modular Python coding (via utils.py)
•	Flask routing and session handling
•	Template rendering using Jinja2
•	File I/O operations for data storage
________________________________________
ALGORITHM:
1.	Start Flask server and load templates.
2.	Accept user inputs via registration or login.
3.	Display category-wise quiz options.
4.	Load relevant questions from questions.txt.
5.	Record and compare answers.
6.	Calculate score and display result.
7.	For admins, show a summary of user data.
________________________________________
FUTURE SCOPE:
•	Add database support (SQLite/PostgreSQL) for scalability.
•	Include quiz timers and difficulty levels.
•	Allow quiz creation via admin dashboard.
•	Track user scores historically.
•	Mobile-friendly responsive design.
________________________________________
FUTURE ENHANCEMENTS:
•	Add email-based verification during registration.
•	Improve accessibility and keyboard navigation.
•	Export results as PDFs.
•	Integrate leaderboard functionality.
ADVANTAGES:
•	Easy to use and lightweight.
•	No need for complex database setups.
•	Web-based and device independent.
•	Modular code allows easy customization
