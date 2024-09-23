import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # User's id
    user_id = session["user_id"]

    # User's cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    total = cash

    # Gather stock information about the user's stocks (what stocks and how many)
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)

    # Add current prices for each stock
    for stock in stocks:
        current_price = lookup(stock["symbol"])["price"]
        stock["price"] = current_price

        # Add to the total shares cost
        total += current_price * stock["total_shares"]

    return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    user_id = session["user_id"]
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        symbol = request.form.get("symbol").upper()
        if not symbol:
            return apology("provide a symbol")

        # Ensure the symbol is valid
        result = lookup(symbol)
        if result is None:
            return apology("the symbol does not exist")

        # Ensure valid number of shares were provided
        shares = request.form.get("shares")
        if not shares:
            return apology("provide number of shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology("number of shares has to be an integer")
        if shares <= 0:
            return apology("number of shares has to be a positive inteher")

        # Calculate the price of the stock shares and user's cash
        price = result["price"]
        total_cost = price * shares
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # Ensure the user has enogh cash
        if current_cash < total_cost:
            return apology("not enogh cash")

        # Subtract the price from user's cash balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?", (current_cash - total_cost), user_id)

        # Add purchase to the transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, time) VALUES (?, ?, ?, ?, DATETIME('now'))",
                   user_id, symbol, shares, price)

        # Indicate the success
        flash(f"You bought {shares} shares of {symbol} for {usd(total_cost)}!")

        # Redirect home after success
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    # Get the transaction history information
    history = db.execute(
        "SELECT symbol, shares, price, time FROM transactions WHERE user_id = ? ORDER BY id DESC", user_id)

    # Render the page
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure sybmol was provided
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Enter the symbol")

        # Ensure the symbol is valid and actually exists
        result = lookup(symbol)
        if result is None:
            return apology("the symbol doesn't exist")

        # Get the information about the stock
        price = result["price"]
        symbol = result["symbol"]

        # Render the page with the current stock quote
        return render_template("quoted.html", price=price, symbol=symbol)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username")

        # Ensure password was submitted
        if not password:
            return apology("must provide password")

        # Ensure confirmation was submitted
        if not confirmation:
            return apology("must confirm your password")

        # Ensure password matches the confirmation
        if password != confirmation:
            return apology("the password does not match")

        # Add the user to the data base
        try:
            id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                            username, generate_password_hash(password))
        except ValueError:
            return apology("the username already exists")

        # Remember which user has logged in
        session["user_id"] = id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Get user's id
    user_id = session["user_id"]

    # User's stocks
    wallet = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)
    stocks = [{stock["symbol"]: stock["total_shares"]} for stock in wallet]
    symbols = [key for d in stocks for key in d]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Function to find a value by key
        def find_value_by_key(key, list_of_dicts):
            for dictionary in list_of_dicts:
                if key in dictionary:
                    return dictionary[key]

        # Ensure symbol was submitted
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("provide a symbol")

        # Ensure the symbol is valid
        result = lookup(symbol)
        if result is None:
            return apology("the symbol does not exist")

        # Ensure valid number of shares were provided
        shares = request.form.get("shares")
        if not shares:
            return apology("provide number of shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology("number of shares has to be an integer")
        if shares <= 0:
            return apology("number of shares has to be a positive inteher")

        if symbol not in symbols:
            return aplogy("you don't own any shares of this stock")

        if find_value_by_key(symbol, stocks) < shares:
            return apology("you don't own enough shares of this stock")

        # Calculate the price of the stock shares and user's cash
        price = result["price"]
        total_profit = price * shares

        # Add the price to user's cash balance
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", (current_cash + total_profit), user_id)

        # Remove shares from the transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, time) VALUES (?, ?, ?, ?, DATETIME('now'))",
                   user_id, symbol, -shares, price)

        # Indicate the success
        flash(f"You sold {shares} shares of {symbol} for {usd(total_profit)}!")

        # Redirect home after success
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html", symbols=symbols)
