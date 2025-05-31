# 豆瓣图书信息爬虫与自动化测试

## 项目简介
本项目是一个基于 Python 的爬虫工具，用于抓取豆瓣图书的公开信息（如书名、作者、评分），并通过自动化测试验证功能正确性。项目使用 `requests` 和 `BeautifulSoup` 实现数据抓取，设计了功能、边界和异常测试用例，并用 `pytest` 编写自动化测试脚本。项目展示了爬虫开发、测试用例设计和自动化测试能力，适合软件测试相关岗位。

## 技术栈
- **语言**：Python 3.8+
- **库**：requests, BeautifulSoup4, pytest
- **功能**：
  - 爬取豆瓣图书信息（如书名、作者、评分）
  - 设计并执行测试用例
  - 自动化测试脚本验证爬虫功能
  - 数据保存至 CSV 文件（可选）

## 安装步骤
1. **确保 Python 环境**：
   - 安装 Python 3.8 或以上版本，验证：`python --version` 或 `python3 --version`。
2. **克隆仓库**：
   ```bash
   git clone https://github.com/Donesumth/Software-testing.git
   cd Software-testing
