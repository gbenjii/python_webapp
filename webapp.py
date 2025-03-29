import webview
import requests

def check_url():
    try:
        response = requests.get("https://example.com", timeout=5)
        if response.status_code != 200:
            show_error()
    except Exception:
        show_error()

def show_error():
    window.load_html(
        """
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        font-size: 48px;
        color: red;
        font-weight: bold;
    ">
        Az oldal betöltése nem sikerült<br>ERROR
    </div>
    """
    )

window = webview.create_window(
    "WebAlkalmazás",
    "https://example.com",
    maximized=True
)

webview.start(check_url)
