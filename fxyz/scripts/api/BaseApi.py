import json
from typing import Any

from fxyz.scripts.Config import Config
from fxyz.scripts.util import DataUtil


def getStockList(flag: int, token: str, method: str = "get") -> Any:
    """
    获取股票列表。
    历史数据收盘后六点更新。
    
    :param flag: 股票类型，0-所有股票，1-深交所股票，2-上交所股票，3-北交所股票，4-指数，5-创业板股票，6-科创板股票，7-ETF，8-ST股票，9-退市股票，10-沪深可转债
    :param token: 激活Token参考 http://www.fxyz.site/#apply
    :param method: 请求方法，默认get
    :return: JSON解码后的数据
    """
    url = Config.SERVER_URL + "/wolf/list"
    params = {"flag": flag, "token": token}
    result = DataUtil.request(url, method, params)
    data = json.loads(result)
    DataUtil.printLog("/wolf/list", params, data)
    return data


def getSector(symbol: str, token: str, method: str = "get") -> Any:
    """获取行业板块、概念板块或特色板块的成分股数据。

    :param symbol: 板块类型，hy-行业板块，gn-概念板块，ts-特色板块
    :param token: 登录网站获取的API Token
    :param method: 请求方法，默认get
    :return: JSON解码后的数据
    """
    url = Config.SERVER_URL + "/wolf/sector"
    params = {"symbol": symbol, "token": token}
    result = DataUtil.request(url, method, params)
    data = json.loads(result)
    DataUtil.printLog("/wolf/sector", params, data)
    return data


def getFinanceMetric(code: str, startDate: str, endDate: str, token: str,
                     method: str = "get") -> Any:
    """获取单只股票在日期范围内的财务核心指标。"""
    url = Config.SERVER_URL + "/wolf/financemetric"
    params = {
        "code": code,
        "startDate": startDate,
        "endDate": endDate,
        "token": token,
    }
    result = DataUtil.request(url, method, params)
    data = json.loads(result)
    DataUtil.printLog("/wolf/financemetric", params, data)
    return data
