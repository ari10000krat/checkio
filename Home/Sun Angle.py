from typing import Union

# def sun_angle(time):
#     # 12 hours - 180 degrees -> 1 hour === 15 degrees
#     # 60 minutes - 15 degrees -> 1 minute === 0.25 degrees
#     return ((int(time[:2])-6)*15 + int(time[3:])*0.25) if int(time.replace(':', '')) in range(600, 1801)

def sun_angle(time: str) -> Union[int, str]:
    if "06:00" <= time <= "18:00":
        hours, minuts = map(int,time.split(":"))
        # if 6 <= hours < 18 :
        hours -= 6  # Count of hours from the sunrise
        hourCoefficient = 90 / 6  # Count of grads in hour
        minutCoefficient = hourCoefficient / 60  # Count of grads in hour
        return hours * hourCoefficient + minuts * minutCoefficient
    else:
        return "I don't see the sun!"



if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
