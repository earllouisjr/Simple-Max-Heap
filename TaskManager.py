class Entry:
    """Represents an entry in the priority queue."""

    def __init__(self, priority, process_id):
        """Initializes an Entry object with a given priority and process ID."""
        self.priority = priority
        self.process_id = process_id

    def __repr__(self):
        """Returns a string representation of the Entry object."""
        return f"Entry(priority={self.priority}, process_id={self.process_id})"

    ####### Implement all Entry class methods under this line #######
    def __gt__(self, other):
        """Compares the priority of this entry with another entry.
        Returns:bool: True if this entry has higher priority than the other, False otherwise."""
        return self.priority > other.priority
    
    def __eq__(self, other):
        """Checks if this entry is equal to another entry based on priority.
        Returns:bool: True if the priorities are equal, False otherwise."""
        return self.priority == other.priority
        
class MaxHeap:
    """Represents a max heap data structure."""

    def __init__(self):
        """Initializes a MaxHeap object."""
        self._heap = []

    ####### Implement all MaxHeap class methods under this line #######    
    def put(self, entry):
        """Inserts an entry into the max heap."""
        self._heap.append(entry)
        self._upheap(len(self._heap) - 1)

    def remove_max(self):
        """Removes and returns the entry with the maximum priority from the max heap.
        Returns:The process ID that was removed from the queue. raise IndexError if the heap is empty"""
        if len(self._heap) == 0:
                raise IndexError
        if len(self._heap) == 1:
            return self._heap.pop().process_id
        max = self._heap[0]
        last_entry = self._heap.pop()
        self._heap[0] = last_entry
        self._downheap(0)
        return max.process_id
        
    

    def change_priority(self, process_id, new_priority):
        """Changes the priority of a process in the max heap.
        Returns:bool: True if the priority change was successful, False otherwise."""
        for entry in self._heap:
            if entry.process_id == process_id:
                old_priority = entry.priority
                entry.priority = new_priority
                if new_priority > old_priority:
                    self._upheap(self._heap.index(entry))
                else:
                    self._downheap(self._heap.index(entry))
                return True
        return False

    def _upheap(self, index):
        """Performs up-heap operation to maintain heap property after insertion."""
        i = index
        p = (i-1)//2
        if i > 0 and self._heap[i] > self._heap[p]:
            self._heap[p], self._heap[i] = self._heap[i], self._heap[p]
            self._upheap(p)

    def _downheap(self, index):
        """Performs down-heap operation to maintain heap property after removal."""
        left = 2 * index + 1
        right = 2 * index + 2
        max = index
        if left < len(self._heap) and self._heap[left] > self._heap[max]:
            max = left
        if right < len(self._heap) and self._heap[right] > self._heap[max]:
            max = right
        if max != index:
            self._heap[index], self._heap[max] = self._heap[max], self._heap[index]
            self._downheap(max)

    def __len__(self):
        """len is number of items in PQ"""
        return len(self._heap)          

class TaskManager:
    """Manages the execution of processes using a priority queue."""

    def __init__(self):
        """Initializes a TaskManager object."""
        self.processor_queue = MaxHeap()
    
    ####### Implement all TaskManager class methods under this line #######
    def add_process(self, entry):
        """Adds a process to the processor queue."""
        self.processor_queue.put(entry)

    def remove_process(self):
        """Removes and returns the process with the highest priority from the processor queue."""
        return self.processor_queue.remove_max()


if __name__ =='__main__':
    entry1 = Entry(priority=5, process_id="Process 1")     
    entry2 = Entry(priority=3, process_id="Process 2")     
    entry3 = Entry(priority=7, process_id="Process 3")     
    entry4 = Entry(priority=8, process_id="Process 4")     
    entry5 = Entry(priority=2, process_id="Process 5")     
    entry6 = Entry(priority=6, process_id="Process 6")     
    entry7 = Entry(priority=4, process_id="Process 7")      
    max_heap = MaxHeap()     
    max_heap.put(entry1)      
    max_heap.put(entry2)     
    max_heap.put(entry3)     
    max_heap.put(entry4)
    max_heap.put(entry5)     
    max_heap.put(entry6)     
    max_heap.put(entry7)     
    max_heap.change_priority(process_id="Process 1", new_priority=10) 
    max_heap.change_priority(process_id="Process 3", new_priority=1) 
    while max_heap:          
        print(f"Removing max priority process: {max_heap.remove_max()}") 
        # Expected output: 
        # Removing max priority process: Process 1 
        # Removing max priority process: Process 4 
        # Removing max priority process: Process 6 
        # Removing max priority process: Process 7 
        # Removing max priority process: Process 2 
        # Removing max priority process: Process 5 
        # Removing max priority process: Process 3