from flask import Flask, render_template, request, url_for, flash, redirect
import random
import yagmail

# ...
app = Flask(__name__)

app.config['SECRET_KEY'] = '4a1d09035fc3ca2f6019e2c11c3755b30f2fa8cc4a7f790a'
messages = []



def generate(length, let, spec, num, cap):
    valid = False
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    nf = False
    pswd = []
    password = ""
    # checks if values are all set to OFF
    if num == False and let == False and cap == False and spec == False:
        # showinfo("unable to create password", "this is because all values are set to OFF")
        nf = True
    # Loop for generation of correct password
    while nf == False:
        while valid == False:
            pswd = []
            # generates the value of what character shall be generated
            for i in range(0, int(length)):
                correct = False
                # initialise random generator
                random.seed()

                # Checks values from file to generate correct characters
                if num == True and let == True and cap == True and spec == True:
                    choice = random.randrange(1, 5)

                elif num == False and let == True and cap == True and spec == True:
                    choice = random.randrange(2, 5)

                elif num == True and let == False and cap == True and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 2:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == False and cap == True and spec == True:
                    choice = random.randrange(3, 5)

                elif num == True and let == True and cap == False and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 3:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == True and cap == False and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 3 or int(choice) == 1:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == True and let == False and cap == False and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 2 or int(choice) == 3:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == False and cap == False and spec == True:
                    choice = random.randrange(4, 5)

                elif num == True and let == True and cap == True and spec == False:
                    choice = random.randrange(1, 4)

                elif num == False and let == True and cap == True and spec == False:
                    choice = random.randrange(2, 4)

                elif num == True and let == False and cap == True and spec == False:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 2 or int(choice) == 4:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == False and cap == True and spec == False:
                    choice = 3

                elif num == True and let == True and cap == False and spec == False:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 3 or int(choice) == 4:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == True and cap == False and spec == False:
                    choice = 2

                elif num == True and let == False and cap == False and spec == False:
                    choice = 1

                pswd.append(int(choice))

                # checks if all requirements are met

            for i in range(0, len(pswd)):
                if pswd[i] == 1:
                    check1 = True
                elif pswd[i] == 2:
                    check2 = True
                elif pswd[i] == 3:
                    check3 = True
                elif pswd[i] == 4:
                    check4 = True

            if check1 == num and check2 == let and check3 == cap and check4 == spec:
                valid = True

            # Generates the password from the choices made in the previous section
            for i in range(0, len(pswd)):
                if pswd[i] == 1:
                    random.seed()
                    value = random.randrange(48, 58)
                    password = password + str(chr(value))
                elif pswd[i] == 2:
                    random.seed()
                    value = random.randrange(97, 123)
                    password = password + str(chr(value))
                elif pswd[i] == 3:
                    random.seed()
                    value = random.randrange(65, 91)
                    password = password + str(chr(value))
                elif pswd[i] == 4:
                    choice2 = random.randrange(1, 5)
                    if choice2 == 1:
                        value = random.randrange(33, 48)
                        password = password + str(chr(value))
                    elif choice2 == 2:
                        value = random.randrange(58, 64)
                        password = password + str(chr(value))
                    elif choice2 == 3:
                        value = random.randrange(94, 97)
                        password = password + str(chr(value))
                    elif choice2 == 4:
                        value = random.randrange(123, 127)
                        password = password + str(chr(value))
                nf = True
    return password


@app.route("/")
def index():
    return render_template('index.html', messages=messages)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        length = request.form['length']
        upperCase = request.form.get('caps')
        lowerCase = request.form.get('lower')
        nos = request.form.get('numbers')
        SpecialChars = request.form.get('special')

        upperCaseInt = 1
        lowerCaseInt = 1
        nosInt = 1
        specialCharsInt = 1

        if upperCase != 'on':
            upperCaseInt = 0
        if lowerCase != 'on':
            lowerCaseInt = 0
        if nos != 'on':
            nosInt = 0
        if SpecialChars != 'on':
            specialCharsInt = 0
        if not title:
            flash('Account name is required!')
        else:
            messages.append(
                {'title': title, 'content': generate(length, lowerCaseInt, specialCharsInt, nosInt, upperCaseInt)})
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/email/', methods=('GET', 'POST'))
def emails():
    if request.method == 'POST':
        emailAdrress = request.form['title']
        return emailAdrress
    return render_template('email.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
