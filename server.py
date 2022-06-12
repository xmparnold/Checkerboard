from re import X
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route( "/" )
@app.route( "/home" )
def show_8_by_8_checkerboard():
    return render_template( "index.html" )

@app.route( "/<x>" )
def show_custom_rows_checkerboard(x):
    return render_template( "custom_rows_checkerboard.html", x_num = int(x) )

@app.route( "/<x>/<y>" )
def show_custom_checkerboard(x, y):
    return render_template( "custom_checkerboard.html", x_num = int(x), y_num = int(y) )


if __name__ == "__main__":
    app.run(debug = True)