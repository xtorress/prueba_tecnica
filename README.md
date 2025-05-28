# Prueba Tecnica - Simulación de Mercado de Tarjetas Gráficas

Esta prueba tecnica consiste en simular un mercado de tarjetas gráficas en el que distintos tipos de agentes (agentes aleatorios, agentes tendeciales, agentes anti tendenciales y uno con una lógica personal) que se diferencian por su política de compra y venta.


## Componentes principales

### `Market`
- Representa un mercado de tarjetas gráficas con:
  - Stock de tarjetas
  - Precio actual y previo
  - Cálculo del cambio porcentual del precio
  - Métodos para comprar y vender tarjetas (ajustan el precio)
  - Método para actualizar mercado después de cada iteración.

### `Agent`
- Solo puede comprar o vender una tarjeta por turno.
- Representa un agente económico que puede:
  - Comprar si tiene dinero suficiente y hay stock
  - Vender si tiene tarjetas
  - Tomar decisiones usando una política (`Politic`)

### `Politic` (estrategia)
- Define el comportamiento de compra/venta:
  - `RandomPolitic`: decisiones aleatorias (sin importar el cambio de precio)
  - `TrendPolitic`: tienen un 75% de probabilidades de comprar y un
25% de probabilidades de no hacer nada si el precio ha subido un 1% (o más). En caso contrario tienen un 20% de probabilidades de vender y un 80% de
probabilidades de no hacer nada. 
  - `AntiTrendPolitic`: tienen un 75% de probabilidades de comprar y un
25% de probabilidades de no hacer nada si el precio ha bajado un 1% (o más). En caso contrario tienen un 20% de probabilidades de vender y un 80% de
probabilidades de no hacer nada. 
  - `PersonalPolitic`: considera la tendencia histórica

### `Simulation`
- Ejecuta la simulación durante `n` iteraciones
- Cada iteración mezcla los agentes y ejecuta sus acciones
- Al final de cada iteración se actualiza el mercado

### `GenerateReport`
- Información final del agente personal.
- Devuelve el top5 de los agentes con mayor balance al finalizar la simulación.

---

## 🚀 Cómo ejecutar

1. Clona el repositorio.
2. Configurar proyecto.
```bash
pip install -e .
```
3. Instalar dependencias.
```bash
pip install -r requirements.txt
```
4. Para ejecutar tests.
```bash
pytest app/tests
```
5. Ejecutar programa:
```bash
python main.py
```