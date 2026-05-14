from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

VERIFY_TOKEN       = os.getenv("VERIFY_TOKEN", "estatica_vital_token")
PAGE_ACCESS_TOKEN  = os.getenv("PAGE_ACCESS_TOKEN")
IG_ACCOUNT_ID      = os.getenv("IG_ACCOUNT_ID")

# ─── Respuestas por tratamiento ───────────────────────────────────────────────

TRATAMIENTOS = {
    "depilacion": {
        "keywords": ["depilacion","depilación","depilar","laser","láser","vello","pelo","vellito"],
        "gancho": (
            "Tu piel merece sentirse libre, suave y sin preocupaciones — "
            "la depilación definitiva no es un lujo, es calidad de vida. 🌿 "
            "En Estática Vital Salud tenemos el tratamiento ideal para tu tipo de piel y tu tono."
        ),
        "pregunta": (
            "¿En qué zona de tu cuerpo te gustaría empezar y hace cuánto tiempo "
            "estás buscando una solución definitiva?"
        ),
    },
    "facial": {
        "keywords": ["facial","cara","rostro","acne","acné","manchas","limpieza facial","poros","piel"],
        "gancho": (
            "Tu rostro habla antes que tú — y merece brillar con salud real, no solo con filtros. ✨ "
            "En Estática Vital Salud transformamos tu piel desde adentro hacia afuera con protocolos personalizados."
        ),
        "pregunta": (
            "¿Qué es lo que más te preocupa de tu piel en este momento "
            "y desde hace cuánto tiempo tienes ese problema?"
        ),
    },
    "masaje": {
        "keywords": ["masaje","relajacion","relajación","tensión","tension","stress","estrés","dolor","espalda","nuca","contractura"],
        "gancho": (
            "Tu cuerpo acumula todo lo que tu mente no puede procesar — estrés, tensión, cansancio acumulado. 💆 "
            "Un buen masaje no es un capricho, es una necesidad que tu cuerpo lleva tiempo pidiendo."
        ),
        "pregunta": (
            "¿En qué parte de tu cuerpo sientes más tensión y con qué frecuencia aparece ese malestar?"
        ),
    },
    "corporal": {
        "keywords": ["cuerpo","corporal","celulitis","grasa","peso","figura","moldear","reducir","reafirmar","flacidez","abdomen"],
        "gancho": (
            "Tu cuerpo tiene el potencial de transformarse — solo necesita el tratamiento correcto y el equipo adecuado. 💪 "
            "En Estática Vital Salud diseñamos un plan hecho exactamente para ti, no uno genérico."
        ),
        "pregunta": (
            "¿Cuál es esa área de tu cuerpo que más quisieras trabajar "
            "y qué has intentado antes sin ver los resultados que esperabas?"
        ),
    },
    "default": {
        "gancho": (
            "Tu bienestar y tu confianza merecen atención real — no soluciones temporales. 🌱 "
            "En Estática Vital Salud cada tratamiento está diseñado para transformarte de verdad, desde adentro."
        ),
        "pregunta": (
            "¿Cuál es ese problema con tu salud o tu cuerpo que llevas tiempo queriendo resolver "
            "pero no has podido?"
        ),
    },
}

# ─── Helpers ──────────────────────────────────────────────────────────────────

def normalizar(texto):
    reemplazos = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    return texto.lower().translate(reemplazos)


def detectar_tratamiento(texto):
    texto_n = normalizar(texto)
    for tratamiento, data in TRATAMIENTOS.items():
        if tratamiento == "default":
            continue
        for kw in data["keywords"]:
            if normalizar(kw) in texto_n:
                return tratamiento
    return "default"


def obtener_nombre(ig_user_id):
    url = f"https://graph.facebook.com/v19.0/{ig_user_id}"
    resp = requests.get(url, params={"fields": "name", "access_token": PAGE_ACCESS_TOKEN})
    nombre_completo = resp.json().get("name", "")
    return nombre_completo.split()[0] if nombre_completo else "amig@"


def construir_mensaje(nombre, texto_comentario):
    tratamiento = detectar_tratamiento(texto_comentario)
    data = TRATAMIENTOS[tratamiento]
    return (
        f"¡Hola {nombre}! 👋\n\n"
        f"{data['gancho']}\n\n"
        f"✨ {data['pregunta']}"
    )


def enviar_dm(ig_user_id, mensaje):
    url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/messages"
    payload = {
        "recipient":       {"id": ig_user_id},
        "message":         {"text": mensaje},
        "access_token":    PAGE_ACCESS_TOKEN,
    }
    r = requests.post(url, json=payload)
    print(f"[DM] → {ig_user_id} | status {r.status_code} | {r.text}")
    return r.json()


# ─── Webhook ──────────────────────────────────────────────────────────────────

@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    if (request.args.get("hub.mode") == "subscribe"
            and request.args.get("hub.verify_token") == VERIFY_TOKEN):
        return request.args.get("hub.challenge"), 200
    return "Forbidden", 403


@app.route("/webhook", methods=["POST"])
def recibir_webhook():
    data = request.get_json(silent=True) or {}

    if data.get("object") != "instagram":
        return "OK", 200

    for entry in data.get("entry", []):
        for change in entry.get("changes", []):
            if change.get("field") != "comments":
                continue

            comentario   = change.get("value", {})
            commenter_id = comentario.get("from", {}).get("id")
            texto        = comentario.get("text", "")

            if not commenter_id:
                continue

            nombre  = obtener_nombre(commenter_id)
            mensaje = construir_mensaje(nombre, texto)
            enviar_dm(commenter_id, mensaje)

    return "OK", 200


# ─── Inicio ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(port=5000, debug=True)
