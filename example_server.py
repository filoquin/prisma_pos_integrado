from pos_integrado import posIntegrado
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('amount',type=float)
parser.add_argument('invoice',type=int)
parser.add_argument('instaments',type=int)
parser.add_argument('tip',type=float)
parser.add_argument('card_code')
parser.add_argument('plan',type=int)
parser.add_argument('commerce')
parser.add_argument('commerce_name')
parser.add_argument('cuit')
parser.add_argument('line_mode')

     

@app.route('/')
def home():
        return render_template('home.html')
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
    
def restart_server():
    func = request.environ.get('werkzeug.server.restart')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/restart', methods=['GET'])
def restart():
    shutdown_server()
    p = posIntegrado()
    p.auto_select_port()
    app.run(host='0.0.0.0',port='5002')
    return 'Server restart...'



class tes(Resource):

    def get(self):
        return p.pos_execute('TES')


class tar(Resource):

    def get(self, tar_id):
        return p.pos_execute('TAR', index=int(tar_id))

class ulc(Resource):

    def get(self, tar_id):
        return p.pos_execute('ULC', index=int(tar_id))

class close(Resource):

    def get(self):
        return p.close()

class list_ports(Resource):

    def get(self):
        return p.list_ports()

class ven(Resource):
    def get(self):
        return p.pos_execute('ULT')
    
    def post(self):
        args = parser.parse_args()
        print(args)
        amount = int(args['amount'] * 100)
        invoice = args['invoice']
        instaments = args['instaments']
        tip = int(args['tip'] * 100)
        card_code = args['card_code']
        plan = args['plan']
        commerce = args['commerce']
        commerce_name = args['commerce_name']
        cuit = args['cuit']
        line_mode = args['line_mode']

        return p.pos_execute('VEN', amount=amount, invoice=invoice, instaments=instaments, tip=tip,
                    card_code=card_code, plan=plan,commerce=commerce,
                    commerce_name=commerce_name, cuit=cuit, line_mode='\x01')        

api.add_resource(tes, '/test')
api.add_resource(close, '/close')
api.add_resource(list_ports, '/list_ports')
api.add_resource(tar, '/tar/<tar_id>')
api.add_resource(ulc, '/ulc/<tar_id>')
api.add_resource(ven, '/ven')


if __name__ == '__main__':
    p = posIntegrado()
    p.auto_select_port()
    app.run(host='0.0.0.0',port='5002')
# Para obtener sabana de enviar CIE y ULT CIE en orden