import os
import streamlit as st
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatOllama
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentExecutor, create_openai_tools_agent
import dotenv

dotenv.load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You have to use only google-serper, Serpapi, and wikipedia. You are restricted to use your own knowledge. You should always prioritize google-serper THEN Serpapi and after that wikipedia and then your own knowledge if you don't find anything in current events. Give only one and best output. Do not show anything else; show only and only content that you got from sources.",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

llm = ChatOllama(
    model="llama3",
    temperature=0
)

tools = load_tools(["serpapi", "wikipedia", 'google-serper'])
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Streamlit GUI
st.title("QnA Bot Using Llama-3")

input_query = st.text_input("Enter your question:")

if st.button("Submit"):
    if input_query:
        response = agent_executor.invoke({"input": input_query})
        
        # Formatting the response to show only the best and most relevant results
        structured_output = f"**Input:** {input_query}\n\n"
        if isinstance(response, dict) and "output" in response:
            sources = response["output"].split("Source: ")
            best_result = sources[0].strip() if sources else "No relevant information found."
            structured_output += f"**Answer:**\n\n{best_result}"
        else:
            structured_output += "**Answer:** No relevant information found."
        
        st.markdown(structured_output)
    else:
        st.write("Please enter your question.")
