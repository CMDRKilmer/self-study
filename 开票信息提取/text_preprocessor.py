class TextPreprocessor:
    def __init__(self):
        # 定义常见的干扰字符和替换规则
        self.replacements = {
            '，': ',',
            '。': '.',
            '：': ':',
            '；': ';',
            '（': '(',
            '）': ')',
            ' ': '',  # 去除空格
            '\t': '',  # 去除制表符
        }
    
    def process(self, text):
        # 替换特殊字符
        for old, new in self.replacements.items():
            text = text.replace(old, new)
        
        # 统一大小写
        text = text.upper()
        
        # 可以添加更多预处理步骤，如去除HTML标签、规范化数字等
        
        return text  