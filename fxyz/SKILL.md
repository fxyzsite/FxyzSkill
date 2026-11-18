---
name: fxyz
description: 黑狼数据API提供全面、准确、稳定的股票实时行情数据，包括沪深京A股、ETF基金、指数等行情数据，以及涨停板、跌停板、炸板、强势股等特色数据，帮助开发者和研究者构建创新的交易和分析工具。
---

# 黑狼数据 (FXYZ)

## 概述

Fxyz（黑狼数据，http://www.fxyz.site/）是一个专业的股票实时数据API服务平台，提供：
- **基础数据**：股票列表、板块成分股、财务核心指标
- **实时行情**：30+行情指标，沪深京A股、ETF基金实时数据
- **特色数据**：涨停板、跌停板、炸板、强势股、次新股实时监控
- **K线数据**：9种周期（1分钟至年线），支持复权处理
- **盘口数据**：买卖五档、竞价数据、逐笔交易、分价统计
- **资金分析**：特大单、大单、中单、小单资金流向

## 快速上手

### 1. 环境准备

- 安装Python运行环境（推荐Python 3.7+）
- 安装 Fxyz Python SDK（包含 `requests` 依赖）：`python -m pip install fxyz`

```bash
python -m pip install fxyz
```

### 2. 获取Token

- 访问黑狼数据官网注册账号：http://www.fxyz.site/
- 登录后在个人中心获取API Token
- Token激活参考：http://www.fxyz.site/#apply

### 3. 配置Token

在 `scripts/Config.py` 中配置您的token：

```python
class Config:
    SERVER_URL = "http://api.fxyz.site"  # Api调用服务地址
    TOKEN = "your_token_here"  # 替换为您的token
```

### 4. 使用API

根据接口文档，使用Python代码获取数据：

```python
from fxyz.scripts.api.BoardApi import BoardApi
from fxyz.scripts.api.MarketApi import MarketApi
from fxyz.scripts.Config import Config

# 获取实时行情
result = BoardApi.getRealTimeQuote(
    symbol="stock",
    code="000001",
    token=Config.TOKEN
)

# 获取K线数据
result = MarketApi.getKLine(
    symbol="stock",
    code="000001",
    period="1d",
    cq="1",
    startDate="2026-04-01",
    endDate="2026-04-14",
    token=Config.TOKEN
)
```

## API模块说明

### Basic Api - 基础接口

- **股票列表** (`BaseApi.getStockList`): 获取各类股票列表（沪深京A股、ETF、指数等）
- **概念成分股** (`BaseApi.getSector`): 获取行业、概念或特色板块成分股
- **财务核心指标** (`BaseApi.getFinanceMetric`): 获取单只股票在日期范围内的财务指标

### Board Api - 涨跌板接口

- **实时行情** (`BoardApi.getRealTimeQuote`): 获取30+行情指标的实时数据
- **涨停板** (`BoardApi.getZhangTingBan`): 获取涨停板实时监控数据
- **跌停板** (`BoardApi.getDieTingBan`): 获取跌停板实时监控数据
- **炸板** (`BoardApi.getZhaBan`): 获取炸板实时监控数据
- **强势股** (`BoardApi.getQiangShiGu`): 获取强势股筛选数据
- **次新股** (`BoardApi.getCiXinGu`): 获取次新股交易数据

### Market Api - 行情接口

- **实时K线** (`MarketApi.getKLine`): 获取9种周期的K线数据，支持复权
- **日线快照** (`MarketApi.getDaySnapshot`): 获取日线级别快照数据
- **买卖五档** (`MarketApi.getFiveLevel`): 获取实时买卖五档盘口数据
- **竞价数据** (`MarketApi.getBidData`): 获取集合竞价数据（09:15-09:25）
- **逐笔交易** (`MarketApi.getDealData`): 获取逐笔成交明细数据
- **分价数据** (`MarketApi.getPriceData`): 获取分价位成交量统计
- **资金流向** (`MarketApi.getMoneyFlow`): 获取主力资金流向分析
- **复权变更** (`MarketApi.getAdjustment`): 获取股票或ETF的复权变更数据

## Python脚本示例

- [完整API调用示例](scripts/StockApiClient.py) - 包含当前17个接口的调用代码
- [涨跌板接口API](scripts/api/BoardApi.py) - Board Api模块实现
- [行情接口API](scripts/api/MarketApi.py) - Market Api模块实现
- [基础接口API](scripts/api/BaseApi.py) - Basic Api模块实现

## 详细文档说明列表

| ID | 文档名称 | 描述 |
|----:|:---------|:-----|
| 1 | [黑狼数据API接口文档](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md) | 17个接口说明，包含请求参数、权限标识和返回字段。 |

## 日志规范

所有API调用都会自动打印格式化的日志信息，包括：
- ✅ 请求参数
- ✅ 返回数据的记录数
- ✅ 返回数据的第一条数据（JSON格式）

示例输出：
```
============================================================
[BoardApi.getRealTimeQuote] API调用成功
  请求参数:
    - symbol: stock
    - code: 000001
  返回数据:
    - 记录数: 1
    - 第一条数据: {
        "code": "000001",
        "name": "平安银行",
        "zxj": 11.07,
        ...
      }
============================================================
```

## 注意事项

1. **Token安全**: 请妥善保管您的Token，不要泄露给他人或提交到公开代码仓库
2. **请求频率**: 请控制API调用频率，避免短时间内大量请求导致IP被封
3. **数据更新**: 
   - 实时数据更新频率按接口说明区分；行情接口包含每分钟、秒级更新描述
   - 历史数据的更新时点以对应接口文档为准，文档中列有收盘后15:30或18:00更新的接口
4. **权限要求**:
   - `code=all`和包年权限要求仅适用于接口文档明确支持的接口，请逐接口核对
5. **错误处理**: 建议实现完善的异常处理和重试机制
