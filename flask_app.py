from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get data from request
    data = request.json
    MY_AR_EXP = data['my_ar_exp']
    MY_AR = data['my_ar']
    WANTED_AR = data['wanted_ar']
    PRIMOGEM_REFILLS_PER_DAY = data['primogem_refills']
    
    # Your Python logic here
    # Calculate and return the result
    result = {"days": "Estimated days calculated by Python script"}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)