def download_time(file_size, units_file, bandwidth, units_bandwindth):
    
    def inb(units):
        if units == "kb":
            return 2 ** 10
        elif units == "kB":
            return 2 ** 10 * 8
        elif units == "Mb":
            return 2 ** 20
        elif units == "MB":
            return 2 ** 20 * 8
        elif units == "Gb":
            return 2 ** 30
        elif units == "GB":
            return 2 ** 30 * 8
        elif units == "Tb":
            return 2 ** 40
        elif units == "TB":
            return 2 ** 40 * 8
        else:
            return 1
    
    hours = 0
    minutes = 0
    seconds = 0
    
    time = 0
    
    file_size_in_b = file_size * inb(units_file)
    bandwidth_in_b = bandwidth * inb(units_bandwindth)
    time = float(file_size_in_b)/bandwidth_in_b
    
    if time - int(time) == 0:
        time = int(time)
    
    hours_str = " hours, "
    minutes_str = " minutes, "
    seconds_str = " seconds"
    
    hours = int(time)/3600
    minutes = (int(time)%3600)/60
    seconds = time - hours*3600 - minutes*60
    
    if hours == 1:
        hours_str = " hour, "
    
    if minutes == 1:
        minutes_str = " minute, "
    
    if seconds == 1:
        seconds_str = " second"
        
    return str(hours) + hours_str + str(minutes) + minutes_str + str(seconds) + seconds_str



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
