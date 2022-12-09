class SessionManager(object):
    def __init__(self):
        self._sessions = []

    def __len__(self) -> int:
        return len(self._sessions)

    def __contains__(self, item) -> bool:
        return item in self._sessions

    def __getitem__(self, key):
        return self._sessions[key]

    def __setitem__(self, key, value):
        self._sessions[key] = value

    def __delitem__(self, key):
        del self._sessions[key]

    def append(self, value):
        self._sessions.append(value)
    
    def remove(self, value):
        self._sessions.remove(value)