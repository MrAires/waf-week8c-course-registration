from flask import Flask, render_template, request

app = Flask(__name__)
registrations = []

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        student_name = request.form.get('student_name', '').strip()
        roll_number = request.form.get('roll_number', '').strip()
        course = request.form.get('course', '').strip()
        if student_name and roll_number and course:
            registrations.append({
                'student_name': student_name,
                'roll_number': roll_number,
                'course': course
            })
            message = 'Course registered successfully!'
    return render_template('index.html', registrations=registrations, message=message)

if __name__ == '__main__':
    app.run(debug=True)
