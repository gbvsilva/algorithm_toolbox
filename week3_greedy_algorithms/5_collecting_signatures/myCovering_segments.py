# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    #write your code here
    
    points = []
    start = segments[0].start
    end = segments[0].end
    for i in range(1, len(segments)):
        #if segments[i].start < interval['start']:
        #if segments[i].end <: 
        if segments[i].end < end:
            end = segments[i].end
        if segments[i].start > end:
            points.append(end)
            start = segments[i].start
            end = segments[i].end     
    points.append(end)
    return points
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(sorted(segments))
    print(len(points))
    for p in points:
        print(p, end=' ')
