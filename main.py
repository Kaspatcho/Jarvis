import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from recordMic import recordMic

def voiceToText():
    import credentials as cred
    ibmUrl = cred.URL
    apiKey = cred.API_KEY
    authenticator = IAMAuthenticator(apiKey)
    speech_to_text = SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(ibmUrl)
    outputFile = recordMic('O que deseja?', 3)
    print('Processando...')
    with open(f'./{outputFile}', 'rb') as audioFile:
        try:
            result = speech_to_text.recognize(audio=audioFile, content_type='audio/wav',
        timestamps = True, word_confidence = True).get_result()['results'][0]['alternatives'][0]['transcript']
        except IndexError:
            result = 'No sound'

    print(f'Acho que voce disse "{result}"')
    return result


understood = False

while not understood:
    result = voiceToText().strip()
    understood = True
    if result == 'play my music\'s': # toca umas musicas legais
            import webbrowser as web
            web.open('https://www.youtube.com/watch?v=-tJYN-eG1zk&list=PL718D16542AE44430&ab_channel=QueenOfficial')
    elif result == 'minesweeper': # abre o campo minado no google
        import webbrowser as web
        web.open('https://www.google.com/search?q=minesweeper&oq=minesweeper&aqs=chrome..69i57.1008j0j7&sourceid=chrome&ie=UTF-8')
    elif result == 'open discord': # abre o discord
        import webbrowser as web
        web.open('https://discord.com/channels/@me')
    elif 'search for' in result: # pesquisa algo no google
        import webbrowser as web
        search = result.replace('search for', '').strip()
        web.open(f'https://google.com/search?q={search}')
    else:
        print('Nao entendi.')
        understood = False
