while True:

    outlook, humidity, windy = input(
        "Input outlook ('sunny' or 'cloudy' or 'windy'), humidity (integer), and windy ('true' or 'false'): ").split()

    humidity = int(humidity)
    print(outlook, humidity, windy)

    if outlook == 'sunny':
        if humidity <= 75:
            print('play')
        else:
            print('not play')
    elif outlook == 'cloudy':
        print('play')
    elif windy == 'true':
        print('play')
    else:
        print('not play')
