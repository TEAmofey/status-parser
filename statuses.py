import pandas as pd


class Statuses:
    data_f = pd.DataFrame


statuses = {"mofeytea": "",
            "mothersterrorist": "",
            "kukuruzka_7": "",
            "ksenono": "",
            "deniskilseev": ""}


def tostr(d: dict) -> str:
    result = ""
    for key in d.keys():
        result += key + ': "' + d[key] + '"\n'
    return result
