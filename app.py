import json
import redis
import sys
from brocas import Brocas
from tongue import Tongue

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6000)
    pubsub = r.pubsub()
    pubsub.subscribe('vocal-cords')

    brocas = Brocas()
    tongue = Tongue()

    print 'Listening...'

    while True:
        for item in pubsub.listen():
            print item['data']

            if (item['data'] != 1):
                speechData = brocas.textToSpeech(item['data'])
                speech = json.loads(speechData)
                tongue.sayIt(speech['sound'])


