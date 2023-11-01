import autoit
import time

def openGoogleChromeIncognito():
    autoit.run('chrome.exe --incognito')
    time.sleep(5)

def openGoogleChromeProfile():
    autoit.run('chrome.exe --profile-directory="ProfileName"')
    time.sleep(5)



# Function to retrieve URLs of open Chrome windows
def get_chrome_window_urls():
    open_window_urls = []
    window_list = autoit.win_get_list("[CLASS:Chrome_WidgetWin_1]")

    for window in window_list:
        autoit.win_activate(window)
        url = autoit.control_command("Chrome_RenderWidgetHostHWND1", "", "Afx Chrome", "ControlGetText", "", "")
        if url.startswith("http"):
            open_window_urls.append(url)

    return open_window_urls

# Function to navigate to a specific URL in the active Chrome window
def navigate_to_url(url):
    autoit.send("^t")  # Open a new tab
    autoit.send(url)
    autoit.send("{ENTER}")


def click_button_on_webpage(x, y):
    # Simulate a left-click at the specified screen coordinates
    autoit.mouse_click("left", x, y, 1)














