from app.services.simulation import Simulation
from app.services.report import GenerateReport

def main():
    while True:
        show_menu()
        option = input("Seleccionar una opción: ")
        simulation = Simulation()
        if option == '1':
            print("Iniciando simulación....")
            print("Terminada.")
            simulation.run()
            report = GenerateReport(simulation.agents)
            report.info_personal_agent()
        elif option == '2':
            report.get_top5_agents()
        elif option == '3':
            break

def show_menu():
    print("\n\n\t\tMENÚ\n")
    print("1. Iniciar simulación.\n" \
          "2. Top5 de agentes con mayor balance.\n" \
            "3. Salir\n")


if __name__ == "__main__":
    main()