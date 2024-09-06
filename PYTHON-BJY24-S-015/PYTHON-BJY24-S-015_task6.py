temp=int(input("enter the temperature : "));
humidity=int(input("enter the humidity : "));

if temp>=20:
    if humidity<=50:
        print("weather is good");
    else:
        print("weather is not good");

else:
    print("weather is not good");