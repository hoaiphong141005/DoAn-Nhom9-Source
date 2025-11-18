import gradio as gr

def greet(name):
    return "Xin chào " + name + "!! Môi trường Hugging Face của Nhóm 9 (fenzihp) đã chạy thành công!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()