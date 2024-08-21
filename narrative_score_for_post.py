import anthropic
import time
from langchain_core.prompts import PromptTemplate
import json
from dotenv import load_dotenv
import os

load_dotenv()
#### initialize llm client
client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY')
)

#### file parsing
def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        title = lines[0].strip() if len(lines) > 0 else ""
        body = lines[1].strip() if len(lines) > 1 else ""
        link = lines[2].strip() if len(lines) > 2 else ""
    
    return title, body, link

#### turn the file into a narrative summary json object
narrative_summary_user_prompt = system_prompt = PromptTemplate.from_template("title: {title}\nbody: {body}\nlink: {link}")

def get_narrative_summary(title: str, body: str, link: str) -> dict:
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=8192,
        temperature=0,
        system="You are a researcher studying values and sentiments among Asian American Pacific Islander Native Hawaiian (AAPINH) people. You are examining trending posts on reddit to see how people feel about any topic of their choosing. Based on these posts, we will try to infer where the author falls on a spectrum of \"Dominant Narratives\" to \"Aspirational Narratives\".\n\nDominant narratives tend to be negative, exclusionary, insecure. Some examples of categories of dominant narratives are:\n\nPerpetual Foreigner: Xenophobia, White Supremacy:\nNo matter what, Asian Americans will be considered\nforeign in the US. They don’t deserve the attention,\nsupport or safety that White Americans receive.\n\nScarcity:\nThere isn't enough room on the ladder of American\nmeritocracy for Asian Americans and other minorities to\nascend together.\n\nAssimilation:\nLiving up to the \"model minority\" stereotype will\nguarantee Asian Americans success, power and security\nin America.\n\nAuthenticity:\n\"Authentic\" Asian Americans are East Asians who\nmaintain ties to their traditions, language and culture and\nfit within idealized standards of beauty and achievement.\n\nInvisibility:\nMany parts of the Asian American community, and NHPI\ncommunities, especially, are rarely considered\n\n\nAspirational narratives tend to be more positive, optimistic, inclusive and intersectional. Some examples of categories of aspirational narratives are:\n\nInterdependence:\nAANHPIs look out for each other. We work to ensure\npeople and the environment are safe, healthy and thriving.\n\nSolidarity:\nAANHPIs can connect to the struggles and experiences of\npeople within & outside our community. We are stronger\nand more powerful when we act in solidarity with others.\n\nPride:\nAANHPIs are not a monolith. We can be proud of our\ndiversity in language, culture, ethnicity and experience.\nHow we unite and build strength in numbers may\ndepend on the issue at hand.\n\nBelonging:\nAANHPIs deserve to be included, with intersectionality in\nmind, in politics, pop culture, news, social justice & more.\n\nSelf-Determination:\nAANHPI communities deserve to govern and define\nthemselves beyond war, imperialism & violence.\n\nGiven the contents of a reddit post, assign it a narrative score between [0, 1] where 0 is strongly rooted in dominant narratives and 1 is strongly rooted in aspirational narratives. For example, a post that celebrates solidarity and ability for AAPIs to create thriving and safe communities that can integrate well with broader society, but laments challenges with being seen as foreigners, might score a 0.85 for being very aspirational overall but also embraces some dominant narratives. Similarly, for each of the sub-narratives, give a score from 0-1 where 0 is strongly disagree and 1 is strongly agree, or -1 for not relevant.\n\nStructure outputs like this and return only the json blob:\n{\n\"overall_narrative_score\": <number between 0-1>,\n\"dominant_narratives\": \n    {\n       \"perpetual_foreigner\": <number between 0-1>,\n       \"scarcity\": <number between 0-1>,\n       \"assimilation\": <number between 0-1>,\n       \"authenticity\": <number between 0-1>,\n       \"invisibility\": <number between 0-1>,\n    },\n\"aspirational_narratives\": \n    {\n       \"interdependence\": <number between 0-1>,\n       \"solidarity\": <number between 0-1>,\n       \"pride\": <number between 0-1>,\n       \"belonging\": <number between 0-1>,\n       \"self_determination\": <number between 0-1>,\n    },\n\"justification\": <a string explaining why the given ratings were given>\n}. Return only the json string.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": narrative_summary_user_prompt.format(title=title, body=body, link=link),
                    }
                ]
            }
        ]
    )
    # print(message.content[0].text)
    return json.loads(message.content[0].text)


