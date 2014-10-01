from __future__ import print_function
from mixpanel import Mixpanel
import json
import params

def get_event_total(unit="day", interval=1):
    events = ["#product-detail", "#related"]

    data = api.request(['events'], {
        'event' : events,
        'unit' : unit,
        'interval' : interval,
        'type': 'general'
    })

    series = data["data"]["series"]

    res = {}
    for event in events:
        event_data = data["data"]["values"][event]
        vals = [event_data[s] for s in series]
        res[event] = sum(vals)

    return res


token = params.token
key = params.key
secret = params.secret

api = Mixpanel(key, secret)


total1 = get_event_total(interval=1)
total7 = get_event_total(interval=7)
total30 = get_event_total(interval=30)

js = json.dumps({
    "1 day" : total1,
    "7 day" : total7,
    "30 day" : total30,
}, indent=4)

with open(params.output_path, "w") as fp:
    fp.write(js)
