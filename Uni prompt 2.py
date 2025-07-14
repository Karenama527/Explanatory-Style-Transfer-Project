step1_prompt = '''
You will analyze this Transferred_Post and select ONE attribution style that it most likely to have:
(Global/Specific, Internal/External, or Stable/Unstable).
Rate it from 1 (most problematic) to 5 (healthy).

Output:
Dimension: <...>
Rating: <1-5>

### **Examples**:
[
 # — Score 1: Fully stable
"I always ruin things. That’s just who I am." → 1
# — Score 3: Mixed
"I underestimated the time, and the scope changed last minute." → 3
# — Score 4: Mostly specific

"The relationship ended because I struggle with vulnerability in partnerships." → 4

### **Your Task**:

You are now a strict classifier. 

Evaluate the **attribution style** in the transferred post. 

Output **only one number (1–5)** to reflect how **specific** the attribution is.

Do not provide explanations.

Transferred_Post:
Our group failed this project. It's all because I didn't work hard enough.
'''

from pydantic import BaseModel
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType

ollama_model = ModelFactory.create(
    model_platform=ModelPlatformType.OLLAMA,
    model_type="llama3.2",
    model_config_dict={"temperature": 0.4},
)

assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=ollama_model, token_limit=4096)

response1 = agent.step(step1_prompt)
print(response1.msg.content.strip())

step2_prompt = '''
Please transform the following Transferred_Post to improve its attribution in the dimension Internal/External.
Keep the event unchanged, and reframe the cause constructively.

Output:
Transferred Post: <...>

### Examples:

Original: "I failed the exam because I’m stupid."
Rating: 1
Transferred Post: "I failed the exam because the questions were very hard."
Original: "I messed up a presentation. I wasn’t mentally present that day."
Rating: 4
Transferred Post: No transfer needed

Do not provide explanations.
Transferred_Post:
Our group failed this project. It's all because I didn't work hard enough.
'''

from pydantic import BaseModel
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType

ollama_model = ModelFactory.create(
    model_platform=ModelPlatformType.OLLAMA,
    model_type="llama3.2",
    model_config_dict={"temperature": 0.4},
)

assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=ollama_model, token_limit=4096)

response2 = agent.step(step2_prompt)
print(response2.msg.content.strip())
