from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
#  Note: one agent can only use one tool 

# custom python tool
# for custom tools, a doc string is necessary at the start of the function, as this is how the agent knows what does a tool do 
# for custom tools, a return type is necessary , as this is how the agent gets the ifo of the type to return
# adk agenst use custom functions and teh return object looks like a dict : {result : "your return value in right format"}
# get_current_time(format:str = "%Y-%m-%d %H:%M:%S") ->dict: we can pass a param, but cannot give a default value to that param, wont work in adk

def get_current_time() ->dict:
     """
     Get the current time in the format of YYYY-MM-DD HH:MM:SS
     """
     return {
         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     }

root_agent = Agent(
    name="tool_agent", #consistent as the file name
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    tools=[google_search] #one agent can only use one tool ,
    # tools=[get_current_time]
    # tools=[google_search, get_current_time] -X NOT SUPPORTED : can't use custom tools with builtin tools
)
