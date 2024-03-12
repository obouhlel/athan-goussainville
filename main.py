from times import get_times

def main():
    times = get_times()
    if times is None:
        print("Times not found")
        exit()
    print(times)

if __name__ == "__main__":
    main()