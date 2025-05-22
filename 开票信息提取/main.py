import re
from unit_name import UnitNameExtractor
from credit_code import CreditCodeExtractor
from address import AddressExtractor
from bank import BankExtractor
from account import AccountExtractor
from text_preprocessor import TextPreprocessor

def main():
    # 模拟从文本框获取的文本
    text = input("请输入需要识别的文本：")
    
    # 文本预处理
    preprocessor = TextPreprocessor()
    processed_text = preprocessor.process(text)
    
    # 单位名称识别
    unit_name_extractor = UnitNameExtractor()
    unit_name = unit_name_extractor.extract(processed_text)
    
    # 信用代码/纳税人识别号识别
    credit_code_extractor = CreditCodeExtractor()
    credit_code = credit_code_extractor.extract(processed_text)
    
    # 地址识别
    address_extractor = AddressExtractor()
    address = address_extractor.extract(processed_text)
    
    # 开户银行识别
    bank_extractor = BankExtractor()
    bank = bank_extractor.extract(processed_text)
    
    # 银行账号识别
    account_extractor = AccountExtractor()
    account = account_extractor.extract(processed_text)
    
    # 输出结果
    print("\n识别结果：")
    print(f"单位名称：{unit_name}")
    print(f"统一社会信用代码/纳税人识别号：{credit_code}")
    print(f"购买方地址：{address}")
    print(f"购方开户银行：{bank}")
    print(f"银行账号：{account}")

if __name__ == "__main__":
    main()  