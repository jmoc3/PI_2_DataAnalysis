# Proyecto Individual #2 - Telecomunicaciones

### **Contexto**

Las telecomunicaciones se refieren a la transmisión de información a través de medios electrónicos, como la telefonía, la televisión, la radio y, más recientemente, el internet. Estos medios de comunicación permiten la transmisión de información entre personas, organizaciones y dispositivos a largas distancias.

El internet, por su parte, es una red global de computadoras interconectadas que permite el intercambio de información en tiempo real. Desde su creación, ha tenido un impacto significativo en la vida de las personas, transformando la manera en que nos comunicamos, trabajamos, aprendemos y nos entretenemos.

La industria de las telecomunicaciones ha jugado un papel vital en nuestra sociedad, facilitando la información a escala internacional y permitiendo la comunicación continua incluso en medio de una pandemia mundial. La transferencia de datos y comunicación se realiza en su mayoría a través de internet, líneas telefónicas fijas, telefonía móvil, y en casi cualquier lugar del mundo. 

En comparación con la media mundial, Argentina está a la vanguardia en el desarrollo de las telecomunicaciones, teniendo para el 2020 un total de [62,12 millones de conexiones](https://www.datosmundial.com/america/argentina/telecomunicacion.php). 

### **Objetivo**

Basado en el contexto de ser un analista de datos para una empresa de telecomunicaciones argentina, los objetivos principales rodean la idea en un **analisis completo** del negocio para poder comprender las caracteristicas del sector a nivel nacional y seguir la mision del mismo, poder ***brindar internet a la mayor cantidad de personas posibles***.

### **Cronologia de eventos**

Lo primero a realizar como siempre es el EDA cuyo proceso interno se compone del arreglo y limpieza de los datos, especificaciones al respecto de con que archivos se trabaja y que se hace con ello lo pueden encontrar en el siguiente enlace: [PI_EDA](https://pi2dataanalysis-hjvi628r8vazuptcaiujmi.streamlit.app/).

Posterior al tratamiento y exportacion de los datos mas bonitos y limpios se realiza un dashboard con el desarrollo no solo del entendimiento del contexto empresarial sino tambien de metricas y KPI's para el mejoramiento del negocio guiado a su mision, esto lo pueden encontrar dentro del archivo dashboard.pbix, solo es importarlo en power BI. En cualquier caso si solo desea echarlo un vistazo lo puede encontrar acontinuacion:  
***
<image src="./Dashboard.png" align="center" style="margin-left:10px" alt="Python icon">  

***
### **Analisis Estadistico**

Lo primero a detallar respecto a los datos es por supuesto la informacion que nos puede brindar respecto al proposito principal de la empresa de accesibilizar la conectividad, sabemos que existen personas que tienen internet y otras que no pero, esta situacion realmente esta cambiando? lo hace a bien o a mal? bueno, de ahi el primer kpi que representa la diferencia porcentual entre la cantidad de personas que poseian internet el semestre pasado y las personas que actualmente se encuentran conectadas de alguna manera, de hecho podemos ver que las cifras aumentaron aproximadamente un 5%, lo que representaria un volumen de 40 mil ciudadanos más en nuestra base de datos.  

Respecto al segundo KPI basado en la velocidad de descarga es importante aclarar que, aunque se mantuvo una diferencia positiva entre el ultimo valor anual y el promedio, hubo una drastica disminucion entre la media de bajada en el ultimo año. Es bueno mantener ese margen de promedio por lo menos para primero enfocarnos mas en al cobertura y mantener un nivel de calidad nivelado pero si podemos prestarle atencion a eso al mismo tiempo  mucho mejor.

Siguiento con esto la calidad del internet esta cuantificada en la cantidad de personas que poseen una red potente como la de 4G, que si se compara respecto a algunas tecnologias realmente tiene una cobertura interesante.

Por ultimo utilice uno de los datasets complementarios basados en las licencias TICs entregadas ya que realmente no podia encontrar ninguna correlacion entre las provincias que no tenian internet y la velocidad de descarga de la conectividad, asi que lo plasme en el mapa y segun se ve y el mapa de microsoft logra identificar se puede detallar ciertos espacios vacios en la localidades con licencia que se encuentran rellenos en las localidades sin conexion. Realmente ese tema depende bastante me imagino de los pagos requeridos por las autoridades politicas de la zona, sin embargo, es otra cosa a la que tarde que temprano tendremos que mirar para poder ampliar nuestro ecosistema.

### **Tecnologias**

  - Python<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width=20 align="center" style="margin-left:10px" alt="Python icon">
  - Pandas<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/225px-Pandas_mark.svg.png" width=20 align="center" style="margin-left:10px" alt="Pandas icon">
   - Matplotlib<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Matplotlib_icon.svg/2048px-Matplotlib_icon.svg.png" width=20 align="center" style="margin-left:10px" alt="Matplotlib icon">
  - Numpy<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1200px-NumPy_logo_2020.svg.png" width=60 align="center" style="margin-left:10px" alt="Numpy icon">
  - Streamlit<image src="https://images.datacamp.com/image/upload/v1640050215/image27_frqkzv.png" width=60 align="center" style="margin-left:10px" alt="streamlit icon">
  - Requests<image src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Requests-logo.png" width=20 align="center" style="margin-left:10px" alt="Requests icon">
  - PowerBI<image src="https://www.uc3m.es/sdic/media/sdic/img/mediana/original/im_power-bi-pro---icono/im_power-bi-pro---icono.png" width=20 align="center" style="margin-left:10px" alt="PowerBI icon">
  
