<div class="git-card">

# Informática - 2026

## Cheatsheet básico de Git para Windows

**Docente:** Ignacio Lavaggi

<span class="git-tag">Git</span>
<span class="git-tag">Windows</span>
<span class="git-tag">Consola</span>
<span class="git-tag">GitHub</span>

Este documento resume los comandos básicos para trabajar con Git desde la consola en Windows. La idea no es memorizar todos los comandos, sino entender el flujo de trabajo más común: descargar un proyecto, modificarlo, guardar cambios y subirlos a un repositorio remoto.

</div>

---

## 0. Consolas recomendadas en Windows

En Windows se puede usar Git desde distintas consolas:

| Consola | Uso recomendado |
|---|---|
| **Git Bash** | Muy recomendada para empezar. Viene incluida al instalar Git for Windows. |
| **PowerShell** | Buena opción moderna de Windows. |
| **CMD** | Funciona, aunque es más limitada. |

<div class="git-info">

Para trabajar con Git en clase, recomiendo usar **Git Bash**, porque muchos comandos se escriben igual que en Linux y macOS.

</div>

---

## 1. Ver si Git está instalado

Para comprobar si Git está instalado:

```bash
git --version
```

Si Git está instalado correctamente, la consola mostrará una versión, por ejemplo:

```text
git version 2.45.0
```

Si el comando no funciona, hay que instalar **Git for Windows**.

También se puede instalar desde PowerShell con:

```powershell
winget install --id Git.Git -e
```

---

## 2. Configuración inicial

Antes de usar Git, conviene configurar el nombre y el correo del usuario. Esta información queda asociada a los commits.

Un **commit** es una captura o registro de cambios dentro del proyecto. Cada commit guarda qué archivos cambiaron y permite volver a consultar el historial del trabajo.

Configurar nombre:

```bash
git config --global user.name "Tu Nombre"
```

Configurar correo:

```bash
git config --global user.email "tu@email.com"
```

Ver la configuración actual:

```bash
git config --list
```

Ver solo el nombre configurado:

```bash
git config user.name
```

Ver solo el correo configurado:

```bash
git config user.email
```

<div class="git-ok">

Conviene usar el mismo correo que se utiliza en GitHub o GitLab, para que los commits queden asociados correctamente a la cuenta.

</div>

---

## 3. Flujo básico de trabajo

El flujo básico de Git es:

```text
editar archivos → revisar estado → agregar cambios → crear commit → subir cambios
```

Ver el estado del repositorio:

```bash
git status
```

Este comando muestra qué archivos fueron modificados, cuáles están listos para commit y si hay cambios pendientes.

Agregar todos los cambios:

```bash
git add .
```

`git add` prepara los archivos modificados para el próximo commit. El punto `.` significa “agregar todos los cambios de esta carpeta”.

Agregar un archivo específico:

```bash
git add archivo.py
```

Crear un commit:

```bash
git commit -m "Mensaje claro del cambio"
```

El mensaje del commit debe explicar brevemente qué se hizo.

Subir los cambios al repositorio remoto:

```bash
git push
```

`push` significa subir los commits locales al repositorio remoto, por ejemplo GitHub.

Traer cambios desde el repositorio remoto:

```bash
git pull
```

`pull` significa traer los cambios que están en el repositorio remoto y aplicarlos en la copia local.

---

## 4. Ejemplo completo de uso diario

Este es el ciclo más común cuando ya existe un proyecto configurado:

```bash
git status
git add .
git commit -m "Corrige validación de formulario"
git push
```

Si se trabaja en una computadora compartida o con otras personas, primero conviene traer los cambios remotos:

```bash
git pull
git status
git add .
git commit -m "Agrega nueva funcionalidad"
git push
```

<div class="git-info">

En proyectos grupales, antes de empezar a trabajar conviene hacer `git pull`. Así se evita trabajar sobre una versión vieja del proyecto.

</div>

---

## 5. Crear un repositorio desde cero

Un **repositorio** es una carpeta controlada por Git. Dentro de un repositorio, Git puede registrar cambios, crear commits y conectarse con servicios como GitHub.

Entrar a la carpeta del proyecto:

```bash
cd C:\Users\TuUsuario\Documents\mi-proyecto
```

Inicializar Git en esa carpeta:

```bash
git init
```

`git init` convierte la carpeta actual en un repositorio local de Git.

Agregar los archivos:

```bash
git add .
```

Crear el primer commit:

```bash
git commit -m "Primer commit"
```

Conectar el repositorio local con un repositorio remoto:

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

Un **remoto** es una dirección externa donde también existe el proyecto. Por ejemplo, un repositorio alojado en GitHub.

Subir por primera vez:

```bash
git push -u origin main
```

El parámetro `-u` vincula la rama local `main` con la rama remota. Después de este primer push, alcanza con usar:

