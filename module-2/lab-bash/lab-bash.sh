#Ejercicios

#Imprime en consola Hello World.
echo Hello World

#Crea un directorio nuevo llamado new_dir.
mkdir new_dir

#Elimina ese directorio.
rm -r new_dir

#Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy.
cp lorem/sedd.txt lorem-copy

#Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;.
cp lorem/at.txt lorem-copy ; cp lorem/lorem.txt lorem-copy

#Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.
cat lorem/sed.txt

#Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
cat lorem/at.txt
cat lorem/lorem.txt

#Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat lorem-copy/sed.txt | head -n 3

#Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat lorem-copy/sed.txt | tail -n 3

#Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.
vim lorem-copy/sed.txt

#Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..
cat lorem-copy/sed.txt | tail -n 3

#Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.
sed 's/et/ET/g' lorem-copy/at.txt

#Encuentra al usuario activo en el sistema.
whoami

#Encuentra dónde estás en tu sistema de ficheros.
pwd

#Lista los archivos que terminan por .txt en la carpeta lorem.
ls lorem/*txt

#Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.
cat lorem/sed.txt | wc -l

#Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.
find . -name "lorem*" | wc -l

#Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.
##Utilizo -w para encontrar solo las apariciones et solitarias, es decir, que no están contenidas dentro de otras.
grep -w -i "et" lorem/at.txt

#Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.
grep -o -i " et" lorem/at.txt | wc -l

#Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.
 grep -r -c -i " et" lorem-copy/


 #BONUS

#Almacena en una variable name tu nombre.
name="Javi"

#Imprime esa variable.
echo $name

#Crea un directorio nuevo que se llame como el contenido de la variable name.
mkdir $name

#Elimina ese directorio.
rm -r $name

#Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus nombres. Intenta primero mostrar los archivos mediante un bucle for
    #Imprime los ficheros
        #Dentro de la carpeta lorem, desde fuera de la carpeta no lo he logrado:
        for file in $(ls);
        do
            if [[ -f $file ]];
            then
                echo archivo: $file
            fi
        done
    #Imprime las longitudes de los nombres de los ficheros
    for file in $(ls);
        do
            if [[ -f $file ]];
            then
                echo ${#file}
            fi
        done
    #Imprime outputs con la siguiente estructura: lorem has 5 characters lenght
    for file in $(ls);
        do
            if [[ -f $file ]];
            then
                echo $file has ${#file} characters lenght
            fi
        done

#Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
    #Usando el comando top o htop
    top
    #Usando el comando ps con argumentos
    ps -auJavi

#Muestra información sobre tu procesador por pantalla
sysctl -n machdep.cpu.brand_string

#Crea 3 alias y haz que estén disponibles cada vez que inicias sesión

#Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz
tar -cvzf lorem-compressed.tar.gz lorem lorem-copy

#Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed
##En toda la documentación que he leido me indica que para descomprimir se usa lo que pongo a continuación,pero por lo que sea no me funciona.
 tar -xvf lorem-compressed.tar.gz
