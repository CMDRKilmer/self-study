import re
from unit_name import UnitNameExtractor
from credit_code import CreditCodeExtractor
from address import AddressExtractor
from bank import BankExtractor
from account import AccountExtractor
from text_preprocessor import TextPreprocessor
import tkinter as tk
from tkinter import scrolledtext

def recognize_info():
    # 获取输入文本框中的文本
    text = input_text.get("1.0", tk.END).strip()
    
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
    
    # 生成输出结果
    result = f"识别结果：\n单位名称：{unit_name}\n统一社会信用代码/纳税人识别号：{credit_code}\n购买方地址：{address}\n购方开户银行：{bank}\n银行账号：{account}"
    
    # 在输出文本框中显示结果
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# 创建主窗口
root = tk.Tk()
root.title("开票信息提取")

# 创建输入文本框
input_label = tk.Label(root, text="请输入需要识别的文本：")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, width=80, height=10)
input_text.pack()

# 创建识别按钮
recognize_button = tk.Button(root, text="识别", command=recognize_info)
recognize_button.pack()

# 创建输出文本框
output_label = tk.Label(root, text="识别结果：")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, width=80, height=10)
output_text.pack()

# 运行主循环
root.mainloop()