"""
  API文档：https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#python
"""
import time
from google import genai
# 导入 API_Key python文件 提供的变量
import API_Key
# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=API_Key.APIKEY)
# 记录代码开始执行的时间
start_time = time.time()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="人工智能是如何工作的"
)
print(response.text)
print(f"代码执行时间: {time.time() - start_time}秒") # 28秒

# 流式返回
# response = client.models.generate_content_stream(
#     model="gemini-2.5-flash",
#     contents=["人工智能是如何工作的"]
# )
# num = 0
# for chunk in response:
#     num += 1
#     print(num, chunk.text, end="")

# stream = client.interactions.create(
#     model="gemini-2.5-flash",
#     input="人工智能是如何工作的",
#     stream=True
# )
# print(f"代码执行时间: {time.time() - start_time}秒") # 9秒
# num = 0
# for chunk in stream:
#     num += 1
#     print(f'--- Chunk {num} ---')
#     if chunk.event_type == "content.delta":
#         if chunk.delta.type == "text":
#             print(chunk.delta.text, end="", flush=True)
#         elif chunk.delta.type == "thought":
#             print(chunk.delta.thought, end="", flush=True)
#     elif chunk.event_type == "interaction.complete":
#         print(f"\n\n--- Stream Finished ---")
#         print(f"Total Tokens: {chunk.interaction.usage.total_tokens}")