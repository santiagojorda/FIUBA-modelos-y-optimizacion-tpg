# Trabajo Final Modelos y Optimizacion I 
### Noviembre 2024
#### Integrantes
- Agustin Demicheli 
- Santiago Jorda
- Nahuel Godoy
- Estefano Polizi 

## 1. Papeleria Godoy SRL

La familia Godoy se dedica hace 30 años al rubro de la papelería,  cuenta con una fábrica en la que elaboran 2 productos, sobres y etiquetas,  la papelería contrató a X trabajadores, los cuales trabajan de lunes a sábados con turnos de 8 HS/DÍA, además cuenta con una máquina M1 que se dedica al doblado de las hojas. Esta cuenta con una disponibilidad de H horas máquina, para evitar de esta manera un costoso mantenimiento constantemente.
Los recursos se obtienen de dos fuentes, del cliente quien proveerá la materia prima para realizar el trabajo solicitado y además un mayorista de papel y cartón, el cual vende por lotes de 100 cajas a un costo de $C y 100 sobres por $S.
Cada persona dedicada a producir sobres demora HS en hacer 1500 sobres, y HE para hacer 2000 etiquetas. Por otro lado, las máquinas funcionan de manera mucho más eficiente demorando HM1 en hacer 10000 sobres Con lo indicado.
Se utilizan fletes para entregar los sobres terminados, cada encomienda puede transportar 7000 de los mismos, y este posee un precio de $CT
 ¿Qué sería lo mejor que puede hacer la familia Godoy?

## 2. Agregar Producto

La papelera Godoy quiere agregar a su producción la producción de diario personalizados. Se utilizará la máquina M1 para el doblado del papel, y deciden utilizar una vieja máquina de impresión M2 que tenían guardada. 
Por cada diario se utilizan ML mililitros de tinta. La tinta se compra en el mayorista por litro a un precio de $CTIN
El papel diario es brindado por los clientes.
Cada persona que hace el trabajo manual de doblar los diarios puede hacer CS por hora. La máquina 1 puede doblar hasta DD por hora y la máquina 2 puede trabajar 100 horas por mes. Necesita que un solo operador esté a cargo.
Los fletes pueden transportar hasta 4000 diarios al mismo precio de antes


## 3. Control de Calidad

La papalera enfrenta desafíos de calidad debido a defectos generados por el uso de maquinaria, lo que requiere un proceso adicional de reparación para mantener los estándares del producto.
Un porcentaje fijo de los sobres producidos por la máquina son rechazados debido a defectos y deben ser reparados, lo que genera costos adicionales en términos de tiempo y dinero $CR.

<div style="page-break-after: always;"></div>

# Informe caso base

## Análisis

El objetivo es determinar la cantidad a admitir de ensobrado y etiquetado, buscando maximizar el beneficio de producción en un mes.

## Hipótesis
 1. En producción para la demanda máxima no se pueden superar los limites (no hay razon mas alla para superar los limites)
 2. Para el consumo de recursos por unidad, de materia prima, es constante y conocida, no va a variar y no hay perdida.
 3. Para las horas base se depende de la cantidad de personal que trabaje
 4. Puede haber horas extras siempre y cuándo estén dentro del limite permitido
 5. Las horas extra son indistinguibles como se distribuye
 6. La producción de los operarios es constante y continua 
 7. La maquina produce con una capacidad constante
 8. Las horas de maquina consumen horas de personal
 9. El transporte tiene una capacidad fija, y siempre esta disponible en caso de ser necesario
 10. El costo del transporte es fijo
 11. La capacidad de las cajas es exacta siempre

## Variables

Las variables del modelo:

- $Producido\ servicio$: Cantidad de unidades producidas de cada servicio.
- $Cantidad\ Cajas\ A\ Comprar\ Para\ servicio$: Cantidad de cajas necesarias para cada servicio.
- $Consumo\ horas\ produccion\ de\ servicio$: Horas necesarias para la producción de cada servicio.
- $Consumo\ horas\ maquina$: Horas de uso de la máquina.
- $Horas\ Extra$: Horas adicionales de trabajo necesarias.
- $Horas\ Sobrantes$: Horas sobrantes de producción que no se utilizan.
- $Cantidad\ de\ Traslados$: Cantidad de traslados necesarios para transportar el producto.

Siendo $Servicio$: ${Ensobrado,Etiquetado}$

## Constantes

