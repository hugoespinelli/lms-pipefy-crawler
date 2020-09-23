from os import getenv
from dotenv import load_dotenv

from flask import Flask
from waitress import serve

load_dotenv()

import search_exam_users


app = Flask(__name__)


@app.route('/start_exams_craw')
def hello_world():
    is_done = search_exam_users.run()
    return {
        "message": "Completado com sucesso" if is_done else "Deu algum erro"
    }


if __name__ == "__main__":
    port = getenv("PORT")
    print(f"Rodando servidor na porta {port}")
    serve(app, host='0.0.0.0', port=port)
