<div class="git-card">

# Informática - 2026

## Guía de ejercicios: práctica básica de Git en Windows

**Docente:** Ignacio Lavaggi

<span class="git-tag">Git</span>
<span class="git-tag">Windows</span>
<span class="git-tag">Consola</span>
<span class="git-tag">Ramas</span>
<span class="git-tag">GitHub</span>

Esta guía tiene como objetivo practicar los comandos básicos de Git desde consola. Los ejercicios están pensados para realizarse en orden, usando **CMD** o **PowerShell** en Windows.

</div>

---

## Objetivos de la práctica

Al finalizar esta guía, el estudiante debería poder:

- Configurar Git en una computadora.
- Crear un repositorio local.
- Entender qué son los commits.
- Registrar cambios usando commits.
- Ver el estado y el historial de un proyecto.
- Conectar un repositorio local con un repositorio remoto.
- Subir y traer cambios usando `push` y `pull`.
- Clonar un repositorio existente.
- Trabajar con branches o ramas.
- Usar comandos básicos para revisar diferencias y deshacer cambios simples.
- Reconocer errores comunes de Git y resolverlos.

---

## Reglas de trabajo

1. Todos los comandos deben ejecutarse desde consola.
2. **No se debe usar** GitHub CLI ni GitHub Desktop para esta práctica.
3. Para crear el repositorio remoto en GitHub, se puede usar la página web de GitHub.
4. Cada ejercicio debe resolverse dejando evidencia mediante commits.
5. Los mensajes de commit deben ser claros y relacionados con el cambio realizado.

<div class="git-info">

Durante toda la guía, conviene ejecutar `git status` antes y después de cada operación importante. Es el comando principal para saber qué está pasando dentro del repositorio.

</div>

---

# Ejercicio 1: verificar instalación y configuración inicial

## Objetivo

Comprobar que Git esté instalado y configurar el nombre y correo del usuario.

## Consigna

Abrí CMD o PowerShell y ejecutá:

```bash
git --version
```

Configurá tu nombre:

```bash
git config --global user.name "Tu Nombre"
```

Configurá tu correo (el que usaste para registrarte):

```bash
git config --global user.email "tu@email.com"
```

Verificá la configuración:

```bash
git config --list
```

## Preguntas

Todas las preguntas que aparezcan de acá en adelante, responderlas en la carpeta. Cualquier pregunta de estas puede entrar en el examen. 

1. ¿Qué versión de Git aparece instalada?
2. ¿Qué datos quedan asociados a los commits?
3. ¿Por qué conviene configurar correctamente el correo?

---

# Ejercicio 2: crear un repositorio local

## Objetivo

Crear una carpeta de trabajo y convertirla en un repositorio de Git.

## Consigna

Creá una carpeta llamada `practica-git`:

```bash
mkdir practica-git
cd practica-git
```

Inicializá Git:

```bash
git init
```

Verificá el estado:

```bash
git status
```

## Explicación

`git init` crea un repositorio local. A partir de ese momento, Git puede registrar los cambios que ocurran dentro de esa carpeta.

## Preguntas

1. ¿Qué significa que una carpeta sea un repositorio?
2. ¿Qué muestra `git status` en este momento?

---

# Ejercicio 3: crear archivos y hacer el primer commit

## Objetivo

Crear archivos, agregarlos al área de preparación y registrar el primer commit.

## Consigna

Creá un archivo llamado `README.md`:

```bash
echo "# Práctica Git" > README.md
```

Verificá el estado:

```bash
git status
```

Agregá el archivo al próximo commit:

```bash
git add README.md
```

Creá el primer commit:

```bash
git commit -m "Agrega README inicial"
```

Verificá nuevamente:

```bash
git status
```

## Explicación

Un **commit** es un registro de cambios. Sirve para guardar un punto importante del proyecto y poder consultar su historial.

## Preguntas

1. ¿Qué diferencia hay entre crear un archivo y hacer un commit?
2. ¿Para qué sirve `git add`?
3. ¿Qué debería mostrar `git status` después del commit?

---

# Ejercicio 4: modificar archivos y crear nuevos commits

## Objetivo

Practicar el ciclo básico de Git: modificar, revisar, agregar y hacer commits.

## Consigna

Agregá este contenido al archivo `README.md`:

```bash
echo "Este proyecto fue creado para practicar comandos básicos de Git." >> README.md
```

Revisá el estado:

```bash
git status
```

Revisá la diferencia:

```bash
git diff
```

Agregá los cambios:

```bash
git add README.md
```

Creá un commit:

```bash
git commit -m "Agrega descripción del proyecto"
```

