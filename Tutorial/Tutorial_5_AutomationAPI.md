# Tutorial 5: 自動化與 API (Automation & API)

當工作流變得複雜，或需要頻繁修改參數時，使用 Python API 直接驅動 ComfyUI 會比手動點擊網頁介面更有效率。

## 1. 為什麼使用 API？
* **避免誤觸**：防止瀏覽器遺失節點或設定錯誤。
* **精準修改**：可以直接透過程式碼修改 `frame_load_cap` 或影片路徑。
* **批次處理**：可以自動排隊處理多段影片。

## 2. API 驅動流程
我們撰寫了 `send_api_lcm.py`，其邏輯為：
1. 讀取 `workflows/ghibli_v2v.json`。
2. 將 UI 格式轉換為 API 格式。
3. 動態注入 LCM LoRA 與 Advanced ControlNet 參數。
4. 使用 `urllib` 將 JSON 發送至 `http://127.0.0.1:8000/prompt`。

## 3. 工作階段自動化 (Bash Scripts)
為了管理開發紀錄，我們建立了：
* `startup.sh`: 自動 `git pull` 並顯示開發日誌。
* `ending.sh`: 自動將日誌更新並 `git push` 到 GitHub。

## 💡 經驗總結
將工作流「代碼化」是專業開發的必經之路。這不僅能留下精確的紀錄，也能讓你的工作成果更容易分享與復現。
