# Tutorial 3: 進階 ControlNet 應用 (Advanced ControlNet)

當我們開啟了「滑動視窗」處理長影片後，ComfyUI 內建的 ControlNet 節點會因為無法同步時序而崩潰。本章節介紹如何修正此問題。

## 1. 錯誤現象
開啟 Context Window 後，運算可能會在 KSampler 階段報錯：
`Control type ControlNet may not support required features for sliding context window`

## 2. 安裝 Advanced ControlNet
我們必須安裝專為長影片設計的擴充插件：
```bash
cd custom_nodes
git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git
```
安裝後必須重啟 ComfyUI 伺服器。

## 3. 替換節點
在工作流中，將原本的 `ControlNetApplyAdvanced` 替換為：
* **節點名稱**：`Apply Advanced ControlNet (Advanced)` (內碼為 `ACN_AdvancedControlNetApply_v2`)

## 💡 經驗總結
Advanced ControlNet 能夠理解 AnimateDiff 的視窗切換邏輯，確保在處理第 100 幀時，ControlNet 的引導依然能與之對齊。
