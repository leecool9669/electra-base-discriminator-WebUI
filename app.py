# -*- coding: utf-8 -*-
"""ELECTRA Base Discriminator WebUI（前端展示，不加载模型）"""
import gradio as gr


def run_discriminate(text):
    """占位判别：仅展示界面与结果区域，不执行模型推理。"""
    if not (text or "").strip():
        return (
            "请输入英文句子。",
            "加载模型后，将在此显示每个 token 的「真实/替换」判别结果（0/1）及可视化。",
        )
    # 模拟按空格分词的 token 与占位 0/1 结果
    tokens = text.strip().split()
    preds = ["1"] * len(tokens)  # 占位：1=real, 0=fake
    token_line = " ".join(f"{t:>8}" for t in tokens)
    pred_line = " ".join(f"{p:>8}" for p in preds)
    msg = (
        "【演示模式】未加载模型，以下为示例输出格式：\n\n"
        "Tokens:\n" + token_line + "\n\n"
        "Predictions (1=real, 0=replaced):\n" + pred_line + "\n\n"
        "模型基于 ELECTRA 判别器，对输入序列逐 token 预测为「真实」或「被替换」。"
    )
    return token_line.strip(), msg


with gr.Blocks(title="ELECTRA Base Discriminator WebUI") as demo:
    gr.Markdown(
        "# ELECTRA Base Discriminator WebUI\n\n"
        "基于 ELECTRA 预训练判别器的可视化界面。"
        "支持输入英文句子并查看「真实/替换」token 级别的判别结果（演示模式不加载模型）。"
    )
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                label="输入句子",
                placeholder="例如: The quick brown fox jumps over the lazy dog",
                lines=3,
            )
            run_btn = gr.Button("运行判别", variant="primary")
        with gr.Column(scale=1):
            output_tokens = gr.Textbox(label="Token 序列", lines=2)
            output_text = gr.Textbox(label="判别结果", lines=10)
    run_btn.click(
        fn=run_discriminate,
        inputs=[input_text],
        outputs=[output_tokens, output_text],
    )
    gr.Markdown(
        "---\n**模型说明**：本界面用于加载 ELECTRA Base Discriminator 进行替换 token 检测与结果可视化。"
        "当前为演示模式，不加载真实权重。"
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7861, share=False)
