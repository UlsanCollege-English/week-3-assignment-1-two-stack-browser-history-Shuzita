# src/history.py

class BrowserHistory:
    def __init__(self, start="home"):
        # current page starts at "home", but NOT in history
        self.cur = start
        self.back_stack = []
        self.fwd_stack = []

    def visit(self, url):
        # push current only if it's not the initial "home"
        if self.cur != "home" or self.back_stack or self.fwd_stack:
            self.back_stack.append(self.cur)
        self.cur = url
        self.fwd_stack.clear()

    def back(self):
        if not self.back_stack:
            raise IndexError("No pages in back history")
        self.fwd_stack.append(self.cur)
        self.cur = self.back_stack.pop()
        return self.cur

    def forward(self):
        if not self.fwd_stack:
            raise IndexError("No pages in forward history")
        self.back_stack.append(self.cur)
        self.cur = self.fwd_stack.pop()
        return self.cur

    def current(self):
        return self.cur


# quick demo (not part of tests, just for manual run)
if __name__ == "__main__":
    h = BrowserHistory()
    print("Start:", h.current())   # home
    h.visit("a"); h.visit("b"); h.visit("c")
    print("Back:", h.back())       # b
    print("Back:", h.back())       # a
    try:
        print("Back again:", h.back())  # should raise IndexError
    except IndexError as e:
        print("Error:", e)
    h.visit("x")
    try:
        print("Forward:", h.forward())  # should raise IndexError
    except IndexError as e:
        print("Error:", e)
