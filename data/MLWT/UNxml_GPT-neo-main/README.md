# GPT-NEO_UNXML
Using TensorFlow to finetune a GPT-neo model with United Nations General Assembly resolutions

Authors: Felix Gröner, Nils Axe

Additional credits: Andonian, Alex and Biderman, Stella and Black, Sid and Gali, Preetham and Gao, Leo and Hallahan, Eric and Levy-Kramer, Josh and Leahy, Connor and Nestler, Lucas and Parker, Kip and Pieler, Michael and Purohit, Shivanshu and Songz, Tri and Wang, Phil and Weinbach, Samuel @ [EleutherAI (https://www.eleuther.ai/)

GPT-NeoX: Large Scale Autoregressive Language Modeling in PyTorch; http://github.com/eleutherai/gpt-neox

## Summary
The goal of this project is to finetune a generative pretrained transformer (GPT) and generate United Nations (UN) resolutions.
### Data
The United Nations started publishing some of their documents in a machine-readable format. More specifically, we retrieved resolutions adopted by the General Assembly in their 75th session (2020/2021). The XML files were downloaded from the official github repository.

UN Resolution have a very specific structure:
 

*   They start with the adopting body, which in our case is always "The GeneralAssembly,"
*   Then, the first half contains the preambular clauses. They usually start with a verb in present progressive (-ing) and end with a comma.
*   The second halfpart contains the operative clauses, which are enumerated. They each start with a verb in simple present and end with a semicolon. The final clause ends with a full stop.




Our XML parser reads the xml and extracts only the relevant parts, i.e. the clauses. Then it concatenates the clauses of all resolutions to a single .txt-file, which we use as training data.

### Model
We use GPT-neo and finetune it to adopt the style of the UN resolutions. More specifically, the pretrained model is GPT3_XL by EleutherAI with 1,3 billion parameters.
Our training takes place in the Google Cloud

### Prompts
To generate a random resolution, the prompt should be "The General Assembly,".

We were able to generate resolutions for a specific topic by setting the prompt to the title of that topic and then adding "The General Assembly,". These work best if the topics are similar to those actually discussed at the United Nations.



### Results
The results have been analyzed by an expert familiar with UN resolutions and evaluated in three aspects: format, content structure and content coherence. A sample can be found at the bottom of this notebook.


The generated resolutions are in accordance with the aforementioned specific structure of UN resolutions. Viable verbs in the correct tenses are used and usually the correct punctuation is set. There sometimes are minor hiccups where a footnote interferes with a clause.


The content structure is surprisingly accurate. The first preambular clauses usually refers to past resolutions while the last operative clause refers to the provisional future agenda.


The content coherence is not as good and gives away that it is a generated resolution. However, this mostly shows in details, which are discovered only by experts. Resolutions codes, adoption dates, resolution titles and resolution content don't always match. Also, memorial days and their dates sometimes don't match. The content appears to be held so general that it can't really be incorrect (like horoscopes) and sometimes includes elements not commonly found in UN documents.
