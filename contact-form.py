# import smtplib
# from email.mime.text import MIMEText
# from flask import Flask, render_template, request
# import mysql.connector

# app = Flask(__name__)

# # Connect to the database
# cnx = mysql.connector.connect(
#     host="localhost",
#     port="3306"
#     user="mrsingh",
#     password="chxxslrlszocvkra",
#     database="web_info"
# )
# cursor = cnx.cursor()


# @app.route('/')
# def index():
#     return render_template('./main.html')

# @app.route('/contact', methods=['POST'])
# def contact():
#     # Get the form data from the request
#     name = request.form.get("name")
#     mobile = request.form.get("mobile")
#     email = request.form.get("email")
#     message = request.form.get("message")

#     # Insert the form data into the database
#     cursor.execute("INSERT INTO contact_form (name, mobile, email, message) VALUES (%s, %s, %s, %s)", (name, mobile, email, message))
#     cnx.commit()

#     # Send response email to client
#     msg = MIMEText("Thank you for contacting us. We will get back to you soon.")
#     msg['Subject'] = 'Contact Form Submission'
#     msg['From'] = 'rude8032@gmail.com'
#     msg['To'] = email
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login('rude8032@gmail.com', 'chxxslrlszocvkra')
#     server.sendmail('rude8032@gmail.com', email, msg.as_string())
#     server.quit()

#     return "Form Submitted"

# if __name__ == '__main__':
#     app.run(debug=True)

# # Close the connection to the database
# cursor.close()
# cnx.close()




import mysql.connector
import smtplib
from email.mime.text import MIMEText

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="mrsingh",
  password="Vikram12345",
  database="web_info"
)


@app.route("/")
def index():
    return render_template('./main.html')




@app.route('/contact', methods=['POST'])
def contact():

    # Create a cursor object to execute queries
    mycursor = mydb.cursor()

    # Create the SQL query to insert the form data into the table
    query = "INSERT INTO contact_form (name, mobile, email, message) VALUES (%s, %s, %s, %s)"

    # Get the form data from the request
    form_data = request.form

    # Extract the form values
    name = form_data["name"]
    mobile = form_data["mobile"]
    email = form_data["email"]
    message = form_data["message"]

    # Insert the form data into the table
    mycursor.execute(query, (name, mobile, email, message))

    # Commit the changes to the database
    mydb.commit()

    # Send an email to the user if they subscribed
    msg = MIMEText(f"Thank you for subscribing, {name}!")
    msg['Subject'] = 'Subscription Confirmation'
    msg['From'] = 'rude8032@gmail.com'
    msg['To'] = email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('rude8032@gmail.com', 'chxxslrlszocvkra')
    server.sendmail('rude8032@gmail.com', email, msg.as_string())
    server.quit()
    
if __name__ == '__main__':
    app.run(debug=True)



return "Form submitted successfully!"
