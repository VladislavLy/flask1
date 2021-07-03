# from faker import Faker
# from flask import Flask
# from flask import render_template

# the_app = Flask(__name__)
# fake = Faker()


# def func(amount):
#     data_names = set()
#     data_emails = set()
#     data_full = []
#     while len(data_names) <= amount or len(data_emails) <= amount:
#         data_names.add(fake.first_name())
#         data_emails.add(fake.email())

#     with open("templates/users.txt", "w") as file:
#         num = 0
#         for i in range(amount):
#             num +=1
#             data_full = str(num) + ". " + list(data_names)[num] + " " + list(data_emails)[num] + " "
#             file.write(data_full + '\n' )


# @the_app.route("/generate-users/<int:number>")
# @the_app.route("/generate-users/")
# @the_app.route("/")
# def index(number=100):
#     func(number)
    
#     with open("templates/users.txt", "r") as f:
#         text = f.readlines()

#     return render_template("users.html", content = text)


# if __name__ == "__main__":
#     the_app.run(debug=True)







