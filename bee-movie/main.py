from textmagic.rest import TextmagicRestClient
import time

def withRiley():
    username = 'dragonfroot'
    token = 'ZirIQGYrmtXULKaTeE0lJuq4SPOHG2'
    client = TextmagicRestClient(username, token)
    script = 'bee.txt'
    string = "This is the tester string"

    # for word in string.split():

    #     message = client.messages.create(phones="17026352122", text=word)
    #     time.sleep(2)
    message = client.messages.create(phones="17026352122", text='word')


def beeLength():
    script = 'bee.txt'
    i = 0
    with open(script, 'r') as file:
        data = file.read().replace('\n', '')
        for word in data.split():
            # i = i + 1
            print(data)
            time.sleep(1)
    # print(i)


# withRiley()
beeLength()