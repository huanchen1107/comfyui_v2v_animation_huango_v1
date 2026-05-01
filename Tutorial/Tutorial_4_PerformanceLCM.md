# Tutorial 4: 運算飆速優化 (Performance Optimization)

處理長影片最痛苦的是等待。本章節介紹如何透過 LCM 技術將 60 分鐘的運算縮短至 10 分鐘。

## 1. 核心原理：LCM (Latent Consistency Model)
一般生成的 KSampler 需要 20-30 步才能畫出清晰影像。使用 LCM 補丁後，AI 只需要 **4-6 步** 就能達成相同效果。

## 2. 準備步驟
下載 LCM LoRA 權重：
```bash
curl -L "https://huggingface.co/latent-consistency/lcm-lora-sdv1-5/resolve/main/pytorch_lora_weights.safetensors" -o models/loras/lcm-lora-sdv1-5.safetensors
```

## 3. 設定 KSampler
* **Steps**: 6 (關鍵：從 20 降到 6)
* **CFG**: 1.5 (LCM 專用的低數值)
* **Sampler**: `lcm`
* **Scheduler**: `sgm_uniform` 或 `normal`

## 💡 經驗總結
LCM 搭配降低影片 FPS (如 8 FPS)，可以達成「指數級」的提速。這對於在個人電腦（如 Mac）上處理長達 2 分鐘的影片至關重要。
