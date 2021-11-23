'''
Design a chat server.

components:

- database to save messages history

hardest problem to solve:
- messages indexing for search
- scaling out the backend, partitioning the users connections between servers
and be able to relay messages to all users in all servers:
-- separate server to accept and save messages, which then signals to all relay servers
to send the message back to all users
-- or make relay servers look for new messages in database on a scheduled interval, like once every 5s + jitter
'''

from datetime import datetime
import bisect

class User:
    def __init__(self, userid: str, username: str):
        self.userid = userid
        self.username = username


class Message:
    def __init__(self, body: str, userid: str, timestamp: datetime):
        self.body = body
        self.timestamp = timestamp
        self.userid = userid

    def __lt__(self, other) -> bool:
        return self.timestamp < other.timestamp


class ChatServer:
    def __init__(self):
        self.users: list[User] = []
        self.messages: list[Message] = []

    def get_messages(self, since: datetime = datetime.now()) -> list[Message]:
        '''Get all messages with timestamp > since'''
        i = bisect.bisect(self.messages, Message('', '', since))
        new_messages = self.messages[i:]
        return new_messages

    def join_server(self, user: User) -> None:
        self.users.append(user)

    def leave_server(self, user: User) -> None:
        self.users.remove(user)

    def send_message(self, message: Message) -> None:
        bisect.insort(self.messages, message)

