# Release Notes - Calendario Zinkro

Documentación de versiones públicas del Calendario Zinkro.

## Formato de Versiones

Se sigue [Semantic Versioning](https://semver.org/lang/es/):
- **MAJOR.MINOR.PATCH** (ej: 1.2.3)
- MAJOR: Cambios incompatibles con versiones anteriores
- MINOR: Nuevas funcionalidades compatibles hacia atrás
- PATCH: Correcciones de bugs

---

## v1.0.0 - 20 de Marzo de 2026: 🚀 Lanzamiento Oficial

**Fecha de Lanzamiento**: 20 de Marzo de 2026  
**Tema**: "Un Calendario Alineado con la Naturaleza"  
**Hito Especial**: Primer Día Zero del Calendario Zinkro

### ✨ Características Principales

#### 1. **Calendario Zinkro Completo**
- ✅ Estructura de 13 meses × 28 días + 1 Día Zero
- ✅ 365 días en años normales, 366 en años bisiestos
- ✅ Alineado con el equinoccio de primavera (20 de marzo)
- ✅ Año 0 reservado para el Día Zero

#### 2. **Conversión Bidireccional Gregoriano ↔ Zinkro**
- ✅ `gregorian_to_zinkro()` - Convierte fechas gregorianas a Zinkro
- ✅ `zinkro_to_gregorian()` - Convierte fechas Zinkro a gregorianas
- ✅ Soporte para la Era Holocena (año gregoriano + 10000)
- ✅ Manejo correcto de años bisiestos

#### 3. **Interfaz Web Bilingüe**
- ✅ Español e Inglés
- ✅ Página de inicio con información del proyecto
- ✅ Cuadrícula visual interactiva del calendario
- ✅ Sección de contexto histórico y propuesta
- ✅ Navegación unificada en todas las páginas

#### 4. **Herramientas CLI**
- ✅ `python convert.py` - Conversión desde línea de comandos
- ✅ Soporta conversión gregoriana → Zinkro
- ✅ Soporta conversión Zinkro → gregoriana
- ✅ Formato predeterminado: Era Holocena (-10000-03-20)

#### 5. **Suite de Tests Completa**
- ✅ 9 tests unitarios cubriendo todos los casos edge
- ✅ Validación de años normales y bisiestos
- ✅ Tests para días especiales (29 de febrero, 20-21 de marzo)
- ✅ 100% de tests pasando

#### 6. **Documentación Exhaustiva**
- ✅ README.md con instrucciones de uso
- ✅ CHANGELOG.md con historial de cambios
- ✅ Ejemplos prácticos en ejemplos_zinkro.py
- ✅ Comentarios de código bien documentados

### 🔄 Lo que cambió respecto a versiones previas

Esta es la **versión estable inicial**, pero incluye un cambio importante respecto a propuestas anteriores:

**Cambio Principal**: Alineación con el equinoccio real de primavera

| Aspecto | Propuesta Original | v1.0.0 Final |
|---------|-------------------|--------------|
| Fecha de inicio | 21 de marzo | 20 de marzo |
| Motivo | Convenio | Equinoccio real |
| Día Zero | No existía | 20 de marzo |
| Precisión | ±1 día | ✓ Exacto |

### 🛠️ Cambios Técnicos

#### Backend (Python)
- Arquitectura modular con separación de responsabilidades
- `zinkro.py`: Lógica de conversión central
- `convert.py`: Interfaz CLI
- `tests/`: Suite de validación automatizada

#### Frontend (JavaScript)
- `zinkro.js`: Lógica de conversión en navegador
- Funciones de utilidad para formateo
- Sincronización con lógica backend

#### Infraestructura
- Estructura de carpetas organizada (`views/`, `tests/`, etc.)
- GitHub Pages ready
- Workflow CI/CD preparado

### 📊 Métricas

- **Cobertura de Tests**: 100%
- **Tests Passing**: 9/9 ✓
- **Archivos de Código**: 15+
- **Idiomas Soportados**: 2 (Español, Inglés)
- **Precisión de Conversión**: ±0 días

### 🐛 Bugs Conocidos

Ninguno reportado en la versión 1.0.0 ✓

### ⚠️ Cambios Incompatibles con Versiones Anteriores

Si existían versiones con "21 de marzo como Día Zero":
- Las fechas **anteriores a 21 de marzo** cambiarán su mapeo Zinkro
- El 20 de marzo ahora retorna `(0, None, None, True)` en lugar de `(año, 13, 28, False)`

**Recomendación**: Actualizar todos los sistemas que usen calendarios Zinkro a v1.0.0

### 📥 Instalación

```bash
# Clonar repositorio
git clone https://github.com/martinolivera/zinkro.git

# Instalar dependencias (solo Python estándar)
cd zinkro
python3 -m pip install -r requirements.txt  # (opcional)

# Ejecutar tests
python3 -m unittest tests.test_zinkro_leap -v

# Probar conversión
python3 convert.py --help
python3 convert.py --date 2026-03-20
```

### 🚀 Próximas Versiones (Roadmap)

#### v1.1.0 (Próximo)
- [ ] Agregar soporte para más idiomas
- [ ] Visualización mejorada de años bisiestos
- [ ] API REST para conversiones
- [ ] Integración con Google Calendar

#### v1.2.0
- [ ] Aplicación móvil (React Native)
- [ ] Sincronización en tiempo real
- [ ] Widget de calendario embebible
- [ ] Notificaciones de Día Zero

#### v2.0.0 (Futuro)
- [ ] Interfaz gráfica de escritorio
- [ ] Bases de datos de eventos históricos
- [ ] Gamificación
- [ ] Exportación a múltiples formatos

### 📝 Notas de Desarrollo

#### Decisiones Arquitectónicas

1. **Python + JavaScript**: Permite compartir lógica entre backend y frontend
2. **Modularidad**: Cada componente tiene responsabilidad única
3. **Tests Primero**: La suite de tests fue central en el desarrollo
4. **Documentación**: Cada cambio importante está documentado

#### Convenciones de Código

- Nombres en español para variables de dominio (día, mes, año)
- Nombres en inglés para variables técnicas (buffer, cache, thread)
- Docstrings completos en funciones públicas
- Comentarios explicativos para lógica compleja

### 🙋 Contribuciones

¿Encontraste un bug? ¿Tienes una idea? ¡Abre un issue en GitHub!

### 📜 Licencia

Especificar según el repositorio (ej: MIT, GPL, etc.)

### 🎉 Agradecimientos

Gracias a todos los que ayudaron a llevar el Calendario Zinkro a la realidad.

---

**Lanzado**: 20 de Marzo de 2026 🌍  
**Estado**: Versión Estable ✓  
**Próxima versión**: v1.1.0 (Q2 2026)

---

## Versiones Anteriores

### v0.9.0 - Beta (Antes de Lanzamiento)
- Pre-lanzamiento con lógica de 21 de marzo
- Disponible bajo rama `develop`
- No soportado en producción

