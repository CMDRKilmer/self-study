import re

class AddressExtractor:
    def __init__(self):
        # 地址相关的关键词
        self.keywords = ['路', '街', '巷', '号', '栋', '楼', '层', '室', '村', '组', '社区', '小区', '园', '广场', '大厦', '省', '市', '县', '区']
        # 地址前缀模式
        self.prefix_pattern = re.compile(r'(地址[:：]\s*)')
    
    def extract(self, text):
        # 先尝试提取"地址:"后面的内容
        address_prefix_pattern = re.compile(r'地址[:：]\s*([^开户银行]+?)(开户银行|$)')
        match = address_prefix_pattern.search(text)
        if match:
            return match.group(1).strip()
        
        # 如果没有"地址:"前缀，尝试从文本中提取包含地址关键词的内容
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检查是否包含地址关键词
            if any(keyword in line for keyword in self.keywords):
                # 去除可能的前缀
                line = self._clean_address(line)
                return line
        
        return "未识别到购买方地址"
    
    def _clean_address(self, address):
        # 去除可能的前缀，如"名称:"、"纳税人识别号:"等
        prefixes = ['名称[:：]', '纳税人识别号[:：]', '统一社会信用代码[:：]', '开户行[:：]', '银行账号[:：]']
        for prefix in prefixes:
            pattern = re.compile(rf'^{prefix}\s*')
            address = pattern.sub('', address)
        
        return address  