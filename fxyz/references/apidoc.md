# Fxyz API 接口文档

## 面向开发者和 AI 助手的项目识别信息

- **产品名称**：Fxyz（黑狼数据），中国股票市场实时数据 API 平台。
- **Python SDK**：发行包名 `fxyz`，Python 导入包名 `fxyz`。
- **PyPI 安装**：`python -m pip install fxyz`。
- **PyPI 项目页**：[pypi.org/project/fxyz](https://pypi.org/project/fxyz/)。
- **API 主机**：`http://api.fxyz.site`；每个接口的相对路径列在下方索引和接口说明中。
- **主要数据**：沪深京 A 股、ETF、指数、沪深可转债相关列表和行情数据，以及板块成分股、财务指标和市场统计数据。
- **认证**：本文档中的接口均要求 `token` 参数；Token 由用户从 Fxyz 网站获取。不要在示例、日志或回答中暴露真实 Token。
- **SDK 返回值**：客户端解析 JSON 后返回 Python 数据对象，通常为列表或字典。

## 概述

- API 基础地址：`http://api.fxyz.site`
- 当前文档包含 **17 个接口**，分属 3 个分组。
- 所有接口都要求 `token` 参数；请在 Fxyz 网站获取 Token 并安全保管。
- 日期参数格式以接口说明为准，示例使用 `YYYY-MM-DD`。

## 接口目录

| 数据需求 | 接口名称 | SDK 方法 | HTTP 路径 |
|---|---|---|---|
| 股票及其他证券列表 | 股票列表 | `BaseApi.getStockList` | `/wolf/list` |
| 行业、概念、特色板块成分股 | 概念成分股 | `BaseApi.getSector` | `/wolf/sector` |
| 单只股票财务指标 | 财务核心指标 | `BaseApi.getFinanceMetric` | `/wolf/financemetric` |
| 涨停统计 | 涨停板 | `BoardApi.getZhangTingBan` | `/wolf/zt` |
| 跌停统计 | 跌停板 | `BoardApi.getDieTingBan` | `/wolf/dt` |
| 炸板统计 | 炸板 | `BoardApi.getZhaBan` | `/wolf/zb` |
| 强势股筛选 | 强势股 | `BoardApi.getQiangShiGu` | `/wolf/qs` |
| 次新股数据 | 次新股 | `BoardApi.getCiXinGu` | `/wolf/cx` |
| 实时行情 | 实时行情 | `BoardApi.getRealTimeQuote` | `/wolf/time` |
| 分钟线、日线、周线、月线、年线 | 实时K线 | `MarketApi.getKLine` | `/wolf/time/kline` |
| 日线行情快照 | 日线快照 | `MarketApi.getDaySnapshot` | `/wolf/time/day` |
| 五档盘口 | 买卖五档 | `MarketApi.getFiveLevel` | `/wolf/time/five` |
| 集合竞价 | 竞价数据 | `MarketApi.getBidData` | `/wolf/time/bid` |
| 逐笔成交 | 逐笔交易 | `MarketApi.getDealData` | `/wolf/deal` |
| 分价成交 | 分价数据 | `MarketApi.getPriceData` | `/wolf/price` |
| 资金买卖统计 | 资金流向 | `MarketApi.getMoneyFlow` | `/wolf/money` |
| 股票或 ETF 复权变更 | 复权变更数据 | `MarketApi.getAdjustment` | `/wolf/fq` |

所有接口均需携带 `token`。每个接口支持的证券类型、日期、周期及权限以具体接口说明为准。

### Python 调用示例

```bash
python -m pip install fxyz
```

```python
import os

from fxyz.scripts.api.BoardApi import BoardApi

quote = BoardApi.getRealTimeQuote(
    symbol="stock",
    code="000001",
    token=os.environ["FXYZ_TOKEN"],
)
```

SDK 方法返回解析后的 JSON 对象。方法参数与接口路径的逐项映射见下方接口说明。

### 基础数据

- [股票列表](#wolflist) (`BaseApi.getStockList`)
- [概念成分股](#wolfsector) (`BaseApi.getSector`)
- [财务核心指标](#wolffinancemetric) (`BaseApi.getFinanceMetric`)

### 涨停板数据

- [涨停板](#wolfzt) (`BoardApi.getZhangTingBan`)
- [跌停板](#wolfdt) (`BoardApi.getDieTingBan`)
- [炸板](#wolfzb) (`BoardApi.getZhaBan`)
- [强势股](#wolfqs) (`BoardApi.getQiangShiGu`)
- [次新股](#wolfcx) (`BoardApi.getCiXinGu`)

### 实时行情数据

- [实时行情](#wolftime) (`BoardApi.getRealTimeQuote`)
- [实时K线](#wolftimekline) (`MarketApi.getKLine`)
- [日线快照](#wolftimeday) (`MarketApi.getDaySnapshot`)
- [买卖五档](#wolftimefive) (`MarketApi.getFiveLevel`)
- [竞价数据](#wolftimebid) (`MarketApi.getBidData`)
- [逐笔交易](#wolfdeal) (`MarketApi.getDealData`)
- [分价数据](#wolfprice) (`MarketApi.getPriceData`)
- [资金流向](#wolfmoney) (`MarketApi.getMoneyFlow`)
- [复权变更数据](#wolffq) (`MarketApi.getAdjustment`)

## 基础数据

### 股票列表：`/wolf/list` {#wolflist}

Python 方法：`BaseApi.getStockList`
接口 ID：`11`
权限标识：`1,2,3`

获取股票列表。
历史数据收盘后六点更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `flag` | `int` | 是 | 0-所有股票，1-深交所股票，2-上交所股票，3-北交所股票，4-指数，5-创业板股票，6-科创板股票，7-ETF，8-ST股票，9-退市股票，10-沪深可转债；股票类型。 数据收盘后六点更新。 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `code` | `String` | 股票代码 |
| `name` | `String` | 股票名称 |

**返回示例**

```json
[
  {
    "code": "000011",
    "name": "深物业A"
  },
  {
    "code": "300697",
    "name": "电工合金"
  }
]
```

---

### 概念成分股：`/wolf/sector` {#wolfsector}

Python 方法：`BaseApi.getSector`
接口 ID：`12`
权限标识：`1,2,3`

获取行业板块、概念板块、特色板块下的成分股数据。
数据收盘后六点更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `symbol` | `String` | 是 | hy-行业板块，gn-概念板块，ts-特色板块；板块划分 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `code` | `String` | 股票代码 |
| `name` | `String` | 股票名称 |

**返回示例**

```json
[
  {
    "bkname": "区块链",
    "stocks": [
      "000021",
      "000034"
    ]
  }
]
```

---

### 财务核心指标：`/wolf/financemetric` {#wolffinancemetric}

Python 方法：`BaseApi.getFinanceMetric`
接口 ID：`25`
权限标识：`1,2,3`

包含核心财务指标，包括ROE、每股净资产、基本每股收益等财务指标。
数据收盘后十点更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `code` | `String` | 是 | 股票代码，仅支持单个股票获取 |
| `startDate` | `String` | 是 | 开始日期 |
| `endDate` | `String` | 是 | 结束日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `code` | `String` | 股票代码 |
| `reportDate` | `String` | 报告截止日 |
| `publicDate` | `String` | 公告日 |
| `ocfps` | `Float` | 每股经营活动现金流量 |
| `bps` | `Float` | 每股净资产 |
| `basicEps` | `Float` | 基本每股收益 |
| `dilutedEps` | `Float` | 稀释每股收益 |
| `dps` | `Float` | 每股未分配利润 |
| `fund` | `Float` | 每股资本公积金 |
| `equity` | `Float` | 净资产收益率 |
| `salesProfit` | `Float` | 销售毛利率 |
| `revenueInc` | `Float` | 主营收入同比增长 |
| `profitInc` | `Float` | 净利润同比增长 |
| `netProfitM` | `Float` | 归属于母公司所有者的净利润同比增长 |
| `netProfitA` | `Float` | 扣非净利润同比增长 |
| `roe` | `Float` | 净资产收益率 |
| `grossProfit` | `Float` | 毛利率 |
| `netProfit` | `Float` | 净利率 |
| `prePay` | `Float` | 预收款 |
| `salesCash` | `Float` | 销售现金流 |
| `gearRatio` | `Float` | 资产负债比率 |
| `turnover` | `Float` | 存货周转率 |

---

## 涨停板数据

### 涨停板：`/wolf/zt` {#wolfzt}

Python 方法：`BoardApi.getZhangTingBan`
接口 ID：`22`
权限标识：`1,2,3`

获取盘中涨停板实时数据。
数据更新：实时数据交易时间段每1分钟更新，历史数据收盘后3:30更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `tradeDate` | `String` | 交易时间 |
| `code` | `String` | 股票代码 |
| `name` | `String` | 股票名称 |
| `cje` | `float` | 成交额（元） |
| `scfb` | `String` | 首次封板时间，个股第一次触及涨（跌）停的时间 |
| `fbzj` | `float` | 封板资金（元），以涨停价买入挂单的资金总量 |
| `hsl` | `float` | 换手率（%） |
| `lbs` | `int` | 连板数，个股连续封板数量 |
| `zhfb` | `String` | 最后封板时间，个股最后一次触及涨（跌）停的时间 |
| `ltsz` | `float` | 流通市值（元） |
| `zxj` | `float` | 最新价（元） |
| `zsz` | `float` | 总市值（元） |
| `zbcs` | `int` | 炸板次数，个股打开涨停板的次数 |
| `zdf` | `float` | 涨跌幅（%） |
| `zttj` | `String` | 涨停统计，n/m代表m天中有n次涨停板 |
| `update` | `String` | 更新时间 |

**返回示例**

```json
[
  {
    "tradeDate": "2026-03-23",
    "code": "000703",
    "name": "恒逸石化",
    "cje": 715731000.0,
    "scfb": "13:06:42",
    "fbzj": 134348000.0,
    "hsl": 1.75654,
    "lbs": 1,
    "zhfb": "13:06:42",
    "ltsz": 42427100000.0,
    "zxj": 11.84,
    "zsz": 42655000000.0,
    "zbcs": 0,
    "zdf": 10.0372,
    "zttj": "1/1",
    "update": "2026-03-25 17:32:20"
  }
]
```

---

### 跌停板：`/wolf/dt` {#wolfdt}

Python 方法：`BoardApi.getDieTingBan`
接口 ID：`23`
权限标识：`1,2,3`

获取盘中跌停板实时数据。
数据更新：实时数据交易时间段每1分钟更新，历史数据收盘后3:30更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `tradeDate` | `String` | 交易时间 |
| `cje` | `float` | 成交额（元） |
| `code` | `String` | 股票代码 |
| `lxdt` | `int` | 连续跌停 |
| `fbcje` | `float` | 板上成交额（元），成交价格为该股票跌停价的所有成交额的总和 |
| `fdzj` | `float` | 封单资金（元） |
| `hsl` | `float` | 换手率（%） |
| `zhfb` | `String` | 最后封板时间，个股最后一次触及涨（跌）停的时间 |
| `ltsz` | `float` | 流通市值（元） |
| `name` | `String` | 股票名称 |
| `kbcs` | `int` | 开板次数，个股打开跌停板的次数 |
| `zxj` | `float` | 最新价（元） |
| `pe` | `float` | 动态市盈率（%） |
| `zsz` | `float` | 总市值（元） |
| `zdf` | `float` | 涨跌幅（%） |
| `update` | `String` | 更新时间 |

**返回示例**

```json
[
  {
    "tradeDate": "2026-03-23",
    "cje": 1003660000.0,
    "code": "000020",
    "lxdt": 1,
    "fbcje": 162989000.0,
    "fdzj": 18813900.0,
    "hsl": 25.7226,
    "zhfb": "14:45:03",
    "ltsz": 3804470000.0,
    "name": "深华发Ａ",
    "kbcs": 1,
    "zxj": 21.0,
    "pe": 209.705,
    "zsz": 5946390000.0,
    "zdf": -9.98714,
    "update": "2026-03-25 17:32:14"
  }
]
```

---

### 炸板：`/wolf/zb` {#wolfzb}

Python 方法：`BoardApi.getZhaBan`
接口 ID：`24`
权限标识：`1,2,3`

获取盘中炸板实时数据。
数据更新：实时数据交易时间段每1分钟更新，历史数据收盘后3:30更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `tradeDate` | `String` | 交易时间 |
| `cje` | `float` | 成交额（元） |
| `code` | `String` | 股票代码 |
| `scfb` | `String` | 首次封板时间，个股第一次触及涨（跌）停的时间 |
| `hsl` | `float` | 换手率（%） |
| `ltsz` | `float` | 流通市值（元） |
| `name` | `String` | 股票名称 |
| `zxj` | `float` | 最新价（元） |
| `zsz` | `float` | 总市值（元） |
| `zbcs` | `int` | 炸板次数，个股打开涨停板的次数 |
| `zdf` | `float` | 涨跌幅（%） |
| `zf` | `float` | 振幅（%） |
| `zs` | `float` | 涨速 |
| `ztp` | `float` | 涨停价 |
| `zttj` | `String` | 涨停统计，n/m代表m天中有n次涨停板 |
| `update` | `String` | 更新时间 |

**返回示例**

```json
[
  {
    "tradeDate": "2026-03-23",
    "cje": 1003660000.0,
    "code": "000020",
    "scfb": "09:25:00",
    "hsl": 25.7226,
    "ltsz": 3804470000.0,
    "name": "深华发Ａ",
    "zxj": 21.0,
    "zsz": 5946390000.0,
    "zbcs": 1,
    "zdf": -9.98714,
    "zf": 19.9743,
    "zs": 0.0,
    "ztp": 25.66,
    "zttj": "5/6",
    "update": "2026-03-25 17:32:18"
  }
]
```

---

### 强势股：`/wolf/qs` {#wolfqs}

Python 方法：`BoardApi.getQiangShiGu`
接口 ID：`25`
权限标识：`1,2,3`

获取盘中强势股票实时数据。
数据更新：实时数据交易时间段每1分钟更新，历史数据收盘后3:30更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `tradeDate` | `String` | 交易时间 |
| `cje` | `float` | 成交额（元） |
| `code` | `String` | 股票代码 |
| `rxly` | `int` | 入选理由，1：60日新高，2：近期多次涨停，3：60日新高且近期多次涨停 |
| `hsl` | `float` | 换手率（%） |
| `lb` | `float` | 量比 |
| `ltsz` | `float` | 流通市值（元） |
| `name` | `String` | 股票名称 |
| `sfxh` | `int` | 是否新高，0：否，1：新高 |
| `zxj` | `float` | 最新价 |
| `zsz` | `float` | 总市值（元） |
| `zdf` | `float` | 涨跌幅（%） |
| `zs` | `float` | 涨速 |
| `ztp` | `float` | 涨停价 |
| `zttj` | `String` | 涨停统计，n/m代表m天中有n次涨停板 |
| `update` | `String` | 更新时间 |

**返回示例**

```json
[
  {
    "tradeDate": "2026-03-23",
    "cje": 1003660000.0,
    "code": "000020",
    "rxly": 3,
    "hsl": 25.7226,
    "lb": 8.95834,
    "ltsz": 3804470000.0,
    "name": "深华发Ａ",
    "sfxh": 1,
    "zxj": 21.0,
    "zsz": 5946390000.0,
    "zdf": -9.98714,
    "zs": 0.0,
    "ztp": 25.66,
    "zttj": "5/6",
    "update": "2026-03-25 17:32:16"
  }
]
```

---

### 次新股：`/wolf/cx` {#wolfcx}

Python 方法：`BoardApi.getCiXinGu`
接口 ID：`26`
权限标识：`1,2,3`

获取次新股数据。
数据更新：实时数据交易时间段每1分钟更新，历史数据收盘后3:30更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `cje` | `float` | 成交额（元） |
| `code` | `String` | 股票代码 |
| `hsl` | `float` | 换手率（%） |
| `ssrq` | `String` | 上市日期 |
| `ltsz` | `float` | 流通市值（元） |
| `name` | `String` | 股票名称 |
| `sfxg` | `int` | 是否新高，0：否，1：新高 |
| `kbrq` | `String` | 开板日期 |
| `kbjr` | `int` | 开板几日 |
| `zxj` | `float` | 最新价 |
| `zsz` | `float` | 总市值（元） |
| `zdf` | `float` | 涨跌幅（%） |
| `ztp` | `float` | 涨停价 |
| `zttj` | `String` | 涨停统计，n/m代表m天中有n次涨停板 |
| `update` | `String` | 更新时间 |

**返回示例**

```json
[
  {
    "cje": 70527500.0,
    "code": "001220",
    "hsl": 7.52699,
    "ssrq": "2026-02-03",
    "ltsz": 942781000.0,
    "name": "世盟股份",
    "sfxg": 0,
    "kbrq": "2026-02-03",
    "kbjr": 43,
    "zxj": 41.7,
    "zsz": 3848490000.0,
    "zdf": 2.03083,
    "ztp": 1.0,
    "zttj": "0/0",
    "update": "2026-04-13 17:31:47"
  }
]
```

---

## 实时行情数据

### 实时行情：`/wolf/time` {#wolftime}

Python 方法：`BoardApi.getRealTimeQuote`
接口 ID：`31`
权限标识：`1,2,3`

获取沪深A股实时行情数据。提供涨速、涨跌幅、换手率、振幅、量比、内盘、外盘、ROE等行情指标数据，适用于投资研究、量化交易。包年版支持all参数获取盘中全市场实时数据。
数据更新：实时数据交易时间段每1分钟更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `symbol` | `String` | 是 | stock-沪深京A股，etf-ETF基金；股票类型 |
| `code` | `String` | 是 | 股票代码。code取值为all，则表示全推全市场数据；code取值为000001，则表示获取单个股票数据。 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `code` | `String` | 股票代码 |
| `name` | `String` | 股票名称 |
| `tradeDate` | `String` | 交易时间 |
| `zxj` | `float` | 最新价（元） |
| `open` | `float` | 开盘价（元） |
| `high` | `float` | 最高价（元） |
| `low` | `float` | 最低价（元） |
| `cjl` | `float` | 成交量（手） |
| `cje` | `float` | 成交额（元） |
| `zrspj` | `float` | 昨日收盘价（元） |
| `jj` | `float` | 均价（元） |
| `ztj` | `float` | 涨停价（元） |
| `dtj` | `float` | 跌停价（元） |
| `zdf` | `float` | 涨跌幅（%） |
| `zde` | `float` | 涨跌额（元） |
| `zf` | `float` | 振幅（%） |
| `hsl` | `float` | 换手率（%） |
| `lb` | `float` | 量比 |
| `zsz` | `float` | 总市值（元） |
| `ltsz` | `float` | 流通市值（元） |
| `sjl` | `float` | 市净率（%） |
| `roe` | `float` | ROE |
| `zgb` | `float` | 总股本（股） |
| `ltgb` | `float` | 流通股本（股） |
| `jtsyl` | `float` | 市盈率（静） |
| `dtsyl` | `float` | 市盈率（动） |
| `ttmsyl` | `float` | 市盈率（TTM） |
| `zdf05` | `float` | 5日涨跌幅（%） |
| `zdf10` | `float` | 10日涨幅（%） |
| `zdf20` | `float` | 20日涨幅（%） |
| `zdf60` | `float` | 60日涨幅（%） |

**返回示例**

```json
[
  {
    "code": "000001",
    "name": "平安银行",
    "tradeDate": "2026-04-13 15:09:37",
    "zxj": 11.07,
    "open": 11.05,
    "high": 11.09,
    "low": 11.03,
    "cjl": 406104.0,
    "cje": 449056800.0,
    "zrspj": 11.09,
    "jj": 11.06,
    "ztj": 12.2,
    "dtj": 9.98,
    "zdf": -0.18,
    "zde": -0.02,
    "zf": 0.54,
    "hsl": 0.21,
    "lb": 0.62,
    "zsz": 214823520000.0,
    "ltsz": 214820000000.0,
    "sjl": 0.48,
    "wb": 51.8,
    "wp": 168946.0,
    "np": 237158.0,
    "roe": 9.15,
    "zgb": 19405918000.0,
    "ltgb": 19405600000.0,
    "jtsyl": 5.04,
    "dtsyl": 5.04,
    "ttmsyl": 5.04,
    "zdf03": -1.34,
    "zdf05": -0.45,
    "zdf10": 0.45,
    "zdf20": 1.28,
    "zdf60": -3.82,
    "zdfyear": -2.98
  }
]
```

---

### 实时K线：`/wolf/time/kline` {#wolftimekline}

Python 方法：`MarketApi.getKLine`
接口 ID：`32`
权限标识：`1,2,3`

获取沪深A股和ETF实时K线数据。包年版支持all参数获取盘后全市场数据，仅限近一周内的日线数据。
数据更新：实时数据交易时间段秒级实时更新，历史数据收盘后3:30更新，all参数历史数据盘后6:00更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `symbol` | `String` | 是 | stock-沪深京A股，etf-ETF基金，bond-沪深可转债，index-指数；股票类型 |
| `code` | `String` | 是 | 股票代码。code取值为000001，则表示获取单个股票数据。包年版支持all参数获取盘后全市场数据，仅限近一周内的日线数据 |
| `period` | `String` | 是 | 1m-1分钟线，5m-5分钟线，15m-15分钟线，30m-30分钟线，1h-1小时线，1d-日线，1w-周线，1mon-月线，1y-年线；K线周期 |
| `cq` | `String` | 是 | 1-不复权，2-前复权，3-后复权；复权类型 |
| `startDate` | `String` | 是 | 开始日期 |
| `endDate` | `String` | 是 | 结束日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `t` | `String` | 交易时间 |
| `code` | `String` | 股票代码 |
| `o` | `float` | 开盘价（元） |
| `c` | `float` | 收盘价（元） |
| `h` | `float` | 最高价（元） |
| `l` | `float` | 最低价（元） |
| `v` | `float` | 成交量（手） |
| `a` | `float` | 成交额（元） |
| `pc` | `float` | 昨收价（元） |

**返回示例**

```json
[
  {
    "t": "2026-03-23 00:00:00",
    "code": "000001",
    "o": 10.68,
    "c": 10.45,
    "h": 10.68,
    "l": 10.43,
    "v": 1580088.0,
    "a": 1666328300.0,
    "pc": 10.77
  }
]
```

---

### 日线快照：`/wolf/time/day` {#wolftimeday}

Python 方法：`MarketApi.getDaySnapshot`
接口 ID：`33`
权限标识：`3`

获取沪深A股和ETF实时日线行情数据。包年版支持all参数获取盘中全市场实时数据。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `symbol` | `String` | 是 | stock-沪深京A股，etf-ETF基金，bond-沪深可转债，index-指数；股票类型 |
| `code` | `String` | 是 | 股票代码。code取值为all，则表示全推全市场数据；code取值为000001，则表示获取单个股票数据。 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `t` | `String` | 交易时间 |
| `code` | `String` | 股票代码 |
| `o` | `float` | 开盘价（元） |
| `c` | `float` | 收盘价（元） |
| `h` | `float` | 最高价（元） |
| `l` | `float` | 最低价（元） |
| `v` | `float` | 成交量（手） |
| `a` | `float` | 成交额（元） |
| `pc` | `float` | 昨收价（元） |

**返回示例**

```json
[
  {
    "t": "2026-04-13 15:00:00",
    "code": "000001",
    "o": 11.05,
    "c": 11.07,
    "h": 11.09,
    "l": 11.03,
    "v": 406104.0,
    "a": 449056800.0,
    "pc": 11.09
  }
]
```

---

### 买卖五档：`/wolf/time/five` {#wolftimefive}

Python 方法：`MarketApi.getFiveLevel`
接口 ID：`34`
权限标识：`3`

买卖五档实时数据。盘中数据毫秒级实时更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `symbol` | `String` | 是 | stock-沪深京A股，etf-ETF基金，bond-沪深可转债，index-指数；股票类型 |
| `code` | `String` | 是 | 股票代码。code取值为000001，则表示获取单个股票数据。 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `t` | `String` | 交易时间 |
| `code` | `String` | 股票代码 |
| `p` | `float` | 最新价（元） |
| `o` | `float` | 开盘价（元） |
| `h` | `float` | 最高价（元） |
| `l` | `float` | 最低价（元） |
| `pc` | `float` | 前收盘价（元） |
| `a` | `float` | 成交总额（元） |
| `v` | `float` | 成交总量（手） |
| `bp1` | `float` | 买一价（元） |
| `bp2` | `float` | 买二价（元） |
| `bp3` | `float` | 买三价（元） |
| `bp4` | `float` | 买四价（元） |
| `bp5` | `float` | 买五价（元） |
| `bv1` | `float` | 买一量（手） |
| `bv2` | `float` | 买二量（手） |
| `bv3` | `float` | 买三量（手） |
| `bv4` | `float` | 买四量（手） |
| `bv5` | `float` | 买五量（手） |
| `sp1` | `float` | 卖一价（元） |
| `sp2` | `float` | 卖二价（元） |
| `sp3` | `float` | 卖三价（元） |
| `sp4` | `float` | 卖四价（元） |
| `sp5` | `float` | 卖五价（元） |
| `sv1` | `float` | 卖一量（手） |
| `sv2` | `float` | 卖二量（手） |
| `sv3` | `float` | 卖三量（手） |
| `sv4` | `float` | 卖四量（手） |
| `sv5` | `float` | 卖五量（手） |

**返回示例**

```json
[
  {
    "t": "2026-04-13 15:00:00",
    "code": "000001",
    "p": 11.07,
    "o": 11.05,
    "h": 11.09,
    "l": 11.03,
    "pc": 11.09,
    "a": 449056800.0,
    "v": 406104.0,
    "bp1": 11.06,
    "bp2": 11.05,
    "bp3": 11.04,
    "bp4": 11.03,
    "bp5": 11.02,
    "bv1": 518.0,
    "bv2": 11463.0,
    "bv3": 11722.0,
    "bv4": 11557.0,
    "bv5": 9087.0,
    "sp1": 11.07,
    "sp2": 11.08,
    "sp3": 11.09,
    "sp4": 11.1,
    "sp5": 11.11,
    "sv1": 146.0,
    "sv2": 2840.0,
    "sv3": 3731.0,
    "sv4": 5127.0,
    "sv5": 2237.0
  }
]
```

---

### 竞价数据：`/wolf/time/bid` {#wolftimebid}

Python 方法：`MarketApi.getBidData`
接口 ID：`35`
权限标识：`3`

获取沪深A股实时竞价数据，竞价时间段：09:15-09:25，盘中数据毫秒级实时更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `code` | `String` | 是 | 股票代码。code取值为000001，则表示获取单个股票数据。 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `code` | `String` | 股票代码 |
| `t` | `String` | 交易时间 |
| `p` | `float` | 最新价（元） |
| `pc` | `float` | 昨日收盘价（元） |
| `zf` | `float` | 竞价涨幅（%） |
| `jv` | `long` | 竞价量（手） |
| `je` | `long` | 竞价金额（元） |
| `nv` | `long` | 未匹配量（手） |
| `ne` | `long` | 未匹配金额（元） |
| `bs` | `int` | 买卖点，-1未匹配量靠近卖一侧，1未匹配量靠近买一侧 |

**返回示例**

```json
[
  {
    "code": "000001",
    "t": "2026-04-13 09:25:00",
    "p": 11.05,
    "pc": 11.09,
    "zf": -0.36,
    "jv": 13041,
    "je": 14410300,
    "nv": 14327,
    "ne": 15831335,
    "bs": -1
  }
]
```

---

### 逐笔交易：`/wolf/deal` {#wolfdeal}

Python 方法：`MarketApi.getDealData`
接口 ID：`36`
权限标识：`3`

获取沪深A股逐笔交易数据，该接口为历史数据接口，盘后更新。
数据更新：历史数据盘后6:00更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `code` | `String` | 是 | 股票代码。code取值为000001，则表示获取单个股票数据。 |
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `t` | `String` | 交易时间 |
| `cjj` | `float` | 成交价（元） |
| `zd` | `float` | 涨跌额（元） |
| `cjl` | `long` | 成交量（手） |
| `cje` | `long` | 成交额（元） |
| `bs` | `int` | 买卖点，-1主动性卖，1主动性买 |

**返回示例**

```json
[
  {
    "t": "2026-04-10 09:15:00",
    "cjj": 11.09,
    "zd": -0.01,
    "cjl": 62,
    "cje": 68758,
    "bs": -1
  }
]
```

---

### 分价数据：`/wolf/price` {#wolfprice}

Python 方法：`MarketApi.getPriceData`
接口 ID：`37`
权限标识：`3`

获取沪深A股分价数据。
数据更新：历史数据盘后6:00更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `code` | `String` | 是 | 股票代码。code取值为000001，则表示获取单个股票数据。 |
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `code` | `String` | 股票代码 |
| `t` | `String` | 交易时间 |
| `p` | `float` | 最新价（元） |
| `pc` | `float` | 昨日收盘价（元） |
| `zf` | `float` | 竞价涨幅（%） |
| `jv` | `long` | 竞价量（手） |
| `je` | `long` | 竞价金额（元） |
| `nv` | `long` | 未匹配量（手） |
| `ne` | `long` | 未匹配金额（元） |
| `bs` | `int` | 买卖点，-1未匹配量靠近卖一侧，1未匹配量靠近买一侧 |

**返回示例**

```json
[
  {
    "cjj": 11.03,
    "cjl": 3962,
    "ratio": 0.98
  },
  {
    "cjj": 11.04,
    "cjl": 44360,
    "ratio": 10.92
  }
]
```

---

### 资金流向：`/wolf/money` {#wolfmoney}

Python 方法：`MarketApi.getMoneyFlow`
接口 ID：`38`
权限标识：`3`

获取沪深A股资金流向数据。资金流数据区分主买、主卖、特大单、大单、中单、小单等。
数据更新：历史数据盘后6:00更新。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `code` | `String` | 是 | 股票代码。code取值为000001，则表示获取单个股票数据。 |
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `c` | `String` | 股票代码 |
| `t` | `String` | k线日期 |
| `buynum` | `int` | 主买单总单数 |
| `sellnum` | `int` | 主卖单总单数 |
| `totalnum` | `int` | 成交笔数 |
| `buytddcje` | `float` | 主买特大单成交额（元） |
| `buyddcje` | `float` | 主买大单成交额（元） |
| `buyzdcje` | `float` | 主买中单成交额（元） |
| `buysdcje` | `float` | 主买小单成交额（元） |
| `selltddcje` | `float` | 主卖特大单成交额（元） |
| `sellddcje` | `float` | 主卖大单成交额（元） |
| `sellzdcje` | `float` | 主卖中单成交额（元） |
| `sellxdcje` | `float` | 主卖小单成交额（元） |
| `buytddcjl` | `int` | 主买特大单成交量（手） |
| `buyddcjl` | `int` | 主买大单成交量（手） |
| `buyzdcjl` | `int` | 主买中单成交量（手） |
| `buyxdcjl` | `int` | 主买小单成交量（手） |
| `selltddcjl` | `int` | 主卖特大单成交量（手） |
| `sellddcjl` | `int` | 主卖大单成交量（手） |
| `sellzdcjl` | `int` | 主卖中单成交量（手） |
| `sellxdcjl` | `int` | 主卖小单成交量（手） |

**返回示例**

```json
[
  {
    "c": "000001",
    "t": "2026-04-10 00:00:00",
    "buynum": 1783,
    "sellnum": 2368,
    "totalnum": 34943,
    "buytddcje": 70971360.0,
    "buyddcje": 92075880.0,
    "buyzdcje": 60690788.0,
    "buysdcje": 13619718.0,
    "selltddcje": 107035810.0,
    "sellddcje": 94592620.0,
    "sellzdcje": 73778180.0,
    "sellxdcje": 21324634.0,
    "buytddcjl": 63944,
    "buyddcjl": 82907,
    "buyzdcjl": 54646,
    "buyxdcjl": 12260,
    "selltddcjl": 96444,
    "sellddcjl": 85188,
    "sellzdcjl": 66448,
    "sellxdcjl": 19205
  }
]
```

---

### 复权变更数据：`/wolf/fq` {#wolffq}

Python 方法：`MarketApi.getAdjustment`
接口 ID：`39`
权限标识：`3`

股票除权除息历史数据，可以获取有复权变化的股票数据。支持查询最近一周内的数据，方便每日更新有复权变化的股票数据。

**请求参数**

| 参数 | 类型 | 必填 | 取值范围 / 说明 |
|---|---|---|---|
| `symbol` | `String` | 是 | stock-沪深京A股，etf-ETF基金；股票类型 |
| `tradeDate` | `String` | 是 | 交易日期 |
| `token` | `String` | 是 | 登录网站获取token |

**返回字段**

| 字段 | 类型 | 说明 |
|---|---|---|
| `code` | `String` | 股票代码 |
| `t` | `String` | 交易时间 |

---
