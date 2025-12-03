# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto de práctica!

## 📋 Flujo de Trabajo

1. **Crea un Issue** para reportar bugs o proponer mejoras
2. **Crea una rama** desde main con un nombre descriptivo
3. **Haz tus cambios** en esa rama
4. **Ejecuta los tests** para verificar que todo funciona
5. **Commit con mensajes claros** siguiendo las convenciones
6. **Push a tu rama**
7. **Crea un Pull Request** hacia main
8. **Espera revisión** y responde a comentarios

## 💬 Formato de Commits

Usa prefijos para mayor claridad:

- `feat:` nueva funcionalidad
- `fix:` corrección de bug
- `docs:` cambios en documentación
- `test:` agregar o modificar tests
- `refactor:` refactorización de código
- `style:` cambios de formato (sin afectar código)

**Ejemplos:**
```
feat: agregar función de potencia a calculadora
fix: corregir división por cero
docs: actualizar README con nuevos ejemplos
```

## ✅ Antes de Crear un PR

- [ ] El código funciona sin errores
- [ ] Todos los tests pasan (`pytest tests/`)
- [ ] Has actualizado la documentación si es necesario
- [ ] Tu código sigue el estilo del proyecto
- [ ] Has agregado comentarios en código complejo

## 🧪 Ejecutar Tests

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todos los tests
pytest tests/

# Ejecutar con más detalle
pytest tests/ -v

# Ejecutar test específico
pytest tests/test_ejemplos.py::test_sumar -v
```

## 📝 Code Review

Cuando revises código de otros:

- ✅ **Sé constructivo** - Sugiere mejoras de forma amable
- ✅ **Sé específico** - Indica exactamente qué y por qué
- ✅ **Pregunta** - Si algo no está claro, pregunta
- ✅ **Reconoce** - Menciona lo que está bien hecho
- ❌ **Evita críticas vagas** - "Está mal" no ayuda

**Ejemplo de buen comentario:**
```
Buen trabajo con la validación de entrada. 
Sugerencia: podrías usar f-strings en lugar de concatenación 
para mejor legibilidad:
return f"Hola, {nombre}!"
```

## 🆘 ¿Necesitas Ayuda?

- Crea un Issue con tu pregunta
- Contacta al instructor
- Revisa la documentación en README.md

---

¡Gracias por contribuir! 🎉
