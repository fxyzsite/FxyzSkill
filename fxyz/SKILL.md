---
name: fxyz
description: Query the Fxyz stock market data API for Chinese A-share, ETF, index, and convertible-bond lists and market data, including quotes, K-lines, order books, limit-up/down boards, sector constituents, financial metrics, adjustment events, and money flow. Use when a task requires retrieving Fxyz data through its authenticated HTTP API.
---

# Fxyz 市场数据 API Skill

Fxyz（黑狼数据）提供中国股票市场实时数据 API。`fxyz` 是已发布到 PyPI 的 SDK 发行包名，也是 Python 导入包名。使用本 Skill 时，根据用户的数据需求选取对应接口，核对必填参数、标的类型和账号权限，再通过 SDK 或 HTTP API 获取数据。接口定义以 [`references/apidoc.md`](references/apidoc.md) 为准；该文档根据服务端 `apidoc.json` 同步。

## 服务与认证

- API 基础地址：`http://api.fxyz.site`
- 官网：[https://www.fxyz.site/](https://www.fxyz.site/)
- PyPI 安装包和 Python 导入包：`fxyz`
- PyPI 项目页：[pypi.org/project/fxyz](https://pypi.org/project/fxyz/)
- PyPI 安装命令：`python -m pip install fxyz`
- 接口认证：所有当前文档中的接口都要求 `token` 参数。Token 由用户在 Fxyz 网站获取，必须从安全配置读取，不要写入代码、日志或回复内容。
- HTTP 接口默认使用 GET，并将接口参数作为 URL 查询参数传递。项目客户端也支持通过 `method="post"` 发起 POST 查询参数请求。

## 能力范围

当前接口文档共包含 17 个接口：

| 类别 | 能力 |
|---|---|
| 基础数据 | 股票列表（含沪深可转债）、行业/概念/特色板块成分股、财务核心指标 |
| 涨停板数据 | 涨停板、跌停板、炸板、强势股、次新股 |
| 实时行情数据 | 实时行情、K 线、日线快照、买卖五档、竞价、逐笔交易、分价、资金流向、复权变更 |

K 线周期包括 `1m`、`5m`、`15m`、`30m`、`1h`、`1d`、`1w`、`1mon`、`1y`。数据类型根据接口支持股票、ETF、指数和沪深可转债；具体可选值及限制见接口文档。

## 按用户意图选择接口

| 用户需要 | 推荐 SDK 方法 |
|---|---|
| 股票、ETF、指数或可转债代码列表 | `BaseApi.getStockList(flag, token)` |
| 行业、概念或特色板块的成分股 | `BaseApi.getSector(symbol, token)` |
| 单只股票的财务核心指标 | `BaseApi.getFinanceMetric(code, startDate, endDate, token)` |
| 单个标的实时行情 | `BoardApi.getRealTimeQuote(symbol, code, token)` |
| K 线、日线快照或买卖五档 | `MarketApi.getKLine(...)`、`getDaySnapshot(...)`、`getFiveLevel(...)` |
| 涨停、跌停、炸板、强势股或次新股 | `BoardApi.getZhangTingBan(...)`、`getDieTingBan(...)`、`getZhaBan(...)`、`getQiangShiGu(...)`、`getCiXinGu(...)` |
| 竞价、逐笔、分价、资金流向或复权变更 | `MarketApi.getBidData(...)`、`getDealData(...)`、`getPriceData(...)`、`getMoneyFlow(...)`、`getAdjustment(...)` |

此表用于快速路由；参数详情和返回字段以 API 接口文档中的对应路径为准。

## Python SDK 使用

从 PyPI 安装 SDK：

```bash
python -m pip install fxyz
```

示例：

```python
import os

from fxyz.scripts.api import BaseApi
from fxyz.scripts.api.MarketApi import MarketApi

token = os.environ["FXYZ_TOKEN"]

# 获取股票、ETF、指数等列表；flag=10 表示沪深可转债
stocks = BaseApi.getStockList(flag=0, token=token)

# 获取财务核心指标（仅支持单只股票）
metrics = BaseApi.getFinanceMetric(
    code="000001",
    startDate="2026-01-01",
    endDate="2026-03-31",
    token=token,
)

# 获取沪深可转债的 1 分钟 K 线
bars = MarketApi.getKLine(
    symbol="bond",
    code="110000",
    period="1m",
    cq="1",
    startDate="2026-03-01",
    endDate="2026-03-31",
    token=token,
)
```

SDK 方法返回 JSON 解码后的 Python 对象。传入 `code="all"` 的范围、周期和账号权限因接口不同而异，调用前请查阅完整接口文档。

## 安全与数据使用

- 不要提交真实 Token。`fxyz/scripts/Config.py` 中的默认 Token 为空。
- 接口权限和全市场查询能力由服务端账号配置决定；不要假定所有 Token 都能访问全部数据。
- 按 API 服务条款和调用限制使用数据，并处理网络错误、权限错误和空结果。
- 行情数据是 API 返回的数据，不构成投资建议。
