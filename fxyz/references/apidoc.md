# 黑狼数据API接口文档

> 官方文档版本：v1.0  
> 最后更新：2026-04-14  
> API基础地址：`http://api.fxyz.site`

---

## 📋 目录

- [概述](#概述)
- [认证说明](#认证说明)
- [接口分类](#接口分类)
- [1. Basic Api - 基础接口](#1-basic-api---基础接口)
  - [1.1 股票列表](#11-股票列表)
- [2. Board Api - 涨跌板接口](#2-board-api---涨跌板接口)
  - [2.1 实时行情](#21-实时行情)
  - [2.2 涨停板](#22-涨停板)
  - [2.3 跌停板](#23-跌停板)
  - [2.4 炸板](#24-炸板)
  - [2.5 强势股](#25-强势股)
  - [2.6 次新股](#26-次新股)
- [3. Market Api - 行情接口](#3-market-api---行情接口)
  - [3.1 实时K线](#31-实时k线)
  - [3.2 日线快照](#32-日线快照)
  - [3.3 买卖五档](#33-买卖五档)
  - [3.4 竞价数据](#34-竞价数据)
  - [3.5 逐笔交易](#35-逐笔交易)
  - [3.6 分价数据](#36-分价数据)
  - [3.7 资金流向](#37-资金流向)
- [注意事项](#注意事项)
- [技术支持](#技术支持)

---

## 概述

黑狼数据（http://www.fxyz.size）是一个专业的股票实时数据API服务平台，提供沪深京A股、ETF基金、指数等全面的金融行情数据。平台致力于为广大投资者、量化交易者和研究人员提供准确、稳定、实时的数据服务。

### 核心功能

- **基础数据**：全市场股票列表、交易日历
- **实时行情**：30+行情指标，包括价格、成交量、涨跌幅、换手率等
- **特色数据**：涨停板、跌停板、炸板、强势股、次新股实时监控
- **K线数据**：支持8种周期（5分钟至年线），支持复权处理
- **盘口数据**：买卖五档、竞价数据、逐笔交易、分价统计
- **资金分析**：特大单、大单、中单、小单资金流向分析

### 数据更新频率

| 数据类型 | 更新频率 | 更新时间 |
|---------|---------|---------|
| 实时行情 | 每分钟 | 交易时间段内 |
| K线数据 | 实时/盘后 | 交易中实时更新，收盘后15:30更新 |
| 历史数据 | 盘后 | 收盘后18:00更新 |
| 涨跌停板 | 每分钟 | 交易时间段内，收盘后15:30更新 |

---

## 认证说明

### Token获取

1. 访问黑狼数据官网：http://www.fxyz.size
2. 注册账号并登录
3. 在个人中心获取API Token
4. Token激活参考：http://www.fxyz.site/#apply

### 使用方式

所有API请求都需要在URL参数中携带 `token` 参数：

```
http://api.fxyz.site/wolf/list?flag=0&token=YOUR_TOKEN
```

---

## 接口分类

黑狼数据API共分为三大类，总计14个接口：

| 分类 | 接口数量 | 说明 |
|------|---------|------|
| Basic Api | 1 | 基础数据接口 |
| Board Api | 6 | 涨跌板特色数据接口 |
| Market Api | 7 | 行情与交易数据接口 |

---

## 1. Basic Api - 基础接口

### 1.1 股票列表

**接口ID**: 11  
**接口名称**: 股票列表  
**接口描述**: 获取股票列表。历史数据收盘后六点更新。  
**请求URL**: `/wolf/list`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| flag | int | ✅ | `0` - 所有股票<br>`1` - 深交所股票<br>`2` - 上交所股票<br>`3` - 北交所股票<br>`4` - 指数<br>`5` - 创业板股票<br>`6` - 科创板股票<br>`7` - ETF<br>`8` - ST股票<br>`9` - 退市股票 | 股票类型筛选 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| code | String | 股票代码 |
| name | String | 股票名称 |

#### 请求示例

```bash
# 获取所有股票列表
curl "http://api.fxyz.site/wolf/list?flag=0&token=88888888"

# 获取深交所股票
curl "http://api.fxyz.site/wolf/list?flag=1&token=88888888"

# 获取ETF基金
curl "http://api.fxyz.site/wolf/list?flag=7&token=88888888"
```

#### 返回示例

```json
[
  {"code":"000011","name":"深物业A"},
  {"code":"300697","name":"电工合金"}
]
```

#### Python调用示例

```python
from fxyz.scripts.api.BaseApi import BaseApi

# 获取所有股票列表
result = BaseApi.getStockList(flag=0, token="your_token")
print(result)

# 获取创业板股票
result = BaseApi.getStockList(flag=5, token="your_token")
print(result)
```

---

## 2. Board Api - 涨跌板接口

### 2.1 实时行情

**接口ID**: 21  
**接口名称**: 实时行情  
**接口描述**: 获取沪深A股实时行情数据。提供涨速、涨跌幅、换手率、振幅、量比、内盘、外盘、ROE等行情指标数据，适用于投资研究、量化交易。包年版支持all参数获取盘中全市场实时数据。  
**数据更新**: 实时数据交易时间段每1分钟更新  
**请求URL**: `/wolf/time`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| symbol | String | ✅ | `stock` - 沪深京A股<br>`etf` - ETF基金 | 股票类型 |
| code | String | ✅ | `all` - 全推全市场数据（包年版）<br>具体股票代码（如`000001`）- 单个股票数据 | 股票代码 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| code | String | 股票代码 |
| name | String | 股票名称 |
| tradeDate | String | 交易时间 |
| zxj | float | 最新价（元） |
| open | float | 开盘价（元） |
| high | float | 最高价（元） |
| low | float | 最低价（元） |
| cjl | float | 成交量（手） |
| cje | float | 成交额（元） |
| zrspj | float | 昨日收盘价（元） |
| jj | float | 均价（元） |
| ztj | float | 涨停价（元） |
| dtj | float | 跌停价（元） |
| zdf | float | 涨跌幅（%） |
| zde | float | 涨跌额（元） |
| zf | float | 振幅（%） |
| hsl | float | 换手率（%） |
| lb | float | 量比 |
| zsz | float | 总市值（元） |
| ltsz | float | 流通市值（元） |
| sjl | float | 市净率 |
| wb | float | 委比（%） |
| wp | float | 外盘（手） |
| np | float | 内盘（手） |
| roe | float | ROE（净资产收益率） |
| zgb | float | 总股本（股） |
| ltgb | float | 流通股本（股） |
| jtsyl | float | 市盈率（静） |
| dtsyl | float | 市盈率（动） |
| ttmsyl | float | 市盈率（TTM） |
| zdf03 | float | 3日涨跌幅（%） |
| zdf05 | float | 5日涨跌幅（%） |
| zdf10 | float | 10日涨幅（%） |
| zdf20 | float | 20日涨幅（%） |
| zdf60 | float | 60日涨幅（%） |
| zdfyear | float | 今年以来涨幅（%） |

#### 请求示例

```bash
# 获取单个股票实时行情
curl "http://api.fxyz.site/wolf/time?symbol=stock&code=000001&token=88888888"

# 获取全市场实时行情（包年版）
curl "http://api.fxyz.site/wolf/time?symbol=stock&code=all&token=88888888"
```

#### 返回示例

```json
[{
  "code":"000001",
  "name":"平安银行",
  "tradeDate":"2026-04-13 15:09:37",
  "zxj":11.07,
  "open":11.05,
  "high":11.09,
  "low":11.03,
  "cjl":406104.0,
  "cje":4.490568E8,
  "zrspj":11.09,
  "jj":11.06,
  "ztj":12.2,
  "dtj":9.98,
  "zdf":-0.18,
  "zde":-0.02,
  "zf":0.54,
  "hsl":0.21,
  "lb":0.62,
  "zsz":2.1482352E11,
  "ltsz":2.1482E11,
  "sjl":0.48,
  "wb":51.8,
  "wp":168946.0,
  "np":237158.0,
  "roe":9.15,
  "zgb":1.9405918E10,
  "ltgb":1.94056E10,
  "jtsyl":5.04,
  "dtsyl":5.04,
  "ttmsyl":5.04,
  "zdf03":-1.34,
  "zdf05":-0.45,
  "zdf10":0.45,
  "zdf20":1.28,
  "zdf60":-3.82,
  "zdfyear":-2.98
}]
```

#### Python调用示例

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取单个股票实时行情
result = BoardApi.getRealTimeQuote(
    symbol="stock", 
    code="000001", 
    token="your_token"
)
print(result)

# 获取全市场实时行情（包年版）
result = BoardApi.getRealTimeQuote(
    symbol="stock", 
    code="all", 
    token="your_token"
)
print(result)
```

---

### 2.2 涨停板

**接口ID**: 22  
**接口名称**: 涨停板  
**接口描述**: 获取盘中涨停板实时数据。  
**数据更新**: 实时数据交易时间段每1分钟更新，历史数据收盘后15:30更新  
**请求URL**: `/wolf/zt`  
**请求方法**: GET  

#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| tradeDate | String | ✅ | 格式：YYYY-MM-DD<br>示例：2026-04-14 | 交易日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| tradeDate | String | 交易日期 |
| code | String | 股票代码 |
| name | String | 股票名称 |
| cje | float | 成交额（元） |
| scfb | String | 首次封板时间，个股第一次触及涨停的时间 |
| fbzj | float | 封板资金（元），以涨停价买入挂单的资金总量 |
| hsl | float | 换手率（%） |
| lbs | int | 连板数，个股连续封板数量 |
| zhfb | String | 最后封板时间，个股最后一次触及涨停的时间 |
| ltsz | float | 流通市值（元） |
| zxj | float | 最新价（元） |
| zsz | float | 总市值（元） |
| zbcs | int | 炸板次数，个股打开涨停板的次数 |
| zdf | float | 涨跌幅（%） |
| zttj | String | 涨停统计，n/m代表m天中有n次涨停板 |
| update | String | 更新时间 |

#### 请求示例

```bash
curl "http://api.fxyz.site/wolf/zt?tradeDate=2026-04-14&token=88888888"
```

#### 返回示例

```json
[{
  "tradeDate":"2026-03-23",
  "code":"000703",
  "name":"恒逸石化",
  "cje":7.15731E8,
  "scfb":"13:06:42",
  "fbzj":1.34348E8,
  "hsl":1.75654,
  "lbs":1,
  "zhfb":"13:06:42",
  "ltsz":4.24271E10,
  "zxj":11.84,
  "zsz":4.2655E10,
  "zbcs":0,
  "zdf":10.0372,
  "zttj":"1/1",
  "update":"2026-03-25 17:32:20"
}]
```

#### Python调用示例

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取指定日期的涨停板数据
result = BoardApi.getZhangTingBan(
    tradeDate="2026-04-14", 
    token="your_token"
)
print(result)
```

---

### 2.3 跌停板

**接口ID**: 23  
**接口名称**: 跌停板  
**接口描述**: 获取盘中跌停板实时数据。  
**数据更新**: 实时数据交易时间段每1分钟更新，历史数据收盘后15:30更新  
**请求URL**: `/wolf/dt`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| tradeDate | String | ✅ | 格式：YYYY-MM-DD | 交易日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| tradeDate | String | 交易日期 |
| cje | float | 成交额（元） |
| code | String | 股票代码 |
| lxdt | int | 连续跌停天数 |
| fbcje | float | 板上成交额（元），成交价格为该股票跌停价的所有成交额的总和 |
| fdzj | float | 封单资金（元） |
| hsl | float | 换手率（%） |
| zhfb | String | 最后封板时间 |
| ltsz | float | 流通市值（元） |
| name | String | 股票名称 |
| kbcs | int | 开板次数，个股打开跌停板的次数 |
| zxj | float | 最新价（元） |
| pe | float | 动态市盈率 |
| zsz | float | 总市值（元） |
| zdf | float | 涨跌幅（%） |
| update | String | 更新时间 |

#### 请求示例

```bash
curl "http://api.fxyz.site/wolf/dt?tradeDate=2026-04-14&token=88888888"
```

#### 返回示例

```json
[{
  "tradeDate":"2026-03-23",
  "cje":1.00366E9,
  "code":"000020",
  "lxdt":1,
  "fbcje":1.62989E8,
  "fdzj":1.88139E7,
  "hsl":25.7226,
  "zhfb":"14:45:03",
  "ltsz":3.80447E9,
  "name":"深华发Ａ",
  "kbcs":1,
  "zxj":21.0,
  "pe":209.705,
  "zsz":5.94639E9,
  "zdf":-9.98714,
  "update":"2026-03-25 17:32:14"
}]
```

#### Python调用示例

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取指定日期的跌停板数据
result = BoardApi.getDieTingBan(
    tradeDate="2026-04-14", 
    token="your_token"
)
print(result)
```

---

### 2.4 炸板

**接口ID**: 24  
**接口名称**: 炸板  
**接口描述**: 获取盘中炸板实时数据。  
**数据更新**: 实时数据交易时间段每1分钟更新，历史数据收盘后15:30更新  
**请求URL**: `/wolf/zb`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| tradeDate | String | ✅ | 格式：YYYY-MM-DD | 交易日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| tradeDate | String | 交易日期 |
| cje | float | 成交额（元） |
| code | String | 股票代码 |
| scfb | String | 首次封板时间 |
| hsl | float | 换手率（%） |
| ltsz | float | 流通市值（元） |
| name | String | 股票名称 |
| zxj | float | 最新价（元） |
| zsz | float | 总市值（元） |
| zbcs | int | 炸板次数 |
| zdf | float | 涨跌幅（%） |
| zf | float | 振幅（%） |
| zs | float | 涨速 |
| ztp | float | 涨停价 |
| zttj | String | 涨停统计 |
| update | String | 更新时间 |

#### 请求示例

```bash
curl "http://api.fxyz.site/wolf/zb?tradeDate=2026-04-14&token=88888888"
```

#### Python调用示例

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取指定日期的炸板数据
result = BoardApi.getZhaBan(
    tradeDate="2026-04-14", 
    token="your_token"
)
print(result)
```

---

### 2.5 强势股

**接口ID**: 25  
**接口名称**: 强势股  
**接口描述**: 获取盘中强势股票实时数据。  
**数据更新**: 实时数据交易时间段每1分钟更新，历史数据收盘后15:30更新  
**请求URL**: `/wolf/qs`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| tradeDate | String | ✅ | 格式：YYYY-MM-DD | 交易日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| tradeDate | String | 交易日期 |
| cje | float | 成交额（元） |
| code | String | 股票代码 |
| rxly | int | 入选理由<br>`1` - 60日新高<br>`2` - 近期多次涨停<br>`3` - 60日新高且近期多次涨停 |
| hsl | float | 换手率（%） |
| lb | float | 量比 |
| ltsz | float | 流通市值（元） |
| name | String | 股票名称 |
| sfxh | int | 是否新高<br>`0` - 否<br>`1` - 是 |
| zxj | float | 最新价 |
| zsz | float | 总市值（元） |
| zdf | float | 涨跌幅（%） |
| zs | float | 涨速 |
| ztp | float | 涨停价 |
| zttj | String | 涨停统计 |
| update | String | 更新时间 |

#### 请求示例

```bash
curl "http://api.fxyz.site/wolf/qs?tradeDate=2026-04-14&token=88888888"
```

#### Python调用示例

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取指定日期的强势股数据
result = BoardApi.getQiangShiGu(
    tradeDate="2026-04-14", 
    token="your_token"
)
print(result)
```

---

### 2.6 次新股

**接口ID**: 26  
**接口名称**: 次新股  
**接口描述**: 获取次新股数据。  
**数据更新**: 实时数据交易时间段每1分钟更新，历史数据收盘后15:30更新  
**请求URL**: `/wolf/cx`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| cje | float | 成交额（元） |
| code | String | 股票代码 |
| hsl | float | 换手率（%） |
| ssrq | String | 上市日期 |
| ltsz | float | 流通市值（元） |
| name | String | 股票名称 |
| sfxg | int | 是否新高<br>`0` - 否<br>`1` - 是 |
| kbrq | String | 开板日期 |
| kbjr | int | 开板几日 |
| zxj | float | 最新价 |
| zsz | float | 总市值（元） |
| zdf | float | 涨跌幅（%） |
| ztp | float | 涨停价 |
| zttj | String | 涨停统计 |
| update | String | 更新时间 |

#### 请求示例

```bash
curl "http://api.fxyz.site/wolf/cx?token=88888888"
```

#### Python调用示例

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取次新股数据
result = BoardApi.getCiXinGu(token="your_token")
print(result)
```

---

## 3. Market Api - 行情接口

### 3.1 实时K线

**接口ID**: 31  
**接口名称**: 实时K线  
**接口描述**: 获取沪深A股和ETF实时K线数据。包年版支持all参数获取盘后全市场数据，仅限近一周内的日线数据。  
**数据更新**: 实时数据交易时间段实时更新，历史数据收盘后15:30更新，all参数历史数据盘后18:00更新  
**请求URL**: `/wolf/time/kline`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| symbol | String | ✅ | `stock` - 沪深京A股<br>`etf` - ETF基金<br>`index` - 指数 | 股票类型 |
| code | String | ✅ | 具体股票代码（如`000001`）<br>`all` - 全推全市场数据（包年版，仅限近一周日线） | 股票代码 |
| period | String | ✅ | `5m` - 5分钟线<br>`15m` - 15分钟线<br>`30m` - 30分钟线<br>`1h` - 1小时线<br>`1d` - 日线<br>`1w` - 周线<br>`1mon` - 月线<br>`1y` - 年线 | K线周期 |
| cq | String | ✅ | `1` - 不复权<br>`2` - 前复权<br>`3` - 后复权 | 复权类型 |
| startDate | String | ✅ | 格式：YYYY-MM-DD | 开始日期 |
| endDate | String | ✅ | 格式：YYYY-MM-DD | 结束日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| t | String | 交易时间 |
| code | String | 股票代码 |
| o | float | 开盘价（元） |
| c | float | 收盘价（元） |
| h | float | 最高价（元） |
| l | float | 最低价（元） |
| v | float | 成交量（手） |
| a | float | 成交额（元） |
| pc | float | 昨收价（元） |

#### 请求示例

```bash
curl "http://api.fxyz.site/wolf/time/kline?symbol=stock&code=000001&period=1d&cq=1&startDate=2026-04-01&endDate=2026-04-14&token=88888888"
```

#### 返回示例

```json
[{
  "t":"2026-03-23 00:00:00",
  "code":"000001",
  "o":10.68,
  "c":10.45,
  "h":10.68,
  "l":10.43,
  "v":1580088.0,
  "a":1.6663283E9,
  "pc":10.77
}]
```

#### Python调用示例

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取日K线数据
result = MarketApi.getKLine(
    symbol="stock",
    code="000001",
    period="1d",
    cq="1",
    startDate="2026-04-01",
    endDate="2026-04-14",
    token="your_token"
)
print(result)

# 获取周K线数据（前复权）
result = MarketApi.getKLine(
    symbol="stock",
    code="000001",
    period="1w",
    cq="2",
    startDate="2026-01-01",
    endDate="2026-04-14",
    token="your_token"
)
print(result)
```

---

### 3.2 日线快照

**接口ID**: 32  
**接口名称**: 日线快照  
**接口描述**: 获取沪深A股和ETF实时日线行情数据。包年版支持all参数获取盘中全市场实时数据。  
**请求URL**: `/wolf/time/day`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| symbol | String | ✅ | `stock` - 沪深京A股<br>`etf` - ETF基金 | 股票类型 |
| code | String | ✅ | `all` - 全推全市场数据<br>具体股票代码 - 单个股票数据 | 股票代码 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| t | String | 交易时间 |
| code | String | 股票代码 |
| o | float | 开盘价（元） |
| c | float | 收盘价（元） |
| h | float | 最高价（元） |
| l | float | 最低价（元） |
| v | float | 成交量（手） |
| a | float | 成交额（元） |
| pc | float | 昨收价（元） |

#### Python调用示例

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取单个股票日线快照
result = MarketApi.getDaySnapshot(
    symbol="stock", 
    code="000001", 
    token="your_token"
)
print(result)

# 获取全市场日线快照（包年版）
result = MarketApi.getDaySnapshot(
    symbol="stock", 
    code="all", 
    token="your_token"
)
print(result)
```

---

### 3.3 买卖五档

**接口ID**: 33  
**接口名称**: 买卖五档  
**接口描述**: 买卖五档实时数据  
**请求URL**: `/wolf/time/five`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| symbol | String | ✅ | `stock` - 沪深京A股<br>`etf` - ETF基金 | 股票类型 |
| code | String | ✅ | 具体股票代码 | 股票代码 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| t | String | 交易时间 |
| code | String | 股票代码 |
| p | float | 最新价（元） |
| o | float | 开盘价（元） |
| h | float | 最高价（元） |
| l | float | 最低价（元） |
| pc | float | 前收盘价（元） |
| a | float | 成交总额（元） |
| v | float | 成交总量（手） |
| bp1-bp5 | float | 买一至买五价（元） |
| bv1-bv5 | float | 买一至买五量（手） |
| sp1-sp5 | float | 卖一至卖五价（元） |
| sv1-sv5 | float | 卖一至卖五量（手） |

#### Python调用示例

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取买卖五档数据
result = MarketApi.getFiveLevel(
    symbol="stock", 
    code="000001", 
    token="your_token"
)
print(result)
```

---

### 3.4 竞价数据

**接口ID**: 34  
**接口名称**: 竞价数据  
**接口描述**: 获取沪深A股实时竞价数据，竞价时间段：09:15-09:25  
**请求URL**: `/wolf/time/bid`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| code | String | ✅ | 具体股票代码 | 股票代码 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| code | String | 股票代码 |
| t | String | 交易时间 |
| p | float | 最新价（元） |
| pc | float | 昨日收盘价（元） |
| zf | float | 竞价涨幅（%） |
| jv | long | 竞价量（手） |
| je | long | 竞价金额（元） |
| nv | long | 未匹配量（手） |
| ne | long | 未匹配金额（元） |
| bs | int | 买卖点<br>`-1` - 未匹配量靠近卖一侧<br>`1` - 未匹配量靠近买一侧 |

#### Python调用示例

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取竞价数据
result = MarketApi.getBidData(
    code="000001", 
    token="your_token"
)
print(result)
```

---

### 3.5 逐笔交易

**接口ID**: 35  
**接口名称**: 逐笔交易  
**接口描述**: 获取沪深A股逐笔交易数据。  
**数据更新**: 历史数据盘后18:00更新  
**请求URL**: `/wolf/deal`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| code | String | ✅ | 具体股票代码 | 股票代码 |
| tradeDate | String | ✅ | 格式：YYYY-MM-DD | 交易日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| t | String | 交易时间 |
| cjj | float | 成交价（元） |
| zd | float | 涨跌额（元） |
| cjl | long | 成交量（手） |
| cje | long | 成交额（元） |
| bs | int | 买卖点<br>`-1` - 主动性卖<br>`1` - 主动性买 |

#### Python调用示例

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取逐笔交易数据
result = MarketApi.getDealData(
    code="000001", 
    tradeDate="2026-04-14", 
    token="your_token"
)
print(result)
```

---

### 3.6 分价数据

**接口ID**: 36  
**接口名称**: 分价数据  
**接口描述**: 获取沪深A股分价数据。  
**数据更新**: 历史数据盘后18:00更新  
**请求URL**: `/wolf/price`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| code | String | ✅ | 具体股票代码 | 股票代码 |
| tradeDate | String | ✅ | 格式：YYYY-MM-DD | 交易日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| cjj | float | 成交价（元） |
| cjl | long | 成交量（手） |
| ratio | float | 占比（%） |

#### Python调用示例

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取分价数据
result = MarketApi.getPriceData(
    code="000001", 
    tradeDate="2026-04-14", 
    token="your_token"
)
print(result)
```

---

### 3.7 资金流向

**接口ID**: 37  
**接口名称**: 资金流向  
**接口描述**: 获取沪深A股资金流向数据。资金流数据区分主买、主卖、特大单、大单、中单、小单等。  
**数据更新**: 历史数据盘后18:00更新  
**请求URL**: `/wolf/money`  
**请求方法**: GET  


#### 请求参数

| 参数名 | 类型 | 必填 | 取值范围 | 说明 |
|--------|------|------|----------|------|
| code | String | ✅ | 具体股票代码 | 股票代码 |
| tradeDate | String | ✅ | 格式：YYYY-MM-DD | 交易日期 |
| token | String | ✅ | - | API认证Token |

#### 返回参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| c | String | 股票代码 |
| t | String | K线日期 |
| buynum | int | 主买单总单数 |
| sellnum | int | 主卖单总单数 |
| totalnum | int | 成交笔数 |
| buytddcje | float | 主买特大单成交额（元） |
| buyddcje | float | 主买大单成交额（元） |
| buyzdcje | float | 主买中单成交额（元） |
| buysdcje | float | 主买小单成交额（元） |
| selltddcje | float | 主卖特大单成交额（元） |
| sellddcje | float | 主卖大单成交额（元） |
| sellzdcje | float | 主卖中单成交额（元） |
| sellxdcje | float | 主卖小单成交额（元） |
| buytddcjl | int | 主买特大单成交量（手） |
| buyddcjl | int | 主买大单成交量（手） |
| buyzdcjl | int | 主买中单成交量（手） |
| buyxdcjl | int | 主买小单成交量（手） |
| selltddcjl | int | 主卖特大单成交量（手） |
| sellddcjl | int | 主卖大单成交量（手） |
| sellzdcjl | int | 主卖中单成交量（手） |
| sellxdcjl | int | 主卖小单成交量（手） |

#### Python调用示例

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取资金流向数据
result = MarketApi.getMoneyFlow(
    code="000001", 
    tradeDate="2026-04-14", 
    token="your_token"
)
print(result)
```

---

## 注意事项

### 1. Token管理

- **安全性**: 请妥善保管您的Token，不要泄露给他人或提交到公开代码仓库
- **有效期**: Token长期有效，如遇问题请联系客服重置
- **多环境**: 建议在开发环境和生产环境使用不同的Token

### 2. 请求限制

- **频率限制**: 请控制API调用频率，避免短时间内大量请求
- **并发限制**: 建议单IP并发请求数不超过10个
- **违规处理**: 频繁违规可能导致IP被封禁

### 3. 数据时效性

| 数据类型 | 更新时机 | 说明 |
|---------|---------|------|
| 实时行情 | 交易时段每分钟 | 9:30-11:30, 13:00-15:00 |
| 涨跌停板 | 交易时段每分钟 | 收盘后15:30更新最终数据 |
| K线数据 | 实时/盘后 | 交易中实时更新，收盘后15:30更新 |
| 历史数据 | 盘后 | 收盘后18:00完成全部更新 |
| 资金流向 | 盘后 | 收盘后18:00更新 |

### 4. 权限说明

- **Level 1**: 基础接口访问权限
- **Level 2**: 高级接口访问权限
- **Level 3**: 专业接口访问权限（需包年版）
- **全市场数据**: `code=all`参数仅包年版用户可用

### 5. 最佳实践

1. **缓存策略**: 对不频繁变化的数据（如股票列表）进行本地缓存
2. **错误处理**: 实现完善的异常处理机制，处理网络超时等情况
3. **重试机制**: 对于临时性失败，实现指数退避重试
4. **日志记录**: 记录API调用日志，便于问题排查
5. **数据验证**: 对返回数据进行有效性验证

---

## 技术支持

### 联系方式

- **官方网站**: http://www.fxyz.size
- **API文档**: 本文档
- **Token申请**: http://www.fxyz.site/#apply
- **技术支持**: 请通过官网联系客服

### 常见问题

**Q: 如何获取Token？**  
A: 访问 http://www.fxyz.size 注册账号，登录后在个人中心获取。

**Q: 返回数据为空怎么办？**  
A: 检查以下几点：
1. Token是否正确且已激活
2. 交易日期是否为交易日
3. 股票代码是否存在
4. 是否具有相应权限等级

**Q: 全市场数据为什么无法获取？**  
A: `code=all`参数需要包年版权限，请确认您的账户等级。

**Q: 数据更新延迟怎么办？**  
A: 实时数据在交易时段每分钟更新，如遇延迟请稍后重试。历史数据在收盘后统一更新。

---

**文档版本**: v1.0  
**最后更新**: 2026-04-14  
**版权所有**: © 2026 黑狼数据
