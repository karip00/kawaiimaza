from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'u ok my guy?'
    elif 'kire' in lowered:
        return 'hiiiiiiiiiiiii >~~~~~~<'
    elif 'metal' in lowered:
        return ">~~~~~~~~~~~~~~~~~~~~~~<"
    elif 'animatron' in lowered:
        return "bal amar niggar baccha"
    elif 'kenpachi' in lowered:
        return "u mean keniggachi?"
    elif "roll a dice" in lowered:
        return f'i can onwwy roll joints - but still as u asked - {randint(1, 6)}'
    elif "flip a coin" in lowered:
        return f'i onwwy flip women off - but still as u asked - {choice(["heads", "tails"])}'
    else:
        return choice(['thikmoto kotha ko nigga :3'
                       'bal amar',
                       ':v',
                       'buzi na ki kos'])

    

