def convert_seconds(seconds):
    hours = 0
    minutes = 0
    sec =0
    
    hours_str = " hours, "
    minutes_str = " minutes, "
    sec_str = " seconds"
    
    hours = int(seconds)/3600
    minutes = (int(seconds)%3600)/60
    sec = seconds - hours*3600 - minutes*60
    
    if hours == 1:
        hours_str = " hour, "
    
    if minutes == 1:
        minutes_str = " minute, "
    
    if sec == 1:
        sec_str = " second"
    
    return str(hours) + hours_str + str(minutes) + minutes_str + str(sec) + sec_str

