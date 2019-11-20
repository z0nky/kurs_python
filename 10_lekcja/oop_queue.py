class Queue:

    def __init__(self, elements):
        self.elements = elements

    def __str__(self):  # nadpisuje informacje jeśli zrobimy print tylko obiektu klasy. Zamiast miejsca w pamieci bedzie wyswietlac to co return
        return "-".join(self.elements)

    # def show_queue(self):
    #     print(self.elements)

    def check_length(self):
        if len(self.elements) > 0:
            print('There are', len(self.elements), 'elements in queue')
        else:
            print("No elements in queue")

    def get(self):
        if len(self.elements) == 0:
            return 'No more elements to take away you greedy creature!'
        else:
            return (self.elements.pop(0) + ' removed')

    def put(self):
        addin = newcomer
        return self.elements.append(addin)


list_elem = ["a", "b", "c", "d"]
queue1 = Queue(list_elem)
newcomer = "Z"

# try:
#     type(list_elem) = list
#
# except TypeError as err:
#     result_er = "Error" + str(err)

#print(queue1.elements)
print(queue1)
Queue.check_length(queue1)
print("First out is", queue1.get())
# print("Added", queue1.put(), "to the queue. Result:", queue1)
queue1.put()
print(queue1)
print(queue1.get())
print(queue1.get())
print(queue1.get())
print(queue1.get())
print(queue1.get())
