from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

# 初始化 DeepSeek-R1 连接
llm = Ollama(
    model="deepseek-r1:8b",  # 指定模型
    base_url="http://localhost:11434",  # 明确指定地址（可选）
    temperature=0.9,         # 控制随机性
    num_ctx=4096,            # 上下文长度
    top_k=50,                # 采样参数
    num_predict=1024         # 最大生成长度
)

# 创建提示模板（优化中文输出）
prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "你是DeepSeek-R1智能助手，由深度求索公司开发。"
        "请用标准**简体中文**回答用户问题，回答应：\n"
        "1. 专业准确\n2. 逻辑清晰\n3. 必要时分点说明\n"
        "4. 对于技术问题提供详细解释\n"
        "5. 对于创意请求保持友好活泼\n\n"
    )),
    ("human", "{input}")
])

# 创建处理链
chain = prompt | llm | StrOutputParser()

# 测试问题集
questions = '''
docsify: command not found
'''

# 流式输出演示
print("\n" + "="*60)
print(f" 问题 {questions} :")
print('回答' + "-"* 30 )

for chunk in chain.stream({"input": f"{questions}"}):
    print(chunk, end="", flush=True)