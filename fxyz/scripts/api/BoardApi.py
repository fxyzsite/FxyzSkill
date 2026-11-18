import json
from typing import Any

from fxyz.scripts.Config import Config
from fxyz.scripts.util import DataUtil


class BoardApi:
    """
    黑狼数据外造接口API
    包括实时行情、涨停板、跌停板、炸板、强势股、次新股等接口
    """

    @staticmethod
    def getRealTimeQuote(symbol: str, code: str, token: str, method: str = "get") -> Any:
        """
        获取沪深A股实时行情数据。
        提供涨速、涨跌幅、换手率、振幅、量比、内盘、外盘、ROE等行情指标数据。
        
        :param symbol: 股票类型，stock-沪深京A股，etf-ETF基金
        :param code: 股票代码，all表示全推全市场数据，具体代码表示单个股票
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/time"
        params = {"symbol": symbol, "code": code, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/time", params, data)
        return data

    @staticmethod
    def getZhangTingBan(tradeDate: str, token: str, method: str = "get") -> Any:
        """
        获取盘中涨停板实时数据。
        
        :param tradeDate: 交易日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/zt"
        params = {"tradeDate": tradeDate, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/zt", params, data)
        return data

    @staticmethod
    def getDieTingBan(tradeDate: str, token: str, method: str = "get") -> Any:
        """
        获取盘中跌停板实时数据。

        :param tradeDate: 交易日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/dt"
        params = {"tradeDate": tradeDate, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/dt", params, data)
        return data

    @staticmethod
    def getZhaBan(tradeDate: str, token: str, method: str = "get") -> Any:
        """
        获取盘中炸板实时数据。

        :param tradeDate: 交易日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/zb"
        params = {"tradeDate": tradeDate, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/zb", params, data)
        return data

    @staticmethod
    def getQiangShiGu(tradeDate: str, token: str, method: str = "get") -> Any:
        """
        获取盘中强势股票实时数据。

        :param tradeDate: 交易日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/qs"
        params = {"tradeDate": tradeDate, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/qs", params, data)
        return data

    @staticmethod
    def getCiXinGu(token: str, method: str = "get") -> Any:
        """
        获取次新股数据。

        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/cx"
        params = {"token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/cx", params, data)
        return data
