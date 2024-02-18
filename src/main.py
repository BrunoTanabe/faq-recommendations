from fastapi import FastAPI

import pandas as pd
import numpy as np
import spacy
from sentence_transformers import SentenceTransformer, util, models

import functions

word_embedding_model = models.Transformer("../models/bert-large-portuguese-cased")
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())

embed_model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
nlp_model = spacy.load("pt_core_news_lg")

embeddings = pd.read_csv("../data/embeddings/embeddings.csv", sep=";")
faq = pd.read_csv("../data/faqs/faq_example.csv", sep=";")


app = FastAPI()


@app.get("/")
def home():
    return {"Status": "ok"}


@app.get("/get_similarities/{text}")
def get_similarities(text: str):
    text_preprocessed = functions.get_clean_text(nlp_model, text)
    similarities = functions.get_similarity(embed_model, embeddings, text_preprocessed)

    response = faq.copy()
    response["Similarity"] = similarities.values
    response.sort_values(by="Similarity", ascending=False, inplace=True)
    response.index = [i for i in range(response.shape[0])]

    return response