# 📖 Instrucciones de Práctica

Sigue estos ejercicios en orden para dominar Git y GitHub.

---

## ✅ Ejercicio 1: Tu Primer Commit

**Objetivo:** Hacer tu primer cambio y subirlo a GitHub

### Pasos:

1. **Abre `README.md`** en VSCode
2. **Busca la sección "Participantes"**
3. **Agrega tu nombre:**
   ```markdown
   - [x] Tu Nombre Aquí
   ```
4. **Guarda el archivo** (`Ctrl+S`)
5. **Abre el panel Git** (`Ctrl+Shift+G`)
6. **Stage el cambio** (clic en `+` junto a README.md)
7. **Escribe mensaje de commit:** "Agregar mi nombre a participantes"
8. **Commit** (✓)
9. **Push** (⬆)
10. **Verifica en GitHub** que apareció tu cambio

### ✅ Completado cuando:
- Tu nombre aparece en GitHub
- Ves tu commit en el historial

---

## ✅ Ejercicio 2: Crear un Issue

**Objetivo:** Reportar una "tarea" usando Issues

### Pasos:

1. **Ve a tu repositorio en GitHub**
2. **Clic en pestaña "Issues"**
3. **Clic en "New Issue"**
4. **Completa:**
   - **Título:** "Mejorar función de saludo"
   - **Descripción:**
     ```markdown
     ## Descripción
     La función `saludar()` en `ejemplos/saludo.py` podría mejorarse.
     
     ## Tareas
     - [ ] Agregar soporte para múltiples idiomas
     - [ ] Agregar mensaje de despedida
     
     ## Fecha límite
     [Fecha de hoy + 1 día]
     ```
5. **Etiquetas:** Agregar `enhancement`
6. **Asignar:** A ti mismo
7. **Create Issue**

