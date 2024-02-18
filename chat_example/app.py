from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Função para obter respostas sugeridas com base na mensagem do cliente
def obter_respostas_sugeridas(mensagem_do_cliente):
    url_da_api = f"http://127.0.0.1:8000/get_similarities/{mensagem_do_cliente}"
    try:
        # Faz uma requisição à API local
        resposta = requests.get(url_da_api)
        if resposta.status_code == 200:
            resposta_json = resposta.json()
            similaridades = resposta_json["Similarity"]
            respostas_sugeridas = []

            # Filtra respostas sugeridas com similaridade maior que 0.5
            for indice, similaridade in similaridades.items():
                pergunta = resposta_json["Question"][indice]
                resposta = resposta_json["Answer"][indice]
                if similaridade < 0:
                    similaridade = 0
                respostas_sugeridas.append((similaridade, pergunta, resposta))

            # Ordena a lista de respostas sugeridas com base nas similaridades (do maior para o menor)
            respostas_sugeridas.sort(reverse=True)

            return respostas_sugeridas

        else:
            return []

    except requests.exceptions.RequestException:
        return []

# Rota principal do aplicativo
@app.route('/', methods=['GET', 'POST'])
def index():
    respostas_sugeridas = []
    conversa = [
        ("Oi, tudo bem?", "usuario"),
        ("Olá! Tudo sim e você?", "atendente"),
        ("Tudo sim. Preciso de uma informação", "usuario"),
        ("Claro! Como posso ajudar?", "atendente"),
    ]

    if request.method == 'POST':
        # Obtém a mensagem do cliente do formulário
        mensagem_do_cliente = request.form['mensagem']
        # Chama a função para obter respostas sugeridas
        respostas_sugeridas = obter_respostas_sugeridas(mensagem_do_cliente)
        # Adiciona a mensagem do cliente à conversa
        conversa.append((mensagem_do_cliente, "usuario"))

        # Se a conversa estiver vazia, adiciona mensagens do atendente previamente criadas
        if not conversa:
            mensagens_atendente = [
                ("Olá! Tudo sim e você?", "atendente"),
                ("Claro! Como posso ajudar?", "atendente"),
            ]
            conversa.extend(mensagens_atendente)

    # Renderiza o template HTML com as respostas sugeridas e a conversa
    return render_template('index.html', respostas_sugeridas=respostas_sugeridas, conversa=conversa)

# Executa o aplicativo em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)