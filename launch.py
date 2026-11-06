import threading, webbrowser
from app import app
threading.Timer(1.5, lambda: webbrowser.open('http://127.0.0.1:5103/')).start()
print('Open in browser: http://127.0.0.1:5103/')
print('Press Ctrl+C in this window to stop the application.')
app.run(host='127.0.0.1', port=5103, debug=False, use_reloader=False)
