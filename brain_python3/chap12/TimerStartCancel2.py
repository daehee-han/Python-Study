import threading

count = 0

def on_timer():
    global count
    count += 1
    print(count)

    if count < 10:
        timer = threading.Timer(1, on_timer)
        timer.start()
    else:
        print("Canceling timer...")

print("Starting timer...")
on_timer()