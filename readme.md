# 🤖 FAQ Recommendations 📞
Welcome to the FAQ-Recommendations repository! This project consists of a web application that simulates a customer service chat, where an attendant can interact with users. The application uses semantic search technology to suggest FAQ answers based on user messages. The main goal is to facilitate customer service by providing relevant answers and streamlining the support process.

## 🎯 Project Objectives
The objective of this project is to create a chat interface that allows attendants to efficiently respond to user queries, using a Frequently Asked Questions (FAQ) base. The system employs Artificial Intelligence technology to analyze user messages and automatically suggest FAQ answers, thus optimizing communication and support efficiency.

## ⭐ Key Features
1. *Interactive Customer Service Chat:* The application simulates a chat interface where attendants can interactively respond to user messages.

2. *FAQ Answer Suggestions:* Based on user messages, AI technology analyzes similarity with the frequently asked questions in the FAQ base and suggests relevant answers.

3. *Similarity Presentation:* The suggested answers are displayed with an indication of similarity to the user's message.

## 🛠 Technologies Used
- *HTML and CSS:* For building the chat interface.
- *Flask:* A Python web development framework used to create the server and application routes.
- *Python:* The main language for business logic and interaction with the AI API.
- *AI Technology:* Utilized for calculating message similarity and suggesting FAQ answers.

## 📋 Requirements

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

## ▶️ Running the Project
### Setting up the environment on Linux (Recommended)
1. Clone this repository using the command `git clone https://github.com/BrunoTanabe/faq-recommendations`.
 
2. Navigate to the faq-recommendations folder using the command `cd faq-recommendations`.

3. Create a virtual environment using the command `python3 -m venv venv`.

4. Activate the virtual environment using the command `source venv/bin/activate`.

5. Install requirements using the command `pip install -r requirements.txt`.

### Setting up the environment on Windows
1. Clone this repository using the command `git clone https://github.com/BrunoTanabe/faq-recommendations`.
 
2. Navigate to the faq-recommendations folder using the command `cd faq-recommendations`.

3. Create a virtual environment using the command `python -m venv venv`.

4. Activate the virtual environment using the command `./venv/scripts/activate`.

5. Install requirements using the command `pip install -r requirements.txt`.

### Downloading Required Models
1. Use the command `cd models` to navigate to the models folder.

2. Run the command `python -m spacy download pt_core_news_lg` to download the NLP model for text processing.

3. Use the command `git clone https://huggingface.co/neuralmind/bert-large-portuguese-cased` to download the embeddings model.

### Running the API
1. Make sure the virtual environment is activated.

2. Use the command `cd src` to navigate to the src folder.

4. Use the command `uvicorn main:app` to start the API.

### Opening the Web Application
1. Run the `app.py` file to start the Flask server: `python app.py`.

2. Access the application in your browser through the address: `http://localhost:5000`.

![Web Application Demonstration](/data/images/demo.png)

### How to make requests directly to the API? (Without using the web application)
To make requests, simply enter the following URL: `http://127.0.0.1:8000/get_similarities/{your text goes here}`, which will return a JSON with FAQ recommendations.

## ❗ Important Note
Make sure to integrate the appropriate AI technology to calculate similarities and suggest FAQ answers.

## 👥 Authors
Bruno Henrique Pereira Domingues and Rafael dos Santos Fortes

## 💙 Special Thanks to Tech4Humans
We would like to express our sincere gratitude to the Tech4Humans team for the exciting learning opportunity and the inspiring project proposed. This journey has provided us with an enriching experience, allowing us to explore and enhance our skills in web development, integration of AI technologies, and creation of interactive solutions.

This project has challenged us to think creatively, work as a team, and tackle technical challenges, empowering us to face real-world situations with confidence and determination. Once again, thank you to Tech4Humans for believing in us and providing us with this amazing experience.