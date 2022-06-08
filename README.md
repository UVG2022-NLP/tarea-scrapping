<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/UVG2022-TEAM/2022-NPL-tarea1-scrapping">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Tarea 1 Scrapping</h3>

  <p align="center">
    Tarea 1 de TEXT MINING & NATURAL LANGUAGE PROCESSING - SECCIÓN - 10 - 2022 - 1
    <br />
    <a href="https://github.com/UVG2022-TEAM/2022-NPL-tarea1-scrapping"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/UVG2022-TEAM/2022-NPL-tarea1-scrapping">View Demo</a>
    ·
    <a href="https://github.com/UVG2022-TEAM/2022-NPL-tarea1-scrapping/issues">Report Bug</a>
    ·
    <a href="https://github.com/UVG2022-TEAM/2022-NPL-tarea1-scrapping/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## Detalles de tarea

<!--  [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

En nuestra última clase vimos algunas herramientas para hacer scrapping de páginas web y realizamos scrapping de Tripadvisor. Realicen scrapping de alguna página web con estas herramientas u otras de alguna página web (puede ser Tripadvisor también u otra página) bajo los siguientes requerimientos:

* el resultado del scrapping debe ser texto clasificado, es decir, una colección de fragmentos de texto cada uno de los cuales pertenece a alguna categoría,
* el código debe quedar alojado en algún repositorio público, dentro de una organización (Github) o grupo (Gitlab) a la que pertenezcan todos los integrantes del grupo de trabajo, 
* en el repositorio debe haber un README.md con 1. instrucciones claras para instalar y correr su código tal que yo pueda ejecutarlo y obtener el resultado del scrapping (p. ej. crea un ambiente de python con este requirements.txt y ejecuta este comando), 2. formato y estructura del resultado (p. ej. CSV con columnas que se llaman así), 3. descripción del contenido del sitio web, así como de lo que representan los fragmentos de texto y las categorías en las que está clasificado, 4. las contribuciones de cada integrante del grupo y 5. cualquier información adicional que consideren importante.

El entregable en Canvas es el link de su repositorio.

<p align="right">(<a href="#top">back to top</a>)</p>



### Desarrollado con

En esta sección incluimos el software necesario para instalar este proyecto.

* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* [Anaconda](https://www.anaconda.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Comenzando ejecución

Clonamos el repositorio con ayuda de Github Destop. Posteriormente, es necesario tener Miniconda o Anaconda instalado para la instalación del enviroment. 

### Prerequisitos

Para cargar el environment configurado se tiene que leer el "environment.yml" con ello tendremos todas las librerías necesarias. Abrimos Anaconda Prompt y nos situamos en la carpeta principal del respositorio "2022-NPL-tarea1-scrapping". Ejecutar la siguiente linea de código:
* Anaconda Prompt
  ```sh
  conda env create -f environment.yml
  ```

Validamos que el enviroment "scrapping-citymax" esté instalado correctamente:

* Anaconda Prompt
  ```sh
  conda env list
  ```

Activamos el nuevo enviroment:

* Anaconda Prompt
  ```sh
  conda activate scrapping-citymax
  ```

_Para mayor detalle consultar la referencia de [como instalar un .yml en conda.](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)_ 

### Ejecución en IDE

Abrir su IDE de Python de preferencia, en nuestro caso usaremos Visual Studio Code. 

1. Abrir la carpeta "2022-NPL-tarea1-scrapping"
2. Tomamos como interprete Python 3.10.4 ('scrapping-citymax')
3. Abrimos la terminal y realizamos los `cd` necesarios para situarnos en la carpeta "...\2022-NPL-tarea1-scrapping\citymax_scrapping\citymax_scrapping"
4. Una vez situados en la carpeta del código de Python ejecutamos el `crawl` en la terminal de nuestro IDE
   ```sh
   scrapy crawl actives -t csv -o citymax.csv
   ```
5. Deberá de generarnos un archivo .csv de nombre "citymax", no tiene límite así que dará scrapping a toda la página, de querer parar la ejecución es necesario presionar CTRL+C en la terminal

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Formato y estructura del resultado

Se genera un .csv que contiene las siguientes columnas:

* _description_: detalle del inmueble. En este ponen información adicional, por ejemplo, que amenidades o conveniencias tiene. 
* _name_: titulo del inmueble.  
* _operation_: se indica si está a la venta o en renta. 
* _price_: precio en dolares o quetzales de inmueble según su operación.
* _type_: tipo de inmueble, ya sea: apartamento, bodega, casas, edificios, fincas, locales comerciales, oficinas, proyectos o terrenos. 

_Ejemplo de [una casa en venta](https://www.citymax-gt.com/126746/Casa-en-venta-para-Inversi%C3%B3n-entrada-a-Olmeca-CES/)_.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Descripción del contenido del sitio web

CityMax Guatemala es una franquicia de negocios inmobiliarios, nacida en América Latina (Guatemala) para Latinoamericanos en el Año 2007. Cuenta a la venta todo tipo de inmuebles. Al presionar una opción dentro de su catalogo podemos obtener el detalle del inmueble. 

_[Catalogo de inmuebles](https://www.citymax-gt.com/resultados-busqueda/?status=&type=&keyword=)_.



<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contribuciones de integrantes

* Francisco Manjón y William Chavarría: Lectura de detalle por inmueble
* Pablo Armas: Ciclo de pagineo y lectura de título de inmueble
* André Rodas: Manejo de versiones y documentación
* Todos: Unificación y QA de código trabajado

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contenido adicional 

El proyecto fué inspirado por un blog de rentabilidad del sector inmobiliario en Guatemala hecho por Daniel Fernández de [UFM Market Trends](https://trends.ufm.edu/articulo/rentabilidad-invertir-sector-inmobiliario-guatemala/).
