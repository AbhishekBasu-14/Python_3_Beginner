# cook your dish here
T= int(input())
for i in range(T):
    finish, distancetoBolt, tigerAcceleration, boltSpeed = map(int, input().split()) #respective value assignemnt
    total_dist=finish+distancetoBolt
    tiger_time= pow(2*(total_dist/tigerAcceleration),1/2) #initial velocity is zero
    bolt_time= finish/boltSpeed
    if tiger_time <= bolt_time:
        print("Tiger")
    else:
        print("Bolt")
    
    