- $LIMITES\ PRODUCCION\ servicio$: Límite de producción de cada servicio.
- $CAPACIDAD\ CAJA\ servicio$: Capacidad de cajas para cada servicio.
- $PRODUCCION\ MAQUINA_A$: Cantidad de producción de máquina para el servicio A.
- $LIMITE\ HORAS\ MAQUINA_A$: Límite de horas de máquina disponibles para el servicio A.
- $PRODUCCION\ HORA\ servicio$: Cantidad de producción por hora de cada servicio.
- $PERSONAL\ NECESARIO\ MAQUINA_A$: Personal necesario para el uso de la máquina para el servicio A.
- $LIMITE\ HORAS\ HOMBRE$: Límite de horas hombre disponibles.
- $MAXIMO\ HORAS\ EXTRA\ PERSONAL$: Límite máximo de horas extra disponibles para el personal.
- $CAPACIDAD\ TRASLADO\ A$: Capacidad de traslado del servicio A.
- $PRECIO\ VENTA\ SERVICIO$: Precio de venta de cada servicio.
- $PRECIO\ CAJAS$: Precio por caja utilizada en la producción de cada servicio.
- $PRECIO\ HORA\ EXTRA$: Precio por hora extra de trabajo.
- $PRECIO\ CAPACIDAD\ OCIOSA$: Precio de la capacidad ociosa.
- $PRECIO\ TRANSLADO_A$: Precio por traslado del servicio A.


## Función Objetivo

La función objetivo del modelo es maximizar el beneficio de la empresa. El beneficio se calcula como la diferencia entre los ingresos y los costos. La fórmula es:

$Beneficio$ = $Ingresos$ - $Costos$

Donde los **ingresos** y **costos** son:

- **Ingresos**:
  $$
  \text{Ingresos} = \sum_{servicio} \text{Precio Venta}_{servicio} \cdot \text{Producido}_{servicio}
  $$

- **Costos**:
  - Materia Prima:
    $$
    \text{Costo Materia Prima} = \sum_{servicio} \text{Precio Cajas} \cdot \text{Cantidad Cajas}_{servicio}
    $$
  - Horas Extra:
    $$
    \text{Costo Horas Extra} = \text{Horas Extra} \cdot \text{Precio Hora Extra}
    $$
  - Capacidad Ociosa:
    $$
    \text{Costo Capacidad Ociosa} = \text{Capacidad Ociosa} \cdot \text{Precio Capacidad Ociosa}
    $$
  - Traslados:
    $$
    \text{Costo Traslados} = \text{Cantidad Traslados} \cdot \text{Precio Traslados}_A
    $$


## Restricciones

1. **Demanda Máxima**:
   $$
   \text{Producido}_{servicio} \leq \text{Límite de Producción}_{servicio}, \quad \forall \, servicio
   $$

2. **Consumo de Recursos**:
   - **Cajas**:
     $$
     \text{Capacidad Caja}_{servicio} \cdot \text{Cantidad Cajas}_{servicio} = \text{Producido}_{servicio}, \quad \forall \, servicio
     $$
   - **Máquina**:
     $$
     \text{Producción Máquina}_A \cdot \text{Horas Máquina} = \text{Producido}_A
     $$
     $$
     \text{Horas Máquina} \leq \text{Límite Horas Máquina}_A
     $$
   - **Horas de Producción**:
     $$
     \text{Producción por Hora}_{servicio} \cdot \text{Horas de Producción}_{servicio} = \text{Producido}_{servicio}, \quad \forall \, servicio
     $$
     $$
     \text{Horas de Producción Totales} = \text{Horas de Producción}_A + \text{Horas de Producción}_B
     $$
   - **Traslados**:
     $$
     \text{Capacidad Traslado}_A \cdot \text{Cantidad Traslados} = \text{Producido}_A
     $$

3. **Restricciones Horarias**:
   $$
   \text{Personal Necesario Máquina}_A \cdot \text{Horas Máquina} + \text{Horas de Producción Totales} = \text{Límite Horas Hombre} + \text{Horas Extra} - \text{Capacidad Ociosa}
   $$

4. **Máximo de Horas Extra**:
   $$
   \text{Horas Extra} \leq \text{Máximo Horas Extra Personal}
   $$
## Resultados
![resultado_variables](caso_base/resultado_variables.png)
![resultado_restricciones](caso_base/resultado_restricciones.png)
![produccion](caso_base/produccion.png)
![porcentajes](caso_base/porcentajes_costos.png)

<div style="page-break-after: always;"></div>

# Informe segundo caso
## Análisis
Se agregó un tercer servicio que se produce y vende $Diarios$, el cual introduce además una máquina 2 que tiene $HM2$ disponibles y tiene una capacidad máxima de produccion $C$, se busca determinar que cántidad de servicio $Ensobrado$, $Etiquetado$ y $Diarios$ cuya variable es $A$, $B$ y $C$ respectivamente realizar en un mes para maximizar las ganancias.
## Hipotesis

- La Calidad del servicio $C$ realizado por la máquina $M2$ y por los operarios es indistinguible
- Los recursos conseguidos para la realización de $C$ no tienen fallas
- Los costos de la tinta por litro se mantiene constante a lo largo del mes ya que no le afecta la inflación
- El personal que trabaja con la máquina 2 trabaja con la misma eficiencia y cualquiera puede trabajar en ella
- Se cuenta con el capital necesario para la producción del producto $C$

## Variables

