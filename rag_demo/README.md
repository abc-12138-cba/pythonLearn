首先请确保你的系统已经安装了 uv 和 Jupyter，否则请参照如下链接安装：

uv: https://docs.astral.sh/uv/getting-started/installation/
Jupyter: https://jupyter.org/install
然后在项目根目录下创建一个名为 .env 的文件，并添加以下内容：

GEMINI_API_KEY=xxx

其中 xxx 为你的 Google Gemini API 密钥。没有密钥的用户可以在 https://aistudio.google.com/apikey 上申请。

安装依赖：
uv add sentence_transformers chromadb google-genai python-dotenv

包介绍：
uv add sentence_transformers chromadb google-genai pythondoteny

sentence_transformers：加载 embedding 和 cross-encoder 模型
chromadb：一个非常流行的向量数据库
google-genai：Google 的 Al SDK,调用 gemini-2.5-flash 必备
pythondoteny：将 Gemini API Key 映射到环境变量中

命令运行：
uv run --with jupyter jupyter lab
