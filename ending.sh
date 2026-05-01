#!/bin/bash
echo "🛑 準備結束目前的工作階段..."
echo ""
echo "🤖 嗨，AI 助手！請確認你已經將本次對話中「所有有意義的除錯、優化與結論」寫入開發日誌中。"
echo "（如果還沒寫，請立刻更新檔案再繼續）"
echo ""

# 讓終端機稍微暫停，確保 AI/User 確認
read -p "請確認開發日誌已更新？ (按 Enter 繼續推送至 GitHub)"

echo "📦 正在將所有檔案推送到 GitHub..."
git add .
git commit -m "Auto-commit: 結束工作階段並更新開發日誌 $(date +%Y-%m-%d)"
git push origin main
echo "✅ 推送完成！"
