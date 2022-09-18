from dotenv import load_dotenv
import cohere
import os

def configure():
    load_dotenv()

def main():
    configure()
    co = cohere.Client(os.getenv('api_key'))
    input = ''
    prompt='Passage: Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn’t the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to “the dusty section of the dictionary” to find its latest words.\n\nTLDR: Wordle has not gotten more difficult to solve.\n--\nPassage: ArtificialIvan, a seven-year-old, London-based payment and expense management software company, has raised $190 million in Series C funding led by ARG Global, with participation from D9 Capital Group and Boulder Capital. Earlier backers also joined the round, including Hilton Group, Roxanne Capital, Paved Roads Ventures, Brook Partners, and Plato Capital.\n\nTLDR: ArtificialIvan has raised $190 million in Series C funding.\n--\nPassage: The National Weather Service announced Tuesday that a freeze warning is in effect for the Bay Area, with freezing temperatures expected in these areas overnight. Temperatures could fall into the mid-20s to low 30s in some areas. In anticipation of the hard freeze, the weather service warns people to take action now.\n\nTLDR: Freeze warning is in effect for the Bay Area.\n--\nPassage: The 2020 Central Coast wildfires have been linked to at least two arson arrests. Less than a day after the most recent fire broke out, the Monterey County Sheriff’s Office and California Highway Patrol arrested a suspect on suspicion of starting a a 2- to 3-acre fire on the Carmel River Road.\n\nTLDR: Wildfires have been linked to at least two arson arrests.\n--\nPassage: Whiskey, wine, and beer are among the White House\'s food and drink stock as of Monday. A Dec. 2 filing lists 106 items, including \"beer, wine, whiskey, vodka, tequila, rum, gin, and mixers\" among the items available at the White House. The list also includes categories such as \"catering supplies,\" \"snow cone & shaved ice syrups,\" \"sodas,\" \"extracts,\" \"flavorings,\" \"condiments,\".',
    response = co.generate(
        model='xlarge',
        prompt=prompt+input,
        max_tokens=150,
        temperature=0.8,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))

main()