# faq-recommendations
# 🤖  FAQ Recommendations 📞
Bem-vindo ao repositório FAQ-Recommendations! Este projeto consiste em uma aplicação web que simula um chat de atendimento, onde um atendente pode interagir com os usuários. A aplicação utiliza uma tecnologia de busca semântica para sugerir respostas do FAQ com base nas mensagens dos usuários. O objetivo principal é facilitar o atendimento ao cliente, fornecendo respostas relevantes e agilizando o processo de suporte.

## 🎯 Objetivos do Projeto
O objetivo deste projeto é criar uma interface de chat que permite aos atendentes responder eficientemente às consultas dos usuários, fazendo uso de uma base de Perguntas Frequentes (FAQ). O sistema emprega uma tecnologia de Inteligência Artificial para analisar as mensagens dos usuários e sugerir automaticamente respostas do FAQ, otimizando assim a comunicação e a eficiência do atendimento.

## ⭐ Funcionalidades Principais
1. *Chat de Atendimento Interativo:* A aplicação simula uma interface de chat em que os atendentes podem responder às mensagens dos usuários de forma interativa.

2. *Sugestão de Respostas do FAQ:* Com base nas mensagens dos usuários, a tecnologia de IA analisa a semelhança com as perguntas frequentes da base de FAQ e sugere respostas relevantes.

3. *Apresentação de Similaridade:* As respostas sugeridas são exibidas com uma indicação de similaridade em relação à mensagem do usuário.

## 🛠 Tecnologias Utilizadas️
- *HTML e CSS:* Para a construção da interface do chat.
- *Flask:* Um framework de desenvolvimento web em Python, usado para criar o servidor e as rotas da aplicação.
- *Python:* A linguagem principal para a lógica de negócios e interação com a API de IA.
- *Tecnologia de IA:* Utilizada para calcular a similaridade das mensagens e sugerir respostas do FAQ.

## 📋Requisitos

<table>
  <tr>
    <td>Python</td>
    <td>Git</td>
  </tr>
  <tr>
    <td>3.11.4 ></td>
    <td>2.41.0</td>
  </tr>
</table>

## ▶️ Executando o Projeto
### Configurando o ambiente no Linux (Recomendado)
1. Clone este repositório utilizando o comando `git clone https://github.com/BrunoTanabe/faq-recommendations`.
 
2. Navegue até a pasta faq-recommendations utilizando o comando `cd faq-recommendations`.

3. Crie um ambiente virtual utilizando o comando `python3 -m venv venv`.

4. Ative o ambiente virtual utilizando o comando `source venv/bin/activate`.

5. instale os requisitos utilizando o comando `pip install -r requirements.txt`.

### Configurando o ambiente no Windows
1. Clone este repositório utilizando o comando `git clone https://github.com/BrunoTanabe/faq-recommendations`.
 
2. Navegue até a pasta faq-recommendations utilizando o comando `cd faq-recommendations`.

3. Crie um ambiente virtual utilizando o comando `python -m venv venv`.

4. Ative o ambiente virtual utilizando o comando `./venv/scripts/activate`.

5. instale os requisitos utilizando o comando `pip install -r requirements.txt`.

### Baixando os Modelos necessários
1. Utilize o comando `cd models` para navegar até a pasta models.

2. Execute o comando `python -m spacy download pt_core_news_lg` para baixar o modelo NLP para processamento de texto.

3. Utilize o comando `git clone https://huggingface.co/neuralmind/bert-large-portuguese-cased` para baixar o modelo de embeddings.

### Executando a API
1. Certifique-se de que o ambiente virtual está ativado

2. Utilize o comando `cd src` para navegar até a pasta src

4. Utilize o comando `uvicorn main:app` para iniciar a API que estará sendo 

### Abrindo a aplicação WEB
1. Execute o arquivo `app.py` para iniciar o servidor Flask: `python app.py`.

2. Acesse a aplicação em seu navegador através do endereço: `http://localhost:5000`.

![Demonstração da Aplicação WEB](/data/images/demo.png)

### Como fazer requisições diretamente a API? (Sem utilizar a aplicação web)
para fazer as requisições basta entrar na seguinte URL: `http://127.0.0.1:8000/get_similarities/{seu texto vai aqui}`, no qual será retornado um JSON com as recomendações do FAQ.

## ❗ Nota Importante
Certifique-se de integrar a tecnologia de IA apropriada para calcular as similaridades e sugerir as respostas do FAQ.

## 👥 Autores
Bruno Henrique Pereira Domingues e Rafael dos Santos Fortes

## 💙 Agradecimento Especial à Tech4Humans
Gostaríamos de expressar nossa sincera gratidão à equipe da Tech4Humans pela emocionante oportunidade de aprendizado e pelo inspirador projeto proposto. Essa jornada nos proporcionou uma experiência enriquecedora, permitindo-nos explorar e aprimorar nossas habilidades no desenvolvimento web, integração de tecnologias de IA e criação de soluções interativas. 

Este projeto nos desafiou a pensar criativamente, trabalhar em equipe e enfrentar desafios técnicos, capacitando-nos a enfrentar situações do mundo real com confiança e determinação. Mais uma vez, obrigado à Tech4Humans por acreditar em nós e nos proporcionar esta experiência incrível.
