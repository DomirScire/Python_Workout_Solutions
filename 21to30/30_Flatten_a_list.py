# DomirScire

def flatten(mylist):
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist]

if __name__ == "__main__":
    print(flatten([[1,2],[3,4]]))
