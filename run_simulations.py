from hydro_simulation import simulate_hydrogen_projects
from simulation_config import config
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


def print_title(simulation_conditions):
    firstPage = plt.figure(figsize=(11.69, 8.27))
    firstPage.clf()
    txt = "".join(
        [
            f"{key} : {simulation_conditions[key]} \n"
            for key in simulation_conditions.keys()
        ]
    )
    firstPage.text(0.5, 0.5, txt, transform=firstPage.transFigure, size=24, ha="center")
    pdf.savefig()
    plt.close()


def plot_marginal_revenue(simulation_conditions, dict_of_revenue):
    x_axis = [day for day in range(0, 365 * simulation_conditions["number_of_years"])]
    rev_no_artis = dict_of_revenue["no_artis"]
    rev_with_artis = dict_of_revenue["with_artis"]

    plt.plot(x_axis, rev_no_artis, label="rev_no_artis")
    plt.plot(x_axis, rev_with_artis, label="rev_with_artis")
    plt.title("Marginal Daily Revenue")
    plt.ylim(ymin=0)
    plt.legend()
    pdf.savefig()
    plt.close()


def plot_cumulative_revenue(simulation_conditions, dict_of_revenue):
    x_axis = [day for day in range(0, 365 * simulation_conditions["number_of_years"])]
    rev_no_artis = dict_of_revenue["no_artis"]
    rev_with_artis = dict_of_revenue["with_artis"]
    cum_rev_no_artis = list()
    cum_rev_with_artis = list()

    for day in x_axis:
        cum_rev_no_artis.append(sum(rev_no_artis[:day]))
        cum_rev_with_artis.append(sum(rev_with_artis[:day]))

    plt.plot(x_axis, cum_rev_no_artis, label="cum_rev_no_artis")
    plt.plot(x_axis, cum_rev_with_artis, label="cum_rev_with_artis")
    plt.title("Cumulative Revenue")
    plt.ylim(ymin=0)
    plt.legend()
    pdf.savefig()
    plt.close()


if __name__ == "__main__":
    with PdfPages("hydro_simulations.pdf") as pdf:
        for simulation_conditions in config:
            dict_of_revenue = simulate_hydrogen_projects(
                simulation_conditions["number_of_years"],
                simulation_conditions["hydrogen_revenue_start_year"],
                simulation_conditions["hydrogen_revenue_end_year"],
                simulation_conditions["potential_derivatives_market_multiplier"],
                simulation_conditions["time_until_artis_launch_in_days"],
                simulation_conditions[
                    "percent_of_potential_market_captured_on_day_one"
                ],
                simulation_conditions["tokens_held_by_hydrogen_project"],
                simulation_conditions["initial_token_supply"],
                simulation_conditions["kg_moved_per_day"],
                simulation_conditions["growth_in_kg_moved"],
            )

            print(dict_of_revenue["no_artis"])
            print(dict_of_revenue["with_artis"])

            print_title(simulation_conditions)
            plot_marginal_revenue(simulation_conditions, dict_of_revenue)
            plot_cumulative_revenue(simulation_conditions, dict_of_revenue)
