import openai

# Configura las credenciales de la API de OpenAI
openai.api_key = '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'

def generar_respuesta_a_pregunta(pregunta):
    # Combina la pregunta con un prompt para generar una respuesta
    prompt = f"Pregunta: {pregunta}\nRespuesta:"
    
    # Realiza una solicitud de generación de texto utilizando el modelo GPT-3.5-turbo
    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        organization='org-NfFDyiyu60gn1aSgTTdpQRyj',
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Extrae y devuelve el contenido de la respuesta generada
    respuesta_generada = response['choices'][0]['message']['content']
    return respuesta_generada

# Loop interactivo para hacer preguntas y obtener respuestas
print("¡Bienvenido al chat con GPT-3!")
print("Puedes escribir 'salir' para terminar la conversación.")

while True:
    # Pide al usuario que haga una pregunta
    pregunta_usuario = input("Tú: ")
    
    # Verifica si el usuario quiere salir
    if pregunta_usuario.lower() == 'salir':
        print("Hasta luego. ¡Espero que hayas tenido una buena conversación!")
        break
    
    # Genera y muestra la respuesta basada en la pregunta
    respuesta_generada = generar_respuesta_a_pregunta(pregunta_usuario)
    print("ChatGPT:", respuesta_generada)
