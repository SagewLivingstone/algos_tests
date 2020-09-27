from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'

def find_seller(graph):
    search_queue = deque()
    search_queue += graph['you']

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f"{person} is a seller!")
            return True
        else:
            search_queue += graph[person]

def main():
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'johnny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['johnny'] = []

    find_seller(graph)

if __name__ == '__main__':
    main()
