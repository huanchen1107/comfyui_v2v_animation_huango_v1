#!/bin/bash
echo "🚀 正在從 GitHub 拉取最新進度 (git pull)..."
git pull origin main

echo ""
echo "================================================="
echo "📖 最新開發日誌內容："
echo "================================================="
# 自動找出以 "開發日誌" 結尾且最新的 md 檔案並顯示內容
LATEST_LOG=$(ls -t *開發日誌*.md 2>/dev/null | head -n 1)

if [ -n "$LATEST_LOG" ]; then
    cat "$LATEST_LOG"
else
    echo "⚠️ 找不到開發日誌檔案！"
fi
echo "================================================="
echo ""
echo "🤖 嗨，AI 助手！請閱讀上方的開發日誌，並總結目前的進度，然後告訴我接下來可以開始哪些任務 (Tasks to start)。"
