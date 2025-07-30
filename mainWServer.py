import webview
import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import threading
from SVGEditAPI import SVGEditAPI

from LocalStorageManager import init_load_storage

# Ruta de tus archivos
html_dir = os.path.abspath("html")
os.chdir(html_dir)

def start_server():
    with TCPServer(("localhost", 8000), SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

threading.Thread(target=start_server, daemon=True).start()

if __name__ == "__main__":

    storageAPI = init_load_storage(html_dir)

    # Crear ventana
    appdata = os.environ.get('APPDATA')
    storage_path = os.path.join(appdata, 'svgpcedit')
    
    window = webview.create_window(
        "SVG Editor", "http://localhost:8000/editor/svg-editor.html", width=1200, height=800, js_api=SVGEditAPI(storageAPI)
    )

    webview.start(storage_path=storage_path,private_mode=False,debug=True)
