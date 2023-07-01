def push_count():
    import RPi.GPIO as GPIO
    from time import sleep

    GPIO.setmode(GPIO.BOARD)
    pin = 10
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING, bouncetime = 500)
    count = 0
    prev_input = False

    while True:
        event = GPIO.event_detected(pin)
        if event == True:
            count +=1
            print(count)
            sleep(1)
            if count == 2:
                break
        elif count == 1 and event == False:
            print(count)
            break

    GPIO.cleanup()

    print("Push-button was pressed", count, "time(s)")
    return count
