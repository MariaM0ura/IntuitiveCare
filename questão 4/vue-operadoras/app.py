from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

def load_data():
    operadoras = []
    with open('Relatorio_cadop.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            operadoras.append(row)
    return operadoras

@app.route('/api/operadoras', methods=['GET'])
def search_operadoras():
    query = request.args.get('query', '')  
    operadoras = load_data()
    
    result = [op for op in operadoras if query.lower() in op['Nome_Fantasia'].lower()]
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
