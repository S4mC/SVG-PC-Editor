
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
})();