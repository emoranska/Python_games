from flask import Flask, request

app = Flask(__name__)

def get_form():
    return """
    <form action="/<user_number>" method="POST">
    <label><input name="more" type="submit" value="więcej"></label>
    <label><input name="less" type="submit" value="mniej"></label>
    <label><input name="correct" type="submit" value="trafiłeś"></label>
    <label><input type="hidden" name="min" value="0"></label>
    <label><input type="hidden" name="max" value="1000"></label>
    </form>
    """

@app.route("/<user_number>", methods=["GET","POST"])
def main_route(user_number):

    if request.method == "POST":

        guess = 500
        max = request.form.get("max", int)
        min = request.form.get("min", int)

        while guess != user_number:
            print(f'Zgaduję: {guess}')
            guess = int((max - min) / 2) + min

            if guess > user_number:
                max = guess
                print("Za dużo!")
                return get_form()

            if guess < user_number:
                min = guess
                print('Za mało!')
                return get_form()

            if guess == user_number:
                print(f'Zgadłeś! {guess} było poprawną liczbą.')

    else:
        return get_form()

app.run()
