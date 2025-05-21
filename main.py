from app.services.simulation import Simulation

def main():
    print("Iniciando simulación")
    print("----------------------")
    simulation = Simulation()
    simulation.run()
    print("Simulación terminada")


if __name__ == "__main__":
    main()