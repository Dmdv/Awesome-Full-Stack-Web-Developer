# Uses python3
import sys
from operator import attrgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    segment_s = sorted(segments, key= attrgetter('end'))

    while(len(segment_s) > 0):

        remaining_segments = []
        first_leave = segment_s[0].end
        points.append(first_leave)

        for s in segment_s:
            if not (first_leave >= s.start and first_leave <= s.end):
               remaining_segments.append(s)
        segment_s = remaining_segments
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
