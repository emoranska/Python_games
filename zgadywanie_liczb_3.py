from flask import Flask

app = Flask(__name__)

min_value = None
max_value = None
guess = None


def comp_guess(feedback):
    global max_value, min_value, guess

    if max_value - min_value <= 1:
        raise Exception("You are not fair")

    if feedback == -1:
        max_value = guess
    else:
        min_value = guess
    return int((max_value + min_value) / 2)


def reset_parameters():
    global min_value, max_value, guess
    min_value = 0
    max_value = 1000
    guess = int((max_value + min_value) / 2)


def get_control_view():
    return """
    <li><a href="/try_more">Too low</a></li>
    <li><a href="/try_less">Too high</a></li>
    <li><a href="/success">Congratulations</a></li>
    """


def get_feedback_view():
    return "<p>My guess {}</p>"


@app.route("/")
def main_page():
    return get_control_view() + get_feedback_view().format(guess)


@app.route("/try_more")
def more_page():
    global guess
    try:
        guess = comp_guess(1)
    except Exception:
        return "You are not fair"

    return get_control_view() + get_feedback_view().format(guess)


@app.route("/try_less")
def less_page():
    global guess
    try:
        guess = comp_guess(-1)
    except Exception:
        return "You are not fair"

    return get_control_view() + get_feedback_view().format(guess)


@app.route("/success")
def success_page():
    return get_control_view() + get_feedback_view().format(guess) + "<p>Yupi!</p>"

reset_parameters()
app.run()