#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        if ticket.source == 'NONE':
            route[0] = ticket.destination
        if ticket.source is not 'NONE' and ticket.destination is not 'NONE':
            hash_table_insert(hashtable, ticket.source, ticket.destination)

    for i in range(length - 1):
        route[i + 1] = hash_table_retrieve(hashtable, route[i])

    route[-1] = 'NONE'
    print(route)
    """
    YOUR CODE HERE
    """

    return route
