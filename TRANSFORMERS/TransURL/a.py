import os
import pandas as pd

# Ruta base de los datasets
base_path = "./Data"

# Mapeo de etiquetas
label_map = {
    "benign": "0",
    "malicious": "1"
}

# Revisión de carpetas en Data
if not os.path.exists(base_path):
    print(f"❌ La carpeta {base_path} no existe.")
    exit()

print(f"📁 Procesando datasets en: {base_path}\n")

# Recorremos las subcarpetas
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        print(f"📂 Revisando carpeta: {folder}")
        for filename in ["Train.csv", "Test.csv"]:
            csv_path = os.path.join(folder_path, filename)
            if os.path.exists(csv_path):
                print(f"  🔍 Encontrado: {filename}")
                try:
                    df = pd.read_csv(csv_path)
                    # Convertir encabezados a minúsculas para uniformidad
                    df.columns = df.columns.str.lower()

                    if "url" in df.columns and "label" in df.columns:
                        output_lines = []
                        for _, row in df.iterrows():
                            label = str(row['label']).strip().lower()
                            if label in label_map:
                                line = f"{row['url']} {label_map[label]}"
                                output_lines.append(line)
                            else:
                                print(f"    ⚠ Etiqueta desconocida: {label}")
                        
                        # Guardar archivo .txt
                        output_filename = filename.replace(".csv", ".txt")
                        output_path = os.path.join(folder_path, output_filename)
                        with open(output_path, "w") as f:
                            f.write("\n".join(output_lines))
                        print(f"  ✅ Guardado: {output_filename} con {len(output_lines)} líneas")
                    else:
                        print(f"  ❌ Faltan columnas 'url' o 'label' en: {filename}")
                except Exception as e:
                    print(f"  ❌ Error al procesar {filename}: {e}")
            else:
                print(f"  ⚠ No encontrado: {filename}")
