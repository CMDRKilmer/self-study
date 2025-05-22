import re

class BankExtractor:
    def __init__(self):
        # 常见银行名称列表
        self.bank_names = [
            '中国工商银行', '中国农业银行', '中国银行', '中国建设银行', '交通银行',
            '中国邮政储蓄银行', '招商银行', '浦发银行', '中信银行', '中国民生银行',
            '中国光大银行', '华夏银行', '广发银行', '兴业银行', '平安银行',
            '恒丰银行', '浙商银行', '渤海银行', '北京银行', '上海银行', '江苏银行',
            '南京银行', '宁波银行', '杭州银行', '广州银行', '深圳发展银行', '徽商银行',
            '齐鲁银行', '长沙银行', '重庆银行', '成都银行', '哈尔滨银行', '盛京银行',
            '天津银行', '河北银行', '晋商银行', '包商银行', '内蒙古银行', '大连银行',
            '锦州银行', '吉林银行', '龙江银行', '苏州银行', '温州银行', '嘉兴银行',
            '湖州银行', '绍兴银行', '金华银行', '台州银行', '浙江泰隆商业银行',
            '浙江民泰商业银行', '浙江稠州商业银行', '福建海峡银行', '泉州银行', '江西银行',
            '齐鲁银行', '烟台银行', '潍坊银行', '济宁银行', '青岛银行', '郑州银行',
            '汉口银行', '湖北银行', '武汉农村商业银行', '长沙银行', '东莞银行',
            '广东南粤银行', '珠海华润银行', '广西北部湾银行', '桂林银行', '海南银行',
            '重庆农村商业银行', '成都银行', '贵阳银行', '富滇银行', '曲靖市商业银行',
            '西藏银行', '西安银行', '长安银行', '兰州银行', '青海银行', '宁夏银行',
            '新疆银行', '乌鲁木齐商业银行', '国家开发银行', '中国进出口银行',
            '中国农业发展银行', '中国人民银行'
        ]
        # 生成银行名称的正则表达式模式
        self.bank_pattern = re.compile(
            r'(' + '|'.join(re.escape(bank) for bank in self.bank_names) + r')'
        )
        # 银行前缀模式
        self.prefix_pattern = re.compile(r'(开户银行[:：]\s*)')
    
    def extract(self, text):
        # 先尝试提取"开户银行:"后面的内容
        match = self.prefix_pattern.search(text)
        if match:
            bank_start = match.end()
            bank_text = text[bank_start:]
            # 查找完整银行名称
            full_bank_match = self.bank_pattern.search(bank_text)
            if full_bank_match:
                return full_bank_match.group(0)
            # 如果没找到完整名称，提取到第一个句号或换行
            end_pos = min(
                (bank_text.find(c) for c in '。,.\n' if bank_text.find(c) != -1),
                default=len(bank_text)
            )
            candidate = bank_text[:end_pos].strip()
            if '银行' in candidate:
                return candidate
        
        # 如果没有前缀，尝试从文本中提取
        match = self.bank_pattern.search(text)
        if match:
            return match.group(0)
        
        # 最后尝试从包含"银行"的行中提取
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if '银行' in line:
                return line
        
        return "未识别到购方开户银行"  