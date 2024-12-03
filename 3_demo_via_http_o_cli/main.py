import subprocess

if __name__ == '__main__':
    mode = input("¿Cómo quieres ejecutar la aplicación? (http/cli): ")

    if mode == "http":
        subprocess.run(["python", "adapters/input/http_adapter.py"])
    elif mode == "cli":
        subprocess.run(["python", "adapters/input/cli_adapter.py", "--nombre", "John", "--apellidos", "Doe", "--rol", "Analista de negocio"])
    else:
        print("Modo no reconocido. Usa 'http' o 'cli'.")
