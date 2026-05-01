# Tutorial 1: 影片前處理 (Video Preprocessing)

在進行 AI 影片轉換之前，正確的素材處理是成功的關鍵。本章節介紹如何準備適合 AnimateDiff 運算的素材。

## 1. 取得原始影片
我們使用 `yt-dlp` 從 YouTube 取得最高品質的原始素材。
```bash
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" "https://www.youtube.com/watch?v=zcH52Z0IxXM" -o youtube_video.mp4
```

## 2. 裁切與縮放 (Trimming & Scaling)
為了確保運算穩定性，建議先從短片段（例如 20 秒）開始測試，並將寬度設定為 512 像素（SD1.5 模型的標準解析度）。
```bash
ffmpeg -i youtube_video.mp4 -ss 00:00:00 -t 00:00:20 -vf "scale=512:-2" youtube_20s_raw.mp4
```

## 3. 調整幀率 (FPS Conversion)
AnimateDiff 運算量極大。雖然原始影片可能是 24 或 30 FPS，但轉換為 **8 FPS** 或 **12 FPS** 可以在不損失太多流暢度的情況下，減少 50% 以上的運算時間。
```bash
# 轉換為 8 FPS
ffmpeg -i youtube_20s_raw.mp4 -filter:v fps=fps=8 youtube_20s.mp4
```

## 💡 經驗總結
* **解析度**：維持在 512x512 或比例接近的大小。
* **長度**：測試階段建議不超過 20 秒。
* **FPS**：8 FPS 對於宮崎駿風格的「手繪感」非常契合。
