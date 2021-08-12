from math import fabs


def solution(args: list):
    result_list = list()
    for num in range(len(args)):
        if args[num] - args[num+1] == 1 or args[num] - args[num+1] == -1:
            temporary_list = list()
            temporary_list.append(args[num])
            for num_1 in range(num, len(args)):
                num_1 += 1
                print(args[num_1])
                if num_1 == 19:
                    result_list.append(f"{temporary_list[:1][0]}{'-'}{temporary_list[-1:][0]}")
                    return result_list
                if args[num_1] - args[num_1+1] == -1 or args[num_1] - args[num_1+1] == 1:
                    temporary_list.append(args[num_1])
                    temporary_list.append(args[num_1+1])
                    num_1 += 1
                else:
                    if len(temporary_list) <= 2:
                        for i in temporary_list:
                            result_list.append(i)
                            num_1 += 1
                    else:
                        temporary_list = set(temporary_list)
                        temporary_list = sorted(list(temporary_list))
                        result_list.append(f"{temporary_list[:1][0]}{'-'}{temporary_list[-1:][0]}")
                        temporary_list.clear()
        else:
            result_list.append(args[num])
    return result_list


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))


def format_duration(seconds):
    hours = 0
    minutes = 0
    while seconds > 1:
        if seconds / 3600 >= 1:
            seconds -= 3600
            hours += 1
        elif seconds / 60 >= 1:
            seconds -= 60
            minutes += 1
        else:
            break
    print(hours, minutes, seconds)
    if hours > 0 and minutes > 0 and seconds > 0:
        return f"{hours} hour{'s' * ((hours - 1)//(hours-1))}, {minutes} minute{'s' * ((minutes - 1)//(minutes-1))}, {seconds} second{'s' * ((seconds - 1)//(seconds-1))}"
    elif hours <= 0 and minutes > 0 and seconds > 0:
        return f"{minutes} minute{'s' * ((minutes - 1)//(minutes-1))}, {seconds} second{'s' * ((seconds - 1)//(seconds-1))}"
    elif hours <= 0 and minutes <= 0 and seconds > 0:
        return f"{seconds} second{'s' * ((seconds - 1)//(seconds-1))}"
    elif


print(format_duration(3237))