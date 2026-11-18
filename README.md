# Fxyz Python SDK：黑狼数据股票行情 API

Fxyz Python SDK 是黑狼数据（FXYZ）的 Python 客户端示例包，可通过 HTTP API 获取沪深京 A 股、ETF 和指数相关行情。它覆盖实时行情、K 线、盘口、逐笔成交、涨跌停板与资金流向等数据，适用于 Python 数据分析、量化研究和行情应用开发。

本仓库同时包含 Fxyz Skill 说明、API 参考文档和 SDK 源码。
- Fxyz 官网：[http://www.fxyz.site/](https://www.fxyz.site/)
- API 服务地址：`http://api.fxyz.site`
- 开源仓库：[https://github.com/fxyzsite/FxyzSkill](https://github.com/fxyzsite/FxyzSkill)
- API 接口文档：[fxyz/references/apidoc.md](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)
- Fxyz Skill 指南：[fxyz/SKILL.md](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/SKILL.md)

---

##  功能特点

- **股票与基金行情**：沪深京 A 股、ETF、指数的实时行情和股票列表。
- **K 线与历史行情**：支持1 分钟、 5 分钟、15 分钟、30 分钟、1 小时、日、周、月、年等周期及复权参数。
- **盘口与成交数据**：买卖五档、集合竞价、逐笔成交、分价统计和日线快照。
- **市场监控数据**：涨停、跌停、炸板、强势股和次新股数据。
- **资金流向**：按大单级别查看资金流向数据。

## 核心优势

- ✅ **全面的数据覆盖** - 沪深京A股、ETF基金、主流指数
- ✅ **实时行情数据** - 30+行情指标，每分钟更新
- ✅ **特色监控数据** - 涨停板、跌停板、炸板、强势股实时追踪
- ✅ **多周期K线** - 9种时间周期（5分钟至年线），支持复权
- ✅ **深度盘口数据** - 买卖五档、竞价数据、逐笔交易
- ✅ **资金流向分析** - 特大单、大单、中单、小单分类统计
- ✅ **规范化日志** - 自动打印请求参数、返回记录数、示例数据

---


## 环境要求

- Python 3.7 或更高版本
- 依赖：`requests`
- 有效的 Fxyz API Token；接口可用范围取决于账号权限

## 安装
从 PyPI 安装：
```bash
python -m pip install fxyz
```

## 获取 API Token

访问 [Fxyz 官网](http://www.fxyz.site/)，注册并登录后按账号页面指引获取 API Token。请勿将真实 Token 写入公开代码、提交到仓库或粘贴到公开日志中。Token 激活说明见 [官网申请页面](http://www.fxyz.site/#apply)。

## 快速开始

SDK 保留仓库现有调用接口，Token 通过参数传入：

```python
from fxyz.scripts.api.BoardApi import BoardApi
from fxyz.scripts.api.MarketApi import MarketApi

token = "YOUR_FXYZ_TOKEN"

# 获取单只股票实时行情
quote = BoardApi.getRealTimeQuote(
    symbol="stock",
    code="000001",
    token=token,
)
print(quote)

# 获取日 K 线（cq: 1 不复权，2 前复权，3 后复权）
kline = MarketApi.getKLine(
    symbol="stock",
    code="000001",
    period="1d",
    cq="1",
    startDate="2026-04-01",
    endDate="2026-04-14",
    token=token,
)
print(kline)
```

API 返回 JSON 解码后的 Python 对象（通常为列表或字典）。全部接口、参数和返回字段请查看[完整 API 文档](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)。

### 支持的 API

| 模块 | 方法 | 数据 |
|---|---|---|
| 基础 | `BaseApi.getStockList` | 股票、指数、ETF 等列表 |
| 市场 | `BoardApi.getRealTimeQuote` | 实时行情 |
| 市场 | `BoardApi.getZhangTingBan`、`getDieTingBan` | 涨停板、跌停板 |
| 市场 | `BoardApi.getZhaBan`、`getQiangShiGu`、`getCiXinGu` | 炸板、强势股、次新股 |
| 行情 | `MarketApi.getKLine`、`getDaySnapshot` | K 线、日线快照 |
| 行情 | `MarketApi.getFiveLevel`、`getBidData` | 五档盘口、集合竞价 |
| 行情 | `MarketApi.getDealData`、`getPriceData` | 逐笔成交、分价统计 |
| 行情 | `MarketApi.getMoneyFlow` | 资金流向 |

## 本地开发与验证

```bash
python -m pip install -e .
python -c "from fxyz.scripts.api.BoardApi import BoardApi; from fxyz.scripts.api.MarketApi import MarketApi; print('Fxyz SDK imports OK')"
```

仓库里的 `fxyz/scripts/StockApiClient.py` 是需要有效 Token 才能访问线上 API 的示例程序；导入检查和本地构建不需要 API Token。

## 项目结构

```text
fxyz/
├── __init__.py
├── SKILL.md
├── references/
│   └── apidoc.md
└── scripts/
    ├── Config.py
    ├── StockApiClient.py
    ├── api/
    │   ├── BaseApi.py
    │   ├── BoardApi.py
    │   └── MarketApi.py
    └── util/
        └── DataUtil.py
pyproject.toml
README.md
```

## 安全与使用说明

- SDK 请求需要有效 Token；全市场查询等能力可能需要相应账号权限。
- 请遵循 Fxyz 官网服务条款和 API 调用限制，并合理控制请求频率。
- 行情数据仅供研究和开发使用；请以服务端返回及官方说明为准。
- 本 SDK 不提供投资建议，也不保证数据适合任何特定交易用途。
- 如遇接口或权限问题，请查阅[接口文档](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)并联系 Fxyz 官方。

## 关键词

Fxyz Python SDK、黑狼数据 Python API、A 股行情 API、沪深京股票数据、ETF 行情接口、Python 实时股票行情、股票 K 线 API、量化数据接口、涨停板数据、资金流向 API。
