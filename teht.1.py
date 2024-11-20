from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):
    result = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
