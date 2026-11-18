# 黑狼数据 Skill (FXYZ)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![API](https://img.shields.io/badge/API-17%20Endpoints-orange.svg)](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)

> Fxyz（黑狼数据）是中国股票市场实时数据 API 平台；Python SDK 的 PyPI 包名和导入名均为 `fxyz`。

**官方网站**: http://www.fxyz.site/
**PyPI安装**: `python -m pip install fxyz`
**API文档**: [references/apidoc.md](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)

---

## 📊 功能特点

- ✅股票与基金行情：沪深京 A 股、ETF、指数的实时行情和股票列表。
- ✅K 线与历史行情：支持1 分钟、 5 分钟、15 分钟、30 分钟、1 小时、日、周、月、年等周期及复权参数。
- ✅盘口与成交数据：买卖五档、集合竞价、逐笔成交、分价统计和日线快照。
- ✅市场监控数据：涨停、跌停、炸板、强势股和次新股数据。
- ✅资金流向：按大单级别查看资金流向数据。

### 核心优势

- ✅ **全面的数据覆盖** - 沪深京A股、ETF基金、主流指数
- ✅ **实时行情数据** - 30+行情指标，每分钟更新
- ✅ **特色监控数据** - 涨停板、跌停板、炸板、强势股实时追踪
- ✅ **多周期K线** - 9种时间周期（1分钟至年线），支持复权
- ✅ **深度盘口数据** - 买卖五档、竞价数据、逐笔交易
- ✅ **资金流向分析** - 特大单、大单、中单、小单分类统计
- ✅ **规范化日志** - 自动打印请求参数、返回记录数、示例数据

### 数据分类

| 分类 | 接口数量 | 主要功能 |
|------|---------|---------|
| **基础数据 API** | 3 | 股票列表、板块成分股、财务核心指标 |
| **涨停板数据 API** | 5 | 涨停、跌停、炸板、强势股、次新股 |
| **实时行情数据 API** | 9 | 实时行情、K线、盘口、成交、资金及复权变更 |

按数据需求查找接口、参数和返回字段，请查看 [API接口文档](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)。SDK 方法返回 JSON 解码后的 Python 对象。

---

## 🚀 快速开始

### 1. 环境要求

- Python 3.7+
- requests 库

### 2. 安装 Python SDK

```bash
python -m pip install fxyz
```

### 3. 获取Token

1. 访问黑狼数据官网：http://www.fxyz.site/
2. 注册账号并登录
3. 在个人中心获取API Token
4. Token激活参考：http://www.fxyz.site/#apply

### 4. 配置Token

将 Token 配置到 `fxyz/scripts/Config.py` 的 `Config.TOKEN` 中，并避免提交真实 Token：

```python
class Config:
    SERVER_URL = "http://api.fxyz.site"  # API服务地址
    TOKEN = "your_token_here"  # 替换为您的Token
```

### 5. 运行测试

```bash
python -m fxyz.scripts.StockApiClient
```

---

## 💡 使用示例

### 基础用法

#### 1. 获取股票列表

```python
from fxyz.scripts.api.BaseApi import BaseApi

# 获取所有A股列表
result = BaseApi.getStockList(flag=0, token="your_token")

# 获取创业板股票
result = BaseApi.getStockList(flag=5, token="your_token")

# 获取ETF基金
result = BaseApi.getStockList(flag=7, token="your_token")
```

#### 2. 获取实时行情

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取单个股票实时行情
result = BoardApi.getRealTimeQuote(
    symbol="stock",
    code="000001",
    token="your_token"
)

# 获取全市场实时行情（以接口权限为准）
result = BoardApi.getRealTimeQuote(
    symbol="stock",
    code="all",
    token="your_token"
)
```

#### 3. 获取K线数据

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取日K线（不复权）
result = MarketApi.getKLine(
    symbol="stock",
    code="000001",
    period="1d",
    cq="1",
    startDate="2026-04-01",
    endDate="2026-04-14",
    token="your_token"
)

# 获取周K线（前复权）
result = MarketApi.getKLine(
    symbol="stock",
    code="000001",
    period="1w",
    cq="2",
    startDate="2026-01-01",
    endDate="2026-04-14",
    token="your_token"
)
```

#### 4. 监控涨停板

```python
from fxyz.scripts.api.BoardApi import BoardApi

# 获取今日涨停板股票
result = BoardApi.getZhangTingBan(
    tradeDate="2026-04-14",
    token="your_token"
)
```

#### 5. 查看资金流向

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取主力资金流向
result = MarketApi.getMoneyFlow(
    code="000001",
    tradeDate="2026-04-14",
    token="your_token"
)
```

### 高级用法

#### 批量获取数据

```python
from fxyz.scripts.api.BoardApi import BoardApi
from fxyz.scripts.Config import Config

# 批量获取多只股票行情
stocks = ["000001", "600000", "000002"]
for code in stocks:
    result = BoardApi.getRealTimeQuote(
        symbol="stock",
        code=code,
        token=Config.TOKEN
    )
    # 处理数据...
```

#### 数据处理与分析

```python
from fxyz.scripts.api.MarketApi import MarketApi

# 获取K线数据并转换为DataFrame
result = MarketApi.getKLine(
    symbol="stock",
    code="000001",
    period="1d",
    cq="1",
    startDate="2026-04-01",
    endDate="2026-04-14",
    token="your_token"
)

# SDK方法已将JSON解析为Python列表或字典
data = result
print(f"获取到 {len(data)} 条K线数据")

