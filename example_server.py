from pos_integrado import posIntegrado
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('amount', type=float)
parser.add_argument('invoice', type=int)
parser.add_argument('instaments', type=int)
parser.add_argument('tip', type=float)
parser.add_argument('card_code')
parser.add_argument('coupon')
parser.add_argument('plan', type=int)
parser.add_argument('commerce')
parser.add_argument('commerce_name')
parser.add_argument('cuit')
parser.add_argument('line_mode')
parser.add_argument('date')


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


@app.route('/auto_select_port', methods=['GET'])
def auto_select_port():
    p.auto_select_port()
    return p.list_ports()


@app.route('/restart', methods=['GET'])
def restart():
    p.close()
    shutdown_server()
    app.run(host='0.0.0.0', port='5002')
    return 'Server restart...'


class tes(Resource):

    def get(self):
        try:
            res = p.pos_execute('TES')
            if res == {}:
                return True
            else:
                return False
        except Exception as e:
            return False


class imt(Resource):

    def get(self):
        return p.pos_execute('IMT')


class imc(Resource):

    def get(self):
        return p.pos_execute('IMC')


class z(Resource):

    def get(self):
        res = {'cie': False, 'Z': []}
        res['cie'] = p.pos_execute('CIE')
        last = ''
        for i in range(0, 6):
            try:
                ulc = p.pos_execute('ULC', index=i)
                if ulc:
                    if 'card_code' in ulc and ulc['card_code'] != last:
                        res['Z'].append(ulc)
                        last = ulc['card_code']
                p.serial_write(p.OKIDOKI)
            except Exception as e:
                break
        return res


class cie(Resource):

    def get(self):
        return p.pos_execute('CIE')


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


class anv(Resource):

    def post(self):
        args = parser.parse_args()
        card_code = args['card_code']
        coupon = int(args['coupon'])

        return p.pos_execute('ANV', coupon=coupon, card_code=card_code)


class dev(Resource):

    def post(self):

        args = parser.parse_args()
        amount = int(args['amount'] * 100)
        date = args['date']
        invoice = args['invoice']
        instaments = args['instaments']
        card_code = args['card_code']
        plan = args['plan']
        commerce = args['commerce']
        commerce_name = args['commerce_name']
        cuit = args['cuit']
        if args['line_mode'] == 0:
            line_mode = '\x00'
        else:
            line_mode = '\x01'

        return p.pos_execute('DEV', amount=amount, invoice=invoice, instaments=instaments, date=date,
                             card_code=card_code, plan=plan, commerce=commerce,
                             commerce_name=commerce_name, cuit=cuit, line_mode=line_mode)


class ven(Resource):

    def get(self):
        return p.pos_execute('ULT')

    def post(self):
        args = parser.parse_args()
        amount = int(args['amount'] * 100)
        invoice = args['invoice']
        instaments = args['instaments']
        tip = int(args['tip'] * 100)
        card_code = args['card_code']
        plan = args['plan']
        commerce = args['commerce']
        commerce_name = args['commerce_name']
        cuit = args['cuit']
        if args['line_mode'] == 0:
            line_mode = '\x00'
        else:
            line_mode = '\x01'

        return p.pos_execute('VEN', amount=amount, invoice=invoice, instaments=instaments, tip=tip,
                             card_code=card_code, plan=plan, commerce=commerce,
                             commerce_name=commerce_name, cuit=cuit, line_mode=line_mode)

api.add_resource(tes, '/test')
api.add_resource(imc, '/imc')
api.add_resource(imt, '/imt')
api.add_resource(close, '/close')
api.add_resource(list_ports, '/list_ports')
api.add_resource(tar, '/tar/<tar_id>')
api.add_resource(ulc, '/ulc/<tar_id>')
api.add_resource(ven, '/ven')
api.add_resource(cie, '/cie')
api.add_resource(anv, '/anv')
api.add_resource(z, '/z')

if __name__ == '__main__':
    logging.basicConfig(filename='pos.log', filemode='w', level=logging.INFO)
    logging.info('Started')

    p = posIntegrado()
    p.auto_select_port()
    app.run(host='0.0.0.0', port='5002')
# Para obtener sabana de enviar CIE y ULT CIE en orden
