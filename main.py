from app.services.simulation import Simulation
from app.services.report import GenerateReport

def main():
    # show_menu()
    simulation = Simulation()
    print("Iniciando simulación....")
    print("Terminada.")
    simulation.run()
    report = GenerateReport(simulation.agents)
    report.info_personal_agent()
    report.get_top5_agents()

# def show_menu():
#     print("\n\n\t\tMENÚ\n")
#     print("1. Iniciar simulación.\n" \
#           "2. Top5 de agentes con mayor balance.\n" \
#             "3. Salir\n")


if __name__ == "__main__":
    main()