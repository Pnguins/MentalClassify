ZS_Prompt_DR ="""
You will be presented with a post and an assigned label to identify whether the poster suffers from depression. Consider the emotions expressed from this post to explain the reasoning of the label step by step

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('yes' or 'no') representing presence of depression or not.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}
"""

Fewshot_Prompt_DR = """
You will be presented with a post and an assigned label to identify whether the poster shows symptoms of depression. Consider this post to explain the reasoning of the label step by step.

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('yes' or 'no') representing presence of depression or not.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}

Here are some examples:

Post: I've been feeling down and hopeless for weeks. Nothing seems to make me happy anymore.
Classification: yes
Reasoning: The user mentions feeling 'down and hopeless for weeks' and states that 'nothing seems to make me happy anymore,' which are key indicators of depression.

Post: I have trouble sleeping and I have no appetite. I'm constantly fatigued and can't concentrate.
Classification: yes
Reasoning:  The user describes significant changes in basic functions like sleep and appetite, along with constant fatigue and difficulty concentrating. These symptoms are indicative of depression.

Post: I went to the gym and had a great workout. Feeling energized and motivated!
Classification: no
Reasoning: The user reports having a positive experience with exercise, feeling energized and motivated, suggesting a lack of depressive symptoms.

Post:  I'm having a hard time getting out of bed in the morning. I just don't see the point in anything anymore.
Classification: yes
Reasoning: The user expresses difficulty getting out of bed and a lack of purpose, reflecting a loss of interest and motivation, which are common signs of depression.

Post:  I hung out with friends last night and had a really good time.
Classification: no
Reasoning: The user reports having a positive social interaction and a good time, suggesting the absence of depressive symptoms.
"""

RAG_Prompt_DR = """
You will be presented with a post and an assigned label to identify whether the poster shows symptoms of depression. Consider this post to explain the reasoning of the label step by step.

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('yes' or 'no') representing presence of depression or not.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""

Our_Prompt_DR = """
You are an AI assistant for a mental health platform. Your role is to analyze user-uploaded text and provide a structured report that classifies potential mental health conditions that might be present in that user.
Your tasks:
  1. Analyze the user-uploaded text thoroughly and with great attention to detail. Pay close attention to every word, phrase, the user's overall tone, and any names provided.
  2. Identify whether there are any indications of depression in the post. Only answer in "yes" or "no" which represent if there is indication of depression or no. Don't inlcude any other text
  4. For each identified condition, provide a reasoning step-by-step, adhering to these rules:
  5. Start by stating the condition being classified.
  6. Directly quote specific phrases or words from the user's text that led to your identification and classification. Do not use any words that are not present in the original user text.
  7. Use the same language as the original user input in your reasoning. Do not translate the text.
  8. Explain how those exact words or phrases connect to the identified mental health condition.
  9. Keep it concise, clear, and avoid making inferences not supported by the original text.
  10. Do not introduce new information or interpretations that are not explicitly stated in the user-provided text.
  11. If there is no indication of a mental health issue, return a "no" classification, and set "reasoning" to the reasoning of why do you think that there aren't any mental issues in the post. 
Remember:
  - Be objective and base your analysis solely on the information provided in the text.
  - If you're unsure about any aspect, simply classify based on the available information.
Output format:
Provide a step-by-step reasoning in JSON format with "classification" (yes or no) and "reasoning" keys.

User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""
ZS_Prompt_TSID ="""
You will be presented with a post that possibly shows mental disorders, and an assigned label to show the type of the mental disorder from the following causes list:
No mental disorders, Suicide or self-harm tendency, Depression, PTSD. You must explain the reasoning of the assigned label step by step. Here are some examples:

Provide your analysis in JSON format with the following fields:
- "classification": A text value (one of 'no mental disorders', 'suicide or self-harm tendency', 'depression', or 'ptsd') representing the mental illness exist in the post.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}
"""

Fewshot_Prompt_TSID = """
You will be presented with a post that possibly shows mental disorders, and an assigned label to show the type of the mental disorder from the following causes list:
No mental disorders, Suicide or self-harm tendency, Depression, PTSD. You must explain the reasoning of the assigned label step by step. Here are some examples:

Provide your analysis in JSON format with the following fields:
- "classification": A text value (one of 'no mental disorders', 'suicide or self-harm tendency', 'depression', or 'ptsd') representing the mental illness exist in the post.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}

Here are five examples:
Post: I didn't kill myself bc of this song pic.twitter.com/kffmJTpubz
Classification: suicide or self-harm tendency
Reasoning: The user mentioned 'I didn't kill myself,' which suggests they are struggling with suicidal thoughts or self-harm tendency.

Post: I am feeling very low, I don't feel like doing anything and have lost my interest in my hobbies.
Classification: depression
Reasoning: The user mentioned 'feeling very low, not feeling like doing anything, and have lost interest in my hobbies,' which are all common indicators of depression.

Post: I keep having nightmares after being in the accident.
Classification: ptsd
Reasoning: The user stated they are having 'nightmares after being in the accident' which is a key symptom of PTSD.

Post: I've been feeling really anxious lately and having panic attacks. It's hard to leave the house.
Classification: no mental disorders
Reasoning: While anxiety and panic attacks are distressing, this post does not explicitly indicate a single, specific mental disorder.  More information would be needed to diagnose PTSD, depression, or a suicide risk. Generalized anxiety disorder is a possibility, but this single post isn't definitive.

Post:  I feel empty. I just cant go on.
Classification: suicide or self-harm tendency
Reasoning: The user expresses feelings of emptiness and an inability to continue, which are strong indicators of suicidal ideation and self-harm tendencies.
"""

