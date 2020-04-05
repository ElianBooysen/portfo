from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)  # sets name to main
# have debug mode on in command prompt
# route() for different aspects of the website see the 2 functions below
# render_template() allows us to send files to web page - need to save html in a folder named 'templates'

'''''
@app.route('/<username>/<int:post_id>')  # decorator if param has arg with '<>'-we can parse arg. eg, username may be parsed
def hello_world(username='username', post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
'''


@app.route('/<string:page_name>')
def html_pg(page_name):
    return render_template(page_name)


@app.route('/')  # homepage
def st():
    return render_template('index.html')


@app.route('/sub_message', methods=['POST', 'GET'])
def sub_message():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # stores data as dictionary
            print(data)
            write_to_csv(data)  # calling the function we created below
            return redirect('/thanks.html')  # thank you message once form is submitted
        except:
            return 'Unable to save to the database'
    else:
        return 'something went wrong'


def to_file(data):  # function that will save data into a text file that we createed
    with open('database.txt', mode='a') as database:  # mode = a is append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')  # writing to text file


def write_to_csv(data):  # going to send data to csv file
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])  # row of data
