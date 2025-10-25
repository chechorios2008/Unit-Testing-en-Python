# 🐍 Proyecto: Notas y Ejemplos de Unit Testing en Python ✅

Este repositorio sirve como mi cuaderno de notas y colección de ejemplos de código prácticos El objetivo es documentar las mejores prácticas, sintaxis clave y conceptos esenciales de las pruebas unitarias.

---

## 🚀 Tecnologías Clave

Este proyecto se centra en las herramientas estándar de prueba de la comunidad Python.

* **Python:** Lenguaje de programación principal.
* **`unittest`:** Módulo estándar de Python para la creación de pruebas unitarias.
* **`pytest` (Opcional):** Framework de pruebas de terceros popular por su simplicidad.
* **Git / GitHub:** Para control de versiones y alojamiento del proyecto.

---

### 📝 Tipos de pruebas para asegurar la calidad del software

1. Pruebas unitarias: Se encargan de validar que cada componente pequeño del código funcione correctamente de manera aislada.
2. Pruebas de integración: Verifican que los distintos componentes trabajen bien en conjunto, evitando problemas en la interacción de partes.
3. Pruebas funcionales: Validan que el sistema en su totalidad funcione como se espera según los requisitos.
4. Pruebas de rendimiento: Aseguran que el software sea rápido y eficiente, evaluando su comportamiento bajo diferentes condiciones de carga.
5. Pruebas de aceptación: Determinan si el software cumple con las expectativas del usuario final.

#### herramientas de Python para testing  
- **UnitTest**: Permite crear pruebas unitarias de manera sencilla, asegurando que todas las partes del código realicen su función correctamente.
- **PyTest**: Facilita la creación de pruebas con una configuración avanzada para cubrir diferentes escenarios.
- **DocTest**: Integra pruebas directamente en los comentarios de las funciones, permitiendo validar el código mientras se mantiene la documentación.

En Python, estas pruebas se automatizan utilizando la palabra clave **assert**, que compara los resultados esperados con los reales.

### 🛠️ Testing con Unit Test en Python
- UnitTest ya viene por defecto en Python en las versiones nuevas.
- Para ejecutar en consola es necesario indicarle a UnitTest donde estan los archivos.
  Comando >>> *** py -m unittest discover -s nombre_carpeta**
-- UnitTest solo lee archivos que inicial por **test_nombre_elemento_a_probar.py**
-- Documentación Oficial Pyhon UnitTest: https://docs.python.org/3/library/unittest.html
-- Para ver detalle de pruebas: Comando >>> *** py -m unittest discover -v -s nombre_carpeta**

#### ✍️ Método Setup en Python
El uso del método **setup** en los tests permite simplificar y evitar la duplicación de código en las pruebas. Al iniciar un test, setup se ejecuta automáticamente, preparando el entorno para cada prueba de forma eficiente. 
El método setup evita la creación repetitiva de instancias en cada test. Para lograr esto:
- Se crea una instancia de cuenta en setup.
- La cuenta creada se comparte entre todas las pruebas usando self.

#### 🧠 Pruebas de Registro de Transacciones.
- El método teardown es esencial para asegurar que nuestras pruebas no interfieran entre sí, y se usa para limpiar cualquier recurso temporal al final de cada prueba.
- El método **teardown** se ejecuta al final de cada prueba, y es utilizado para limpiar recursos como archivos temporales o cerrar conexiones.
- El **teardown** nos permite eliminar el archivo de log después de cada prueba para que no interfiera con otras. Implementamos una función que, si el archivo existe, lo borra utilizando **os.remove**. Esto asegura que las pruebas se ejecutan en un entorno limpio y los logs no se acumulan entre pruebas.
¿Cómo validamos la existencia del archivo de log?
- Verificamos si el archivo de log se crea exitosamente. Utilizamos la función **os.path.exists**
Para validar que los logs tienen la información correcta: 
1. Contamos las líneas después de crear la cuenta (debe haber una línea).
2. Hacemos un depósito y volvemos a contar las líneas (debe haber dos líneas).
3. Si no limpiáramos el archivo con teardown, el número de líneas sería incorrecto.

### ⚠️ Métodos de Assert en UnitTest para Pruebas Efectivas

- La TestCaseclase proporciona varios métodos de aserción para detectar y reportar fallos.
- assertEqual(a, b) > a == b,  assertNotEqual(a, b) > a != b, assertTrue(x) > bool(x) is True, 
  assertFalse(x) > bool(x) is False,   assertIs(a, b) > a is b, assertIsNot(a, b) > a is not b,
  assertIsNone(x) > x is None, assertIsNotNone(x) > x is not None, assertIn(a, b) > a in b,
  assertNotIn(a, b) > a not in b, assertIsInstance(a, b) > isinstance(a, b).
- Aplican a partir de Python 3.14. 
  assertNotIsInstance(a, b) > not isinstance(a, b), assertIsSubclass(a, b) issubclass(a, b),
  assertNotIsSubclass(a, b) > not issubclass(a, b).

### ✨ Decoradores de Unit Test para Saltar Pruebas y Detectar Fallos

Python y unittest ofrecen decoradores que nos permiten omitir pruebas temporalmente, sin comprometer el flujo de trabajo ni la integridad del proyecto. ***@skip, @skipIf y @expectedFailure***
- El decorador **@skip** se utiliza cuando sabemos que una prueba no debería ejecutarse temporalmente.
- El decorador **@skipIf** es útil cuando queremos omitir una prueba bajo una condición específica.


### ⚙️ Organización y Ejecución de Pruebas con Python Unit Test



 📝 💡 ✍️  🐛