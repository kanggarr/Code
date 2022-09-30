while True:
    outlook, humidity, windy = input().split()

    if outlook == 'cloudy':
        print("play")

    elif outlook == 'sunny':
        if int(humidity) <= 75:
            print("play")
        else:
            print("not play")
    elif outlook == 'rainy':
        if windy == 't' or windy == 'true':
            print("not play")
        else:
            print("play")

    else:
        print("Invalid outlook. Please try again.")
