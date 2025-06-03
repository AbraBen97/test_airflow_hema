from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Fonction qui sera appelée par le DAG
def afficher_message():
    print("Bonjour depuis Airflow ! 😊")

# Définition du DAG
with DAG(
    dag_id='dag_message_simple',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # Pas de planification automatique
    catchup=False,
    tags=["exemple"]
) as dag:

    tache_afficher = PythonOperator(
        task_id='afficher_message',
        python_callable=afficher_message
    )

    tache_afficher
