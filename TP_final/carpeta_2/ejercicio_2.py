# Título:
# Modelo de Productos, Excepciones y Persistencia (40 puntos)

# Consigna:
# Para la división de equipamiento sustentable de EcoTech Solutions, se requiere un módulo de software que gestione los productos del catálogo, impida inconsistencias en el inventario mediante validaciones de negocio y garantice la persistencia del stock en disco.
# Punto A: Dominio del Catálogo y Reglas de Inventario: Construye la jerarquía orientada a objetos para los productos ecológicos. Diseña una clase de excepción personalizada StockInvalidoError y aplícala dentro de la clase base DispositivoEcológico para impedir que el stock tome valores negativos mediante encapsulamiento explícito. Desarrolla la clase especializada PanelSolar, incorporando sus atributos específicos mediante herencia y aplicando polimorfismo para personalizar la emisión de su ficha técnica comercial.
# Punto B: Persistencia y Gestión del Catálogo: Implementa la clase GestorInventario con el método guardar_catalogo_json(lista_dispositivos, ruta_archivo) capaz de serializar y almacenar en catalogo_ecotech.json las instancias creadas en el Punto A. Incluye un bloque de prueba donde se verifique la captura controlada de StockInvalidoError ante un intento de asignación de stock erróneo, finalizando con la exportación exitosa de los productos válidos al archivo JSON.

import json


# Punto A: Dominio del Catálogo y Reglas de Inventario

class StockInvalidoError(Exception):
    # Excepción que se lanza cuando se intenta asignar un stock negativo.
    pass


class DispositivoEcologico:
    def __init__(self, codigo, nombre, precio, stock):
        # Inicializa los atributos básicos del dispositivo y valida el stock inicial.
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        # Encapsulamiento exclusivo.
        self.__stock = 0
        self.asignar_stock(stock)

    def get_stock(self):
        # Retorna la cantidad actual de stock
        return self.__stock

    def asignar_stock(self, nuevo_stock):
        # Actualiza el stock chequeando que no sea negativo; si lo es, lanza StockInvalidoError.
        if nuevo_stock < 0:
            mensaje_error = f"No se puede asignar un stock negativo ({nuevo_stock}) al producto '{self.nombre}'."
            raise StockInvalidoError(mensaje_error)
        else:
            self.__stock = nuevo_stock

    def emitir_ficha_tecnica(self):
        # Genera un texto con los datos del dispositivo.
        stock_actual = self.get_stock()
        ficha = f"[Dispositivo Ecológico] Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {stock_actual} unidades"
        return ficha

    def convertir_a_diccionario(self):
        # Convierte los datos del dispositivo a un diccionario para guardarlo en JSON.
        datos = {
            "tipo": "DispositivoEcologico",
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.get_stock(),
        }
        return datos


class PanelSolar(DispositivoEcologico):
    def __init__(self, codigo, nombre, precio, stock, potencia_watts, eficiencia):
        # Inizaliza el panel solar reutilizando el constructor de la clase base, agrega potencia y eficiencia.
        super().__init__(codigo, nombre, precio, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    def emitir_ficha_tecnica(self):
        # Sobrescribe el método base para incluir la potencia y eficiencia en la ficha técnica.
        stock_actual = self.get_stock()
        ficha = f"[Panel Solar] Código: {self.codigo} | Nombre: {self.nombre} | Potencia: {self.potencia_watts}W | Eficiencia: {self.eficiencia}% | Precio: ${self.precio} | Stock: {stock_actual} unidades"
        return ficha

    def convertir_a_diccionario(self):
        # Agrega los atributos del panel solar al diccionario.
        datos = {
            "tipo": "PanelSolar",
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.get_stock(),
            "potencia_watts": self.potencia_watts,
            "eficiencia": self.eficiencia,
        }
        return datos


# Punto B: Persistencia y Gestión del Catálogo

class GestorInventario:
    # Clase encargada de gestionar el inventario y guardar el catálogo en JSON.

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        # Recorre la lista de productos, los convierte a diccionario y los gurada en JSON.
        lista_para_guardar = []
        for dispositivo in lista_dispositivos:
            lista_para_guardar.append(dispositivo.convertir_a_diccionario())

        with open(ruta_archivo, "w") as archivo_json:
            json.dump(lista_para_guardar, archivo_json, indent=4)

        print(f"Catálogo guardado con éxito en: {ruta_archivo}")


# Bloque Principal de Prueba
if __name__ == "__main__":
    print("=" * 65)
    print("   GESTIÓN DE INVENTARIO Y CATÁLOGO - ECOTECH SOLUTIONS")
    print("=" * 65)

    catalogo_valido = []
    print("\n[1] CREACIÓN DE PRODUCTOS Y FICHAS TÉCNICAS (POLIMORFISMO):")
    try:
        termostato = DispositivoEcologico("ECO-101", "Termostato Inteligente", 85.50, 15)
        panel_residencial = PanelSolar("SOL-201", "Panel Monocristalino 450W", 320.00, 10, 450, 21.5)
        panel_industrial = PanelSolar("SOL-202", "Panel Bifacial Industrial 600W", 480.00, 8, 600, 23.0)

        catalogo_valido.append(termostato)
        catalogo_valido.append(panel_residencial)
        catalogo_valido.append(panel_industrial)

        for producto in catalogo_valido:
            ficha_producto = producto.emitir_ficha_tecnica()
            print(f"  • {ficha_producto}")

    except StockInvalidoError as error:
        print(f"  [ERROR DE STOCK]: {error}")
    print("\n[2] PRUEBA DE VALIDACIÓN DE STOCK NEGATIVO:")
    try:
        print("  Intentando crear un Panel Solar con stock -5...")
        panel_erroneo = PanelSolar("SOL-999", "Panel Solar Defectuoso", 200.00, -5, 300, 18.0)
        catalogo_valido.append(panel_erroneo)
    except StockInvalidoError as error:
        print(f"  -> Excepción capturada correctamente: {error}")

    try:
        print("  Intentando modificar el stock de un producto existente a -3...")
        termostato.set_stock(-3)
    except StockInvalidoError as error:
        print(f"  -> Excepción capturada correctamente: {error}")
    print("\n[3] EXPORTACIÓN DEL CATÁLOGO A JSON:")
    ruta_json = "carpeta_2/catalogo_ecotech.json"

    gestor = GestorInventario()
    try:
        gestor.guardar_catalogo_json(catalogo_valido, ruta_json)
    except FileNotFoundError:
        ruta_json = "catalogo_ecotech.json"
        gestor.guardar_catalogo_json(catalogo_valido, ruta_json)

    print("=" * 65)
    print(" Developed By: Sucutrule Productions          8-)")
    print("""
______██████████████
-____██▓▓▓▓▓▓▓▓▓ M ▓████
-__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
-__██████░░░░██░░██████
██░░░░████░░██░░░░░░░░██
██░░░░████░░░░██░░░░░░██
-__████░░░░░░██████████
-__██░░░░░░░░░░░░░██
_____██░░░░░░░░░██
-______██░░░░░░██
-____██▓▓████▓▓▓█
-_██▓▓▓▓▓▓████▓▓█
██▓▓▓▓▓▓███░░███░
-__██░░░░░░███████
-____██░░░░███████
-______██████████
-_____██▓▓▓▓▓▓▓▓▓██
-_____█████████████
""")
