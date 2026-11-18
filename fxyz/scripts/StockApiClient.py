from fxyz.scripts.Config import Config
from fxyz.scripts.api import BaseApi
from fxyz.scripts.api.BoardApi import BoardApi
from fxyz.scripts.api.MarketApi import MarketApi


class StockApiClient(object):

    def demoForAllApis(self):

        token = Config.TOKEN
        try:

            # ========== Base Api 测试 ==========
            # 1. 股票列表
            data = BaseApi.getStockList(flag=0, token=token)

            # 2. 概念成分股
            data = BaseApi.getSector(symbol="gn", token=token)

            # 3. 财务核心指标（单只股票）
            data = BaseApi.getFinanceMetric(
                code="000001",
                startDate="2026-01-01",
                endDate="2026-04-13",
                token=token,
            )

            # ========== Board Api 测试 ==========
            # 1. 实时行情
            data = BoardApi.getRealTimeQuote(symbol="stock", code="000002", token=token)

            # 2. 涨停板
            data = BoardApi.getZhangTingBan(tradeDate="2026-04-13", token=token)

            # 3. 跌停板
            data = BoardApi.getDieTingBan(tradeDate="2026-04-13", token=token)

            # 4. 炸板
            data = BoardApi.getZhaBan(tradeDate="2026-04-13", token=token)

            # 5. 强势股
            data = BoardApi.getQiangShiGu(tradeDate="2026-04-13", token=token)

            # 6. 次新股
            data = BoardApi.getCiXinGu(token=token)

            # ========== Market Api 测试 ==========
            # 1. 实时K线
            data = MarketApi.getKLine(
                symbol="stock",
                code="000002",
                period="1d",
                cq="1",
                startDate="2026-04-01",
                endDate="2026-04-13",
                token=token
            )

            # 2. 日线快照
            data = MarketApi.getDaySnapshot(symbol="stock", code="000002", token=token)

            # 3. 买卖五档
            data = MarketApi.getFiveLevel(symbol="stock", code="000002", token=token)

            # 4. 竞价数据
            data = MarketApi.getBidData(code="000002", token=token)

            # 5. 逐笔交易
            data = MarketApi.getDealData(code="000002", tradeDate="2026-04-13", token=token)

            # 6. 分价数据
            data = MarketApi.getPriceData(code="000002", tradeDate="2026-04-13", token=token)

            # 7. 资金流向
            data = MarketApi.getMoneyFlow(code="000002", tradeDate="2026-04-13", token=token)

            # 8. 复权变更数据
            data = MarketApi.getAdjustment(
                symbol="stock", tradeDate="2026-04-13", token=token
            )

        except Exception as e:
            print(f"调用失败: {e}")


if __name__ == "__main__":
    # 创建客户端实例,测试所有API接口
    client = StockApiClient()
    client.demoForAllApis()
