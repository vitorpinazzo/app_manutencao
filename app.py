from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import csv
import os
from datetime import datetime
app = Flask(__name__)
PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join( PASTA_PROJETO, "solicitacoes.csv")
def carregar_solicitacoes():
solicitacoes = []
if os.path.exists(ARQUIVO):
with open(
ARQUIVO, "r", newline="", encoding="utf-8"
) as arquivo:
leitor = csv.DictReader(arquivo)
solicitacoes.extend(leitor)
return solicitacoes
def salvar_solicitacoes(solicitacoes):
with open(
ARQUIVO, "w", newline="", encoding="utf-8"
) as arquivo:
escritor = csv.DictWriter(
arquivo, fieldnames=CAMPOS
)
escritor.writeheader()
escritor.writerows(solicitacoes)
def gerar_novo_id(solicitacoes):
ids = []
for solicitacao in solicitacoes:
try:
ids.append(
int(solicitacao["id"])
)
except (ValueError, KeyError):
pass
return str( max(ids, default=0) + 1 )
@app.route("/")
def inicio():
solicitacoes = carregar_solicitacoes()
return render_template(
"index.html",
solicitacoes=solicitacoes
)
if __name__ == "__main__":
app.run(debug=True)
