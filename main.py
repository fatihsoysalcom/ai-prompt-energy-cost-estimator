import math

def estimate_eco_cost(prompt_text: str):
    """
    Estimates the ecological cost (energy and CO2) of an AI prompt
    based on a simplified model, simulating the EcoPrompt concept.
    """
    # --- EcoPrompt Modeling Parameters (Hypothetical) ---
    # These parameters represent the core of the 'EcoPrompt' modeling approach.
    # In a real scenario, these would be derived from extensive research
    # on model architecture, inference efficiency, hardware, and energy mix.

    # 1. Computational Load Proxy:
    # We'll use the number of 'tokens' (words) in the prompt as a simple proxy
    # for the computational effort required by the AI model.
    # More complex prompts are assumed to require more computation.
    words = prompt_text.split()
    computational_tokens = len(words)
    if computational_tokens == 0:
        print("Prompt is empty, no cost to estimate.")
        return

    # 2. Energy Consumption per Unit of Computation:
    # Hypothetical energy cost per computational token (e.g., Joules per token).
    # This is a placeholder for the complex interplay of GPU operations, memory access, etc.
    energy_per_token_joules = 0.0005  # Joules per 'token' (word) - a very small, illustrative value

    # 3. Energy to CO2 Emission Factor:
    # Average CO2 emissions per kilowatt-hour (kWh). This varies significantly
    # based on the electricity source (e.g., coal vs. renewables).
    # Using a global average for demonstration (e.g., ~400 grams CO2 per kWh).
    co2_per_kwh_grams = 400.0  # grams of CO2 per kWh

    # --- Calculations ---

    # Calculate total estimated energy in Joules
    total_energy_joules = computational_tokens * energy_per_token_joules

    # Convert Joules to Kilowatt-hours (1 kWh = 3.6 * 10^6 Joules)
    joules_to_kwh_factor = 1 / (3.6 * 10**6)
    total_energy_kwh = total_energy_joules * joules_to_kwh_factor

    # Calculate total estimated CO2 emissions
    total_co2_grams = total_energy_kwh * co2_per_kwh_grams

    # --- Output Results ---
    print(f"--- EcoPrompt Cost Estimation ---")
    print(f"Prompt: '{prompt_text[:50]}{'...' if len(prompt_text) > 50 else ''}'")
    print(f"Estimated Computational Tokens: {computational_tokens}")
    print(f"Estimated Energy Consumption: {total_energy_joules:.6f} Joules")
    print(f"                            ({total_energy_kwh:.9f} kWh)")
    print(f"Estimated CO2 Emissions:    {total_co2_grams:.6f} grams CO2")
    print(f"---------------------------------")

# --- Example Usage ---
if __name__ == "__main__":
    sample_prompts = [
        "Hello, how are you?",
        "Write a short poem about a cat sitting on a mat.",
        "Generate a detailed technical explanation of quantum entanglement for a layperson, including analogies and potential applications in future technologies.",
        "", # Empty prompt test
        "Summarize the key findings of the latest IPCC report on climate change, focusing on the most urgent actions required by governments and industries to limit global warming to 1.5 degrees Celsius above pre-industrial levels. Include specific examples of policy interventions and technological innovations that could contribute to achieving these targets, and discuss the socio-economic implications of both inaction and aggressive climate mitigation strategies. Also, touch upon the role of international cooperation and equitable burden-sharing among nations."
    ]

    for i, prompt in enumerate(sample_prompts):
        print(f"\n--- Running Example {i+1} ---")
        estimate_eco_cost(prompt)
