# CV-Enhancer

Este proyecto es una herramienta para mejorar y personalizar un currículum vitae (CV) basado en una oferta de trabajo específica. Utiliza inteligencia artificial de Google (Gemini) para analizar la oferta de trabajo y adaptar el CV existente para que coincida mejor con los requisitos del puesto.

## Cómo funciona

1. **Entrada**: El script `main.py` recibe como argumento una URL de una oferta de trabajo.

2. **Datos de entrada**:
   - Clave API de Google GenAI desde `key.txt`.
   - Currículum en formato JSON desde `data/resume_gary_en.json`.
   - Plantilla LaTeX desde `data/latex_template.tex`.

3. **Procesamiento**:
   - El modelo Gemini analiza la oferta de trabajo en la URL proporcionada.
   - Extrae habilidades, cualificaciones y experiencias clave requeridas.
   - Selecciona y ajusta la información relevante del currículum JSON.
   - Genera un CV personalizado en formato LaTeX, siguiendo la estructura de la plantilla.
   - El texto se genera en el idioma especificado (actualmente configurado en Francés).

4. **Salida**: El CV generado se guarda en `output.tex`.

## Requisitos

- Python 3.x
- Biblioteca `google-genai`: Instala con `pip install google-genai`
- Una clave API válida de Google GenAI en `key.txt`

## Instalación

1. Clona o descarga el repositorio.
2. Instala las dependencias: `pip install google-genai`
3. Coloca tu clave API de Google GenAI en el archivo `key.txt`.

## Uso

Ejecuta el script desde la línea de comandos con la URL de la oferta de trabajo:

```
python main.py <URL_DE_LA_OFERTA>
```

Por ejemplo:
```
python main.py https://ejemplo.com/oferta-trabajo
```

El archivo `output.tex` se generará con el CV personalizado.

## Notas

- Asegúrate de que la URL de la oferta de trabajo sea accesible.
- El currículum JSON debe contener información estructurada sobre experiencia, proyectos, etc.
- La plantilla LaTeX define la estructura del CV de salida.