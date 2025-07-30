import os

localStorageOverwrite = """
(function() {
    const originalSetItem = localStorage.setItem;
    const originalRemoveItem = localStorage.removeItem;

    localStorage.setItem = function(key, value) {
        originalSetItem.call(this, key, value);
        notificarCambio();
    };

    localStorage.removeItem = function(key) {
        originalRemoveItem.call(this, key);
        notificarCambio();
    };

    function notificarCambio() {
        const data = {...localStorage};
        pywebview.api.storageAPI.save_localStorage(data);
    }
})();"""

class APIStorageManager:
    def __init__(self, js_path, overwrite):
        self.storage_file = js_path
        self.overwrite = overwrite

    def save_localStorage(self, data):
        try:
            # Plantilla de código JS
            script_content = f"""const datos = {data};

localStorage.clear();
for (const clave in datos) {{
    localStorage.setItem(clave, datos[clave]);
}}"""
            if (self.overwrite):
                script_content += localStorageOverwrite

            with open(self.storage_file, "w", encoding="utf-8") as f:
                f.write(script_content)
            print(f"localStorage guardado en: {self.storage_file}")
        except Exception as e:
            print(f"Error al guardar localStorage: {e}")


def init_load_storage(main_html_path, js_name="LocalStorageSave", overwrite = True):
    """This function create a js_file that have the local storage in the same folder that main_html with the name js_name"""
    # Pre-cargar y restaurar localStorage ANTES de crear la ventana
    js_path = os.path.join(os.path.dirname(main_html_path), f"{js_name}.js")
    if overwrite and not os.path.exists(js_path):
        with open(js_path, "w") as js_file:
            js_file.write(localStorageOverwrite)
    return APIStorageManager(js_path, overwrite)
