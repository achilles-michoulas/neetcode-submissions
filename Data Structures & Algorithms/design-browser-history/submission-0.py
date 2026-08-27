class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.curPage = self.homepage

    def visit(self, url: str) -> None:
        newPage = Node(url)

        self.curPage.next = newPage
        newPage.prev = self.curPage

        self.curPage = newPage

    def back(self, steps: int) -> str:
        while self.curPage.prev and steps > 0:
            self.curPage = self.curPage.prev
            steps -= 1

        return self.curPage.data

    def forward(self, steps: int) -> str:
        while self.curPage.next and steps > 0:
            self.curPage = self.curPage.next
            steps -= 1

        return self.curPage.data

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)