### ✅ Completado cuando:
- El Issue aparece en la lista
- Tiene número (ej: #1)

---

## ✅ Ejercicio 3: Trabajar en una Rama (Branch)

**Objetivo:** Crear una rama para trabajar sin afectar main

### Pasos:

1. **En VSCode, clic en la rama actual** (esquina inferior izquierda, dice "main")
2. **Selecciona "Create new branch"**
3. **Nombre:** `mejora/saludo-multilenguaje`
4. **Presiona Enter**
5. **Verifica que cambiaste de rama** (esquina inferior izquierda)

### ✅ Completado cuando:
- Estás en la nueva rama (no en main)
- VSCode muestra el nombre de tu rama

---

## ✅ Ejercicio 4: Modificar Código

**Objetivo:** Editar un archivo de código

### Pasos:

1. **Asegúrate de estar en tu rama** `mejora/saludo-multilenguaje`
2. **Abre `ejemplos/saludo.py`**
3. **Reemplaza todo el contenido con:**
   ```python
   def saludar(nombre, idioma="es"):
       """Saluda en diferentes idiomas."""
       if idioma == "es":
           return f"¡Hola, {nombre}!"
       elif idioma == "en":
           return f"Hello, {nombre}!"
       elif idioma == "fr":
           return f"Bonjour, {nombre}!"
       else:
           return f"Hi, {nombre}!"
   
   def despedir(nombre):
       """Se despide de una persona."""
       return f"¡Adiós, {nombre}!"
   
   # Ejemplos de uso
   if __name__ == "__main__":
       print(saludar("Ana"))
       print(saludar("John", "en"))
       print(saludar("Marie", "fr"))
       print(despedir("Ana"))
   ```
4. **Guarda el archivo**

### ✅ Completado cuando:
- El archivo tiene el nuevo código
- VSCode muestra "M" (modificado) en el archivo

---

## ✅ Ejercicio 5: Commit y Push de la Rama

**Objetivo:** Guardar cambios y subirlos a GitHub

### Pasos:

1. **Panel Git** (`Ctrl+Shift+G`)
2. **Revisa los cambios** (clic en `ejemplos/saludo.py` para ver diff)
3. **Stage** (`+`)
4. **Mensaje de commit:** "feat: agregar soporte multiidioma y función despedir. Closes #1"
   - Nota: `Closes #1` cerrará automáticamente el Issue #1
5. **Commit** (✓)
6. **Push** (⬆)
   - Si es primera vez: VSCode preguntará publicar la rama → Clic "Yes"

### ✅ Completado cuando:
- El push fue exitoso
- La rama aparece en GitHub

---

## ✅ Ejercicio 6: Crear Pull Request

**Objetivo:** Proponer integrar tus cambios a main

### Pasos:

1. **Ve a GitHub**
2. **Verás un banner:** "mejora/saludo-multilenguaje had recent pushes"
3. **Clic en "Compare & pull request"**
   - O ve a "Pull requests" → "New pull request"
4. **Completa el PR:**
   - **Título:** "Mejorar función de saludo con soporte multiidioma"
   - **Descripción:**
     ```markdown
     ## Cambios realizados
     - ✅ Agregado parámetro `idioma` a función `saludar()`
     - ✅ Soporte para español, inglés y francés
     - ✅ Nueva función `despedir()`
     - ✅ Actualizados ejemplos de uso
     
     ## Cierra Issue
     Closes #1
     
     ## Tests
     - [x] El código se ejecuta sin errores
     - [x] Todas las funciones retornan valores correctos
     ```
5. **Create Pull Request**

### ✅ Completado cuando:
- El PR aparece en la lista
- Tiene número (ej: #2)

---

## ✅ Ejercicio 7: Code Review

**Objetivo:** Revisar tu propio código (simulando ser el docente)

### Pasos:

1. **En el PR, ve a pestaña "Files changed"**
2. **Pasa el mouse sobre una línea de código**
3. **Clic en el "+" azul**
4. **Escribe un comentario:**
   ```
   Excelente implementación! El código es claro y fácil de entender.
   Sugerencia: Podrías agregar más idiomas en el futuro.
   ```
5. **"Add single comment"**
6. **Repite en 2-3 líneas más** con diferentes comentarios
7. **Clic en "Review changes"** (arriba a la derecha)
8. **Selecciona "Approve"**
9. **Escribe:**
   ```
   Código aprobado. Buena documentación y ejemplos claros.
   Listo para merge.
   ```
10. **Submit review**

### ✅ Completado cuando:
- Tienes varios comentarios en el código
- El PR está aprobado (✓)

---

## ✅ Ejercicio 8: Merge Pull Request

**Objetivo:** Integrar cambios a la rama main

### Pasos:

1. **En el PR, scroll hasta abajo**
2. **Clic en "Merge pull request"** (botón verde)
3. **Confirma el merge**
4. **Observa:**
   - ✓ PR cerrado y merged
   - ✓ Issue #1 cerrado automáticamente (por el "Closes #1")
5. **Opcional: Clic en "Delete branch"** (limpiar)

### ✅ Completado cuando:
- PR está merged
- Issue #1 está cerrado
- Cambios están en main

---

## ✅ Ejercicio 9: Actualizar tu Rama Local

**Objetivo:** Traer los cambios de GitHub a tu computadora

### Pasos:

1. **En VSCode, cambia a rama `main`**
   - Clic en nombre de rama (esquina inferior izquierda)
   - Selecciona `main`
2. **Panel Git → "..." → Pull**
3. **Abre `ejemplos/saludo.py`**
4. **Verifica que tiene las mejoras** que hiciste

### ✅ Completado cuando:
- Estás en rama main
- El archivo local tiene los cambios merged

---

## ✅ Ejercicio 10: Ejecutar Tests

**Objetivo:** Verificar que el código pasa los tests automáticos

### Pasos:

**Opción A: En tu PC (si tienes Python):**
```bash
pip install pytest
pytest tests/
```

**Opción B: En Codespaces:**
1. Abre este repo en Codespaces
2. Terminal automática ejecutará los tests
3. O ejecuta: `pytest tests/`

### ✅ Completado cuando:
- Ves: `2 passed` (todos los tests pasan)
- No hay errores

---

## 🎉 ¡Ejercicios Completados!

Has practicado todo el flujo de trabajo de GitHub:
- ✅ Commits
- ✅ Branches
- ✅ Issues
- ✅ Pull Requests
- ✅ Code Review
- ✅ Merge
- ✅ Tests

## 🚀 Próximos Pasos

1. **Práctica adicional:** Crea otro Issue y repite el proceso
2. **Explora GitHub Classroom:** Si tu instructor configuró un assignment
3. **Experimenta con Codespaces:** Abre el repo en la nube

---

## 💡 Ejercicio Extra: Conflicto de Merge (Avanzado)

¿Quieres practicar resolver conflictos? Sigue estos pasos:

1. Crea rama `experimental-1`
2. Edita línea 5 de `saludo.py`
3. Commit y push
4. Vuelve a `main`
5. Crea rama `experimental-2`
6. Edita LA MISMA línea 5 de `saludo.py` (diferente texto)
7. Commit y push
8. Intenta merge de ambas a main → ¡Conflicto!
9. Resuélvelo manualmente en VSCode

---

**¿Preguntas?** Crea un Issue en este repositorio.
