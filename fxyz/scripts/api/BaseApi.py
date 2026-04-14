import json

from fxyz.scripts.Config import Config
from fxyz.scripts.util import DataUtil


def getStockList(flag: int, token: str, method: str = "get") -> str:
    """
    获取股票列表。
    历史数据收盘后六点更新。
    
    :param flag: 股票类型，0-所有股票，1-深交所股票，2-上交所股票，3-北交所股票，4-指数，5-创业板股票，6-科创板股票，7-ETF，8-ST股票，9-退市股票
    :param token: 激活Token参考 http://www.fxyz.site/#apply
    :param method: 请求方法，默认get
    :return: JSON格式的字符串数据
    """
    url = Config.SERVER_URL + "/wolf/list"
    params = {"flag": flag, "token": token}
    result = DataUtil.request(url, method, params)
    data = json.loads(result)
    DataUtil.printLog("/wolf/list", params, data)
    return data
