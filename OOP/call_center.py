'''
Imagine you have a call center with three levels of employees: respondent, manager, and director.
An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't
handle the call, he or she must escalate the call to a manager. If the manager is not free or not able
to handle it, then the call should be escalated to a director. Design the classes and data structures
for this problem. Implement a method dispatchCall() which assigns a call to the first available employee.

questions:

- free / not able to handle is the same thing?
'''

from collections import namedtuple
from queue import Queue
import heapq

Call = namedtuple('Call', 'caller')

class CallHandler:
    pass

class CallHandler:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority
        self.available = True

    def handle_call(self, call: Call) -> None:
        print(f'Hello {call.caller}, {self.name} speaking')

    def __lt__(self, other: CallHandler) -> bool:
        return self.priority < other.priority


class Respondent(CallHandler):
    def __init__(self, name: str):
        super().__init__(name, 1)

    def handle_call(self, call: Call) -> None:
        super().handle_call(call)
        print('I am a respondent')


class Manager(CallHandler):
    def __init__(self, name: str):
        super().__init__(name, 10)

    def handle_call(self, call: Call) -> None:
        super().handle_call(call)
        print('I am a manager')


class Director(CallHandler):
    def __init__(self, name: str):
        super().__init__(name, 100)

    def handle_call(self, call: Call) -> None:
        super().handle_call(call)
        print('I am a director')


class CallCenter:
    def __init__(self, respondents_count: int = 10):
        self.call_queue = Queue(25)
        self.employees = []
        for i in range(respondents_count):
            heapq.heappush(self.employees, Respondent('respondent_'+str(i)))

        heapq.heappush(self.employees, Manager('Joe'))
        heapq.heappush(self.employees, Director('Mark'))

    def handle_call(self) -> CallHandler:
        if self.call_queue.empty():
            return

        if not len(self.employees):
            print('No employees available to handle a call, please wait')
            return None

        current_call = self.call_queue.get(False)
        handler = heapq.heappop(self.employees)
        handler.handle_call(current_call)
        return handler

    def dispatch_call(self, call: Call) -> None:
        print('dispatching a call')
        if self.call_queue.full():
            print('Call queue is full, please call again later')
            return

        self.call_queue.put(call, block=False)
        print('dispatching a call done')

    def finish_call(self, employee: CallHandler) -> None:
        heapq.heappush(self.employees, employee)


if __name__ == '__main__':
    print('starting dispatching')
    callcenter = CallCenter()
    for i in range(50):
        print(i)
        callcenter.dispatch_call(Call('caller_'+str(i)))

    for i in range(50):
        e = callcenter.handle_call()
        if e and i%3 == 0:
            callcenter.finish_call(e)
