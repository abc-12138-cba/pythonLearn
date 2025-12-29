"""
  API文档：https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#python
"""
from google import genai
# 导入 API_Key python文件 提供的变量
import API_Key
# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = client = genai.Client(api_key=API_Key.APIKEY)


response = client.models.generate_content(
    model="gemini-2.5-flash", contents="你是谁??"
)
print(response.text)