from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host='localhost',
    user='phpmyadmin',
    password='12986sku',
    database='shuttle',
)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/passenger")
def passenger():
    return render_template("passenger.html")

@app.route("/driver")
def driver():
    return render_template("driver.html")

@app.route("/shuttles1")
def shuttles1():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shuttle WHERE driver_lic_num = 1;")
    shuttles = cursor.fetchall()
    return render_template("shuttles.html", data = shuttles)

@app.route("/shuttles2")
def shuttles2():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shuttle WHERE driver_lic_num = 2;")
    shuttles = cursor.fetchall()
    return render_template("shuttles.html", data = shuttles)

@app.route("/shuttles5")
def shuttles5():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shuttle WHERE driver_lic_num = 5;")
    shuttles = cursor.fetchall()
    return render_template("shuttles.html", data = shuttles)

@app.route("/company")
def company():
    return render_template("company.html")

@app.route("/drivers1")
def drivers1():
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, ssc_tin, license_number, phone_number FROM driver JOIN phone_numbers ON driver.license_number = phone_numbers.driver_lic_number WHERE driver.ssc_tin = 1;")
    drivers = cursor.fetchall()
    return render_template("drivers.html", data = drivers)

@app.route("/drivers2")
def drivers2():
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, ssc_tin, license_number, phone_number FROM driver JOIN phone_numbers ON driver.license_number = phone_numbers.driver_lic_number WHERE driver.ssc_tin = 2;")
    drivers = cursor.fetchall()
    return render_template("drivers.html", data = drivers)

@app.route("/drivers3")
def drivers3():
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, ssc_tin, license_number, phone_number FROM driver JOIN phone_numbers ON driver.license_number = phone_numbers.driver_lic_number WHERE driver.ssc_tin = 3;")
    drivers = cursor.fetchall()
    return render_template("drivers.html", data = drivers)

@app.route("/drivers4")
def drivers4():
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, ssc_tin, license_number, phone_number FROM driver JOIN phone_numbers ON driver.license_number = phone_numbers.driver_lic_number WHERE driver.ssc_tin = 4;")
    drivers = cursor.fetchall()
    return render_template("drivers.html", data = drivers)

@app.route("/drivers5")
def drivers5():
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, ssc_tin, license_number, phone_number FROM driver JOIN phone_numbers ON driver.license_number = phone_numbers.driver_lic_number WHERE driver.ssc_tin = 5;")
    drivers = cursor.fetchall()
    return render_template("drivers.html", data = drivers)

@app.route("/busses1")
def busses1():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bus WHERE bus.ssc_tin = 1;")
    busses = cursor.fetchall()
    return render_template("busses.html", data = busses)

@app.route("/busses2")
def busses2():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bus WHERE bus.ssc_tin = 2;")
    busses = cursor.fetchall()
    return render_template("busses.html", data = busses)

@app.route("/busses3")
def busses3():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bus WHERE bus.ssc_tin = 3;")
    busses = cursor.fetchall()
    return render_template("busses.html", data = busses)

@app.route("/busses4")
def busses4():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bus WHERE bus.ssc_tin = 4;")
    busses = cursor.fetchall()
    return render_template("busses.html", data = busses)

@app.route("/busses5")
def busses5():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bus WHERE bus.ssc_tin = 5;")
    busses = cursor.fetchall()
    return render_template("busses.html", data = busses)

@app.route("/add_ticket")
def add_ticket():
    return render_template("add_ticket.html")

@app.route("/del_ticket")
def del_ticket():
    return render_template("del_ticket.html")

if __name__ == "__main__":
    app.run()
