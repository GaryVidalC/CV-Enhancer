# CV-Enhancer

Este proyecto es una herramienta para mejorar y personalizar un currículum vitae (CV) basado en una oferta de trabajo específica. Utiliza inteligencia artificial de Google (Gemini) para analizar la oferta de trabajo y adaptar el CV existente para que coincida mejor con los requisitos del puesto.

## Cómo usar

1. **Preparación**:
   - Asegúrate de tener Python 3.x instalado.
   - Instala la biblioteca necesaria: `pip install google-genai`
   - Coloca tu clave API de Google GenAI en el archivo `key.txt` (debe estar en la raíz del proyecto).
   - Prepara tu currículum en formato JSON en `data/resume_gary_en.json`.
   - Asegúrate de que la plantilla LaTeX esté en `data/latex_template.tex`.

2. **Ejecución**:
   - Abre una terminal en la carpeta del proyecto.
   - Ejecuta el script con la URL de la oferta de trabajo como argumento:
     ```
     python main.py <URL_DE_LA_OFERTA>
     ```
     Por ejemplo:
     ```
     python main.py https://ejemplo.com/oferta-trabajo
     ```

3. **Resultado**:
   - El script generará un archivo `output.tex` con el CV personalizado en formato LaTeX.
   - Puedes compilar `output.tex` con un procesador LaTeX (como pdflatex) para obtener un PDF.

## Requisitos

- Python 3.x
- Biblioteca `google-genai`
- Clave API válida de Google GenAI
- Archivos de datos: `data/resume_gary_en.json` y `data/latex_template.tex`

## Notas

- El idioma del CV generado está configurado en Francés; puedes cambiarlo en el código si es necesario.
- Asegúrate de que la URL de la oferta de trabajo sea accesible y contenga la información necesaria.