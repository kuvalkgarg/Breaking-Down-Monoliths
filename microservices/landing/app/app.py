from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def perform_operation(operation, n1, n2):
    result = None
    error_message = None

    try:
        if operation == 'add':
            result = n1 + n2
        elif operation == 'minus':
            result = n1 - n2
        elif operation == 'multiply':
            result = n1 * n2
        elif operation == 'divide':
            if n2 == 0:
                raise ZeroDivisionError("Cannot divide by 0")
            result = n1 / n2
        elif operation == "modulo":
            if n2 == 0:
                raise ZeroDivisionError("Cannot modulo by 0")
            result = n1 % n2
        elif operation == "exponent":
            result = n1 ** n2
        elif operation == "gcd":
            result = gcd(n1, n2)
    except ZeroDivisionError as e:
        error_message = str(e)
    except:
        error_message = "Input 2 valid integers and select the desired operation to perform"

    return result, error_message


def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


@app.route('/', methods=['POST', 'GET'])
def index():
    result = None
    error_message = None

    if request.method == 'POST':
        try:
            number_1 = int(request.form.get("first"))
            number_2 = int(request.form.get('second'))
            operation = request.form.get('operation')

            result, error_message = perform_operation(
                operation, number_1, number_2)
        except:
            error_message = "Input 2 valid integers and select the desired operation to perform"

        if result is not None:
            flash(
                f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        elif error_message is not None:
            flash(error_message)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
