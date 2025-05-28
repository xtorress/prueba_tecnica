from app.services.simulation import Simulation

def main():
    print("Iniciando simulación")
    print("----------------------")
    simulation = Simulation()
    simulation.run()
    print("Agente personal")
    print(f"- Balance final: {simulation.personal_agent.balance}")
    print(f"- n° tarjetas: {simulation.personal_agent.cards}")
    print("Simulación terminada")


if __name__ == "__main__":
    main()