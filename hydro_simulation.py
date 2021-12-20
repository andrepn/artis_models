import matplotlib.pyplot as plt
import numpy as np
import random

ARTIS_TRADING_FEE = 0.002  # .2%
PROFIT_PER_SCF: float = 0.0002  # USD
PROFIT_PER_KG = PROFIT_PER_SCF * 423.3  # 423 scf in 1 kg then per million


# tokens generated from data per day with artis
# sqrt is a simple choice for a function that decreases with scale
# reporting gives a public and open source data feed for regulators to monitor
def tokens_generated_with_artis(kg: float) -> float:
    tokens = np.sqrt(kg) * 3  # tokens generated for producer, transporter, and consumer
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
    kg_moved_per_day,
    growth_in_kg_moved,
    num_of_producers,
) -> dict:

    number_of_days = number_of_years * 365
    growth_in_hydro_market_per_day = (
        hydrogen_revenue_end_year - hydrogen_revenue_start_year
    ) / number_of_days

    implied_kg_of_hydrogen_produced_start = (
        hydrogen_revenue_start_year / 2
    )  # billion kg
    implied_kg_of_hydrogen_pruduced_end = hydrogen_revenue_end_year / 2  # billion kg

    # assume linear growth
    growth_in_hydro_kg_produced_per_day = (
        implied_kg_of_hydrogen_pruduced_end - implied_kg_of_hydrogen_produced_start
    ) / number_of_days

    # dict { 'no_artis': list, 'with_artis': list}
    dict_of_outcomes = dict()
    list_of_rev_no_artis = list()
    list_of_rev_with_artis = list()

    for day in range(0, number_of_days):
        if day == 0:
            kg_moved_on_day = kg_moved_per_day
        else:
            kg_moved_on_day = (
                kg_moved_on_day
                + (kg_moved_per_day * random.randrange(-1, 2) * 0.0025)
                + growth_in_kg_moved
            )  # * (
            #    random.randint(-10, 10) * 0.1
            # )

        list_of_rev_no_artis.append(kg_moved_on_day * PROFIT_PER_KG)

        if day == 0:
            total_hydro_market = hydrogen_revenue_start_year
        else:
            total_hydro_market = total_hydro_market + growth_in_hydro_market_per_day

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
                percent_of_derivatives_market_capture + 0.04 * random.randint(-1, 2)
                if percent_of_derivatives_market_capture < 39
                else percent_of_derivatives_market_capture
            )

        if day % 100 == 0:
            print(percent_of_derivatives_market_capture)

        volume_on_artis = get_volume_on_artis(
            total_hydro_market,
            potential_derivatives_market_multiplier,
            percent_of_derivatives_market_capture,
        )

        fee_to_equity, fee_to_tokens = fee_dividends(volume_on_artis, ARTIS_TRADING_FEE)

        if day == 0:
            tokens_generated = 0
            token_supply = initial_token_supply

        if day >= time_until_artis_launch_in_days:
            # split production between all producers evenly as assumption
            seperated_production = total_kg_produced / num_of_producers

            tokens_generated = sum(
                [
                    tokens_generated_with_artis(seperated_production)
                    for x in range(0, num_of_producers)
                ]
            )
            tokens_generated_for_project = (
                tokens_generated_with_artis(kg_moved_per_day) / 3
            )  # divide by three since we are only one player
            token_supply = token_supply + tokens_generated
            tokens_held_by_hydrogen_project = (
                tokens_held_by_hydrogen_project + tokens_generated_for_project
            )

            marginal_revenue_added_by_artis = (
                tokens_held_by_hydrogen_project / token_supply
            ) * fee_to_tokens

            list_of_rev_with_artis.append(
                (kg_moved_on_day * PROFIT_PER_KG) + marginal_revenue_added_by_artis
            )
        else:
            list_of_rev_with_artis.append((kg_moved_on_day * PROFIT_PER_KG))

    dict_of_outcomes = {
        "no_artis": list_of_rev_no_artis,
        "with_artis": list_of_rev_with_artis,
    }

    return dict_of_outcomes
