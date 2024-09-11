import gradio as gr
from app import get_answer, get_context


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(get_context("shakespeare_chatbot"), type="messages")

    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        chat_history.append({"role": "user", "content": message})
        response = get_answer(chat_history)
        chat_history.append({"role": "assistant", "content": response})
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
