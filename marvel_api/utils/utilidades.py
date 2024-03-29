from unicodedata import normalize
from datetime import datetime

def cores_olhos(text):
    if text == 'red':
        text = 'vermelho'
    elif text == 'white':
        text = 'branco'
    elif text == 'black' or text == 'dark':
        text = 'preto'
    elif text == 'gray' or text == 'grey':
        text = 'cinza'
    elif text == 'blue':
        text = 'azul'
    elif text == 'green':
        text = 'verde'
    elif text == 'brown':
        text = 'castanho'
    elif text == 'amber':
        text = 'ambar'
    elif text == 'blond':
        text = 'loiro'
    elif text == 'orange':
        text = 'laranja'
    elif text == 'yellow':
        text = 'amarelo'
    elif text == 'light' or text == 'fair':
        text = 'clara'
    else:
        text = text

    return text

def cores_cabelo(text):
    if text == 'red':
        text = 'vermelho'
    elif text == 'white':
        text = 'branco'
    elif text == 'black' or text == 'dark':
        text = 'preto'
    elif text == 'gray' or text == 'grey':
        text = 'cinza'
    elif text == 'blue':
        text = 'azul'
    elif text == 'green':
        text = 'verde'
    elif text == 'brown':
        text = 'castanho'
    elif text == 'amber':
        text = 'ambar'
    elif text == 'blond':
        text = 'loiro'
    elif text == 'orange':
        text = 'laranja'
    elif text == 'light' or text == 'fair':
        text = 'clara'
    else:
        text = text

    return text

def cores_pele(text):
    if text == 'red':
        text = 'vermelho'
    elif text == 'white':
        text = 'branco'
    elif text == 'black' or text == 'dark':
        text = 'negro'
    elif text == 'gray' or text == 'grey':
        text = 'cinza'
    elif text == 'blue':
        text = 'azul'
    elif text == 'green':
        text = 'verde'
    elif text == 'brown':
        text = 'castanho'
    elif text == 'amber':
        text = 'ambar'
    elif text == 'blond':
        text = 'loiro'
    elif text == 'orange':
        text = 'laranja'
    elif text == 'gold':
        text = 'dourada'
    elif text == 'light' or text == 'fair':
        text = 'clara'
    else:
        text = text

    return text

def sexo(text):
    if text == 'male':
        text = 'Masculino'
    elif text == 'female':
        text = 'Feminino'
    elif text == 'hermaphrodite':
        text = 'hermafrodita'
    else:
        text = text

    return text

def to_date_swagger(txt):
    n_date = datetime.strptime(txt, "%Y-%m-%d").date()
    day, month, year = n_date.day, n_date.month, n_date.year
    if day < 10: day = "0"+str(n_date.day)
    if month < 10: month = "0"+str(n_date.month)
    return f"{day}/{month}/{year}"
