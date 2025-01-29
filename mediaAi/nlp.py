import joblib


def predict(text):
    loaded_model = joblib.load('D:\studying\mediaPlayer\pproject2\mediaAi\model.pkl')

    label_mapping = {
        0: "fast forward",
        1: "back",
        2: "pause",
        3: "resume",
        4: "mute",
        5: "2x speed",
        6: "raise voice",
        7: "down voice",
    }

    delimiters = ["and", "then"]

    sentences = []
    current_sentence = ""
    for word in text.split():
        current_sentence += word + " "
        if any(delimiter in word for delimiter in delimiters):
            sentences.append(current_sentence.strip())
            current_sentence = ""

    if current_sentence:
        sentences.append(current_sentence.strip())

    orders=[]
    for sentence in sentences:
        predicted_labels=loaded_model.predict([sentence])
        print(label_mapping[predicted_labels[0]])
        orders.append(label_mapping[predicted_labels[0]])


    return orders
