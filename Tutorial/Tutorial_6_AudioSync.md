# Tutorial 6: 音訊同步 (Audio Synchronization)

預設的影像處理流程通常只專注於畫面。本章節介紹如何將原始影片的音軌合併回 AI 生成後的影片中。

## 1. 音訊來源
在 ComfyUI 中，`VHS_LoadVideo` 節點除了輸出影像外，也會輸出一個 `AUDIO` 類型。

## 2. 節點連接
我們需要將音訊直接串接到最終的輸出節點：
* **來源節點**：`VHS_LoadVideo` (Node 1) 的 **AUDIO** 輸出。
* **目標節點**：`VHS_VideoCombine` (Node 12) 的 **audio** 輸入。

## 3. API 腳本修正
在 Python API 腳本中，這對應到對 `prompt` 字典的修改：
```python
# 將 Node 1 的第 3 個輸出 (index 2) 連接到 Node 12 的 audio 輸入
prompt["12"]["inputs"]["audio"] = ["1", 2]
```

## 💡 經驗總結
* **同步性**：如果我們大幅改變了影像的 FPS 或播放速度，音訊可能會發生不同步的現象。
* **格式建議**：`VHS_VideoCombine` 支援將影像與音訊重新封裝為 MP4 或 MKV 格式。