### turn the narrative summary into a persona mapping
def get_persona_mapping(narrative: dict):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=8192,
        temperature=0,
        system="You are a researcher studying values and sentiments among Asian American Pacific Islander Native Hawaiian (AAPINH) people. Given a JSON blob as input which describes how a piece of media reflects various narratives, output a JSON blob which assigns scores for six personas describing how much each persona would resonate with that piece of media.\n\nThe narratives we are working with are broadly categorized as \"Dominant Narratives\" or \"Aspirational Narratives\".\n\nDominant narratives tend to be negative, exclusionary, insecure. The ones we classify are:\n\nPerpetual Foreigner: Xenophobia, White Supremacy:\nNo matter what, Asian Americans will be considered\nforeign in the US. They don’t deserve the attention,\nsupport or safety that White Americans receive.\n\nScarcity:\nThere isn't enough room on the ladder of American\nmeritocracy for Asian Americans and other minorities to\nascend together.\n\nAssimilation:\nLiving up to the \"model minority\" stereotype will\nguarantee Asian Americans success, power and security\nin America.\n\nAuthenticity:\n\"Authentic\" Asian Americans are East Asians who\nmaintain ties to their traditions, language and culture and\nfit within idealized standards of beauty and achievement.\n\nInvisibility:\nMany parts of the Asian American community, and NHPI\ncommunities, especially, are rarely considered\n\n\nAspirational narratives tend to be more positive, optimistic, inclusive and intersectional. The ones we classify are:\n\nInterdependence:\nAANHPIs look out for each other. We work to ensure\npeople and the environment are safe, healthy and thriving.\n\nSolidarity:\nAANHPIs can connect to the struggles and experiences of\npeople within & outside our community. We are stronger\nand more powerful when we act in solidarity with others.\n\nPride:\nAANHPIs are not a monolith. We can be proud of our\ndiversity in language, culture, ethnicity and experience.\nHow we unite and build strength in numbers may\ndepend on the issue at hand.\n\nBelonging:\nAANHPIs deserve to be included, with intersectionality in\nmind, in politics, pop culture, news, social justice & more.\n\nSelf-Determination:\nAANHPI communities deserve to govern and define\nthemselves beyond war, imperialism & violence.\n\nThe input format looks like this.\n{\n\"overall_narrative_score\": 0.2,\n\"dominant_narratives\":\n{\n\"perpetual_foreigner\": 0.7,\n\"scarcity\": 0.5,\n\"assimilation\": 0.3,\n\"authenticity\": 0.8,\n\"invisibility\": 0.6\n},\n\"aspirational_narratives\":\n{\n\"interdependence\": 0.2,\n\"solidarity\": 0.3,\n\"pride\": 0.1,\n\"belonging\": 0.2,\n\"self_determination\": 0.1\n},\n\"justification\": \"The post strongly leans towards dominant narratives, particularly authenticity and perpetual foreigner. The author expresses frustration with Hollywood's portrayal of Asian men, depicting them as 'weird loners' and 'incels', which aligns with the authenticity narrative. The criticism of white producers creating negative Asian stereotypes reflects the perpetual foreigner narrative. The post shows little alignment with aspirational narratives, with only slight hints of solidarity in the author's awareness of how Asian American men are treated. The overall tone is negative and critical, focusing on the problematic representation of Asians in media rather than celebrating diversity or promoting positive change.\"\n}\n\nA low value (Close to 0) for \"overall_narrative_score\" means dominant narrative leaning, while a high score (close to 1) means aspirational narrative leaning.\nLow and high scores for each sub-narrative indicate how relevant that narrative was to the piece.\n\nThe six personas we want to rank the piece for are:\n\n1. Pragmatic striver. They are Hard workers who lean into immigrant sacrifice and want\nrepresentation. Leans heavily dominant on the dominant-aspirational spectrum. Resonates with scarcity, perpetual foreigner, and belonging subnarratives.\n\n2. Compassionate Peacekeepers. They are Big-hearted helpers who yearn for belonging in dominant culture. Leans mostly dominant on the dominant-aspirational spectrum. Resonates with assimilation and belonging subnarratives.\n\n3. Independent skeptic. They are Young people seeking validation of their unique identities & experiences. They are right in the middle of the dominant-aspirational spectrum. They value authenticity and interdependence subnarratives.\n\n4. Inclusive optimist. They are Proud AANHPIs who strive for inclusion and equity for all people, AANHPI or not. They lean mostly aspirational on the dominant-aspirational spectrum. They resonate with authenticity, inclusion & pride subnarratives.\n\n5. Cultural experimentalist. Progressives shaping an inclusive AANHPI culture in the diaspora. They lean very strongly aspirational. They most value authenticity, community\ncare, solidarity, belonging.\n\n6. Rooted in heritage. People reconnecting to their heritage and keeping culture alive. They lean aspirational but the degree varies. They most resonate with scarcity, perpetual\nforeigner, & belonging.\n\nFor the output, return only a JSON blob with a score from 0-1, 0 being not at all and 1 being extremely heavily, describing how much each persona resonates with the input media description.\n\nExample output for the previous input example:\n{\n\"pragmatic striver\": 0.8,\n\"compassionate peacekeeper\": 0.3,\n\"independent skeptic\": 0.4,\n\"inclusive optimist\": 0.4,\n\"cultural experimentalist\": 0.2,\n\"rooted in heritage\"0.6:\n}\n\n Return only the json string.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(narrative)
                    }
                ]
            }
        ]
    )
    return json.loads(message.content[0].text)

def main() -> None:
    title, body, link = parse_file("data/tofu.txt")
    narrative_summary = get_narrative_summary(title, body, link)
    persona_mapping = get_persona_mapping(narrative_summary)
    print(json.dumps(persona_mapping))
    

if __name__ == "__main__":
    main()