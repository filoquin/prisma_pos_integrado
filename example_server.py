from pos_integrado import posIntegrado
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class home(Resource):

    def get(self):
        return 'hola'


class tes(Resource):

    def get(self):
        return p.pos_execute('TES')


class tar(Resource):

    def get(self, tar_id):
        return p.pos_execute('TAR', index=int(tar_id))


api.add_resource(home, '/')
api.add_resource(tes, '/test')
api.add_resource(tar, '/tar/<tar_id>')


if __name__ == '__main__':
    p = posIntegrado()
    p.auto_select_port()

    print(p.pos_execute('TES'))
    app.run(port='5002')
