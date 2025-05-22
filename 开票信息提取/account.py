import re

class AccountExtractor:
    def __init__(self):
        # 更灵活的银行账号模式，12-30位数字，可能包含空格或短横线分隔
        self.account_pattern = re.compile(
            r'(?<!\d)(?:\d[ -]?){12,30}\d(?!\d)'
        )
        # 银行账号前缀模式
        self.prefix_pattern = re.compile(r'(银行账号[:：]\s*)')
    
    def extract(self, text):
        # 先尝试提取"银行账号:"后面的数字
        match = self.prefix_pattern.search(text)
        if match:
            account_start = match.end()
            account_text = text[account_start:account_start + 40]  # 假设账号不会超过40个字符
            # 从account_text中提取连续的数字
            digits = re.findall(r'\d+', account_text)
            if digits:
                return ''.join(digits)
        
        # 如果没有前缀，尝试直接从文本中提取
        match = self.account_pattern.search(text)
        if match:
            # 去除空格和短横线
            return match.group(0).replace(' ', '').replace('-', '')
        
        return "未识别到银行账号"  