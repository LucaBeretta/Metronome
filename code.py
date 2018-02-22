#First implement
import time
timesig = int(input("Time Sign: "))
bpmin = int(input("BPM: "))

def main(bpm = bpmin, bpb = timesig):
    sleep = 60.0 / bpm
    counter = 0
    while True:
        counter += 1
        if counter % bpb:
            print ('tick')
        else:
            print ('TICK')
        time.sleep(sleep)

main()