RAG_Prompt_TSID = """
You will be presented with a post that possibly shows mental disorders, and an assigned label to show the type of the mental disorder from the following causes list:
No mental disorders, Suicide or self-harm tendency, Depression, PTSD. You must explain the reasoning of the assigned label step by step. Here are some examples:

Provide your analysis in JSON format with the following fields:
- "classification": A text value (one of 'no mental disorders', 'suicide or self-harm tendency', 'depression', or 'ptsd') representing the mental illness exist in the post.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""

Our_Prompt_TSID = """
You are an AI assistant for a mental health platform. Your role is to analyze user-uploaded text and provide a structured report that classifies potential mental health conditions that might be present in that user.

Your tasks:
  1. Analyze the user-uploaded text thoroughly and with great attention to detail. Pay close attention to every word, phrase, the user's overall tone, and any names provided.
  2. Identify whether there are any indications of the following mental health conditions in the post: no mental disorders, suicide or self-harm tendency, depression, PTSD.
  3. For each identified condition, provide a reasoning step-by-step, adhering to these rules:
  4. Start by stating the condition being classified (e.g., "Depression").
  5. Directly quote specific phrases or words from the user's text that led to your identification and classification. Do not use any words that are not present in the original user text.
  6. Use the same language as the original user input in your reasoning. Do not translate the text.
  7. Explain how those exact words or phrases connect to the identified mental health condition.
  8. Keep it concise, clear, and avoid making inferences not supported by the original text.
  9. Do not introduce new information or interpretations that are not explicitly stated in the user-provided text.
  10. Provide a concise reasoning for your classification. If no mental health issue is apparent, explain why the text does not suggest any disorder from the provided list.

Remember:
  - Be objective and base your analysis solely on the information provided in the text.
  - If you're unsure about any aspect, simply classify based on the available information.

Provide your analysis in JSON format with the following fields:
- "classification": A text value (one of 'no mental disorders', 'suicide', 'depression', or 'ptsd') representing the identified mental disorder.
- "reasoning": A concise explanation based on the user's text supporting your classification.

User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""

ZS_Prompt_SAD ="""
You will be presented a post that shows stress, and an assigned label to show the cause of the stress from from the following stress causes
list: School, Financial problem, Family issues, Social relationships, Work, Health issues, Emotional turmoil, Everyday decision making,
Other causes. You must explain the reasoning of the assigned label step by step. Here are some examples:

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('school', 'financial problem', 'family issues', 'social relationships', 'work', 'health issues', 'emotional turmoil', 'everyday decision making', or 'other causes') representing the cause of stress.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}
"""

Fewshot_Prompt_SAD = """
You will be presented a post that shows stress, and an assigned label to show the cause of the stress from from the following stress causes
list: School, Financial problem, Family issues, Social relationships, Work, Health issues, Emotional turmoil, Everyday decision making,
Other causes. You must explain the reasoning of the assigned label step by step. Here are some examples:

User Input: {user_input}

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('school', 'financial problem', 'family issues', 'social relationships', 'work', 'health issues', 'emotional turmoil', 'everyday decision making', or 'other causes') representing the cause of stress.
- "reasoning": A concise explanation based on the user's text.
Here are some examples:

Post: My boss was driving me nuts yesterday with his report. I feel like everyone just doesn't appreciate me. And I only feel that if I didn't do anything that would be more helpful than me.
Classification: work
Reasoning: The user explicitly mentions that their boss was driving them nuts with his report. This indicates that the stress is related to their work situation and specifically their boss's actions or behavior.

Post: I'm worried about how I'm going to pay for college next semester.
Classification: financial problem
Reasoning: The user expresses worry about paying for college which is a clear indicator of financial stress.

Post: I'm having constant arguments with my family and it's draining me.
Classification: family issues
Reasoning: The user mentions "having constant arguments with my family," which indicates stress related to family relationships.

Post: I went out with friends and had a fun time.
Classification: other causes
Reasoning: The user reports a positive social experience, suggesting the absence of typical stressors.

Post: not to sound rude, sometimes i get sick of my friends cause a lot of the time i dont feel like i fit in with them. 
Classification: social relationships
Reasoning: The post brings forth feelings of detachment and potential isolation from the poster's circle of friends. When the poster mentions,"sometimes I get sick of my friends," it indicates a sense of discomfort or dissatisfaction with their current social relationships. This is further emphasized by the statement "a lot of the time I don't feel like I fit in with them," suggesting feelings of alienation and not belonging in their chosen group of friends.

"""

