from flask import Flask, jsonify, request
from repository.conta_repository import conta_repository
from repository.usuarios_repository import usuarios_repository
from repository.transacoes_repository import transacoes_repository
from datetime import datetime
import random
from flask_cors import CORS



app = Flask(__name__)

CORS(app)



@app.route("/saldo", methods=["GET"])
def saldo():



    repo = conta_repository()
    id_usuario = request.args.get("idusuario")
    id_conta = request.args.get("idconta")
    saldo = repo.get_saldo(id_usuario, id_conta)
    return(jsonify({
        "idusuario":id_usuario,
        "id_conta":id_conta,
        "saldo":saldo

    }))



@app.route("/usuario", methods=["GET"])
def usuario():

    repo = usuarios_repository()
    id_usuario = request.args.get("idusuario")
    usuario = repo.get_usuario(id_usuario)
    for u in usuario:
        return(jsonify({
            "idusuario": id_usuario,
            "usuario": u["nome"],
            "email": u["email"],
            "data": u["data_cadastro"]

        }))



@app.route("/transacao", methods=["GET"])
def transacao():

    repo = transacoes_repository()
    id_conta = request.args.get("idconta")
    id_conta_destino = request.args.get("idcontadestinatario")
    transacao = repo.get_transacao(id_conta, id_conta_destino)
    for t in transacao:

        return(jsonify({
            "idconta": id_conta,
            "idcontadestino": t["idcontadestino"],
            "datatransacao": t["data_transacao"],
            "valor": t["valor"],
            "tipo": t["id_tipo"]

        }))





@app.route("/usuario", methods=["POST"])

def criar_usuario():

   
    repo_u = usuarios_repository()
    repo_c = conta_repository()
    id_aleatorio = random.randint(100000, 999999)
    id_aleatorio_conta = random.randint(10000, 99999)
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = request.json
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senhahash")


    if not nome or not email or not senha:
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400



    try:
        repo_u.criar_usuario(id_aleatorio, nome, email, senha, agora)
        repo_c.criar_conta(id_aleatorio_conta, id_aleatorio, 1000)
        return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201

    except Exception as e:

        return jsonify({"erro": str(e)}), 500



@app.route("/transacao", methods=["POST"])

def criar_transacao():

    data = request.json
    transacao_repo = transacoes_repository()
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    idusuario = data.get("idusuario")
    valor = data.get("valor")
    tipo = data.get("tipo")
    id_aleatorio = random.randint(100000, 999999)
    idcontadestino = data.get("idcontadestinatario")
    idcontaremetente = data.get("idcontaremetente")
    status = "aprovado"



    if not idusuario or not valor or not tipo or not idcontadestino or not idcontaremetente:
        return jsonify({"erro": "Campos obrigatórios faltando (idusuario, valor, tipo, idcontadestinatario, idcontaremetente)"}), 400



    try:
        transacao_repo.criar_transacao(id_aleatorio, idusuario, tipo, valor, status, agora, idcontaremetente, idcontadestino)
        return jsonify({"mensagem": "Transação registrada com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__": app.run(debug=True)