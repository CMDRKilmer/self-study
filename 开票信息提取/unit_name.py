import re

class UnitNameExtractor:
    def __init__(self):
        # 常见单位名称后缀
        self.suffix_pattern = re.compile(
            r'(有限公司|有限责任公司|股份有限公司|集团有限公司|合伙企业|个人独资企业|合作社|研究院|研究所|中心|厂|店|部|学校|医院|协会|学会|基金会|委员会|局|厅|处|所|馆|站|社|行|园|公司|集团|商场|超市|酒店|饭店|影院|剧院|出版社|银行|保险|学院|大学|中学|小学|幼儿园|党校|技校)'
        )
        # 排除一些常见的非单位名称词汇
        self.exclude_pattern = re.compile(r'(^[省市县乡村]|^[0-9一二三四五六七八九十]+$)')
    
    def extract(self, text):
        # 先尝试提取"名称:"后面的内容
        name_prefix_pattern = re.compile(r'名称[:：]\s*([^，。,.;;]+?)[，。,.;;]')
        match = name_prefix_pattern.search(text)
        if match:
            potential_name = match.group(1)
            if self.suffix_pattern.search(potential_name):
                return potential_name
        
        # 再尝试从行中识别
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检查是否包含单位名称后缀
            if self.suffix_pattern.search(line):
                # 排除一些明显不是单位名称的情况
                if not self.exclude_pattern.search(line):
                    return line
        
        return "未识别到单位名称"  