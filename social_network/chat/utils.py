def correct_messages(ignores, messages):
    mess = []
    for message in messages:
        bool = True
        for ignore in ignores:
            if ignore.whom == message.author:
                bool = False
        if bool is True:
            mess.append(message)
    return mess
