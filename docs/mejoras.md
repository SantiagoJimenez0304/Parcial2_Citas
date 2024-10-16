# Mejoras Realizadas y Nuevas Agregadas

## 12 Mejoras Realizadas

1. **Lectura de datos desde CSV y JSON**:
   - Se agregaron funciones para leer los archivos `pacientes.csv`, `medicos.json` y `citas.csv` y cargar la información en el hospital.

2. **Estructura de clases**:
   - Se crearon clases para `Hospital`, `Paciente`, `Medico` y `Cita` para mejorar la organización del código.

3. **Métodos en `Hospital`**:
   - Se agregaron métodos en la clase `Hospital` para **agregar pacientes, médicos y citas** y para **buscar pacientes y médicos** por su identificador.

4. **Fecha y hora en citas**:
   - Se agregó la capacidad de almacenar tanto la **fecha** como la **hora** de las citas, mejorando la precisión de la programación.

5. **Validación de paciente y médico al agendar citas**:
   - En la carga de citas, se validó que tanto el paciente como el médico existan antes de crear la cita, evitando errores de referencia.

6. **Corrección del formato CSV para pacientes**:
   - En la lectura de `pacientes.csv`, se dividió el nombre completo en `nombre` y `apellido` para cumplir con los requerimientos.

7. **Uso de `DictReader` para leer CSV**:
   - Se utilizó `csv.DictReader` para leer los archivos CSV, lo cual facilita la manipulación de datos por nombre de campo.

8. **Uso de JSON para cargar médicos**:
   - Se introdujo la carga de datos desde un archivo JSON para los médicos, con la finalidad de manejar datos más complejos de manera estructurada.

9. **Error handling para archivo no encontrado**:
   - Se implementó un manejo de errores básico para el caso en que los archivos CSV o JSON no se encuentren en la ruta especificada.

10. **Incorporación de rutas relativas**:
   - Se usaron rutas relativas (`../datos/`) para leer los archivos, facilitando la organización del proyecto y la portabilidad.

11. **Eliminación de dependencias innecesarias**:
   - Se eliminó el código redundante y simplificado en las clases para mejorar la claridad y la eficiencia.

12. **Modularización del código**:
   - La lógica de carga de datos fue modularizada en una función independiente (`cargar_datos_iniciales`), mejorando la mantenibilidad del código.

---

## 2 Nuevas Agregadas

1. **Formato de fecha en citas**:
   - Se añadió la capacidad de parsear correctamente la fecha y hora de las citas desde el archivo CSV con el formato `'%Y-%m-%d %H:%M:%S'` usando `datetime.strptime()`.

2. **Instanciación de objetos `Paciente` y `Medico` desde los datos CSV/JSON**:
   - Se mejoró la creación de instancias de `Paciente` y `Medico` usando los datos cargados desde los archivos, asegurando que las instancias sean creadas con los atributos correctos.
