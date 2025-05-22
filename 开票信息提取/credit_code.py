import re

class CreditCodeExtractor:
    def __init__(self):
        # 统一社会信用代码模式 (18位，数字或字母)
        self.credit_code_pattern = re.compile(
            r'(?<!\d)[0-9A-HJ-NPQRTUWXY]{2}\d{6}[0-9A-HJ-NPQRTUWXY]{10}(?!\d)'
        )
        # 纳税人识别号模式 (15-20位，数字或字母)
        self.tax_id_pattern = re.compile(
            r'(?<!\d)[0-9A-Z]{15,20}(?!\d)'
        )
        # 前缀模式
        self.prefix_pattern = re.compile(r'(统一社会信用代码[:：]\s*|纳税人识别号[:：]\s*)')
    
    def extract(self, text):
        # 先尝试提取前缀后面的代码
        match = self.prefix_pattern.search(text)
        if match:
            code_start = match.end()
            code_text = text[code_start:code_start + 30]  # 假设代码不会超过30个字符
            # 尝试匹配信用代码
            credit_match = self.credit_code_pattern.search(code_text)
            if credit_match:
                return credit_match.group(0)
            # 尝试匹配纳税人识别号
            tax_match = self.tax_id_pattern.search(code_text)
            if tax_match:
                return tax_match.group(0)
        
        # 如果没有前缀，尝试直接从文本中提取
        credit_match = self.credit_code_pattern.search(text)
        if credit_match:
            return credit_match.group(0)
        
        tax_match = self.tax_id_pattern.search(text)
        if tax_match:
            return tax_match.group(0)
        
        return "未识别到统一社会信用代码/纳税人识别号"  