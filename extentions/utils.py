from . import jalaly
from django.utils import timezone

def number_conventor(mystr):
    number = {
        "0":"0",
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9"
    }
    for e,p in number.items():
        mystr = mystr.replace(e,p)
    return mystr


def jalali_converted(time):
    list_of_mouth = ["فروردین","بهار",
	"اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر",	
    "پاییز","آبان","آذر","دی","بهمن","اسفند"]
    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple = jalaly.Gregorian(time_to_str).persian_tuple()
    time_to_list=list(time_to_tuple)
    for index,str in enumerate(list_of_mouth):
        if index==time_to_list[1]+1:
            time_to_list[1]=str
            break
    output = "{}:{} {}\{}\{} ".format(time.hour,time.minute,time_to_list[0],time_to_list[1],time_to_list[2])
    return number_conventor(output)