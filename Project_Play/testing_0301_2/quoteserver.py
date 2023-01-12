from flask import Flask, jsonify, request, abort
from quoteDAO import quoteDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

# Gives all quotes
#curl "http://127.0.0.1:5000/quotes"
@app.route('/quotes')
def getAll():
    #print("in getall")
    results = quoteDAO.getAll()
    return jsonify(results)

# Gives quote with id of 1
#curl "http://127.0.0.1:5000/quotes/1"
@app.route('/quotes/<int:id>')
def findById(id):
    foundQuote = quoteDAO.findByID(id)

    return jsonify(foundQuote)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"quote\":\"Let it be\",\"author\":\"Paul McCartney\"}" http://127.0.0.1:5000/quotes
@app.route('/quotes', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    quote = {
        "quote": request.json['quote'],
        "author": request.json['author'],
    }
    values =(quote['quote'],quote['author'])
    newId = quoteDAO.create(values)
    quote['id'] = newId
    return jsonify(quote)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/quotes/<int:id>', methods=['PUT'])
def update(id):
    foundQuote = quoteDAO.findByID(id)
    if not foundQuote:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'quote' in reqJson:
        foundQuote['quote'] = reqJson['quote']
    if 'Author' in reqJson:
        foundQuote['author'] = reqJson['author']
    values = (foundQuote['quote'],foundQuote['author'],foundQuote['id'])
    quoteDAO.update(values)
    return jsonify(foundQuote)
        

    

@app.route('/quotes/<int:id>' , methods=['DELETE'])
def delete(id):
    quoteDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)