```bash
git push
```

---

## 6. Clonar un repositorio

**Clonar** significa descargar una copia completa de un repositorio remoto en la computadora.

Clonar usando HTTPS:

```bash
git clone https://github.com/usuario/repositorio.git
```

Clonar usando SSH:

```bash
git clone git@github.com:usuario/repositorio.git
```

Entrar a la carpeta descargada:

```bash
cd repositorio
```

<div class="git-info">

Cuando se clona un repositorio, no se descargan solo los archivos actuales. También se descarga el historial de commits del proyecto.

</div>

---

## 7. Ver repositorios y remotos

Para ver a qué repositorio remoto está conectada la carpeta actual:

```bash
git remote -v
```

Ejemplo:

```text
origin  https://github.com/usuario/repositorio.git (fetch)
origin  https://github.com/usuario/repositorio.git (push)
```

`origin` suele ser el nombre por defecto del repositorio remoto principal.

Cambiar la dirección del remoto:

```bash
git remote set-url origin NUEVA_URL
```

Ejemplo para cambiar de HTTPS a SSH:

```bash
git remote set-url origin git@github.com:usuario/repositorio.git
```

---

## 8. Ver los repositorios de GitHub desde consola

Git por sí solo no lista todos los repositorios de una cuenta de GitHub. Para eso se usa **GitHub CLI**, una herramienta oficial para trabajar con GitHub desde consola.

Instalar GitHub CLI en Windows:

```powershell
winget install --id GitHub.cli -e
```

Iniciar sesión:

```bash
gh auth login
```

Ver los repositorios de la cuenta:

```bash
gh repo list
```

Ver más resultados:

```bash
gh repo list --limit 100
```

Ver solo repositorios privados:

```bash
gh repo list --visibility private
```

Ver solo repositorios públicos:

```bash
gh repo list --visibility public
```

Clonar un repositorio desde GitHub CLI:

```bash
gh repo clone usuario/repositorio
```

---

## 9. Repositorios privados

Un repositorio privado es un proyecto que no puede ser visto por cualquier persona. Para acceder, hay que estar autenticado y tener permisos.

### Opción recomendada: GitHub CLI

Iniciar sesión:

```bash
gh auth login
```

Verificar autenticación:

```bash
gh auth status
```

Clonar un repositorio privado:

```bash
gh repo clone usuario/repo-privado
```

Después de clonar, el trabajo diario es igual:

```bash
git status
git add .
git commit -m "Actualiza proyecto"
git push
```

### Opción alternativa: HTTPS con token

Clonar por HTTPS:

```bash
git clone https://github.com/usuario/repo-privado.git
```

Cuando la consola pida usuario y contraseña:

```text
Username: tu_usuario
Password: tu_token
```

<div class="git-warn">

En repositorios privados no conviene usar contraseñas comunes. Lo correcto es usar GitHub CLI, SSH o un token de acceso personal.

</div>

---

## 10. Branches o ramas

Una **branch** o **rama** es una línea de trabajo separada dentro del mismo proyecto.

Sirve para modificar el código sin afectar directamente la versión principal. Por ejemplo, se puede crear una rama para probar una nueva función, corregir un error o trabajar en una parte del proyecto sin romper la rama principal.

La rama principal suele llamarse:

```text
main
```

Ejemplo de uso:

```text
main → versión estable del proyecto
feature/login → rama para desarrollar el login
fix/error-sensor → rama para corregir un error
```

Ver ramas locales:

```bash
git branch
```

Ver ramas remotas:

```bash
git branch -r
```

Ver todas las ramas:

```bash
git branch -a
```

Crear una rama nueva:

```bash
git branch nombre-rama
```

Cambiarse a otra rama:

```bash
git switch nombre-rama
```

Crear una rama y cambiarse a ella al mismo tiempo:

```bash
git switch -c nombre-rama
```

Ejemplo:

```bash
git switch -c feature/login
```

Subir una rama nueva al remoto:

```bash
git push -u origin feature/login
```

Volver a la rama principal:

```bash
git switch main
```

Fusionar una rama con la rama actual:

```bash
git merge nombre-rama
```

`merge` significa unir los cambios de una rama con otra.

Borrar una rama local:

```bash
git branch -d nombre-rama
```

Borrar una rama remota:

```bash
git push origin --delete nombre-rama
```

<div class="git-ok">

Usar ramas permite trabajar de forma más ordenada. En lugar de modificar directamente `main`, se trabaja en una rama aparte y después se integra cuando el cambio ya está listo.

</div>

---

## 11. Ver historial

El historial muestra los commits realizados en el proyecto.

Ver historial completo:

```bash
git log
```

Ver historial resumido:

```bash
git log --oneline
```

Ver historial con ramas:

```bash
git log --oneline --graph --all
```

Ver información del último commit:

```bash
git show
```

---

