import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        # Create navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.setStatusTip("Forward to next page")
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        nav_bar.addWidget(self.url_bar)

        search_btn = QAction("Search", self)
        search_btn.setStatusTip("Search Google")
        search_btn.triggered.connect(self.search)
        nav_bar.addAction(search_btn)

        self.browser.urlChanged.connect(self.update_urlbar)

        # Set the central widget
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle("Web Browser")
        self.show()

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def search(self):
        search_query = self.url_bar.text()
        q = QUrl("https://www.google.com/search?q=" + search_query)
        self.browser.setUrl(q)

def main():
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("Web Browser")
    window = WebBrowser()
    app.exec_()

if __name__ == "__main__":
    main()