$C$ : Cantidad de diarios a producir y vender por mes\
$CONSUMO$ _$M2$ :  consumo de horas de máquina 2  por mes\
$CANTIDAD$ _$TINTA$ : cantidad de tinta a comprar para producir diarios\
$CANTIDAD$ _$DE$ _$TRASLADO$ _$DIARIOS$ : cantidad de traslado de diarios realizado por mes\
$CONSUMOS$ _$DE$ _$C$ : consumo de horas de produccion por $C$ por mes \
$COSTOS$ _$MATERIA$ _$PRIMA$ _$DIARIOS$ : costos de produccion diaria por el servicio $C$
## Constantes 
$LIMITES$_ $PRODUCCION$ _ $C$ \
$PRECIO$_$TINTA$ \
$TINTA$ _$DIARIO$ \
$PRECIO$ _$VENTA$ _$C$\
$LIMITE$ _$HORAS$ _$MAQUINA$ _$2$\
$PRODUCCION$ _$MAQUINA$ _$C$\
$PERSONAL$ _$NECESARIO$ _$MAQUINA$ _$2$\
$PRODUCCION$ _$HORA$ _ $C$\
$CAPACIDAD$ _$TRASLADO$ _ $C$\
$PRECIO$ _$TRASLADO$ _$C$
## Funcion Objetivo

 $INGRESOS$ se agrego -> $PRECIO$ _$VENTA$ _$C$ * $C$ y en los\
 $COSTOS$ se agrego -> $COSTOS$ _$MATERIA$ _$PRIMA$ _$DIARIOS$ 
 donde $COSTOS$ _$MATERIA$ _$PRIMA$ _$DIARIOS$  = 
$PRECIO$_$TINTA$ * $CANTIDAD$ _$TINTA$

## Restricciones y código modificado 

$servicios.append(C)$\
$maquinas.append(M2)$\
$costos$ = $costos$ _$materia$ _$prima$ + $costo$ _$horas$ _$extra$ + $costo$ _$capacidad$ _$ociosa$ + $costo$ _$translado$ \
$costo$ _$materia$ _$prima$ _$diarios$ = $PRECIO$ _$TINTA$ * $cantidad$ _$tinta$ $/ 1000$  \
$costos$ _$materia$ _$prima$ = $costo$ _$materia$ _$prima$ _$sobres$ + $costo$ _$materia$ _$prima$ _$diarios$

- $CANTIDAD$ _ $TINTA$ $=$ $producido[C]$ * $TINTA$_$DIARIO$\

- $PRODUCCION$ _ $MAQUINA[M2]*horas$ _$maquina[M2]$ = $producido[C]$

- $CAPACIDAD \_TRANSLADO[C]*cantidad \_translados\_diarios$ = $producido[C]$

- $suma$ _$horas$ _$maquina$ = $(PERSONAL$ _$NECESARIO$ _$MAQUINA[M1]$*$horas$_$maquina[M1])$ +  $(PERSONAL$ _ $NECESARIO$ _ $MAQUINA[M2]$*$horas$_ $maquina[M2])$ 

- $producido[servicio] <= LIMITES$ _ $PRODUCCION[servicio]$

- $PRODUCCION$ _ $HORA[servicio]*horas$ _ $produccion$ _$producto[servicio]$ = $producido[servicio]$

## Servicios
Se agregó el servicio $Diarios$ el cual utiliza recursos tinta cuyo costo es $PRECIO$_$TINTA$ y la máquina $M2$ con todos los subitems que ello conlleva, precio de tinta, capacidad de produccion de diarios diaria, consumo de tinta diario

## Resultados
Lo que sucedió en este caso fue que se obtuvo una mayor ganancia debido a que es más rentable la venta de producir y vender diarios antes que tener una mayor capacidad ociosa ya que se les paga a los trabajadores por no hacer nada.

![resultado_variables](caso_dos/resultado_variables.png)
![resultado_restricciones](caso_dos/resultado_restricciones.png)
![produccion](caso_dos/produccion.png)
![porcentajes](caso_dos/porcentajes_costos.png)

<div style="page-break-after: always;"></div>

# Informe tercer caso
## Variables
- $R_m$: Sobres rechazados por maquina
- $H_{rs}$: Horas invertidas en reparacion por maquina
## Constantes
- $C_{rs}$: Costo de reparacion sobre
- $PR_{M1}$: Porcentaje de rechazo
- $REP_{hr}$: Cantidad de reparacion por hora
## Restricciones
### Consumo Maquina
- Consumo: R_m = P_{A} * PR_{M1} 
### Rechazo Maquinas
- Rechazo: $R_m = H_{rs} * REP_{hr}$
### Costos reparacion
- Costo reparacion: $C_{rep} = R_m * C_{rs}$
- Costo total: $C_{total} = C_{mp} + C_{he} + C_{co} + C_{tr} + C_{rs}$
## Resultados
![resultado_variables](caso_tres/resultado_variables.png)
![resultado_restricciones](caso_tres/resultado_restricciones.png)
![produccion](caso_tres/produccion.png)
![porcentajes](caso_tres/porcentajes_costos.png)



---
# Analisis de Sensibilidad 
 