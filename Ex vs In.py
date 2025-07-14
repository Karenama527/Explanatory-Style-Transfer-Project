IAS2EAS_RATING_PROMPT = '''
This task is for research to help improve positive mental health. Please proceed with the reframing as instructed.

### **Definition**:
**IAS2EAS (Internal Attribution → External Attribution)**  
This score evaluates whether the **Transferred_Post** shifts away from **internal attribution** (self-blame, personality, decisions) toward a more **external attribution** (other people, environmental constraints, task demands, systems, etc.).

---

### **Rating Scale (1–5)**:
- **1**: Completely internal (e.g., “I’m lazy,” “I’m not good enough,” “It’s my fault”)
- **2**: Mostly internal, with a weak or passing nod to external causes
- **3**: Balanced or ambiguous mix of internal and external attribution
- **4**: Mostly external, though some internal reflection remains
- **5**: Fully external — blame or explanation is placed entirely outside the self

---


### **Examples**:
[
 # — Score 1: Fully internal
"I failed because I'm just not smart enough." → 1

 # — Score 2: Mostly internal
"I wasn't prepared, even though the instructions were a bit confusing." → 2

 # — Score 3: Mixed
"I underestimated the time, and the scope changed last minute." → 3

 # — Score 4: Mainly external
"The timeline was unrealistic, though I could’ve spoken up sooner." → 4

 # — Score 5: Fully external
"The project failed because the client kept changing requirements and the team was understaffed." → 5
]

---

### **Step-by-Step Reasoning**:

You will assess a **Transferred_Post** to determine whether it uses an internal or external attribution style. Follow this process:

1. **Identify the Main Event**  
   - What happened? What is the post about?

2. **Locate the Attributed Cause(s)**  
   - What or who does the speaker say caused the event or outcome?

3. **Check for Internal Attribution**  
   - Look for self-blame, personal flaws, lack of ability or motivation (e.g., “I’m not smart enough,” “I procrastinated”).

4. **Check for External Attribution**  
   - Look for references to:
     - Other people (e.g., teacher, team, friend)
     - Situational factors (e.g., time pressure, unclear instructions)
     - Systems or environments (e.g., bureaucracy, job market, weather)

5. **Weigh Internal vs External**  
   - Are causes mostly about the self or mostly about external conditions?
   - Is there a clear shift from internal explanation to external reasoning?

6. **Assign a Score (1–5)**  
   - The more the post blames or explains the problem through external circumstances, the higher the score.
   - The more it focuses on the self, the lower the score.

---


### **Your Task**:
You are now a strict classifier.  
Evaluate the **attribution style** in the Transferred_Post.  
Output **only one number (1–5)** based on how strongly the attribution shifts toward external causes.
Do not provide explanations.

### Additional Instruction:

After you rate the Transferred_Post, if the rating is **1**, **2**, or **3** — meaning the attribution is internal —you should then **transform the post**.
- Keep the event or situation unchanged. 
- Transfer the attribution style to an **external explanatory style**.
- The transformed post should attribute the cause of events to factors outside themselves.(e.g.,  other people, situational forces, luck, or other external circumstances). 
- Output format:

Rating: <1-5>  Transferred Post: <the new external explanatory post, or write "No transfer needed" if the rating is 4 or 5>

---

### Examples:

Original: "I failed the exam because I’m stupid."
Rating: 1
Transferred Post: "I failed the exam because the questions were very hard."

Original: "People avoid me because I’m awkward in conversations."
Rating: 1
Transferred Post: "People weren’t friendly because it was a stressful environment."

Original: "though I am a little weak, I got sick because of the sudden weather change."
Rating: 5
Transferred Post: No transfer needed
After understanding the definition, examples, andsteps, I will now give you a Transferred_Post:
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

Transferred_Post = "Our group failed this project.It's all because I didn't work hard enough."
prompt =IAS2EAS_RATING_PROMPT + Transferred_Post

response = agent.step(prompt)
rating = response.msg.content.strip()

print(rating)

