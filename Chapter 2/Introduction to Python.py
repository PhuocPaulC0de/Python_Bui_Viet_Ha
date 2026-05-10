#Example 1
print(type(123))
print(type("Ha Noi"))
print(type(3>2))
print(type(2.4))

#Example 2
x = 1.23
y = 2
z = x < 1
t = "123"+"456"
print (type(x))
print (type(y))
print (type(z))
print (type(t))

#Example 3 (equations)
print(5/2)
print(5//2) #kết quả là số nguyên lớn nhất không vượt quá 2.5
print(-3/2)
print(-3//2) #kết quả là số nguyên lớn nhất không vượt quá -1.5
print (3%2) #Toán tử lấy số dư được kí hiệu là mod
print (-3%2)
print (3%-2)
print (4%-6)

#Example 4
x = 2
y = x+3
z = y*2
print (x,y,z)
a = b = c = 14
print (a,b,c)

#Example 5 (reverse the position of 2 variables)
x,y = 1,7
print (x,y)
x,y = y,x #đổi 2 giá trị của biến x, y
print (x,y)
temp = x
x = y
y = temp
print(x,y)

#Example 6
x += 1
y -= x
print (x,y)

#Example 7 (divnmod)
print (divmod(12.5, 2))

#Example 8
x=''' Dù ai nói ngả nói nghiêng
Lòng ta vẫn vững như kiềng ba chân.'''
print (x)

#Exercise 23
sum = ((10+1) * ((10-1)/1+1)) / 2
print (int(sum))

#Exercise 25 (this took me a month to do it)
#Time converter
def convert_time(value, unit):
    # Convert everything to seconds first
    if unit == "s":
        seconds = value
    elif unit == "m":
        seconds = value * 60
    elif unit == "h":
        seconds = value * 3600
    elif unit == "d":
        seconds = value * 86400
    else:
        return "Invalid unit!"

    # Convert to all units
    minutes = seconds / 60
    hours = seconds / 3600
    days = seconds / 86400

    return {
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days
    }


# User input
value = float(input("Enter the time value: "))
unit = input("Enter the unit (s/m/h/d): ").lower()

result = convert_time(value, unit)

if isinstance(result, dict):
    print(f"\nConverted Time:")
    print(f"{result['seconds']} seconds")
    print(f"{result['minutes']} minutes")
    print(f"{result['hours']} hours")
    print(f"{result['days']} days")
else:
    print(result)