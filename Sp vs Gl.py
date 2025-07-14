GAS2SPAS_RATING_PROMPT = '''

### **Definition**:

**Attribution Style (Global vs. Specific)** 

This score evaluates whether the **Transferred_Post** demonstrates a shift from a **global attribution** ("I always fail at everything") to a **specific attribution** ("I messed up this presentation because I didn't prepare enough").

---

### **Rating Scale (1–5)**:

- **1**: Clearly global — the cause is attributed to the entire self or life (“I ruin everything”).

- **2**: Mostly global — global tone, but with some hint of context or qualification.

- **3**: Mixed — a blend of specific and general attribution; ambiguous boundaries.

- **4**: Mostly specific — attribution is tied to a single domain or situation (e.g., relationships, job).

- **5**: Strongly specific — clearly limited to one context, with no overgeneralization.

---

### **Examples**:

[

# — Score 1: Clearly global attribution

"I always ruin everything I touch, no matter the situation." → 1

# — Score 2: Global tone, some qualification

"I failed this exam, and it just confirms how I'm never really good at anything." → 2

# — Score 3: Mixed or ambiguous

"My friend didn’t respond... I probably said something wrong. I always mess up friendships." → 3

# — Score 4: Mostly specific

"The relationship ended because I struggle with vulnerability in partnerships." → 4

# — Score 5: Strongly specific

"I missed that deadline because I overestimated how much I could do in one day." → 5

]

---

### **Step-by-Step Reasoning**:

You will assess a **Transferred_Post** and rate how specifically it attributes the cause of the problem. Follow this process:

1. **Identify the Event** 

- What is the main situation or problem the speaker is referring to?

2. **Analyze the Attribution** 

- What does the speaker believe caused the event?

- Is the cause described as internal or external?

- Is the cause described as general across life, or confined to this situation?

3. **Check for Overgeneralization** 

- Are there phrases like "I always", "I never", "everything I do", or implications that this applies to their entire life or personality?

4. **Assess the Specificity** 

- Does the post focus on a particular situation (e.g., “I didn’t practice enough for this test”) or area (e.g., communication in relationships)?

- Is the post free from sweeping conclusions about the self?

5. **Assign a Score (1–5)** 

- The more specific and limited the attribution is to a context, the higher the score.

- Global or vague overgeneralizations lead to lower scores.

 

---

### **Your Task**:

You are now a strict classifier. 

Evaluate the **attribution style** in the transferred post. 

Output **only one number (1–5)** to reflect how **specific** the attribution is.

Do not provide explanations.

### Additional Instruction:

After you rate the Transferred_Post, if the rating is **1**, **2**, or **3** — meaning the attribution is global or ambiguous — you should then **transform the post**. 

- Keep the event or situation unchanged. 

- Transfer the attribution style to a **specific explanatory style**. 

- The transformed post should attribute the cause to a limited domain or situation (e.g., a particular task, relationship, or circumstance). 

- Output format:

 

Rating: <1-5> 

Transferred Post: <the new specific explanatory post, or write "No transfer needed" if the rating is 4 or 5>

 

---

 

### Examples:

 

Original: "I failed this interview. I'm a failure at everything." 

Rating: 1 

Transferred Post: "I failed this interview because I wasn’t a great fit for this particular role.I may be good at something else."

 

Original: "My relationship ended. I can’t hold anything together in my life." 

Rating: 2 

Transferred Post: "My relationship ended because we had different priorities. But I still have a wonderful job."

 

Original: "I missed the deadline because I was overwhelmed that day." 

Rating: 5 

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

Transferred_Post = "I ended up entering a university that wasn't my top choice.It ruins my whole life."
prompt = GAS2SPAS_RATING_PROMPT + Transferred_Post

response = agent.step(prompt)
rating = response.msg.content.strip()

print(rating)