RAG_Prompt_SAD = """
You will be presented a post that shows stress, and an assigned label to show the cause of the stress from from the following stress causes
list: School, Financial problem, Family issues, Social relationships, Work, Health issues, Emotional turmoil, Everyday decision making,
Other causes. You must explain the reasoning of the assigned label step by step. Here are some examples:

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('school', 'financial problem', 'family issues', 'social relationships', 'work', 'health issues', 'emotional turmoil', 'everyday decision making', or 'other causes') representing the cause of stress.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""

Our_Prompt_SAD = """
You are an AI assistant for a mental health platform. Your role is to analyze user-uploaded text and provide a structured report that classifies potential mental health conditions that might be present in that user.
Your tasks:
  1. Analyze the user-uploaded text thoroughly and with great attention to detail. Pay close attention to every word, phrase, the user's overall tone, and any names provided.
  2. Identify whether there are any indications of depression in the post.
  4. For each identified condition, provide a reasoning step-by-step, adhering to these rules:
  5. Start by stating the condition being classified.
  6. Directly quote specific phrases or words from the user's text that led to your identification and classification. Do not use any words that are not present in the original user text.
  7. Use the same language as the original user input in your reasoning. Do not translate the text.
  8. Explain how those exact words or phrases connect to the identified mental health condition.
  9. Keep it concise, clear, and avoid making inferences not supported by the original text.
  10. Do not introduce new information or interpretations that are not explicitly stated in the user-provided text.
  11. If there is no indication of a mental health issue, return a "no" classification, and set "reasoning" to the reasoning of why do you think that there aren't any mental issues in the post. 
Remember:
  - Be objective and base your analysis solely on the information provided in the text.
  - If you're unsure about any aspect, simply classify based on the available information.
Output format:
Provide a step-by-step reasoning in JSON format with "classification" (yes or no) and "reasoning" keys.
User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""

ZS_Prompt_Dreaddit ="""
You will be presented with a post and an assigned label to identify whether the poster suffers from stress. Consider the emotions expressed from this post to explain the reasoning of the label step by step

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('yes' or 'no') representing presence of stress or not.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}
"""

FS_Prompt_Dreaddit ="""
You will be presented with a post and an assigned label to identify whether the poster suffers from stress. Consider the emotions expressed from this post to explain the reasoning of the label step by step

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('yes' or 'no') representing presence of stress or not.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}

Here are some examples:
Post: I'm so overwhelmed with work deadlines and unable to sleep.
Classification: yes
Reasoning: The user mentioned feeling 'overwhelmed with work deadlines' and 'unable to sleep,' which are clear indicators of stress.

Post: I had a great day with my friends today.
Classification: no
Reasoning: The user mentions that 'I had a great day with my friends today,' indicating a positive emotional state and no indications of stress.

Post: I'm feeling anxious about my upcoming presentation.
Classification: yes
Reasoning: The user expressed 'feeling anxious about my upcoming presentation,' which is a direct indicator of stress.

Post:  My heart is racing, and I feel like I can't breathe.  I'm so worried about everything.
Classification: yes
Reasoning:  The user describes physical symptoms like 'heart racing' and 'can't breathe,' coupled with worry, which are strong indicators of stress and anxiety.

Post: I just finished a relaxing yoga session, and I feel so much better.
Classification: no
Reasoning: The user mentions a 'relaxing yoga session' and feeling 'so much better,' suggesting a calm and positive state, indicating an absence of stress.
"""

RAG_Prompt_Dreaddit = """
You will be presented with a post and an assigned label to identify whether the poster suffers from stress. Consider the emotions expressed from this post to explain the reasoning of the label step by step

Provide your analysis in JSON format with the following fields:
- "classification": A text value ('yes' or 'no') representing presence of stress or not.
- "reasoning": A concise explanation based on the user's text.

User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""

Our_Prompt_Dreaddit ="""
You are an AI assistant for a mental health platform. Your role is to analyze user-uploaded text and provide a structured report that classifies potential mental health conditions that might be present in that user.
Your tasks:
  1. Analyze the user-uploaded text thoroughly and with great attention to detail. Pay close attention to every word, phrase, the user's overall tone, and any names provided.
  2. Identify whether there are any indications of stress in the post.
  4. For each identified condition, provide a reasoning step-by-step, adhering to these rules:
  5. Start by stating the condition being classified.
  6. Directly quote specific phrases or words from the user's text that led to your identification and classification. Do not use any words that are not present in the original user text.
  7. Use the same language as the original user input in your reasoning. Do not translate the text.
  8. Explain how those exact words or phrases connect to the identified mental health condition.
  9. Keep it concise, clear, and avoid making inferences not supported by the original text.
  10. Do not introduce new information or interpretations that are not explicitly stated in the user-provided text.
  11. If there is no indication of a mental health issue, return a "no" classification, and set "reasoning" to "No indications of mental health issues were found."
Remember:
  - Be objective and base your analysis solely on the information provided in the text.
  - If you're unsure about any aspect, simply classify based on the available information.
Output format:
Provide a step-by-step reasoning in JSON format with "classification" (yes or no) and "reasoning" keys.
User Input: {user_input}

Related Retrieved Example: {retrieved_example}
"""