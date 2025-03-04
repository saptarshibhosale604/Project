## ## Method 01, CSV File loader

# from langchain.document_loaders import CSVLoader

# loader = CSVLoader('./penguins.csv')

# data = loader.load()

# # print(data)

# print("type::",type(data))

# print("data0::",data[0])

# print("data1::",data[1])

# print("data0content::",data[0].page_content)


# from langchain.prompts import (
#     ChatPromptTemplate,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )
# from langchain.chat_models import ChatOpenAI
# from langchain.document_loaders import WikipediaLoader

## ## Method 02, Wikepedia File loader
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_community.document_loaders import WikipediaLoader

# # Testing wikipedia loader
# docs = WikipediaLoader(query="god",load_max_docs=1)

# print("\n\n## docs ##:",docs)
# print("\n\n## docs.load() ##:",docs.load())
# print("\n\n## docs.load()[0].page_content ##:",docs.load()[0].page_content)


def answer_question_about(person_name,question):
    # Get Wikipedia Article
    docs = WikipediaLoader(query=person_name,load_max_docs=1)
    context_text = docs.load()[0].page_content

    print("\n\n## docs ##:",docs)
    print("\n\n## context_text ##:",context_text)
    
    # Connect to OpenAI Model
    # myTestKey07 #saptarshibhosale604@gmail.com
    f = open('openai_api_key.txt')
    api_key = f.read().strip()
    model = ChatOpenAI(openai_api_key=api_key)
    
    print("\n\n## model ##:",model)
    
    # Ask Model Question
    human_prompt = HumanMessagePromptTemplate.from_template('Answer this question\n{question}, here is some extra context:\n{document}')
    print("\n\n## human_prompt ##:",human_prompt)
    
    # Assemble chat prompt
    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
    print("\n\n## chat_prompt ##:",chat_prompt)
    
    #result
    result = model.invoke(chat_prompt.format_prompt(question=question,document=context_text).to_messages())
    print("\n\n## docs ##:",docs)
    
    print(result.content)

answer_question_about("Claude Shannon","When was he born?")
