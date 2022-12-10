# ciencia-de-datos
El jar de la aplicación se encuentra ubicado en el link anterior: NewsWordCount-1.0-SNAPSHOT.jar. La aplicación recibe como entrada 5 argumentos:
- Directorio de entrada que contiene los datos a analizar. En el cluster se encuentran los datasets cargados en: /user/bigdata01/inputXX
- Directorio de salida donde se va a guardar el resultado obtenido
- La tecnología a utilizar: mapreduce o spark
- Directorio donde se encuentran los stopwords para cada idioma. En el cluster se encuentran cargados en: /user/bigdata01/stopwords/
- De que sección de la noticia vamos a realizar el análisis: titulos o cuerpos

##### MapReduce
```
hadoop jar NewsWordCount-1.0-SNAPSHOT.jar WordCount {input_dir} {output_dir} mapreduce {stopwords_dir} {titulos/cuerpos}
```
##### Spark
```
spark-submit --class WordCount NewsWordCount-1.0-SNAPSHOT.jar {input_dir} {output_dir} spark {stopwords_dir} {titulos/cuerpos}
```

Los resultados obtenidos para cada escenario de prueba que se ejecutó se encuentran en:
* https://github.com/ABD-MINE4102/202220-Grupo01/tree/main/tareas/tarea1/NewsWordCount/resultados
