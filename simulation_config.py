number_of_years = 8
# hydrogen market assumptions
# from Road Map to a US hydrogen Ecosystem
# numbers for US
# assuming realized price of $2/kg for hydrogen produced
hydrogen_revenue_per_year_2021: float = 17600  # million USD
hydrogen_revenue_per_year_2030: float = 140000  # million USD
# assume linear
hydrogen_market_percent_growth_per_day = (
    hydrogen_revenue_per_year_2030 - hydrogen_revenue_per_year_2021
) / (hydrogen_revenue_per_year_2021 * number_of_years * 365)

potential_derivatives_market_multiplier: int = 3
time_until_artis_launch_in_days = 365
percent_of_potential_market_captured_on_day_one: float = 2
# token assumptions
initial_token_supply = 100000000  # HET
tokens_held_by_hydrogen_project = 0  # HET

num_of_producers = 100


config = [
    {
        "number_of_years": number_of_years,
        "hydrogen_revenue_start_year": hydrogen_revenue_per_year_2021,
        "hydrogen_revenue_end_year": hydrogen_revenue_per_year_2030,
        "potential_derivatives_market_multiplier": potential_derivatives_market_multiplier,
        "time_until_artis_launch_in_days": time_until_artis_launch_in_days,
        "percent_of_potential_market_captured_on_day_one": percent_of_potential_market_captured_on_day_one,
        "tokens_held_by_hydrogen_project": 0,
        "initial_token_supply": initial_token_supply,
        "kg_moved_per_day": 1,  # millions of kg
        "growth_in_kg_moved": 0,
        "num_of_producers": num_of_producers,
    },
    {
        "number_of_years": number_of_years,
        "hydrogen_revenue_start_year": hydrogen_revenue_per_year_2021,
        "hydrogen_revenue_end_year": hydrogen_revenue_per_year_2030,
        "potential_derivatives_market_multiplier": potential_derivatives_market_multiplier,
        "time_until_artis_launch_in_days": time_until_artis_launch_in_days,
        "percent_of_potential_market_captured_on_day_one": percent_of_potential_market_captured_on_day_one,
        "tokens_held_by_hydrogen_project": 10000,
        "initial_token_supply": initial_token_supply,
        "kg_moved_per_day": 1,  # in millions of kg
        "growth_in_kg_moved": 0,
        "num_of_producers": num_of_producers,
    },
    {
        "number_of_years": number_of_years,
        "hydrogen_revenue_start_year": hydrogen_revenue_per_year_2021,
        "hydrogen_revenue_end_year": hydrogen_revenue_per_year_2030,
        "potential_derivatives_market_multiplier": potential_derivatives_market_multiplier,
        "time_until_artis_launch_in_days": time_until_artis_launch_in_days,
        "percent_of_potential_market_captured_on_day_one": percent_of_potential_market_captured_on_day_one,
        "tokens_held_by_hydrogen_project": 50000,
        "initial_token_supply": initial_token_supply,
        "kg_moved_per_day": 1,  # in millions of kg
        "growth_in_kg_moved": 0,
        "num_of_producers": num_of_producers,
    },
    {
        "number_of_years": number_of_years,
        "hydrogen_revenue_start_year": hydrogen_revenue_per_year_2021,
        "hydrogen_revenue_end_year": hydrogen_revenue_per_year_2030,
        "potential_derivatives_market_multiplier": potential_derivatives_market_multiplier,
        "time_until_artis_launch_in_days": time_until_artis_launch_in_days,
        "percent_of_potential_market_captured_on_day_one": percent_of_potential_market_captured_on_day_one,
        "tokens_held_by_hydrogen_project": 100,
        "initial_token_supply": initial_token_supply,
        "kg_moved_per_day": 0.01,  # in millions of kg
        "growth_in_kg_moved": 0,
        "num_of_producers": num_of_producers,
    },
    {
        "number_of_years": number_of_years,
        "hydrogen_revenue_start_year": hydrogen_revenue_per_year_2021,
        "hydrogen_revenue_end_year": hydrogen_revenue_per_year_2030,
        "potential_derivatives_market_multiplier": potential_derivatives_market_multiplier,
        "time_until_artis_launch_in_days": time_until_artis_launch_in_days,
        "percent_of_potential_market_captured_on_day_one": percent_of_potential_market_captured_on_day_one,
        "tokens_held_by_hydrogen_project": 0,
        "initial_token_supply": initial_token_supply,
        "kg_moved_per_day": 0.01,  # in millions of kg
        "growth_in_kg_moved": 0,
        "num_of_producers": num_of_producers,
    },
    {
        "number_of_years": number_of_years,
        "hydrogen_revenue_start_year": hydrogen_revenue_per_year_2021,
        "hydrogen_revenue_end_year": hydrogen_revenue_per_year_2030,
        "potential_derivatives_market_multiplier": potential_derivatives_market_multiplier,
        "time_until_artis_launch_in_days": time_until_artis_launch_in_days,
        "percent_of_potential_market_captured_on_day_one": percent_of_potential_market_captured_on_day_one,
        "tokens_held_by_hydrogen_project": 1000,
        "initial_token_supply": initial_token_supply,
        "kg_moved_per_day": 0,  # in millions of kg
        "growth_in_kg_moved": 0,
        "num_of_producers": num_of_producers,
    },
]
