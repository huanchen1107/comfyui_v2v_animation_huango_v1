# Tutorial 2: 突破長度限制 (Breaking the Frame Limit)

預設的 AnimateDiff 模型通常有 32 幀的上限。本章節介紹如何使用「滑動視窗」技術處理長影片。

## 1. 錯誤現象
如果你嘗試載入超過 32 幀的影片，ComfyUI 會報錯：
`ValueError: Without a context window, AnimateDiff model has upper limit of 32 frames.`

## 2. 解決方案：AnimateDiff Gen1
我們需要將舊版的 Loader 替換為支援 Context 的新版節點：

* **核心節點 1**：`ADE_AnimateDiffLoaderGen1` (AnimateDiff 加載器 Gen1)
* **核心節點 2**：`ADE_StandardUniformContextOptions` (標準統一上下文選項)

## 3. 設定滑動視窗 (Sliding Window)
在 `StandardUniformContextOptions` 中設定：
* **context_length**: 16 (每次運算的視窗長度)
* **context_overlap**: 4 (視窗重疊幀數，確保銜接自然)
* **fuse_method**: `pyramid` (金字塔融合，效果最穩定)

## 💡 經驗總結
透過將 `context_options` 連接到 `AnimateDiffLoaderGen1`，AI 會像掃描一樣，一次處理一小段並銜接下一段，從而實現無限長度的影片生成。
