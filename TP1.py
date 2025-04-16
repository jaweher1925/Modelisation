import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


def read_csv(file_path):
    data = pd.read_csv(file_path, sep=';')
    return data 


def write_csv(data, file_path):
    data.to_csv(file_path, index=False)


def plot_data(data, column_name):

        plt.figure(figsize=(10, 6))
        sns.histplot(data[column_name], bins=30, kde=True)
        plt.title(f'Histogramme de {column_name}')
        plt.xlabel('Valeurs')
        plt.ylabel('Fréquence')
        plt.show()
  


if __name__ == "__main__":
    file_path = r"c:/Users/dell/Desktop/M1_DataSc/modelisation_houda/census.csv"
   
    output_path = r"c:/Users/dell/Desktop/M1_DataSc/modelisation_houda/census_cleaned.csv"



    # Étapes du TP
    data = read_csv(file_path)
    write_csv(data, output_path)
   
    
    print("Colonnes disponibles :", list(data.columns))
    
    while True:
        col = input("Entrez le nom de la colonne à visualiser : ")
        
        if col in data.columns:
            plot_data(data, col)
            break
        else:
            print(f"La colonne '{col}' n'existe pas. Essayez à nouveau.")