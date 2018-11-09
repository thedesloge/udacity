connections = []
imported_list = ["John is connected to Bryant, Debra, Walter."]
person = ""
connections_string = ""
cleaned_list = []
for element in imported_list:
    #print(person, connections_string, cleaned_list)
    print(element)
    person, connections_string = element.split(" is connected to ")
    connections = connections_string.split(",")
    #print(person, connections_string, cleaned_list)
    for connection in connections:
        cleaned_list.append(connection.strip())
        #print(person, connections_string, cleaned_list)
graph = [person.strip(), cleaned_list]
print(graph)