## Explicación

`git diff` muestra qué cambió en los archivos antes de guardar esos cambios en un commit.

## Preguntas

1. ¿Qué muestra `git diff`?
2. ¿Por qué conviene revisar los cambios antes de hacer commit?
3. ¿El segundo commit reemplaza al primero o se suma al historial?

---

# Ejercicio 5: crear varios archivos y usar `git add .`

## Objetivo

Practicar cómo agregar varios archivos al mismo tiempo.

## Consigna

Creá una carpeta llamada `src`:

```bash
mkdir src
```

Creá un archivo dentro de esa carpeta:

```bash
echo "print('Hola Git')" > src/app.py
```

Creá otro archivo:

```bash
echo "Notas de la práctica" > notas.txt
```

Verificá el estado:

```bash
git status
```

Agregá todos los cambios:

```bash
git add .
```

Creá un commit:

```bash
git commit -m "Agrega archivos iniciales del proyecto"
```

## Explicación

`git add .` agrega todos los cambios de la carpeta actual. Es útil, pero hay que usarlo con cuidado para no agregar archivos que no correspondan.

## Preguntas

1. ¿Qué diferencia hay entre `git add archivo` y `git add .`?
2. ¿Qué archivos se agregaron en este ejercicio?

---

# Ejercicio 6: ver historial del proyecto

## Objetivo

Consultar los commits realizados.

## Consigna

Ver el historial completo:

```bash
git log
```

Ver el historial resumido:

```bash
git log --oneline
```

Ver el historial con forma de gráfico:

```bash
git log --oneline --graph --all
```

## Explicación

El historial permite ver los commits realizados, sus mensajes, sus autores y sus identificadores.

## Preguntas

1. ¿Cuántos commits tiene el proyecto?
2. ¿Qué diferencia hay entre `git log` y `git log --oneline`?
3. ¿Para qué puede servir revisar el historial?

---

# Ejercicio 7: crear un repositorio remoto en GitHub y conectarlo

## Objetivo

Conectar el repositorio local con un repositorio remoto.

## Consigna

Desde la página web de GitHub, creá un repositorio vacío llamado:

```text
practica-git
```

No agregues README, `.gitignore` ni licencia desde GitHub, porque ya existe contenido local.

Luego, desde la consola, dentro de la carpeta del proyecto, agregá el remoto:

```bash
git remote add origin https://github.com/usuario/practica-git.git
```

Verificá el remoto:

```bash
git remote -v
```

Renombrá la rama principal a `main`:

```bash
git branch -M main
```

Subí el proyecto por primera vez:

```bash
git push -u origin main
```

## Explicación

Un **remoto** es una ubicación externa donde también está guardado el repositorio. Por ejemplo, GitHub.

`push` significa subir los commits locales al repositorio remoto.

## Preguntas

1. ¿Por qué primero hay que crear el repositorio remoto en GitHub?
2. ¿Qué función cumple `origin`?
3. ¿Qué hace `git push -u origin main`?

---

# Ejercicio 8: clonar un repositorio

## Objetivo

Descargar una copia completa de un repositorio remoto.

## Consigna

Salí de la carpeta actual:

```bash
cd ..
```

Cloná el repositorio en otra carpeta:

```bash
git clone https://github.com/usuario/practica-git.git practica-git-copia
```

Entrá a la carpeta clonada:

```bash
cd practica-git-copia
```

Verificá los archivos:

```bash
ls
```

Verificá el remoto:

```bash
git remote -v
```

## Explicación

**Clonar** significa descargar un repositorio remoto en la computadora. Al clonar, no solo se descargan los archivos actuales, sino también el historial de commits.

## Preguntas

1. ¿Qué diferencia hay entre crear una carpeta común y clonar un repositorio?
2. ¿La copia clonada conserva el historial?
3. ¿Qué muestra `git remote -v` en el repositorio clonado?

---

# Ejercicio 9: practicar `pull` y `push`

## Objetivo

Entender cómo se sincronizan los cambios entre la copia local y el repositorio remoto.

## Consigna

En la carpeta clonada, modificá el archivo `notas.txt`:

```bash
echo "Cambio realizado desde la copia clonada." >> notas.txt
```

Agregá y commiteá:

```bash
git add notas.txt
git commit -m "Actualiza notas desde copia clonada"
```

Subí los cambios:

```bash
git push
```

Ahora volvé a la carpeta original:

```bash
cd ..
cd practica-git
```

Traé los cambios remotos:

```bash
git pull
```

Abrí o revisá `notas.txt` y verificá que el cambio haya llegado.

## Explicación

