from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 初始化Ollama LLM，指定模型和Docker中Ollama服务的地址
llm = Ollama(
    model="llama2",
    base_url="http://localhost:11434"  # 对应Docker映射的端口
)

# 创建一个简单的提示模板
prompt = PromptTemplate(
    input_variables=["question"],
    template="请解释以下概念：{question}"
)

# 创建LLM链
chain = LLMChain(llm=llm, prompt=prompt)

# 调用模型
question = "什么是量子计算？"
response = chain.run(question)

print("问题：", question)
print("回答：", response)

# 另一个示例：进行多轮对话
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory

# # 创建带记忆的对话链
# conversation = ConversationChain(
#     llm=llm,
#     memory=ConversationBufferMemory()
# )

# print("\n对话示例：")
# print(conversation.predict(input="你好，我叫小明"))
# print(conversation.predict(input="我刚才告诉你我的名字了吗？"))
# print(conversation.predict(input="那你能重复一下我的名字吗？"))
