import requests
import threading
import time

URL = "http://localhost:8000/api/epreuves/"
TOTAL_REQUESTS = 50
CONCURRENCY = 10  # Nombre de requêtes simultanées

results = {"success": 0, "errors": 0, "times": []}
lock = threading.Lock()


def send_request():
    try:
        start = time.time()
        response = requests.get(URL, timeout=5)
        duration = (time.time() - start) * 1000

        with lock:
            if response.status_code == 200:
                results["success"] += 1
                results["times"].append(duration)
            else:
                results["errors"] += 1
    except Exception as e:
        with lock:
            results["errors"] += 1
            print(f"Détail de l'erreur : {e}")  # <-- Ajoute cette ligne

def run_load_test():
    threads = []
    print(f"Lancement de {TOTAL_REQUESTS} requêtes avec une concurrence de {CONCURRENCY}...")
    start_total = time.time()

    for i in range(TOTAL_REQUESTS):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

        # Si on atteint le niveau de concurrence, on attend qu'ils finissent un lot
        if len(threads) >= CONCURRENCY:
            for t in threads:
                t.join()
            threads = []

    # S'il reste des threads
    for t in threads:
        t.join()

    total_time = time.time() - start_total

    print("\n--- RÉSULTATS DU TEST DE CHARGE ---")
    print(f"Temps total : {total_time:.2f} secondes")
    print(f"Requêtes réussies : {results['success']}/{TOTAL_REQUESTS}")
    print(f"Erreurs : {results['errors']}")
    if results["times"]:
        avg_time = sum(results["times"]) / len(results["times"])
        print(f"Temps de réponse moyen : {avg_time:.2f} ms")


if __name__ == "__main__":
    run_load_test()