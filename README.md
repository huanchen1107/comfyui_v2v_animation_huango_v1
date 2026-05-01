# ComfyUI Video-to-Video Animation (Ghibli Style)

This repository contains the complete workflow and automation scripts for generating a 20-second continuous Ghibli-style anime video using ComfyUI, AnimateDiff, and ControlNet.

## Contents
* `ghibli_v2v.json`: The original ComfyUI workflow JSON (UI format).
* `send_api_lcm.py`: The automated Python script that reconstructs the workflow into API format, applies LCM (Latent Consistency Model) LoRA, disables frame limits, enables AnimateDiff Sliding Context Windows, and queues it to the ComfyUI server.
* `2026.5.1開發日誌.md`: The development and troubleshooting log detailing the journey of fixing the memory limits, AnimateDiff 32-frame context limits, and ControlNet compatibility issues.

## Requirements
* ComfyUI
* `ComfyUI-AnimateDiff-Evolved`
* `ComfyUI-Advanced-ControlNet` (Required for infinite sliding window processing)
* `ComfyUI-VideoHelperSuite`
* Model: `mm_sd_v15_v2.ckpt` (AnimateDiff v2)
* LoRA: `StudioGhibli-Redmond-V2.safetensors`
* LoRA: `lcm-lora-sdv1-5.safetensors`

## How to Use
1. Start ComfyUI.
2. Run `python send_api_lcm.py` to automatically queue the high-speed 8 FPS LCM processing task.
