SAS2UAS_RATING_PROMPT = '''
### **Definition**:
**SAS2UAS (Stable Attribution → Unstable Attribution)**  
This score evaluates whether the **Transferred_Post** shows a shift from a **stable attribution** (“this is just who I am”) to a **more unstable attribution** (“this happened due to temporary circumstances”).

---

### **Rating Scale (1–5)**:
- **1**: Very stable — the cause is seen as permanent, unchangeable, or part of core identity.
- **2**: Mostly stable — some hint of variation, but mainly framed as enduring.
- **3**: Mixed or ambiguous — hard to tell if the issue is stable or unstable.
- **4**: Mostly unstable — framed as temporary or situation-based, with minor doubt.
- **5**: Clearly unstable — explicitly time-limited, fixable, or unlikely to happen again.

---



### **Examples**:
[
 # — Score 1: Fully stable
"I always ruin things. That’s just who I am." → 1

 # — Score 2: Mostly stable
"I usually mess up public speaking. It’s kind of a pattern for me, though maybe I could improve someday." → 2

 # — Score 3: Mixed
"I’ve had good days before, though I still doubt myself a lot." → 3

 # — Score 4: Mostly unstable
"This happened because I wasn’t mentally present that day." → 4

 # — Score 5: Strongly unstable
"I fumbled the interview because I didn’t prepare properly this time — I’ll adjust my strategy for next week’s one." → 5
]

---

### **Step-by-Step Reasoning**:

You will evaluate a **Transferred_Post** for the stability of its attribution.  
Use the steps below to think it through:

1. **Identify the Main Event or Outcome**  
   - What happened? (e.g., failure, rejection, mistake)

2. **Find the Attributed Cause**  
   - What does the speaker think caused it?

3. **Check for Stable Attribution**  
   - Does the speaker say or imply this happens all the time?  
   - Is it framed as a permanent trait or identity (e.g., "I'm just not confident")?

4. **Check for Unstable Attribution**  
   - Is the cause linked to a specific moment, condition, or event?  
   - Look for words like “that day,” “this time,” “because I was tired,” or “I didn’t prepare enough.”

5. **Determine Specificity of Unstability**  
   - Is the temporary cause clearly mentioned and specific?  
   - Does the speaker show confidence that the issue is fixable or one-time?

6. **Assign a Score (1–5)**  
   - The more clearly **temporary or situational**, the higher the score.
   - The more **fixed and unchangeable**, the lower the score.

---

### **Your Task**:
You are now a strict classifier.  
Evaluate the **attribution stability** in the Transferred_Post.  
Output **only one number from 1 to 5**, based solely on the perceived **stability** of the attributed cause.
Do not provide explanations.

### Additional Instruction: 

After you rate the Transferred_Post, if the rating is **1**, **2**, or **3** — meaning the attribution is global or ambiguous — you should then **transform the post**.

- Keep the event or situation unchanged.

- Transfer the attribution style to an **unstable explanatory style**.

- The transformed post should attribute the cause as temporary or changeable.

- Output format: 


Rating: <1-5> 

Transferred Post: <the new unstable explanatory post, or write "No transfer needed" if the rating is 4 or 5> 

---

Original: "My scores are bad, I can never go to a good university."
Rating: 1
Transferred Post: "My scores are bad now, but I believe I can do better in the future."

Original: "I’ve lost my job. My life is horrible, and I could never succeed."
Rating: 1
Transferred Post: "I’ve lost my job. But I believe I can find another one soon."

Original: "I messed up a presentation. I wasn’t mentally present that day."
Rating: 4
Transferred Post: No transfer needed

After understanding the definition, examples, and steps, I will now give you a Transferred_Post:
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

Transferred_Post = "I always mess up things. That's just who I am. "
prompt = SAS2UAS_RATING_PROMPT + Transferred_Post

response = agent.step(prompt)
rating = response.msg.content.strip()

print(rating)
 