`push` sube cambios al remoto.

`pull` trae cambios desde el remoto y los aplica en la copia local.

## Preguntas

1. ¿Qué pasaría si se hace un cambio en una copia pero no se ejecuta `push`?
2. ¿Qué hace `pull` en la carpeta original?
3. ¿Por qué es importante hacer `pull` antes de empezar a trabajar?

---

# Ejercicio 10: trabajar con branches o ramas

## Objetivo

Crear una rama para trabajar sin modificar directamente `main`.

## Explicación

Una **branch** o **rama** es una línea de trabajo separada dentro del mismo proyecto.

La rama principal suele llamarse `main`. Se recomienda usar ramas para probar cambios, agregar funcionalidades o corregir errores sin alterar directamente la versión principal del proyecto.

Por ejemplo:

```text
main                 versión principal
feature/menu         desarrollo de un menú
fix/error-texto      corrección de un error
```

## Consigna

Ver ramas existentes:

```bash
git branch
```

Crear y entrar a una rama nueva:

```bash
git switch -c feature/presentacion
```

Modificar el README:

```bash
echo "Trabajo realizado en una rama nueva." >> README.md
```

Guardar el cambio:

```bash
git add README.md
git commit -m "Agrega texto desde rama feature"
```

Ver el historial:

```bash
git log --oneline --graph --all
```

Volver a `main`:

```bash
git switch main
```

Verificá el contenido de `README.md`.

## Preguntas

1. ¿El cambio hecho en la rama aparece automáticamente en `main`?
2. ¿Para qué sirve trabajar en una rama separada?
3. ¿Qué muestra el gráfico del historial?

---

# Ejercicio 11: unir una rama con `merge`

## Objetivo

Integrar los cambios de una rama dentro de `main`.

## Consigna

Estando en `main`, ejecutar:

```bash
git merge feature/presentacion
```

Verificar el estado:

```bash
git status
```

Ver historial:

```bash
git log --oneline --graph --all
```

Subir los cambios:

```bash
git push
```

## Explicación

`merge` significa fusionar o unir los cambios de una rama con otra. En este caso, se integran los cambios de `feature/presentacion` dentro de `main`.

## Preguntas

1. ¿Qué cambió después del `merge`?
2. ¿Por qué primero hay que estar parado en `main`?
3. ¿Qué se sube al hacer `git push` después del merge?

---

# Ejercicio 12: usar `fetch` y compararlo con `pull`

## Objetivo

Entender la diferencia entre traer información remota y aplicar cambios.

## Consigna

Desde una de las carpetas, hacé un cambio, commit y push.

En la otra carpeta, ejecutá:

```bash
git fetch
```

Luego revisá el historial:

```bash
git log --oneline --all --graph
```

Después ejecutá:

```bash
git pull
```

## Explicación

`fetch` trae información desde el remoto, pero no modifica directamente los archivos locales.

`pull` trae los cambios remotos y además los aplica en la rama actual.

## Preguntas

1. ¿Qué diferencia hay entre `fetch` y `pull`?
2. ¿Por qué `fetch` puede ser útil antes de actualizar?
3. ¿Cuál de los dos modifica los archivos locales?

---

# Ejercicio 13: deshacer cambios antes del commit

## Objetivo

Practicar cómo descartar cambios locales que todavía no fueron commiteados.

## Consigna

Modificá `README.md` agregando una línea de prueba:

```bash
echo "Texto que voy a descartar." >> README.md
```

Verificá el estado:

```bash
git status
```

Revisá la diferencia:

```bash
git diff
```

Descartá el cambio:

```bash
git restore README.md
```

Verificá nuevamente:

```bash
git status
```

## Explicación

`git restore` permite volver un archivo al último estado guardado por Git, siempre que el cambio no haya sido commiteado.

## Preguntas

1. ¿El cambio descartado se puede recuperar fácilmente?
2. ¿Por qué hay que tener cuidado con `git restore`?
3. ¿Qué muestra `git status` después de restaurar el archivo?

---

# Ejercicio 14: sacar archivos del staging

## Objetivo

Entender la diferencia entre modificar un archivo y prepararlo para commit.

## Consigna

Modificá `notas.txt`:

```bash
echo "Cambio temporal." >> notas.txt
```

Agregá el archivo al staging:

```bash
git add notas.txt
```

Verificá el estado:

```bash
git status
```

Sacalo del staging:

```bash
git restore --staged notas.txt
```

Verificá otra vez:

```bash
git status
```

## Explicación

El área de staging contiene los cambios que van a entrar en el próximo commit. `git restore --staged` saca un archivo de esa área, pero no borra sus modificaciones.

