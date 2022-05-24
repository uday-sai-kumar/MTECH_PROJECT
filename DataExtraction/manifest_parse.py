def parse_manifest(my_apk):
    intent_filters = set()
    activities = set(my_apk.get_receivers())
    permissions = set(my_apk.get_permissions())
    receivers = set(my_apk.get_receivers())
    services = set(my_apk.get_services())
    providers = set(my_apk.get_providers())
    _list = ['activity', 'service', 'receiver']

    for _a in activities:
        _values = my_apk.get_intent_filters(_list[0], _a)
        if len(_values) != 0:
            my_list = _values["action"]
            for _intents in my_list:
                intent_filters.add(_intents)

    for _a in services:
        _values = my_apk.get_intent_filters(_list[1], _a)
        if len(_values) != 0:
            my_list = _values["action"]
            for _intents in my_list:
                intent_filters.add(_intents)

    for _a in receivers:
        _values = my_apk.get_intent_filters(_list[2], _a)
        if len(_values) != 0:
            my_list = _values["action"]
            for _intents in my_list:
                intent_filters.add(_intents)

    return activities, permissions, receivers, services, providers, intent_filters



