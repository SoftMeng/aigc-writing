# AI 辅助小说写作

AIGC 辅助中国文学小说创作工具集，用于小说续写、章节创作和剧情管理。

## 项目结构

```
根目录/
├── .claude/skills/              # 共享写作技能
│   ├── writing-chinese-literary/  # 小说写作核心技能
│   └── comfyui-image-generation/   # AI 插画生成技能
├── 小说A/                     # 示例小说项目
│   ├── 正文/                       # 已完成的章节文件
│   ├── 原子库/                     # 人物、地点、设定等资料库
│   ├── 插图/                       # AI 生成的插画
│   ├── 章节简要梗概/               # 章节梗概
│   ├── 章节修改备注.md             # 修改记录
│   └── 故事介绍.md                 # 故事背景介绍
└── CLAUDE.md                      # Claude Code 项目指南
```

## 快速开始

1. 创建新的小说项目目录
2. 使用 `writing-chinese-literary` 技能进行章节创作
3. 使用 `comfyui-image-generation` 技能生成插画

## 技能命令

- `/writing-chinese-literary` - 拆解小说写作任务，生成结构化章节
- `/comfyui-image-generation` - 生成 AI 插画并保存到 Images/ 目录

更多详情请参考 [CLAUDE.md](./CLAUDE.md)