## 12. Ver diferencias

`diff` sirve para ver qué cambió en los archivos antes de crear un commit.

Ver cambios que todavía no fueron agregados:

```bash
git diff
```

Ver cambios que ya fueron agregados con `git add`:

```bash
git diff --staged
```

<div class="git-info">

Antes de hacer un commit importante, conviene revisar `git diff` para confirmar que se están guardando los cambios correctos.

</div>

---

## 13. Deshacer cambios simples

Deshacer los cambios de un archivo antes de hacer commit:

```bash
git restore archivo.py
```

`restore` devuelve un archivo al último estado guardado por Git.

Sacar un archivo del área de preparación:

```bash
git restore --staged archivo.py
```

Esto no borra el archivo ni sus cambios. Solo lo quita del próximo commit.

Cambiar el mensaje del último commit:

```bash
git commit --amend -m "Nuevo mensaje"
```

Deshacer el último commit, pero mantener los cambios:

```bash
git reset --soft HEAD~1
```

Deshacer el último commit y borrar los cambios:

```bash
git reset --hard HEAD~1
```

<div class="git-danger">

Cuidado con `git reset --hard`. Este comando puede borrar cambios locales. Antes de usarlo hay que estar seguro de que esos cambios no hacen falta.

</div>

---

## 14. Comandos ultra básicos

| Acción | Comando |
|---|---|
| Ver estado del proyecto | `git status` |
| Agregar todos los cambios | `git add .` |
| Crear commit | `git commit -m "mensaje"` |
| Subir cambios | `git push` |
| Traer y aplicar cambios remotos | `git pull` |
| Traer cambios remotos sin aplicarlos | `git fetch` |
| Ver historial resumido | `git log --oneline` |
| Ver ramas | `git branch` |
| Crear rama y entrar | `git switch -c nombre-rama` |
| Cambiar de rama | `git switch nombre-rama` |
| Ver remoto | `git remote -v` |
| Clonar repositorio | `git clone URL` |

### Diferencia entre `pull` y `fetch`

`fetch` trae información nueva desde el repositorio remoto, pero no modifica directamente los archivos locales.

```bash
git fetch
```

`pull` trae los cambios remotos y además intenta aplicarlos en la rama actual.

```bash
git pull
```

<div class="git-info">

Forma simple de recordarlo: `fetch` mira qué hay de nuevo; `pull` trae y aplica esos cambios.

</div>

---

## Errores comunes

### Error: `fatal: not a git repository`

Significa que la consola no está ubicada dentro de una carpeta controlada por Git.

Solución:

```bash
cd ruta\del\proyecto
```

O inicializar Git en la carpeta actual:

```bash
git init
```

---

### Error: `remote origin already exists`

Significa que ya existe un remoto llamado `origin`.

Ver remotos:

```bash
git remote -v
```

Cambiar la URL del remoto:

```bash
git remote set-url origin URL_NUEVA
```

---

### Error: `Authentication failed`

Significa que hay un problema de autenticación con GitHub o GitLab.

Solución recomendada con GitHub CLI:

```bash
gh auth login
```

Verificar sesión:

```bash
gh auth status
```

---

### Error: `Permission denied (publickey)`

Significa que se está intentando usar SSH, pero la clave no está configurada correctamente.

Probar conexión:

```bash
ssh -T git@github.com
```

Ver claves SSH en Git Bash:

```bash
ls ~/.ssh
```

Ver claves SSH en PowerShell:

```powershell
dir $env:USERPROFILE\.ssh
```

---

### Error: `Updates were rejected`

Significa que el repositorio remoto tiene cambios que todavía no están en la computadora local.

Solución típica:

```bash
git pull
git push
```

Si aparecen conflictos, hay que resolverlos en los archivos, luego ejecutar:

```bash
git add .
git commit -m "Resuelve conflictos"
git push
```

---

### Error: conflicto de merge

Un conflicto ocurre cuando Git no puede decidir automáticamente qué versión de un archivo conservar.

En el archivo puede aparecer algo así:

```text
<<<<<<< HEAD
versión local
=======
versión remota
>>>>>>> main
```

Hay que editar el archivo manualmente, dejar la versión correcta y borrar esas marcas.

Después:

```bash
git add .
git commit -m "Resuelve conflicto"
git push
```

---

<div class="git-card">

## Resumen final

Para trabajar todos los días con Git, los comandos principales son:

```bash
git status
git add .
git commit -m "mensaje claro"
git pull
git push
```

Para trabajar con ramas:

```bash
git switch -c nombre-rama
git push -u origin nombre-rama
git switch main
git pull
```

Antes de subir cambios, siempre conviene revisar:

```bash
git status
```

Un buen uso de Git permite trabajar de forma ordenada, registrar avances, volver atrás si algo sale mal y compartir proyectos de manera profesional.

</div>
