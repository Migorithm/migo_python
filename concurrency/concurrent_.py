import concurrent.futures

def worker_process(i):
    return i * i # square the argument

def main():
    lst = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(worker_process, i) for i in range(10)]
        for future in concurrent.futures.as_completed(futures):
            lst.append(future.result())
    print(lst)
if __name__ =="__main__":
    main()