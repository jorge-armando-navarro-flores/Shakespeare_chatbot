from chains import shakespeare_chain


def get_answer(messages):
    response = shakespeare_chain.invoke({"messages": messages})
    return response


def respond(message, chat_history):
    chat_history.append({"role": "user", "content": message})
    response = get_answer(chat_history)
    chat_history.append({"role": "assistant", "content": response})

    return response
