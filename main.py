import gradio as gr
from app import respond


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    gr.ChatInterface(fn=respond, chatbot=chatbot, type="messages")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
