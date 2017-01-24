import json
from tkinter import *

fname = 'suggested-topics.json'

# Add a object to the schedule
def writeNewTopic(topic):
    with open(fname) as jsonTopics:
        topics = json.load(jsonTopics)

        topics.append(topic)

    with open(fname, 'w') as jsonTopics:
        json.dump(topics, jsonTopics, indent=4)

    print(json.dumps(topic))
    print("Was added")

def nextField():
    global i
    i+=1
    extraField()

def extraField():
    global extra
    global moveOn
    global i
    global labels

    extra.pack_forget()
    moveOn.pack_forget()
    add.pack_forget()
    addEntry()
    extra["text"] = "Add another " + labels[i].rstrip('s')
    extra.pack(pady=5)
    if(i+1 < len(labels)):
        moveOn["text"] = "Add " + labels[i+1]
        moveOn.pack(pady=5)
    else:
        add.pack()

def addEntry():
    global labels
    global i
    global entries

    Label(text=labels[i].rstrip('s')).pack(side="top", anchor="w")
    e = Entry(width=100)
    e.pack()
    Frame(height=2, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)
    if(i > 1):
        entries[i].append(e)
    else:
        entries[i] = e

def submitTopic():
    global entries
    global master
    global labels
    newTopic = {}
    leng = len(labels)
    for i in range(leng):
        if(isinstance(entries[i], list)):
            toAdd = []
            for e in entries[i]:
                toAdd.append(e.get())
            newTopic[labels[i]] = toAdd
        else:
            newTopic[labels[i]] = entries[i].get()
    writeNewTopic(newTopic)
    master.destroy()






labels = ["topic", "excerpt", "tags", "references", "see-also"]
i = 0
entries = [None, None, [], [], []]
master = Tk()

extra = Button(master, text="Add another " + labels[2].rstrip('s'), command=lambda: extraField())
moveOn = Button(master, text="Add " + labels[3], command=lambda: nextField())
add = Button(master, text="Submit Topic", command=lambda: submitTopic())

while(i < 3):
    addEntry()
    i+=1

i = 2

extra.pack(pady=5)
moveOn.pack(pady=5)



mainloop()




