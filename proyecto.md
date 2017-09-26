### PROYECTO 1
Se trata de el primer trabajo de la asignatura Sistemas Operativos, en el cual, incide sobre dos
vertientes de los Sistemas Operativos: Seguridad y Procesos.

La competición tendrá la siguiente estructura:

- Todos los grupos tendrán que iniciar su aplicación, que debe crear una canalización con el
nombre "So_ <número del grupo>" en el directorio / home / so / y leer el archivo
/home/so/dicionario.txt;
- Una aplicación desarrollada por el docente de la asignatura, al mismo tiempo, enviará a todos los
canalizaciones existentes en el directorio / home / so / una palabra encriptada;
- Cada grupo tendrá que basarse en la lista de palabras minúsculas contenidas en el archivo
encontrar la palabra encriptada, asumiendo que cualquier carácter de la palabra puede estar en
mayúscula o minúscula;
- Una vez que se encuentre la palabra correspondiente, ésta deberá enviarse a la canalización
"So_server" en el formato: "grupo_ <número del grupo>: <palabra>: <palabra encriptada>";
- Gana el grupo que descifra tres contraseñas primero.
Todos los programas tendrán que guardar en un archivo de texto los registros necesarios para
analizar en en tiempo real el estado de su programa. Se podrán utilizar procesos en paralelo (fork)
para obtener un mejor rendimiento. El recurso a esta tecnología influenciará la nota final.

 ### PROYECTO 2

 Se trata de el segundo trabajo de la asignatura Sistemas Operativos, en el cual, incide sobre tres
vertientes de los Sistemas Operativos: Seguridad, Threads y señales.

El servidor de trabajo práctico 1, debe ser modificado para enviar un conjunto de palabras
encriptadas en secuencia (sólo enviar la siguiente palabra después de recibir la palabra
desencadenada). Deberá adaptar el trabajo práctico 1 sometido a:

- Tener un subproceso (thread_control) que lee las palabras colocadas en la canalización "so_
<numero de grupo> "en el directorio / home / so;
- Tener un conjunto de subprocesos (subprocesos de búsqueda) que se notifica de la existencia de
palabras encriptadas y que deben hacer el proceso de descifrado, teniendo en cuenta que las
palabras pueden tener minúsculas y / o mayúsculas;
- Los subprocesos de búsqueda deben estar sincronizados con el subproceso_control y deben
iniciar la sesión búsqueda tan pronto como el thread_controlo lo indique;
- El subproceso que busca la palabra debe notificar el subproceso de control, que envía el mensaje
resultado para la canalización del servidor (servidor);
- Cuando un subproceso busca búsqueda, todos los demás subprocesos deben para su
procesamiento y esperar un nuevo trabajo;
- Al ejecutar Ctrl + Z durante la búsqueda de una palabra clave, la aplicación debe imprimir el
documento el número de palabras del diccionario ya procesadas (por subproceso y total);
- Al ejecutar Ctrl + C deberá cerrar todos los recursos utilizados y terminar la aplicación.
