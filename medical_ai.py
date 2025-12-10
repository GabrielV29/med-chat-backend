def medical_ai_response(user_text: str) -> str:
    text = user_text.lower()

    #Ejemplos de reglas simples
    if "dolor" in text and "cabeza" in text:
        return(
            "Parece que presentas un dolor de cabeza. "
            "Si es reciente, hidrátate, descansa y evita pantallas. "
            "Si el dolor persiste más de 24 horas, es muy intenso o se acompaña de vómito o visión borrosa, busca atención médica."
        )
    if "fiebre" in text:
        return(
            "La fiebre puede deberse a infecciones virales o bacterianas. "
            "Controla la temperatura, mantente hidratado y consulta si supera los 38.5°C por más de 48 horas."
        )
    if "tos" in text:
        return(
            "La tos es un síntoma común de infecciones respiratorias. "
            "Si es seca podría ser viral, si es con flema puede indicar infección bacteriana. "
            "Consulta si tienes dificultad para respirar o persiste más de una semana."
        )
    # Respuesta por defecto
    return "Puedo darte una orientación general. Cuéntame más sobre tus síntomas o desde cuándo los sientes."