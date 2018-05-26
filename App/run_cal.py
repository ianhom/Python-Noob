while True:
    distance = input("Please input the kms: ")
    mins     = input("Please input the minuts: ")
    secs     = input("Please input the seconds: ")

    min_temp = (mins+secs/60.00)

    speed = 60.00*distance/min_temp
    pace  = min_temp/distance
    r_min = int(pace)
    r_sec = int((pace - r_min)*60)

    
    print
    print "Your average speed is %.2f km/H " % (speed)
    print "Your average pace is %d\"%d' per km " % (r_min,r_sec)
    print
