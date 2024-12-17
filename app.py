from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to check password complexity
def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=" for c in password)

    criteria = {
        'Length': length >= 8,
        'Uppercase Letter': has_upper,
        'Lowercase Letter': has_lower,
        'Digit': has_digit,
        'Special Character': has_special
    }

    strength = sum(criteria.values())

    if strength == 5:
        return "Strong", criteria
    elif strength >= 3:
        return "Medium", criteria
    else:
        return "Weak", criteria

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# API route for checking password strength
@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password', '')
    strength, criteria = check_password_strength(password)
    return jsonify({'strength': strength, 'criteria': criteria})

if __name__ == '__main__':
    app.run(debug=True)
