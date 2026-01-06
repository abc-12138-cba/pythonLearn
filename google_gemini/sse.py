from google import genai
# 导入 API_Key python文件 提供的变量
import API_Key
# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=API_Key.APIKEY)


from flask import Flask, Response
import time

app = Flask(__name__)

def generate():
    # response = client.models.generate_content_stream(
    #   model="gemini-2.5-flash",
    #   contents=["人工智能是如何工作的"]
    # )
    # num= 1
    # for chunk in response:
    #   num+=1
    #   yield f"data: {chunk.text}\n\n"


    stream = client.interactions.create(
      model="gemini-2.5-flash",
      input="人工智能是如何工作的",
      stream=True
    )
    """根据 stream 生成 SSE 数据流"""
    for chunk in stream:
        if chunk.event_type == "content.delta":
            if chunk.delta.type == "text":
                yield f"data: {chunk.delta.text}\n\n"
            elif chunk.delta.type == "thought":
                yield f"data: {chunk.delta.thought}\n\n"
        elif chunk.event_type == "interaction.complete":
            yield f"data: \n--- Stream Finished ---\nTotal Tokens: {chunk.interaction.usage.total_tokens}\n\n"
    # while True:
    #     time.sleep(1)  # 模拟一些实时数据生成过程
    #     yield f"data: 当前时间是 {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

@app.route('/sse')
def sse():
     # 设置正确的响应头，确保字符编码为 UTF-8
    headers = {
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*',  # 允许跨域
    }
    """处理 SSE 请求"""
    return Response(generate(), content_type='text/event-stream; charset=utf-8', headers = headers)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)