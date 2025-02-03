import json

import gradio as gr
import requests
import time


def chat_with_ollama(user_input, api_url="http://localhost:11434/api/generate"):
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "model": "deepseek-llama2-r1:32b",  # 确保模型名称正确
        "prompt": user_input,
        "stream": True,  # 启用流式输出
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, stream=True)
        if response.status_code != 200:
            return f"Error: {response.text}"

        result = []
        for chunk in response.iter_lines():
            if b'data: ' in chunk:
                try:
                    line = chunk.decode().split('data: ')[1]
                    data = json.loads(line)
                    result.append(data["text"])
                    yield "".join(result)
                except Exception as e:
                    print(f"Error parsing stream: {e}")
        return ""
    except Exception as e:
        print(f"Request failed: {e}")
        return "请求失败，请检查 Ollama 服务是否在运行。"


def respond(user_message, chatbot_history):
    api_url = "http://localhost:11434/api/generate"

    # 发送请求到 Ollama
    response_stream = chat_with_ollama(user_message, api_url)

    # 在 Gradio 中逐步显示生成内容
    partial_response = ""
    for text in response_stream:
        if not text.strip():
            continue
        partial_response += text
        yield "", [(user_message, partial_response)]

    return "", chatbot_history


# 创建 Gradio 界面
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="输入你的问题：", placeholder="请输入...")
    clear = gr.ClearButton([msg, chatbot])


    # 定义消息处理函数
    def respond(user_message, chatbot_history):
        return respond(user_message, chatbot_history)


    msg.submit(
        fn=respond,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )

# 启动应用
if __name__ == "__main__":
    demo.launch()