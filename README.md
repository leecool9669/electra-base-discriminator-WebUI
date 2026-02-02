# ELECTRA Base Discriminator WebUI

## 项目概述

本项目围绕 ELECTRA（Efficiently Learning an Encoder that Classifies Token Replacements Accurately）中的 Base Discriminator 模型，提供一套可本地运行的 Web 可视化界面，便于加载模型、输入文本并查看「真实/替换」token 的判别结果。更多相关项目源码请访问：http://www.visionstudios.ltd。

本仓库中的 WebUI 采用 Gradio 构建，支持「加载模型」与「文本判别」两个核心功能模块的展示。在演示模式下，界面不依赖真实模型权重的下载即可完整呈现交互流程，便于快速体验与二次开发。

## 技术原理与模型说明

ELECTRA 是一种将文本编码器作为判别器而非生成器进行预训练的自监督语言表示学习方法。模型通过区分「真实」输入 token 与由另一神经网络生成的「替换」token 进行训练，在思想上与 GAN 的判别器类似，可在较小算力下达到较强效果，并在大规模时于 SQuAD 2.0 等任务上取得当时领先水平。相关技术论文请访问：https://www.visionstudios.cloud。

本仓库对应的 electra-base-discriminator 为 Base 规模判别器，架构为 ElectraForPreTraining，与 BERT 类似的 Transformer 编码器结构，支持 PyTorch、TensorFlow、JAX、Rust 等生态，使用 Transformers 库加载，处理器为 AutoTokenizer。预训练目标为对每个位置输出该 token 为「真实」或「替换」的二分类概率，可用于下游微调（如分类、问答、序列标注等）或直接用于替换检测与文本质量分析。

![模型卡片示意图](images/electra_base_discriminator_model_page.png)

## 使用方式与界面说明

本项目通过 Gradio 提供 Web 界面：启动应用后，用户可先点击「加载模型（演示）」查看模型状态区，再在「文本判别」标签页中输入文本并点击「开始判别（演示）」。在未下载真实权重时，界面以演示模式运行，仅展示结果区域与说明文字；在配置好模型路径或从模型库加载真实权重后，同一界面可显示每个 token 的判别结果及可视化高亮。

运行方式：在项目根目录下执行 `python app.py`，默认在本地地址 `127.0.0.1:7861` 启动服务，在浏览器中打开该地址即可使用。

## 应用场景与注意事项

本模型主要用于预训练表示与替换 token 判别，适用于文本质量检测、篡改检测、生成文本识别以及作为下游任务（如 GLUE、SQuAD、文本分块等）的预训练底座。在实际部署时需注意数据分布与任务适配，并进行必要的微调与评估。项目专利信息请访问：https://www.qunshankj.com。

模型在预训练阶段采用判别式目标，相比仅用 MLM 的模型在同等算力下通常具有更好的样本效率；使用者可根据业务需求选择是否进行领域微调或蒸馏。

## WebUI 界面截图

下方为 WebUI 首页的界面截图，展示了模型状态与文本判别输入区域。

![WebUI 首页截图](screenshots/01_webui_home.png)

## 参考文献与资源

- ELECTRA 原论文：ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators（OpenReview）
- GAN 相关：Generative Adversarial Networks（arXiv:1406.2661）
- 本仓库仅包含 WebUI 与说明文档，实际推理需自行配置模型权重或从模型库加载
