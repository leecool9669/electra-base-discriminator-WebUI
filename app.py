# -*- coding: utf-8 -*-
"""ELECTRA Base Discriminator WebUI 演示（不加载真实模型，仅界面展示）。"""
from __future__ import annotations
import gradio as gr

def fake_load_model():
    return "模型状态：electra-base-discriminator（ELECTRA 判别器）已就绪（演示模式，未加载真实权重）"

def fake_discriminate(text: str) -> tuple[str, str]:
    if not (text or text.strip()):
        return "", "请先输入一段英文或中文文本再进行判别。"
    out_text = (
        "【演示模式】当前未加载真实模型，以下为界面展示示例。\n\n"
        "加载真实模型后，将在此显示：\n"
        "· 每个 token 的「真实/替换」判别结果（0=真实，1=替换）\n"
        "· 判别器输出的可视化（如高亮被判别为替换的 token）\n"
        "· 可用于检测文本中被篡改或生成的 token"
    )
    return "0 0 0 1 0 0 0 0（演示）", out_text

def build_ui():
    with gr.Blocks(title="ELECTRA Base Discriminator · WebUI") as demo:
        gr.Markdown("## ELECTRA Base Discriminator · WebUI 演示")
        gr.Markdown(
            "本界面用于展示基于 ELECTRA 判别器（Discriminator）的典型使用流程，"
            "包括模型加载状态与「真实/替换」token 判别结果的可视化展示。"
        )
        with gr.Row():
            load_btn = gr.Button("加载模型（演示）", variant="primary")
            status_box = gr.Textbox(label="模型状态", value="尚未加载", interactive=False)
        load_btn.click(fn=fake_load_model, outputs=status_box)
        with gr.Tabs():
            with gr.Tab("文本判别"):
                gr.Markdown("输入一段文本，判别器将对其每个 token 判断为「真实」或「替换」（由生成器替换）。")
                text_inp = gr.Textbox(label="输入文本", placeholder="例如：The quick brown fox jumps over the lazy dog", lines=3)
                pred_out = gr.Textbox(label="判别结果（0=真实，1=替换）", interactive=False)
                detail_out = gr.Textbox(label="结果说明", lines=8, interactive=False)
                run_btn = gr.Button("开始判别（演示）")
                run_btn.click(fn=fake_discriminate, inputs=text_inp, outputs=[pred_out, detail_out])
        gr.Markdown("---\n*说明：当前为轻量级演示界面，未实际下载与加载模型参数。*")
    return demo

def main():
    build_ui().launch(server_name="127.0.0.1", server_port=7861, share=False)

if __name__ == "__main__":
    main()
