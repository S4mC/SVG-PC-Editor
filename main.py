# nuitka --msvc=latest --onefile --onefile-cache-mode=cached --windows-console-mode=disable --windows-icon-from-ico=icon.ico --include-data-dir="html=html" --onefile-tempdir-spec="%CACHE_DIR%\SVG-PC-Editor\Cache" "main.py"

import webview
import os
import sys

from SVGEditAPI import SVGEditAPI

# Construir la ruta al archivo HTML relativa al script
def get_html_path():
    # Carpeta donde está el ejecutable o script
    if getattr(sys, 'frozen', False):
        # Si no existe, buscar en Program Data
        cache_dir = os.environ.get("CACHE_DIR")
        program_data_html = os.path.join(cache_dir, "SVG-PC-Editor", "Cache", "html", "editor", "svg-editor.html")
        return program_data_html
    else:
        # Script en desarrollo
        app_dir = os.path.dirname(os.path.abspath(__file__))
        # Primero buscar en la carpeta actual
        local_html = os.path.join(app_dir, "html", "editor", "svg-editor.html")
        return local_html

html_path = get_html_path()

class SVGEditor():
    def __init__(self, svgToEdit=None, private_mode=False, callback_funct=None, start_main=True):
        self.svgToEdit = svgToEdit
        self.callback_funct = callback_funct
        
        self.window = webview.create_window(
            "SVG Editor", f"file://{html_path}", width=1200, height=800, js_api=SVGEditAPI(self.final_svg)
        )
        self.window.events.loaded += self.open_svg_to_edit
        self.window.events.before_closing = self.before_closing
        
        if (start_main):
            webview.start(debug=True, private_mode=private_mode)
    
    def destroy(self):
        self.window.destroy()

    def open_svg_to_edit(self):
        if (self.svgToEdit):
            # Edit the svg only works before make a better html
            self.window.dispatch_custom_event("openThisSVG", {"svg": self.svgToEdit})

    def before_closing(self):
        # We call the beforeClosing event to save the current configuration and the SVG. This function also calls final_svg.
        self.window.dispatch_custom_event("beforeClosing")

    def final_svg(self, svgContentHtml):
        if (self.callback_funct):
            self.callback_funct(svgContentHtml)

if __name__ == "__main__":
    SVGEditor()