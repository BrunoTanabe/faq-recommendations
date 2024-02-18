import pandas as pd
import numpy as np
import torch
import spacy
from sentence_transformers import SentenceTransformer, util

import re


def get_similarity(model, embeddings, text):
    text_embed = model.encode(text)
    similarities = []

    for column in embeddings.columns:
        similarity = util.cos_sim(text_embed, embeddings[column].values.astype(np.float32))
        similarities.append(similarity)
    

    return pd.Series(similarities).astype(float)


def get_clean_text(model, text:str):
    text_tokens = model(text)

    clean_text = []

    for token in text_tokens:
        if not token.is_stop and not token.is_punct:
            clean_text.append(token.text)

    clean_text = " ".join(clean_text)

    return re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', clean_text).lower()