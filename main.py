import webview
import os
import time

from SVGEditAPI import SVGEditAPI
from LocalStorageManager import init_load_storage

# Todo: Allow export button
# Todo: Add the name of the file open for default if exist in save, Review: added save with pywebview api..

if __name__ == "__main__":
    html_path = os.path.abspath("html/editor/svg-editor.html")
    
    storageAPI = init_load_storage(html_path, overwrite=False)
    
    # Crear ventana
    appdata = os.environ.get('APPDATA')
    storage_path = os.path.join(appdata, 'svgpcedit')
    
    window = webview.create_window(
        "SVG Editor", f"file://{html_path}", width=1200, height=800, js_api=SVGEditAPI(storageAPI)
    )

    webview.start(debug=True)
