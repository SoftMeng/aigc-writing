# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

这是一个**中国文学小说/长篇文学作品 AI 辅助写作项目**，用于进行小说续写、章节创作和剧情管理。每个小说目录是独立的项目单元，根目录包含共享的写作技能和资源。

## Repository Structure

```
根目录/
├── .claude/
│   └── skills/                      # 共享写作技能
│       ├── writing-chinese-literary/  # 小说写作核心技能
│       └── comfyui-image-generation/   # AI 插画生成技能
├── 小说项目A/                       # 独立小说项目（可以有多个）
│   ├── 正文/                         # 已完成的章节文件
│   ├── 原子库/                       # 人物、地点、设定等资料库
│   ├── 插图/                         # AI 生成的插画（可选）
│   ├── 章节简要梗概/                 # 章节梗概（可选，各项目自定义命名）
│   ├── 故事介绍.md                   # 故事背景介绍
│   └── CLAUDE.md                     # 项目级指南（可选）
├── 小说项目B/
├── 插画提示词生成流程.md             # 插画提示词设计指南
└── CLAUDE.md                         # 本文件
```