from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI,VectorDBQA
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
import os
class DataBaseChat(object):
    qa=None

    def __init__(self):
        # 加载文件夹中的所有txt类型的文件
        loader = DirectoryLoader('./data/', glob="**/[!.]*")
        # 将数据转成 document 对象，每个文件会作为一个 document
        documents = loader.load()
        # # 初始化加载器
        # text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
        # # 切割加载的 document
        # split_docs = text_splitter.split_documents(documents)
        # 初始化 openai 的 embeddings 对象
        embeddings = OpenAIEmbeddings()
        # 将 document 通过 openai 的 embeddings 对象计算 embedding 向量信息并临时存入 Chroma 向量数据库，用于后续匹配查询
        #不分割文件，每个文件分别向量化
        docsearch = Chroma.from_documents(documents, embeddings)#,persist_directory="./persist_directory")#
        # 创建问答对象
        self.qa = VectorDBQA.from_chain_type(llm=OpenAI(model_name="gpt-3.5-turbo",max_tokens=1024), chain_type="stuff", vectorstore=docsearch,return_source_documents=True)

    def chat(self,query:str):
        result = self.qa({"query": query})
        return result