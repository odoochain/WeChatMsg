#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time        : 2025/3/11 20:46 
@Author      : SiYuan 
@Email       : 863909694@qq.com 
@File        : wxManager-2-contact.py 
@Description : 
"""

import os
import sys
import time
# 添加父目录到Python路径
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wxManager import DatabaseConnection

# 输出文件路径
output_file = './output/contacts_output.txt'

db_dir = './output/silenwoods/Msg'  # 第一步解析后的数据库路径，例如：./wxid_xxxx/db_storage
db_version = 3  # 数据库版本，4 or 3

conn = DatabaseConnection(db_dir, db_version)  # 创建数据库连接
database = conn.get_interface()  # 获取数据库接口

st = time.time()
cnt = 0

# 打开文件准备写入
with open(output_file, 'w', encoding='utf-8') as f:
    contacts = database.get_contacts()
    for contact in contacts:
        f.write('*' * 80 + '\n')
        f.write(f"{contact}\n")
        contact.small_head_img_blog = database.get_avatar_buffer(contact.wxid)
        cnt += 1
        if contact.is_chatroom:
            f.write('-' * 60 + '\n')
            chatroom_members = database.get_chatroom_members(contact.wxid)
            f.write(f"{contact.wxid} 群成员个数： {len(chatroom_members)}\n")
            for wxid, chatroom_member in chatroom_members.items():
                chatroom_member.small_head_img_blog = database.get_avatar_buffer(wxid)
                f.write(f"{chatroom_member}\n")
                cnt += 1

    f.write('=' * 80 + '\n')
et = time.time()

# 写入统计信息
with open(output_file, 'a', encoding='utf-8') as f:
    f.write(f'联系人个数：{cnt} 耗时：{et - st:.2f}s\n')

# 打印完成信息
print(f"结果已保存至 {os.path.abspath(output_file)}")
