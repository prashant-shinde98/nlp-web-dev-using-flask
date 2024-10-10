import nlpcloud


def ner(text,search_term):

    client = nlpcloud.Client("finetuned-llama-3-70b", "2b21ce3bf88d4ba196c69b7c42119a9cc8c33766", gpu=True)
    response = client.entities(text, searched_entity=search_term)
    return response


def senti(text):

    client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b21ce3bf88d4ba196c69b7c42119a9cc8c33766", gpu=False)
    response = client.sentiment(text)

    L = []
    for i in response['scored_labels']:
      L.append(i['score'])

    index = sorted(list(enumerate(L)), key= lambda x:x[1], reverse=True)[0][0]

    res = (response['scored_labels'][index]['label'])
    return res

def summery(text):
    client = nlpcloud.Client("t5-base-en-generate-headline", "2b21ce3bf88d4ba196c69b7c42119a9cc8c33766", gpu=False)
    response = client.summarization(text)
    return response