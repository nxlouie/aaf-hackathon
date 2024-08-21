from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=anthropic_api_key,
)


POST_PROMPT = "You are a researcher working on understanding Asian American voices. The task at hand is to distill reddit posts down into a short (six to eight words max) summary that captures the key sentiment of the post. Also come up with an emoji that best fits that distilled sentiment. Output only the tagline and emoji.\n\nTry to relate the summary to one of these narratives if relevant:\nPerpetual Foreigner: Xenophobia, White Supremacy\nNo matter what, Asian Americans will be considered\nforeign in the US. They don’t deserve the attention,\nsupport or safety that White Americans receive.\nScarcity\nThere isn't enough room on the ladder of American\nmeritocracy for Asian Americans and other minorities to\nascend together.\nAssimilation\nLiving up to the \"model minority\" stereotype will\nguarantee Asian Americans success, power and security\nin America.\nAuthenticity\n\"Authentic\" Asian Americans are East Asians who\nmaintain ties to their traditions, language and culture and\nfit within idealized standards of beauty and achievement.\nInvisibility\nMany parts of the Asian American community, and NHPI\ncommunities, especially, are rarely considered.\nRacism\n-\nInterdependence\nAANHPIs look out for each other. We work to ensure\npeople and the environment are safe, healthy and thriving.\nSolidarity\nAANHPIs can connect to the struggles and experiences of\npeople within & outside our community. We are stronger\nand more powerful when we act in solidarity with others.\nPride\nAANHPIs are not a monolith. We can be proud of our\ndiversity in language, culture, ethnicity and experience.\nHow we unite and build strength in numbers may\ndepend on the issue at hand.\nBelonging\nAANHPIs deserve to be included, with intersectionality in\nmind, in politics, pop culture, news, social justice & more.\nSelf-Determination\nAANHPI communities deserve to govern and define\nthemselves beyond war, imperialism & violence.\n\n\nExample post:\nDoes anyone else think the movie didi is insanely racist towards Asian men?\nI saw Didi in theaters with my boyfriend. We both saw the trailer and thought it would be your typical slice of life but with Asians as the protagonists. But towards the middle I noticed something was wrong. They changed the main characters' personality completely and made his some kind of bitter incel. He was super rude to his parents that even his white 'friends' had to call him out on it and they even depicted the father as being absent.\n\nAfter reading through this sub, I have become painfully aware of how Asian American men are treated and the trailer makes you think its going to be a fun movie but then it ends up being one of the most depressing things you've ever seen.\n\nI don't like how hollywood will only depict asian men in these weird ways even in movies dedicated for asians.\n\nDoes anyone know, is it a boba liberal production? From what I can see the director is an asian men so I don't know why he decided to have such a negative portrayal of asians. Even towards the end my boyfriend pointed out that the only person didi committed violence to was the Korean kid which I also thought was a weird choice.\n\nEDIT: But I just found it weird how it singled out east asian men as being weird loners with no friends, no social skills and are absent from life. There's too much of that in the media already but I found it worse than even the awkward tween stuff. The beginning was awkward angsty tween stuff, what it morphed into was something weirder entirely.\n\nJust found out the producers were white males which explains alot. Please don't watch the movie, it promotes a certain image of asian men\n\nEDIT2: After thinking about it, I realized that the whole point of the movie is to single out the Asian character as someone who had something intesely, deeply wrong with HIM. It's not his tween angst because the beginning is about that. Nobody showed him racism (except for a small incident with that girl) and even then his response was to self isolate.\n\nIt was weird and gave me big incel vibes.\n\n\nExample response:\nMovie perpetuates negative Asian male stereotypes 😡"
SUMMARY_PROMPT ="""Group these posts into themes, and have the link to each post that fits into the theme at the end of each group. Like so:
Theme 1:
<theme summary>
relevant urls:
url 1
url 2

Theme 2:
<theme summary>
relevant urls:
url 3
url 4

Give the output in valid json
"""

def summarize(input_str):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system=SUMMARY_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": input_str,
                    }
                ]
            }
        ]
    )
    return message.content
