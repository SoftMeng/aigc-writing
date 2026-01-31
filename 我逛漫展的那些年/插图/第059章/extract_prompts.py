#!/usr/bin/env python3
"""
从提示词文件提取内容并生成图片
"""

import os
import re
from pathlib import Path

# 定义提示词文件路径
PROMPTS_DIR = Path("/Users/xiangyuanmeng/Documents/TowerProject2/aigc-writing/我逛漫展的那些年/插图/第059章")

# 定义8个角色的提示词文件
PROMPT_FILES = {
    "雷电芽衣": "雷电芽衣_战斗提示词.md",
    "布洛妮娅": "布洛妮娅_战斗提示词.md",
    "陈": "陈_战斗提示词.md",
    "星熊": "星熊_战斗提示词.md",
    "神里绫华": "神里绫华_战斗提示词.md",
    "胡桃": "胡桃_战斗提示词.md",
    "Scathach": "Scathach_战斗提示词.md",
    "宫本武藏": "宫本武藏_战斗提示词.md",
}

def extract_prompt(file_path):
    """从markdown文件中提取提示词"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 移除markdown标题和分隔符
    lines = content.split("\n")

    # 找到第一个分隔符 --- 的位置
    separator_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            separator_idx = i
            break

    if separator_idx:
        # 取分隔符之后的内容（提示词部分）
        prompt_lines = lines[separator_idx + 1:]
    else:
        prompt_lines = lines

    # 合并成一行，并清理多余空白
    prompt = " ".join([line.strip() for line in prompt_lines if line.strip()])

    # 清理markdown格式
    prompt = re.sub(r'\*\*(.*?)\*\*', r'\1', prompt)  # 移除粗体
    prompt = re.sub(r'\*(.*?)\*', r'\1', prompt)  # 移除斜体
    prompt = re.sub(r'`(.*?)`', r'\1', prompt)  # 移除代码格式
    prompt = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', prompt)  # 移除链接

    return prompt

def main():
    """主函数：提取所有提示词并打印"""
    prompts = {}

    for role_name, file_name in PROMPT_FILES.items():
        file_path = PROMPTS_DIR / file_name
        if file_path.exists():
            prompt = extract_prompt(file_path)
            prompts[role_name] = prompt
            print(f"\n{'='*80}")
            print(f"角色: {role_name}")
            print(f"文件: {file_name}")
            print(f"提示词长度: {len(prompt)} 字符")
            print(f"提示词预览: {prompt[:200]}...")
            print(f"{'='*80}\n")

    # 保存提示词到JSON文件
    json_path = PROMPTS_DIR / "prompts.json"
    import json
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"\n提示词已保存到: {json_path}")

    return prompts

if __name__ == "__main__":
    main()
