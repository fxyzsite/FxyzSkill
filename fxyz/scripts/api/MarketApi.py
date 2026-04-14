import json

from fxyz.scripts.Config import Config
from fxyz.scripts.util import DataUtil


class MarketApi:
    """
    黑狼数据盯盘接口API
    包括实时K线、日线快照、买卖五档、竞价数据、逐笔交易、分价数据、资金流向等接口
    """

    @staticmethod
    def getKLine(symbol: str, code: str, period: str, cq: str, startDate: str, endDate: str,
                 token: str, method: str = "get") -> str:
        """
        获取沪深A股和ETF实时K线数据。
        
        :param symbol: 股票类型，stock-沪深京A股，etf-ETF基金，index-指数
        :param code: 股票代码，具体代码表示单个股票，all表示全推全市场数据（包年版）
        :param period: K线周期，5m/15m/30m/1h/1d/1w/1mon/1y
        :param cq: 复权类型，1-不复权，2-前复权，3-后复权
        :param startDate: 开始日期，格式：YYYY-MM-DD
        :param endDate: 结束日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/time/kline"
        params = {
            "symbol": symbol,
            "code": code,
            "period": period,
            "cq": cq,
            "startDate": startDate,
            "endDate": endDate,
            "token": token
        }
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/time/kline", params, data)
        return data

    @staticmethod
    def getDaySnapshot(symbol: str, code: str, token: str, method: str = "get") -> str:
        """
        获取沪深A股和ETF实时日线行情数据。
        
        :param symbol: 股票类型，stock-沪深京A股，etf-ETF基金
        :param code: 股票代码，all表示全推全市场数据，具体代码表示单个股票
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/time/day"
        params = {"symbol": symbol, "code": code, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/time/day", params, data)
        return data

    @staticmethod
    def getFiveLevel(symbol: str, code: str, token: str, method: str = "get") -> str:
        """
        获取买卖五档实时数据。
        
        :param symbol: 股票类型，stock-沪深京A股，etf-ETF基金
        :param code: 股票代码
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/time/five"
        params = {"symbol": symbol, "code": code, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/time/five", params, data)
        return data

    @staticmethod
    def getBidData(code: str, token: str, method: str = "get") -> str:
        """
        获取沪深A股实时竞价数据，竞价时间段：09:15-09:25
        
        :param code: 股票代码
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/time/bid"
        params = {"code": code, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/time/bid", params, data)
        return data

    @staticmethod
    def getDealData(code: str, tradeDate: str, token: str, method: str = "get") -> str:
        """
        获取沪深A股逐笔交易数据。
        
        :param code: 股票代码
        :param tradeDate: 交易日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/deal"
        params = {"code": code, "tradeDate": tradeDate, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/deal", params, data)
        return data

    @staticmethod
    def getPriceData(code: str, tradeDate: str, token: str, method: str = "get") -> str:
        """
        获取沪深A股分价数据。
        
        :param code: 股票代码
        :param tradeDate: 交易日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/price"
        params = {"code": code, "tradeDate": tradeDate, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/price", params, data)
        return data

    @staticmethod
    def getMoneyFlow(code: str, tradeDate: str, token: str, method: str = "get") -> str:
        """
        获取沪深A股资金流向数据。
        资金流数据区分主买、主卖、特大单、大单、中单、小单等。
        
        :param code: 股票代码
        :param tradeDate: 交易日期，格式：YYYY-MM-DD
        :param token: 激活Token参考 http://www.fxyz.site/#apply
        :param method: 请求方法，默认get
        :return: JSON格式的字符串数据
        """
        url = Config.SERVER_URL + "/wolf/money"
        params = {"code": code, "tradeDate": tradeDate, "token": token}
        result = DataUtil.request(url, method, params)
        data = json.loads(result)
        DataUtil.printLog("/wolf/money", params, data)
        return data
