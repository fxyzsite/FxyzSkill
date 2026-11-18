import json
from typing import Any

import requests

def request(url: str, method: str = "get", params=None):
    if method == 'post':
        response = requests.post(url, params=params)
        return response.content.decode('utf-8')
    else:
        response = requests.get(url, params=params)
        return response.content.decode('utf-8')


def printLog(apiName: str, params: dict, data: Any) -> Any:
    # Tokens are passed as query parameters by the API; never echo credentials to logs.
    safe_params = {key: ("***" if key.lower() == "token" else value) for key, value in params.items()}
    if isinstance(data, list):
        print(f"{apiName}，返回 {len(data)} 条记录，参数{safe_params}，数据样例：{data[0] if len(data) > 0 else {} }")
    else:
        print(f"{apiName}，返回异常信息，参数{safe_params}，异常详情：{data}")
    return data
