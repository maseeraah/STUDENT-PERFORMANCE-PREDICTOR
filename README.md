STUDENT PERFORMANCE PREDICTOR

OVERVIEW
The Student Performance Predictor is a basic console-based Python program that utilizes linear regression to forecast a student's exam score based on two distinct inputs:
- Hours spent studying
- Attendance Percentage  

The aim of the project is to highlight basic concepts of Artificial Intelligence and Machine Learning: problem solving agents, knowledge representation, probability/statistics, supervised learning basics. This project has been built to fit within the syllabus for an academic project.

FEATURES
- Create and train a linear regression model using a small dataset of student records.
- Test your model's accuracy by using **Mean Squared Error (MSE)** on both the training and validation set.
- Accept input from the user (hours studied, attendance percent) to predict exam score.
- Thorough inline comments for every step of the algorithm.
- Build to be light weight and beginner friendly - no external libraries needed!

TECHNOLOGIES/TOOLS USED
- Python 3.x (core language)
- Random module (for shuffling dataset)
- Basic math functionality (for simple gradient descent and error calculation)
- Console I/O (for user input)

STEPS TO INSTALL AND RUN
1. Verify that you have Python 3.x installed on your system.
2. Download or copy the project file:  
   `student_performance_predictor.py`
3. Open a terminal/command prompt from the directory of the project.
4. Program can then be run by:  
   ```bash
   python student_performance_predictor.py

SCREENSHOT FOR THE OUTPUT
<img width="2560" height="1440" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/78fbf75f-93dc-4fef-9881-27b157c187a6" />

GUIDLINES FOR TESTING
Upon starting the application, it will:
Train the regression model on some sample student data.
Show learned weights and MSEs for both the training and validation sets.
You will be asked for:
Hours studied (for example, 4.5)
Attendance rate (between 0 and 1, for example, .85), and
it will then produce a predicted exam score based on your input.
Feel free to try different values to see how predictions adjust.