## Preguntas

1. ¿El archivo perdió los cambios?
2. ¿Qué cambió después de usar `git restore --staged`?
3. ¿Para qué puede servir sacar un archivo del staging?

---

# Ejercicio 15: resolver un error común

## Objetivo

Reconocer y resolver un problema típico al trabajar con repositorios remotos.

## Consigna

Intentá agregar nuevamente el remoto `origin`:

```bash
git remote add origin https://github.com/usuario/otro-repo.git
```

Es probable que aparezca el error:

```text
remote origin already exists
```

Verificá los remotos:

```bash
git remote -v
```

Corregí la URL del remoto:

```bash
git remote set-url origin https://github.com/usuario/practica-git.git
```

Volvé a verificar:

```bash
git remote -v
```

## Explicación

Este error aparece cuando se intenta crear un remoto llamado `origin`, pero ya existe uno con ese nombre. En lugar de crearlo otra vez, hay que modificar su URL.

## Preguntas

1. ¿Por qué aparece el error?
2. ¿Qué diferencia hay entre `git remote add` y `git remote set-url`?
3. ¿Cómo se verifica que el remoto quedó bien configurado?

---

# Ejercicio 16: mini proyecto final

## Objetivo

Integrar los comandos principales vistos en la guía.

## Consigna

Crear un repositorio llamado `mini-proyecto-git`.

Debe tener:

```text
README.md
src/app.py
notas.txt
```
(src es una carpeta, dentro de ella habrá un archivo app.py)


El archivo `README.md` debe incluir:

```text
Nombre del proyecto
Descripción
Comandos de Git usados
```

El archivo `src/app.py` debe imprimir un mensaje simple.

El archivo `notas.txt` debe incluir al menos tres notas sobre lo aprendido.

## Requisitos

El proyecto debe tener al menos:

- Un repositorio local.
- Un repositorio remoto en GitHub.
- Tres commits con mensajes claros.
- Una rama llamada `feature/mejora-readme`.
- Un merge de esa rama hacia `main`.
- Un push final al remoto.

## Comandos que deberían aparecer durante el trabajo

```bash
git init
git status
git add .
git commit -m "mensaje"
git branch
git switch -c feature/mejora-readme
git switch main
git merge feature/mejora-readme
git remote add origin URL
git push -u origin main
git push
git log --oneline --graph --all
```

## Entrega

Debés entregar:

1. La URL del repositorio remoto.
2. Una captura de `git log --oneline --graph --all`.
3. Una captura de `git status` mostrando que no quedan cambios pendientes.
4. Respuestas breves:
   - ¿Qué es un commit?
   - ¿Qué es una branch?
   - ¿Qué diferencia hay entre `push` y `pull`?
   - ¿Qué diferencia hay entre `fetch` y `pull`?
   - ¿Para qué sirve `git status`?

---

<div class="git-card">

## Resumen de comandos practicados

| Acción | Comando |
|---|---|
| Ver versión de Git | `git --version` |
| Configurar usuario | `git config --global user.name "Nombre"` |
| Configurar email | `git config --global user.email "email"` |
| Crear repo local | `git init` |
| Ver estado | `git status` |
| Agregar archivo | `git add archivo` |
| Agregar todo | `git add .` |
| Crear commit | `git commit -m "mensaje"` |
| Ver historial | `git log --oneline` |
| Ver diferencias | `git diff` |
| Conectar remoto | `git remote add origin URL` |
| Ver remotos | `git remote -v` |
| Subir cambios | `git push` |
| Traer cambios | `git pull` |
| Traer sin aplicar | `git fetch` |
| Clonar repo | `git clone URL` |
| Ver ramas | `git branch` |
| Crear y entrar a rama | `git switch -c nombre-rama` |
| Cambiar de rama | `git switch nombre-rama` |
| Fusionar rama | `git merge nombre-rama` |
| Restaurar archivo | `git restore archivo` |
| Sacar del staging | `git restore --staged archivo` |

</div>

---

## Criterios de evaluación para el TP

| Criterio | Logrado | En proceso |
|---|---|---|
| Configura Git correctamente |  |  |
| Crea repositorio local |  |  |
| Realiza commits claros |  |  |
| Usa `status`, `diff` y `log` |  |  |
| Conecta repositorio remoto |  |  |
| Usa `push` y `pull` correctamente |  |  |
| Clona un repositorio |  |  |
| Crea y usa branches |  |  |
| Realiza merge correctamente |  |  |
| Resuelve errores comunes |  |  |
| Entrega el mini proyecto final |  |  |

