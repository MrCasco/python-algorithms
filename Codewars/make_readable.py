# Given n seconds, convert it to human readable time. Ex: '00:01:55'

# BEST SOLUTION
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

# MY SOLUTION
def make_readable(seconds):
    h = seconds//3600
    m = (seconds-(h*3600))//60
    s = (seconds-(m*60))%60
    x = lambda a: '0'+str(a) if len(str(a)) == 1 else str(a)
    return '{}:{}:{}'.format(x(h), x(m), x(s))
