import requests
import json
from config import curency_dict


class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def conv(quote: str, base: str, amount: str):
        
        try:
            amount: str = float(amount) # количество, которое необходимо перевести
        except ValueError:
            raise APIException(f'Вводить количество необходимо при помощи цифр "{amount}"')
        
        
        if quote == base:
            raise APIException(f'Нельзя конвертировать одну и ту же валюту {base}')
        
        try:
            quote_ticker = curency_dict[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote} ')
        
        try:
            base_ticker = curency_dict[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base} ')
        
         # Запрос к API
        req_get = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    
        # Преобразование ответа от API в словарь Python
        d_content: dict = json.loads(req_get.content)
        
        summ = d_content[curency_dict[base]] * amount
        
        return summ