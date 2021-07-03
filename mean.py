# import requests
# from flask import Flask
# from flask import render_template

# the_app = Flask(__name__)


# @the_app.route("/mean/")
# @the_app.route("/")
# def index():
#     amount = 0
#     height_result = 0
#     weight_result = 0

#     with open("templates/hw.csv", "r") as f:
#         file = f.readlines()

#     for i in file[1:]:
#         if i == "\n":
#             continue
#         i = i.split(",")
        
#         height_result = height_result + float(i[1])
#         weight_result = weight_result + float(i[2])
#         amount += 1


#     arithmetic_mean_height = height_result/amount
#     arithmetic_mean_weight = weight_result/amount
#     w = round(arithmetic_mean_weight, 5)     
#     h = round(arithmetic_mean_height, 5)

#     return render_template("arithmetic_mean.html", weight = w, height = h)


# if __name__ == "__main__":
#     the_app.run(debug=True)













