from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response
from flask_cors import CORS
from Utils.dados import Application, JsonDefault

app = Flask(__name__)
app.json.sort_keys = False

CORS(app, origins=['*'])

spec = FlaskPydanticSpec('flask', title='API de Combustíveis')
spec.register(app)


@app.get('/GetData')
@spec.validate(resp=Response(HTTP_200=JsonDefault))
def GetData():
    """Retorna todos os indicadores análisados."""
    try:
        json = Application.ConstruindoJson()

        return jsonify(json), 200

    except Exception as e:
        return jsonify(
            {
                'message': f'{e}\nNão foi possível processar a sua solitação pois ouve um erro interno.'
            }
        ), 500


if __name__ == '__main__':
    app.run(debug=True)
