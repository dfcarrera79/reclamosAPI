def deducir_mensaje_error(o_error):
    mensaje = ""
    hubo = False
    
    if hasattr(o_error, 'message') and o_error.message:
        mensaje = (
            "La aplicación no logra conectarse con el servidor, revise si su dispositivo esta con internet o si el servidor esta disponible."
            if o_error.message == "Network Error"
            else o_error.message
        )
        hubo = True
    
    if hasattr(o_error, 'config') and hasattr(o_error.config, 'url') and o_error.config.url:
        mensaje += f"<br><span style='color:red'>{o_error.config.url}</span>"
        hubo = True
    
    if not hubo:
        import json
        mensaje = json.dumps(o_error)
    
    return mensaje
