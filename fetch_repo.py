# -*- coding: utf-8 -*-
"""拉取 google/electra-base-discriminator 仓库（排除大文件）并下载页面图。"""
import os
import urllib.request
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

def main():
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        print("pip install huggingface_hub")
        return
    base = os.path.dirname(os.path.abspath(__file__))
    local_dir = os.path.join(base, "hf_repo")
    os.makedirs(local_dir, exist_ok=True)
    snapshot_download(
        repo_id="google/electra-base-discriminator",
        local_dir=local_dir,
        ignore_patterns=["*.safetensors", "*.bin", "*.msgpack", "*.ot", "*.h5", "*.pt", "*.ckpt"],
    )
    print("Repo downloaded to", local_dir)
    img_url = "https://hf-mirror.com/front/thumbnails/google.png"
    img_path = os.path.join(base, "images", "electra_base_discriminator_model_page.png")
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    with urllib.request.urlopen(req) as resp, open(img_path, "wb") as f:
        f.write(resp.read())
    print("Image saved to", img_path)

if __name__ == "__main__":
    main()
