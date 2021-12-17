import matplotlib.pyplot as plt
import numpy as np
import random

# hydrogen market assumptions
# from Road Map to a US hydrogen Ecosystem
# numbers for US
# assuming realized price of $2/kg for hydrogen produced
hydrogen_revenue_per_year_2021: float = 17600000000  # USD
hydrogen_revenue_per_year_2030: float = 140000000000  # USD


potential_derivatives_market_multiplier: int = 5
time_until_artis_launch_in_days: int = 365
percent_of_potential_market_captured_on_day_one: float = 1
artis_trading_fee = 0.002  # .2%

# token assumptions
initial_token_supply = 1000000000  # HET
tokens_held_by_hydrogen_project = 0  # HET

# create mock physical hydrogen investments
PROFIT_PER_SCF: float = 0.0002  # USD
PROFIT_PER_KG = PROFIT_PER_SCF * 423.3  # 423 scf in 1 kg
# simulate 1 project transporting x volume per day
scf_moved_per_day: list = 42000000000
kg_moved_per_day = scf_moved_per_day / 423.3  # 423 scf in 1 kg

# tokens generated from data per day with artis
# log is a simple choice for a function that decreases with scale
# reporting gives a public and open source data feed for regulators to monitor
def tokens_generated_with_artis(kg: float) -> float:
    tokens = np.log(kg)
    return tokens


# calculate dollar volume on artis
def get_volume_on_artis(
    total_hydro_rev: float,
    potential_derivatives_market_multiplier: float,
    percent_of_derivatives_market_capture: float,
) -> float:
    return (
        total_hydro_rev
        * potential_derivatives_market_multiplier
        * (percent_of_derivatives_market_capture / 100)
    )


# calculate fee revenue on artis
def fee_dividends(volume_on_artis: float, trading_fee: float) -> (float, float):
    total_fees = volume_on_artis * trading_fee
    fee_to_equity = total_fees * (2 / 3)
    fee_to_tokens = total_fees * (1 / 3)
    return fee_to_equity, fee_to_tokens  # USD


# calculate token supply
def current_token_supply(
    previous_token_supply: int, tokens_generated_this_epoch: int
) -> int:
    return previous_token_supply + tokens_generated_this_epoch


def dividend_per_token_per_day(token_supply: int, fee_to_tokens: float) -> float:
    return fee_to_tokens / token_supply  # USD/token


# simulate hydrogen projects assuming linear growth in total hydrogen market
def simulate_hydrogen_projects(
    number_of_years,
    hydrogen_revenue_start_year,
    hydrogen_revenue_end_year,
    potential_derivatives_market_multiplier,
    time_until_artis_launch_in_days,
    percent_of_potential_market_captured_on_day_one,
    tokens_held_by_hydrogen_project,
    initial_token_supply,
    artis_trading_fee,
    kg_moved_per_day,
) -> dict:

    number_of_days = number_of_years * 365
    growth_in_hydro_market_per_day = (
        hydrogen_revenue_end_year - hydrogen_revenue_start_year
    ) / number_of_days

    implied_kg_of_hydrogen_produced_start = (
        hydrogen_revenue_start_year / 2
    )  # billion kg
    implied_kg_of_hydrogen_pruduced_end = (
        hydrogen_revenue_per_year_2030 / 2
    )  # billion kg

    # assume linear growth
    growth_in_hydro_kg_produced_per_day = (
        implied_kg_of_hydrogen_pruduced_end - implied_kg_of_hydrogen_produced_start
    ) / number_of_days

    # dict { 'no_artis': list, 'with_artis': list}
    dict_of_outcomes = dict()
    list_of_rev_no_artis = list()
    list_of_rev_with_artis = list()

    for day in range(0, number_of_days):
        kg_moved_on_day = kg_moved_per_day * (random.randint(-1, 2) * 0.01)
        list_of_rev_no_artis.append(kg_moved_on_day * PROFIT_PER_KG)

        total_hydro_market = (
            hydrogen_revenue_start_year + growth_in_hydro_market_per_day * day
        )

        total_kg_produced = (
            implied_kg_of_hydrogen_produced_start
            + growth_in_hydro_kg_produced_per_day * day
        )

        if day == 0:
            percent_of_derivatives_market_capture = (
                percent_of_potential_market_captured_on_day_one
            )
        else:
            # assume our market capture grows randomly between -.01 and .05% per day
            percent_of_derivatives_market_capture = (
                percent_of_derivatives_market_capture + random.randint(-1, 5) * 0.01
            )

        volume_on_artis = get_volume_on_artis(
            total_hydro_market,
            potential_derivatives_market_multiplier,
            percent_of_derivatives_market_capture,
        )

        fee_to_equity, fee_to_tokens = fee_dividends(volume_on_artis, artis_trading_fee)

        if day == 0:
            tokens_generated = 0
            token_supply = initial_token_supply

        if day >= time_until_artis_launch_in_days:
            tokens_generated = tokens_generated_with_artis(total_kg_produced)
            tokens_generated_for_project = tokens_generated_with_artis(kg_moved_per_day)
            token_supply = token_supply + tokens_generated
            tokens_held_by_hydrogen_project = (
                tokens_held_by_hydrogen_project + tokens_generated_for_project
            )

        marginal_revenue_added_by_artis = (
            tokens_held_by_hydrogen_project / token_supply
        ) * fee_to_tokens

        if day % 100 == 0:
            print(tokens_held_by_hydrogen_project / token_supply)

        list_of_rev_with_artis.append(
            (kg_moved_on_day * PROFIT_PER_KG) + marginal_revenue_added_by_artis
        )

    dict_of_outcomes = {
        "no_artis": list_of_rev_no_artis,
        "with_artis": list_of_rev_with_artis,
    }

    return dict_of_outcomes


if __name__ == "__main__":
    number_of_years = 8
    hydrogen_revenue_start_year = hydrogen_revenue_per_year_2021
    hydrogen_revenue_end_year = hydrogen_revenue_per_year_2030

    dic_of_revenue = simulate_hydrogen_projects(
        number_of_years,
        hydrogen_revenue_start_year,
        hydrogen_revenue_end_year,
        potential_derivatives_market_multiplier,
        time_until_artis_launch_in_days,
        percent_of_potential_market_captured_on_day_one,
        tokens_held_by_hydrogen_project,
        initial_token_supply,
        artis_trading_fee,
        kg_moved_per_day,
    )

    x_axis = [day for day in range(0, 365 * number_of_years)]
    rev_no_artis = dic_of_revenue["no_artis"]
    rev_with_artis = dic_of_revenue["with_artis"]
    cum_rev_no_artis = list()
    cum_rev_with_artis = list()

    for day in x_axis:
        cum_rev_no_artis.append(sum(rev_no_artis[0:day]))
        cum_rev_with_artis.append(sum(rev_with_artis[0:day]))

    plt.plot(x_axis, cum_rev_no_artis, label="rev_no_artis")
    plt.plot(x_axis, cum_rev_with_artis, label="rev_with_artis")
    plt.legend()
    plt.savefig("hydro_sim.pdf")
    plt.show()
