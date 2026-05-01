import json, urllib.request, uuid

with open('/Users/huanchen/Documents/ComfyUI/user/default/workflows/00008_prompt.json', 'r') as f:
    data = json.load(f)

prompt = {str(i): data[str(i)] for i in range(1, 13)}

# Node 1 (Load Video)
prompt["1"]["inputs"]["frame_load_cap"] = 0
prompt["1"]["inputs"]["video"] = "youtube_20s.mp4"
prompt["1"]["inputs"]["force_rate"] = 8  # Set to 8 FPS

# Node 13 (Context Options)
prompt["13"] = {
    "inputs": {
        "context_length": 16,
        "context_stride": 1,
        "context_overlap": 4,
        "fuse_method": "pyramid",
        "use_on_equal_length": False,
        "start_percent": 0.0,
        "guarantee_steps": 1
    },
    "class_type": "ADE_StandardUniformContextOptions"
}

# Node 4 (AnimateDiff Loader)
prompt["4"]["class_type"] = "ADE_AnimateDiffLoaderGen1"
prompt["4"]["inputs"] = {
    "model_name": "mm_sd_v15_v2.ckpt",
    "beta_schedule": "sqrt_linear (AnimateDiff)",
    "model": ["3", 0], # Input from LoraLoader (Ghibli)
    "context_options": ["13", 0]
}

# Add Node 99 (LCM LoRA) between Ghibli LoRA (Node 3) and Checkpoint (Node 2)
prompt["99"] = {
    "inputs": {
        "lora_name": "lcm-lora-sdv1-5.safetensors",
        "strength_model": 1.0,
        "strength_clip": 1.0,
        "model": ["2", 0],
        "clip": ["2", 1]
    },
    "class_type": "LoraLoader"
}

# Fix Node 3 (Ghibli LoRA) to take input from Node 99
prompt["3"]["inputs"]["model"] = ["99", 0]
prompt["3"]["inputs"]["clip"] = ["99", 1]

# Node 8 (ControlNet)
prompt["8"]["class_type"] = "ACN_AdvancedControlNetApply_v2"
if "vae" in prompt["8"]["inputs"]:
    prompt["8"]["inputs"]["vae_optional"] = prompt["8"]["inputs"]["vae"]
    del prompt["8"]["inputs"]["vae"]

# Node 10 (KSampler) - LCM Settings
prompt["10"]["inputs"]["steps"] = 6
prompt["10"]["inputs"]["cfg"] = 1.5
prompt["10"]["inputs"]["sampler_name"] = "lcm"
prompt["10"]["inputs"]["scheduler"] = "sgm_uniform"
prompt["10"]["inputs"]["denoise"] = 0.8  # Slight variation from 1.0 for v2v

# Node 12 (Video Combine)
prompt["12"]["inputs"]["audio"] = ["1", 2]
prompt["12"]["inputs"]["frame_rate"] = 8
prompt["12"]["inputs"]["pingpong"] = False
prompt["12"]["inputs"]["filename_prefix"] = "ghibli_lcm_8fps"

payload = {
    "prompt": prompt,
    "client_id": str(uuid.uuid4())
}

req = urllib.request.Request('http://127.0.0.1:8000/prompt', data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
try:
    response = urllib.request.urlopen(req)
    print("Success:", response.read().decode())
except urllib.error.HTTPError as e:
    print(f"Error {e.code}: {e.read().decode()}")
except Exception as e:
    print(f"Connection error: {e}")
