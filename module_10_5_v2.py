import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data += line
            if line == "":
                break
        file.close()


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

'''Линейный вызов'''
start = datetime.datetime.now()
for name in filenames:
    read_info(name)
end = datetime.datetime.now()
print(end - start)
'''время выполнения: 0:00:10.985214'''


'''Многопроцессный'''
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
'''время выполнения: 0:00:04.079093'''



