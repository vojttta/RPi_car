from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

value = 0  # Výchozí hodnota

@app.route('/')
def index():
    return render_template('index.html', value=value)

@app.route('/handle_key', methods=['POST'])
def handle_key():
    global value
    data = request.get_json()
    key = data.get('key')
    
    # Zde můžeš provést akci podle stisknuté klávesy
    # Například zvýšení nebo snížení hodnoty podle klávesy
    print(key)
    if key == 'ArrowDown':
        print('DA')
    elif key == 'ArrowUp':
        print('UA')
    if key == 'ArrowLeft':
        print('LA')
    elif key == 'ArrowRight':
        print('RA')
    
    return jsonify({'message': 'OK'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
