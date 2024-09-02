
def add(phone_book,num, name):
    phone_book[num] = name

def delete(phone_book, num):
    if phone_book.get(num) != None:
        del(phone_book[num])

def find(phone_book , num):
    print(phone_book.get(num, "not found"))
    

def phone_book_manager(phone_book , queries):
    for query in queries:
        if query[0] == 'add':
            add(phone_book, query[1],query[2])
        elif query[0] == 'del':
            delete(phone_book, query[1])
        elif query[0] == 'find':
            find(phone_book, query[1])

def main():
    n = int(input("Number of queries : "))
    phone_book = {}
    query_lines = []
    print("Input queries : ")
    for i in range(n):
        query_lines.append(input().split())
    print("Output : ")
    phone_book_manager(phone_book,query_lines)

if __name__ == '__main__':
    main()