# 计算涨跌幅
if len(data) >= 2:
    first_close = data[0]['c']
    last_close = data[-1]['c']
    change_pct = (last_close - first_close) / first_close * 100
    print(f"期间涨跌幅: {change_pct:.2f}%")
```

---

## 📚 API接口总览

### API 方法与数据需求映射

| 数据需求 | SDK 方法 | API 路径 |
|---|---|---|
| 股票、指数、ETF、可转债列表 | `BaseApi.getStockList` | `/wolf/list` |
| 行业、概念、特色板块成分股 | `BaseApi.getSector` | `/wolf/sector` |
| 财务核心指标 | `BaseApi.getFinanceMetric` | `/wolf/financemetric` |
| 实时行情、涨停、跌停、炸板、强势股、次新股 | `BoardApi` 方法 | `/wolf/time`、`/wolf/zt`、`/wolf/dt`、`/wolf/zb`、`/wolf/qs`、`/wolf/cx` |
| K线、日线快照、买卖五档、竞价 | `MarketApi` 方法 | `/wolf/time/kline`、`/wolf/time/day`、`/wolf/time/five`、`/wolf/time/bid` |
| 逐笔、分价、资金流向、复权变更 | `MarketApi` 方法 | `/wolf/deal`、`/wolf/price`、`/wolf/money`、`/wolf/fq` |

全部 17 个接口的请求参数、权限标识和返回字段见 [API 接口文档](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)。


---

## 🏗️ 项目结构

```
DemoFxyzythonSkill/
├── fxyz/
│   ├── references/              # 参考文档
│   │   └── apidoc.md           # API接口参数和返回字段
│   ├── scripts/                 # 源代码
│   │   ├── api/                # API模块
│   │   │   ├── BaseApi.py      # Basic Api实现
│   │   │   ├── BoardApi.py     # Board Api实现
│   │   │   └── MarketApi.py    # Market Api实现
│   │   ├── util/               # 工具类
│   │   │   ├── DataUtil.py     # HTTP请求工具
│   │   ├── Config.py           # 配置文件
│   │   └── StockApiClient.py   # 客户端示例（含测试）
│   └── SKILL.md                # Skill说明文档
├── README.md                    # 本文件
└── requirements.txt             # 依赖清单
```

---

## 📝 日志规范

所有API调用都会自动输出格式化日志：

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

**日志内容包括**:
- ✅ 请求参数详情
- ✅ 返回数据记录数
- ✅ 第一条数据示例（JSON格式）

---

## ⚠️ 注意事项

### 1. Token管理

- 🔐 **安全性**: 请勿将Token泄露或提交到公开代码仓库
- 🔄 **有效期**: Token长期有效，如遇问题请联系客服重置
- 🌐 **多环境**: 建议开发和生产环境使用不同Token

### 2. 请求限制

- ⏱️ **频率控制**: 避免短时间内大量请求
- 🔢 **并发限制**: 单IP并发请求数建议不超过2个

### 3. 数据时效性

| 数据类型 | 更新时机 | 说明 |
|---------|---------|------|
| 实时行情 | 交易时段每分钟 | 9:30-11:30, 13:00-15:00 |
| 涨跌停板 | 交易时段每分钟 | 收盘后15:30更新最终数据 |
| K线数据 | 实时/盘后 | 交易中实时更新，收盘后15:30更新 |
| 历史数据 | 盘后 | 收盘后18:00完成全部更新 |
| 资金流向 | 盘后 | 收盘后18:00更新 |

### 4. 最佳实践

1. **缓存策略**: 对不频繁变化的数据进行本地缓存
2. **错误处理**: 实现完善的异常处理机制
3. **重试机制**: 对于临时性失败，实现指数退避重试
4. **日志记录**: 记录API调用日志，便于问题排查
5. **数据验证**: 对返回数据进行有效性验证

---

## ❓ 常见问题

**Q: 如何获取Token？**  
A: 访问 http://www.fxyz.site/ 注册账号，登录后在个人中心获取。

**Q: 返回数据为空怎么办？**  
A: 检查以下几点：
1. Token是否正确且已激活
2. 交易日期是否为交易日
3. 股票代码是否存在
4. 是否具有相应权限等级

**Q: 全市场数据为什么无法获取？**  
A: `code=all`仅适用于接口文档明确支持该参数的接口；其中实时行情、K线和日线快照的全市场查询有包年版说明。请查看对应接口的参数描述和账号权限。

**Q: 数据更新延迟怎么办？**  
A: 实时数据在交易时段每分钟更新，如遇延迟请稍后重试。历史数据在收盘后统一更新。

**Q: 如何判断API调用是否成功？**  
A: 查看日志输出中的"API调用成功"提示，以及返回数据的记录数。

---

## 📖 相关文档

- 📘 [API接口文档](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md) - 完整的接口说明
- 📗 [Skill说明](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/SKILL.md) - Skill使用指南
- 📙 [代码示例](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/scripts/StockApiClient.py) - 完整测试代码

---

## 🤝 技术支持

- **官方网站**: http://www.fxyz.site/
- **API文档**: [references/apidoc.md](https://github.com/fxyzsite/FxyzSkill/blob/main/fxyz/references/apidoc.md)
- **Token申请**: http://www.fxyz.site/#apply
- **问题反馈**: 请通过官网联系客服

---

## 📄 许可证

本项目仅供学习和研究使用，请勿用于商业用途。使用时请遵守黑狼数据的使用条款。

**版权所有**: © 2026 黑狼数据

