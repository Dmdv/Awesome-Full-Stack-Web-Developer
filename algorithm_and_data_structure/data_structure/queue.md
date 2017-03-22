<!--
@Author: Anas Aboureada <anas>
@Date:   Mon, 20th Mar 2017, T 19:01 +01:00
@Email:  me@anasaboureada.com
@Last modified by:   anas
@Last modified time: Mon, 20th Mar 2017, T 19:03 +01:00
@License: MIT License
@Copyright: Copyright (c) 2017 Anas Aboureada <me@anasaboureada.com>
-->

# Queue

## Resources:

-   [Using Queues First-In First-Out(video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Using-queues-first-first-out/149042/177122-4.html)
-   [Queue (video)](https://www.coursera.org/learn/data-structures/lecture/EShpq/queue)
-   [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)
-   [Priority Queues (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Priority-queues-deques/149042/177123-4.html)

## TODO:

-   Implement using linked-list, with tail pointer:

    -   enqueue(value) - adds value at position at tail
    -   dequeue() - returns value and removes least recently added element (front)
    -   empty()

-   Implement using fixed-sized array:

    -   enqueue(value) - adds item at end of available storage
    -   dequeue() - returns value and removes least recently added element
    -   empty()
    -   full()

### Cost:

-   a bad implementation using linked list where you enqueue at head and dequeue at tail would be O(n)
      because you'd need the next to last element, causing a full traversal each dequeue
-   enqueue: O(1) (amortized, linked list and array [probing])
-   dequeue: O(1) (linked list and array)
-   empty: O(1) (linked list and array)
