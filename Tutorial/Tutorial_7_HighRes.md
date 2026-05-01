# Tutorial 7: 高解析度處理與優化 (High-Resolution Processing)

基礎的 512px 解析度雖然運算快，但在大螢幕上細節不足。本章節介紹如何安全地提升解析度，同時避免系統崩潰。

## 1. 調整基礎解析度
雖然 Stable Diffusion 1.5 的基礎是 512px，但在 36GB 以上記憶體的 Mac 上，可以嘗試提升到 **768px** 或 **896px**。

## 2. 局部測試策略
高解析度運算非常耗時且容易報錯。建議先從長影片中裁切出最精彩的 10 秒進行測試：
```bash
# 裁切出最後 10 秒並同時縮放至 896px
ffmpeg -i input_20s.mp4 -ss 00:00:10 -t 00:00:10 -vf "scale=896:-2" test_10s_896p.mp4
```

## 3. API 腳本設定
在 `send_api_lcm.py` 中，確保 `custom_width` 與素材一致：
```python
prompt["1"]["inputs"]["video"] = "youtube_10s_896p.mp4"
prompt["1"]["inputs"]["custom_width"] = 896
```

## 💡 經驗總結
* **畫質提升**：896p 的總像素量是 512p 的 3 倍，細節會豐富非常多。
* **風險控管**：高解析度下 AnimateDiff 的 VRAM 消耗會激增，務必開啟 LCM 加速來減少運算步數，以維持系統穩定性。
